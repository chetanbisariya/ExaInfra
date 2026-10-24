<?php
/**
 * ExaInfra Rentals (exainfra.in) - Property Rental Confirmations API
 * Handles reserving and confirming the rental flat with token deposit
 */

require_once __DIR__ . '/config.php';

$pdo = getDbConnection();
$method = $_SERVER['REQUEST_METHOD'];

if ($method === 'POST') {
    $rawInput = file_get_contents('php://input');
    $data = json_decode($rawInput, true);

    $aptId = (int)str_replace('apt-', '', $data['apartmentId'] ?? '1');
    $tenantName = trim($data['tenantName'] ?? '');
    $tenantPhone = trim($data['tenantPhone'] ?? '');
    $tenantEmail = trim($data['tenantEmail'] ?? '');
    $tokenDeposit = (int)($data['tokenDeposit'] ?? 10000);
    $moveInDate = trim($data['moveInDate'] ?? date('Y-m-d', strtotime('+7 days')));
    $confCode = 'EXA-RENT-' . strtoupper(substr(md5(uniqid(rand(), true)), 0, 8));

    if (empty($tenantName) || empty($tenantPhone)) {
        http_response_code(422);
        echo json_encode(['status' => 'error', 'message' => 'Tenant name and phone are required']);
        exit();
    }

    $stmt = $pdo->prepare("INSERT INTO property_confirmations 
        (apartment_id, tenant_name, tenant_phone, tenant_email, token_deposit, move_in_date, confirmation_code, status) 
        VALUES (:apt_id, :name, :phone, :email, :token, :move_in, :code, 'confirmed_token_paid')");
    
    $stmt->execute([
        ':apt_id' => $aptId,
        ':name' => $tenantName,
        ':phone' => $tenantPhone,
        ':email' => $tenantEmail,
        ':token' => $tokenDeposit,
        ':move_in' => $moveInDate,
        ':code' => $confCode
    ]);

    // Update apartment status to rented_out or reserved
    $updApt = $pdo->prepare("UPDATE apartments SET status = 'rented_out' WHERE id = :id");
    $updApt->execute([':id' => $aptId]);

    echo json_encode([
        'status' => 'success',
        'message' => 'Rental property confirmed successfully!',
        'confirmation_code' => $confCode,
        'move_in_date' => $moveInDate,
        'token_paid' => $tokenDeposit
    ]);
    exit();
}
