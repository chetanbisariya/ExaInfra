<?php
/**
 * ExaInfra Rentals (exainfra.in) - Leads, Revenue & Visit Bookings API
 * Saves paid customer passes, owner contact unlocks, and visit requests
 */

require_once __DIR__ . '/config.php';

$pdo = getDbConnection();
$method = $_SERVER['REQUEST_METHOD'];

// ====================================================================
// POST: Save Customer Lead / Payment / Visit
// ====================================================================
if ($method === 'POST') {
    $rawInput = file_get_contents('php://input');
    $data = json_decode($rawInput, true);

    if (!$data) {
        http_response_code(400);
        echo json_encode(['status' => 'error', 'message' => 'Invalid JSON payload']);
        exit();
    }

    $action = $data['action'] ?? 'tenant_pass';

    // 0. Contact Us & Legal Advisory Inquiries -> contact@exainfra.in
    if ($action === 'contact_form') {
        $name    = trim($data['name'] ?? '');
        $email   = trim($data['email'] ?? '');
        $phone   = trim($data['phone'] ?? '');
        $subject = trim($data['subject'] ?? 'ExaInfra Portal Inquiry');
        $message = trim($data['message'] ?? '');

        if (empty($name) || empty($message)) {
            http_response_code(422);
            echo json_encode(['status' => 'error', 'message' => 'Name and message are required']);
            exit();
        }

        // Email alert to contact@exainfra.in
        $recipient = defined('ADMIN_EMAIL') ? ADMIN_EMAIL : 'contact@exainfra.in';
        $emailSubject = "[ExaInfra Inquiry] {$subject} from {$name}";
        $msg = "New Contact Us Submission on ExaInfra.in\n"
             . "----------------------------------------\n"
             . "Name   : {$name}\n"
             . "Email  : {$email}\n"
             . "Phone  : {$phone}\n"
             . "Subject: {$subject}\n"
             . "Date   : " . date('Y-m-d H:i:s') . "\n\n"
             . "Message:\n{$message}\n";
        @mail($recipient, $emailSubject, $msg, "From: no-reply@exainfra.in\r\nReply-To: {$email}\r\n");

        echo json_encode([
            'status' => 'success',
            'message' => 'Inquiry sent directly to contact@exainfra.in'
        ]);
        exit();
    }

    // 1. Tenant Pass / Contact Unlock
    if ($action === 'tenant_pass') {
        $tenantName = trim($data['name'] ?? '');
        $tenantPhone = trim($data['phone'] ?? '');
        $apartmentId = isset($data['apartmentId']) ? (int)str_replace('apt-', '', $data['apartmentId']) : null;
        $passType = trim($data['passType'] ?? 'tenant_freedom_pass');
        $amount = (float)($data['amount'] ?? 399.00);

        if (empty($tenantName) || empty($tenantPhone)) {
            http_response_code(422);
            echo json_encode(['status' => 'error', 'message' => 'Name and phone number are required']);
            exit();
        }

        $stmt = $pdo->prepare("INSERT INTO tenant_leads 
            (tenant_name, tenant_phone, apartment_id, pass_type, amount_paid, payment_status, payment_method) 
            VALUES (:name, :phone, :apt_id, :pass_type, :amount, 'paid', 'UPI')");
        
        $stmt->execute([
            ':name' => $tenantName,
            ':phone' => $tenantPhone,
            ':apt_id' => $apartmentId,
            ':pass_type' => $passType,
            ':amount' => $amount
        ]);

        $leadId = $pdo->lastInsertId();

        // Admin alert
        if (defined('ADMIN_EMAIL') && filter_var(ADMIN_EMAIL, FILTER_VALIDATE_EMAIL)) {
            $msg = "💰 New Revenue on ExaInfra: ₹{$amount}\n"
                 . "Customer: {$tenantName} ({$tenantPhone})\n"
                 . "Package: {$passType}\n"
                 . "Date: " . date('Y-m-d H:i:s');
            @mail(ADMIN_EMAIL, "New Tenant Pass Sold (₹{$amount})", $msg, "From: no-reply@exainfra.in\r\n");
        }

        echo json_encode([
            'status' => 'success',
            'message' => 'Lead and payment recorded successfully',
            'lead_id' => $leadId
        ]);
        exit();
    }

    // 2. Schedule Visit Booking & Tenant Move-In Lead
    if ($action === 'schedule_visit') {
        $visitorName = trim($data['name'] ?? '');
        $visitorPhone = trim($data['phone'] ?? '');
        $visitorEmail = trim($data['email'] ?? '');
        $apartmentId = trim($data['apartmentId'] ?? 'apt-unknown');
        $apartmentTitle = trim($data['apartmentTitle'] ?? 'Bangalore Rental Apartment');
        $portalSource = trim($data['portalSource'] ?? 'NoBroker');
        $moveInDate = trim($data['moveInDate'] ?? 'Immediate');
        $preferredSlot = trim($data['preferredSlot'] ?? 'Weekend Morning (10am-1pm)');
        $tenantType = trim($data['tenantType'] ?? 'Working Professional');
        $companyName = trim($data['companyName'] ?? '');
        $specialNotes = trim($data['specialNotes'] ?? '');

        if (empty($visitorName) || empty($visitorPhone)) {
            http_response_code(422);
            echo json_encode(['status' => 'error', 'message' => 'Name and phone number are required']);
            exit();
        }

        $stmt = $pdo->prepare("INSERT INTO scheduled_visits 
            (apartment_id, apartment_title, portal_source, visitor_name, visitor_phone, visitor_email, tentative_move_in_date, preferred_slot, tenant_type, company_name, special_notes, status) 
            VALUES (:apt_id, :apt_title, :portal, :name, :phone, :email, :move_in, :slot, :tenant_type, :company, :notes, 'new_lead')");
        
        $stmt->execute([
            ':apt_id' => $apartmentId,
            ':apt_title' => $apartmentTitle,
            ':portal' => $portalSource,
            ':name' => $visitorName,
            ':phone' => $visitorPhone,
            ':email' => $visitorEmail,
            ':move_in' => $moveInDate,
            ':slot' => $preferredSlot,
            ':tenant_type' => $tenantType,
            ':company' => $companyName,
            ':notes' => $specialNotes
        ]);

        $visitId = $pdo->lastInsertId();

        // Admin alert
        if (defined('ADMIN_EMAIL') && filter_var(ADMIN_EMAIL, FILTER_VALIDATE_EMAIL)) {
            $msg = "📅 New Visit & Move-In Lead on ExaInfra!\n"
                 . "Property: {$apartmentTitle} ({$portalSource})\n"
                 . "Seeker: {$visitorName} ({$visitorPhone})\n"
                 . "Tentative Move-In: {$moveInDate}\n"
                 . "Preferred Slot: {$preferredSlot}\n"
                 . "Profile: {$tenantType} at {$companyName}\n"
                 . "Notes: {$specialNotes}\n";
            @mail(ADMIN_EMAIL, "New Visit Request: {$visitorName} ({$moveInDate})", $msg, "From: no-reply@exainfra.in\r\n");
        }

        echo json_encode([
            'status' => 'success',
            'message' => 'Visit lead and move-in preference recorded successfully',
            'visit_id' => $visitId
        ]);
        exit();
    }

    // 2b. City Early Access Waitlist
    if ($action === 'city_waitlist') {
        $city = trim($data['city'] ?? 'Mumbai');
        $contact = trim($data['contact'] ?? '');

        if (empty($contact)) {
            http_response_code(422);
            echo json_encode(['status' => 'error', 'message' => 'Contact information is required']);
            exit();
        }

        $stmt = $pdo->prepare("INSERT INTO city_waitlist (city, contact_info) VALUES (:city, :contact)");
        $stmt->execute([':city' => $city, ':contact' => $contact]);

        echo json_encode([
            'status' => 'success',
            'message' => 'Added to early access waitlist'
        ]);
        exit();
    }

    // 3. Save Rental Agreement Draft
    if ($action === 'save_agreement') {
        $owner = trim($data['ownerName'] ?? '');
        $tenant = trim($data['tenantName'] ?? '');
        $address = trim($data['propertyAddress'] ?? '');
        $rent = (int)($data['rent'] ?? 0);
        $deposit = (int)($data['deposit'] ?? 0);
        $tenure = trim($data['tenure'] ?? '11 Months');

        $stmt = $pdo->prepare("INSERT INTO rental_agreements 
            (owner_name, tenant_name, property_address, monthly_rent, security_deposit, tenure) 
            VALUES (:owner, :tenant, :addr, :rent, :deposit, :tenure)");
        
        $stmt->execute([
            ':owner' => $owner,
            ':tenant' => $tenant,
            ':addr' => $address,
            ':rent' => $rent,
            ':deposit' => $deposit,
            ':tenure' => $tenure
        ]);

        echo json_encode([
            'status' => 'success',
            'message' => 'Agreement deed saved to database',
            'agreement_id' => $pdo->lastInsertId()
        ]);
        exit();
    }
}

// ====================================================================
// GET: Admin Revenue & Customer Summary
// ====================================================================
if ($method === 'GET') {
    $totalRevenue = $pdo->query("SELECT COALESCE(SUM(amount_paid), 0) AS total FROM tenant_leads WHERE payment_status = 'paid'")->fetch()['total'];
    $totalLeads = $pdo->query("SELECT COUNT(*) AS count FROM tenant_leads")->fetch()['count'];
    $totalVisits = $pdo->query("SELECT COUNT(*) AS count FROM scheduled_visits")->fetch()['count'];
    $recentLeads = $pdo->query("SELECT * FROM tenant_leads ORDER BY created_at DESC LIMIT 10")->fetchAll();

    echo json_encode([
        'status' => 'success',
        'metrics' => [
            'total_revenue_inr' => (float)$totalRevenue,
            'total_tenant_leads' => (int)$totalLeads,
            'total_scheduled_visits' => (int)$totalVisits
        ],
        'recent_leads' => $recentLeads
    ]);
    exit();
}
