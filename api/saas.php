<?php
/**
 * ExaInfra Rentals (exainfra.in) - Landlord & PG Management SaaS API
 * Handles landlord property units, tenant rent tracking, UPI payment links & maintenance tickets
 */

require_once __DIR__ . '/config.php';

$pdo = getDbConnection();
$method = $_SERVER['REQUEST_METHOD'];

// ====================================================================
// GET: Fetch Landlord Dashboard Data
// ====================================================================
if ($method === 'GET') {
    $action = $_GET['action'] ?? 'dashboard';

    if ($action === 'dashboard') {
        echo json_encode([
            'status' => 'success',
            'kpis' => [
                'total_units' => 4,
                'monthly_rent_collected' => 145000,
                'pending_rent' => 38000,
                'security_deposits_held' => 420000,
                'occupancy_rate' => '100%'
            ],
            'units' => [
                [
                    'unit_id' => 'UNIT-302',
                    'society' => 'Prestige Falcon City',
                    'bhk' => '3 BHK',
                    'tenant_name' => 'Aditya Saxena',
                    'tenant_phone' => '',
                    'monthly_rent' => 48000,
                    'deposit_held' => 144000,
                    'rent_status' => 'paid',
                    'paid_date' => '05 Oct 2026',
                    'due_date' => '05 Nov 2026',
                    'lease_end' => '15 Aug 2027'
                ],
                [
                    'unit_id' => 'UNIT-104',
                    'society' => 'Sobha Dream Acres',
                    'bhk' => '2 BHK',
                    'tenant_name' => 'Sneha Rao',
                    'tenant_phone' => '',
                    'monthly_rent' => 38000,
                    'deposit_held' => 110000,
                    'rent_status' => 'due_soon',
                    'paid_date' => null,
                    'due_date' => '28 Oct 2026',
                    'lease_end' => '30 Mar 2027'
                ],
                [
                    'unit_id' => 'UNIT-201',
                    'society' => 'Godrej Eternity',
                    'bhk' => '2 BHK',
                    'tenant_name' => 'Rahul Mehta',
                    'tenant_phone' => '',
                    'monthly_rent' => 33000,
                    'deposit_held' => 99000,
                    'rent_status' => 'paid',
                    'paid_date' => '01 Oct 2026',
                    'due_date' => '01 Nov 2026',
                    'lease_end' => '31 Dec 2026'
                ],
                [
                    'unit_id' => 'UNIT-112',
                    'society' => 'Raheja Residency',
                    'bhk' => '2 BHK',
                    'tenant_name' => 'Arjun Nambiar',
                    'tenant_phone' => '',
                    'monthly_rent' => 26000,
                    'deposit_held' => 67000,
                    'rent_status' => 'paid',
                    'paid_date' => '03 Oct 2026',
                    'due_date' => '03 Nov 2026',
                    'lease_end' => '30 Jun 2027'
                ]
            ],
            'tickets' => [
                [
                    'ticket_id' => 'TCK-801',
                    'unit_id' => 'UNIT-302',
                    'issue' => 'Master Bedroom AC Servicing & Cooling Check',
                    'status' => 'in_progress',
                    'reported_date' => '22 Oct 2026',
                    'priority' => 'High'
                ],
                [
                    'ticket_id' => 'TCK-802',
                    'unit_id' => 'UNIT-104',
                    'issue' => 'Kitchen RO Water Purifier Filter Replacement',
                    'status' => 'pending_approval',
                    'reported_date' => '23 Oct 2026',
                    'priority' => 'Medium'
                ]
            ]
        ]);
        exit();
    }
}

// ====================================================================
// POST: Send UPI Payment Link / Add Maintenance Ticket
// ====================================================================
if ($method === 'POST') {
    $rawInput = file_get_contents('php://input');
    $data = json_decode($rawInput, true);

    $action = $data['action'] ?? 'send_rent_reminder';

    if ($action === 'send_rent_reminder') {
        $unitId = trim($data['unitId'] ?? '');
        $tenantName = trim($data['tenantName'] ?? 'Tenant');
        $tenantPhone = trim($data['tenantPhone'] ?? '');
        $amount = (int)($data['amount'] ?? 0);

        // Simulated UPI Payment Intent Link
        $upiLink = "upi://pay?pa=exainfra.landlord@okhdfcbank&pn=ExaInfra%20Rentals&am={$amount}&cu=INR&tn=Rent%20for%20{$unitId}";

        echo json_encode([
            'status' => 'success',
            'message' => "Automated WhatsApp Rent reminder sent to {$tenantName} ({$tenantPhone}) for ₹" . number_format($amount),
            'upi_link' => $upiLink,
            'timestamp' => date('Y-m-d H:i:s')
        ]);
        exit();
    }

    if ($action === 'update_ticket_status') {
        $ticketId = trim($data['ticketId'] ?? '');
        $newStatus = trim($data['status'] ?? 'resolved');

        echo json_encode([
            'status' => 'success',
            'message' => "Ticket {$ticketId} marked as " . strtoupper($newStatus),
            'ticket_id' => $ticketId,
            'new_status' => $newStatus
        ]);
        exit();
    }
}

http_response_code(400);
echo json_encode(['status' => 'error', 'message' => 'Invalid SaaS request']);
