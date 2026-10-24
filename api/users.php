<?php
/**
 * ExaInfra Rentals (exainfra.in) - User Accounts & Quota API
 * Supports Landlord (5 Free Postings) & Tenant (20 Free Chats) Accounts
 */

require_once __DIR__ . '/config.php';

$pdo = getDbConnection();
$method = $_SERVER['REQUEST_METHOD'];

// Handle CORS
if ($method === 'OPTIONS') {
    http_response_code(200);
    exit();
}

// ====================================================================
// POST: Register or Login Account
// ====================================================================
if ($method === 'POST') {
    $rawInput = file_get_contents('php://input');
    $data = json_decode($rawInput, true);

    $action = $data['action'] ?? 'login_or_register';

    if ($action === 'login_or_register') {
        $name = trim($data['name'] ?? 'User');
        $email = strtolower(trim($data['email'] ?? ''));
        $phone = trim($data['phone'] ?? '');
        $role = in_array($data['role'] ?? '', ['landlord', 'tenant']) ? $data['role'] : 'tenant';

        if (empty($email) || empty($phone)) {
            http_response_code(422);
            echo json_encode(['status' => 'error', 'message' => 'Email and phone number are required']);
            exit();
        }

        // Check if user already exists
        $stmt = $pdo->prepare("SELECT * FROM users WHERE email = :email LIMIT 1");
        $stmt->execute([':email' => $email]);
        $user = $stmt->fetch();

        if (!$user) {
            // New user registration with default quotas:
            // 5 Free Property Postings for Landlords
            // 20 Free Landlord Inquiries for Tenants
            $insert = $pdo->prepare("INSERT INTO users 
                (name, email, phone, role, free_posts_remaining, free_chats_remaining, is_premium) 
                VALUES (:name, :email, :phone, :role, 5, 20, 0)");
            $insert->execute([
                ':name' => $name,
                ':email' => $email,
                ':phone' => $phone,
                ':role' => $role
            ]);
            $userId = $pdo->lastInsertId();

            $user = [
                'id' => (int)$userId,
                'name' => $name,
                'email' => $email,
                'phone' => $phone,
                'role' => $role,
                'free_posts_remaining' => 5,
                'free_chats_remaining' => 20,
                'is_premium' => 0
            ];
        }

        echo json_encode([
            'status' => 'success',
            'message' => 'User logged in successfully',
            'user' => [
                'id' => (int)$user['id'],
                'name' => $user['name'],
                'email' => $user['email'],
                'phone' => $user['phone'],
                'role' => $user['role'],
                'free_posts_remaining' => (int)$user['free_posts_remaining'],
                'free_chats_remaining' => (int)$user['free_chats_remaining'],
                'is_premium' => (bool)$user['is_premium']
            ]
        ]);
        exit();
    }

    // Buy additional quota
    if ($action === 'upgrade_quota') {
        $userId = (int)($data['userId'] ?? 0);
        $package = $data['package'] ?? ''; // 'landlord_post_pack' (₹499) or 'tenant_chat_pack' (₹399)

        if ($package === 'landlord_post_pack') {
            $stmt = $pdo->prepare("UPDATE users SET free_posts_remaining = free_posts_remaining + 5 WHERE id = :id");
            $stmt->execute([':id' => $userId]);
        } elseif ($package === 'tenant_chat_pack') {
            $stmt = $pdo->prepare("UPDATE users SET free_chats_remaining = free_chats_remaining + 25 WHERE id = :id");
            $stmt->execute([':id' => $userId]);
        }

        echo json_encode([
            'status' => 'success',
            'message' => 'Quota upgraded successfully'
        ]);
        exit();
    }
}
