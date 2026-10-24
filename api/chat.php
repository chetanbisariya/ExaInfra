<?php
/**
 * ExaInfra Rentals (exainfra.in) - In-App Chat & Messaging API
 * Enforces 20 Free Landlord Inquiries for Tenants
 */

require_once __DIR__ . '/config.php';

$pdo = getDbConnection();
$method = $_SERVER['REQUEST_METHOD'];

// ====================================================================
// GET: Fetch Messages for a conversation
// ====================================================================
if ($method === 'GET') {
    $convoId = (int)($_GET['conversation_id'] ?? 0);
    $aptId = (int)str_replace('apt-', '', $_GET['apartment_id'] ?? '0');

    if ($convoId > 0) {
        $stmt = $pdo->prepare("SELECT * FROM chat_messages WHERE conversation_id = :id ORDER BY sent_at ASC");
        $stmt->execute([':id' => $convoId]);
        $messages = $stmt->fetchAll();
    } else {
        $messages = [];
    }

    echo json_encode([
        'status' => 'success',
        'messages' => $messages
    ]);
    exit();
}

// ====================================================================
// POST: Send Chat Message / Initiate Chat
// ====================================================================
if ($method === 'POST') {
    $rawInput = file_get_contents('php://input');
    $data = json_decode($rawInput, true);

    $aptId = (int)str_replace('apt-', '', $data['apartmentId'] ?? '1');
    $tenantName = trim($data['tenantName'] ?? 'Renter');
    $tenantPhone = trim($data['tenantPhone'] ?? '');
    $messageText = trim($data['message'] ?? '');
    $userId = (int)($data['userId'] ?? 0);

    // Verify Free Chat Quota
    $userStmt = $pdo->prepare("SELECT free_chats_remaining, is_premium FROM users WHERE id = :id");
    $userStmt->execute([':id' => $userId]);
    $user = $userStmt->fetch();

    if ($user && $user['free_chats_remaining'] <= 0 && !$user['is_premium']) {
        http_response_code(403);
        echo json_encode([
            'status' => 'quota_exceeded',
            'message' => 'You have used all 20 free landlord inquiries. Please upgrade to continue chatting.',
            'upgrade_required' => true
        ]);
        exit();
    }

    // Decrement free chat count if applicable
    if ($user && $user['free_chats_remaining'] > 0) {
        $updateQuota = $pdo->prepare("UPDATE users SET free_chats_remaining = free_chats_remaining - 1 WHERE id = :id");
        $updateQuota->execute([':id' => $userId]);
    }

    // Find or create conversation
    $convoStmt = $pdo->prepare("SELECT id FROM chat_conversations WHERE apartment_id = :apt_id AND tenant_phone = :phone LIMIT 1");
    $convoStmt->execute([':apt_id' => $aptId, ':phone' => $tenantPhone]);
    $convo = $convoStmt->fetch();

    if (!$convo) {
        // Fetch landlord info from apartment
        $aptStmt = $pdo->prepare("SELECT owner_name, owner_phone FROM apartments WHERE id = :id LIMIT 1");
        $aptStmt->execute([':id' => $aptId]);
        $apt = $aptStmt->fetch() ?: ['owner_name' => 'Property Owner', 'owner_phone' => ''];

        $insConvo = $pdo->prepare("INSERT INTO chat_conversations 
            (apartment_id, landlord_name, landlord_phone, tenant_id, tenant_name, tenant_phone, last_message) 
            VALUES (:apt_id, :l_name, :l_phone, :t_id, :t_name, :t_phone, :msg)");
        
        $insConvo->execute([
            ':apt_id' => $aptId,
            ':l_name' => $apt['owner_name'],
            ':l_phone' => $apt['owner_phone'],
            ':t_id' => $userId ?: null,
            ':t_name' => $tenantName,
            ':t_phone' => $tenantPhone,
            ':msg' => $messageText
        ]);
        $convoId = $pdo->lastInsertId();
    } else {
        $convoId = $convo['id'];
        $updConvo = $pdo->prepare("UPDATE chat_conversations SET last_message = :msg WHERE id = :id");
        $updConvo->execute([':msg' => $messageText, ':id' => $convoId]);
    }

    // Insert tenant message
    $insMsg = $pdo->prepare("INSERT INTO chat_messages (conversation_id, sender_role, sender_name, message_text) VALUES (:cid, 'tenant', :name, :msg)");
    $insMsg->execute([
        ':cid' => $convoId,
        ':name' => $tenantName,
        ':msg' => $messageText
    ]);

    $remainingChats = $user ? max(0, $user['free_chats_remaining'] - 1) : 19;

    echo json_encode([
        'status' => 'success',
        'conversation_id' => (int)$convoId,
        'free_chats_remaining' => $remainingChats,
        'message' => 'Message delivered to owner'
    ]);
    exit();
}
