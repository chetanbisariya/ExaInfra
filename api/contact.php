<?php
/**
 * ExaInfra.in - Contact Us & Institutional Inquiry API
 * Handles lead transmission, database storage, and email delivery to contact@exainfra.in
 */

require_once __DIR__ . '/config.php';

$pdo = getDbConnection();
$method = $_SERVER['REQUEST_METHOD'];

if ($method !== 'POST') {
    http_response_code(405);
    echo json_encode(['status' => 'error', 'message' => 'Method not allowed. Use POST.']);
    exit();
}

// Ensure contact_submissions table exists
$pdo->exec("
    CREATE TABLE IF NOT EXISTS contact_submissions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(255) NOT NULL,
        email VARCHAR(255) NOT NULL,
        phone VARCHAR(64) DEFAULT NULL,
        subject VARCHAR(255) DEFAULT 'General Inquiry',
        message TEXT NOT NULL,
        ip_address VARCHAR(45) DEFAULT NULL,
        user_agent TEXT DEFAULT NULL,
        status VARCHAR(32) DEFAULT 'new',
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
");

// Read input from JSON or standard POST
$rawInput = file_get_contents('php://input');
$data = json_decode($rawInput, true);

if (!$data) {
    $data = $_POST;
}

$name    = trim($data['name'] ?? '');
$email   = trim($data['email'] ?? '');
$phone   = trim($data['phone'] ?? '');
$subject = trim($data['subject'] ?? 'Statutory Due Diligence & Terminal Inquiry');
$message = trim($data['message'] ?? '');

// Validation
if (empty($name) || empty($message)) {
    http_response_code(422);
    echo json_encode(['status' => 'error', 'message' => 'Name and message are required fields.']);
    exit();
}

if (empty($email)) {
    http_response_code(422);
    echo json_encode(['status' => 'error', 'message' => 'Please provide a valid email address.']);
    exit();
}

if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
    http_response_code(422);
    echo json_encode(['status' => 'error', 'message' => 'Invalid email address format.']);
    exit();
}

$ipAddress = $_SERVER['REMOTE_ADDR'] ?? '127.0.0.1';
$userAgent = substr($_SERVER['HTTP_USER_AGENT'] ?? 'Unknown Browser', 0, 255);

// Insert into database
try {
    $stmt = $pdo->prepare("
        INSERT INTO contact_submissions 
        (name, email, phone, subject, message, ip_address, user_agent, status) 
        VALUES (:name, :email, :phone, :subject, :message, :ip, :ua, 'new')
    ");

    $stmt->execute([
        ':name'    => $name,
        ':email'   => $email,
        ':phone'   => $phone ?: null,
        ':subject' => $subject,
        ':message' => $message,
        ':ip'      => $ipAddress,
        ':ua'      => $userAgent
    ]);

    $inquiryId = $pdo->lastInsertId();

    // Transmit email directly to contact@exainfra.in
    $recipient = defined('ADMIN_EMAIL') ? ADMIN_EMAIL : 'contact@exainfra.in';
    $emailSubject = "[ExaInfra Inquiry #{$inquiryId}] {$subject} - {$name}";

    $emailBody = "====================================================\n"
               . "NEW INQUIRY TRANSMITTED TO CONTACT@EXAINFRA.IN\n"
               . "====================================================\n\n"
               . "Inquiry ID : EXA-INQ-{$inquiryId}\n"
               . "Sender Name: {$name}\n"
               . "Email      : {$email}\n"
               . "Subject    : {$subject}\n"
               . "Date (IST) : " . date('Y-m-d H:i:s') . "\n"
               . "Client IP  : {$ipAddress}\n\n"
               . "MESSAGE CONTENT:\n"
               . "----------------------------------------------------\n"
               . $message . "\n"
               . "----------------------------------------------------\n\n"
               . "Republic of India Sovereign Statutory Terminal\n"
               . "ExaInfra.in • Legal, Valuation & Due Diligence Desk\n";

    $headers = [];
    $headers[] = 'From: ExaInfra Portal <no-reply@exainfra.in>';
    if (!empty($email)) {
        $headers[] = "Reply-To: {$name} <{$email}>";
    }
    $headers[] = 'X-Mailer: PHP/' . phpversion();
    $headers[] = 'Content-Type: text/plain; charset=UTF-8';

    $mailSent = @mail($recipient, $emailSubject, $emailBody, implode("\r\n", $headers));

    echo json_encode([
        'status'     => 'success',
        'message'    => 'Your message has been securely transmitted to contact@exainfra.in.',
        'inquiry_id' => $inquiryId,
        'email_sent' => (bool)$mailSent,
        'recipient'  => $recipient
    ]);
    exit();

} catch (Exception $e) {
    error_log("Error saving contact submission: " . $e->getMessage());
    http_response_code(500);
    echo json_encode([
        'status'  => 'error',
        'message' => 'Failed to save submission. Please contact us directly at contact@exainfra.in.'
    ]);
    exit();
}
