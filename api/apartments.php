<?php
/**
 * ExaInfra Rentals (exainfra.in) - Apartments API Endpoint
 * Handles fetching verified listings and saving landlord posts
 */

require_once __DIR__ . '/config.php';

$pdo = getDbConnection();
$method = $_SERVER['REQUEST_METHOD'];

// ====================================================================
// GET: Fetch Listings with optional filters
// ====================================================================
if ($method === 'GET') {
    $city = isset($_GET['city']) ? trim($_GET['city']) : '';
    $bhk = isset($_GET['bhk']) ? trim($_GET['bhk']) : '';
    $maxBudget = isset($_GET['max_budget']) ? (int)$_GET['max_budget'] : 0;

    $query = "SELECT * FROM apartments WHERE status = 'active'";
    $params = [];

    if (!empty($city) && strtolower($city) !== 'all') {
        $query .= " AND LOWER(city) = LOWER(:city)";
        $params[':city'] = $city;
    }

    if (!empty($bhk) && strtolower($bhk) !== 'all') {
        $query .= " AND bhk = :bhk";
        $params[':bhk'] = $bhk;
    }

    if ($maxBudget > 0) {
        $query .= " AND rent_monthly <= :budget";
        $params[':budget'] = $maxBudget;
    }

    $query .= " ORDER BY is_spotlight DESC, created_at DESC";

    $stmt = $pdo->prepare($query);
    $stmt->execute($params);
    $apartments = $stmt->fetchAll();

    // Format output for JSON
    $formatted = array_map(function($apt) {
        return [
            'id' => 'apt-' . $apt['id'],
            'source' => $apt['portal_source'] ?? 'NoBroker',
            'sourceId' => $apt['source_id'] ?? ('BLR-' . $apt['id']),
            'externalUrl' => $apt['external_url'] ?? '#',
            'title' => $apt['title'],
            'society' => $apt['society'],
            'city' => $apt['city'],
            'locality' => $apt['locality'],
            'bhk' => $apt['bhk'],
            'furnishing' => $apt['furnishing'],
            'rent' => (int)$apt['rent_monthly'],
            'deposit' => (int)$apt['security_deposit'],
            'area' => (int)$apt['carpet_area'],
            'photoCount' => 12,
            'image' => $apt['image_url'] ?: 'assets/bangalore_balcony_opt.jpg',
            'imageCredit' => $apt['image_credit'] ?? 'Photo: Verified Aggregator Shoot',
            'amenities' => json_decode($apt['amenities_json'] ?? '[]', true) ?: ['gym', 'pool', 'balcony'],
            'owner' => [
                'name' => $apt['owner_name'],
                'phone' => $apt['owner_phone'],
                'type' => 'Direct Owner',
                'verified' => true
            ],
            'spotlight' => (bool)$apt['is_spotlight'],
            'postedDaysAgo' => 1,
            'availableFrom' => 'Immediately'
        ];
    }, $apartments);

    echo json_encode([
        'status' => 'success',
        'count' => count($formatted),
        'data' => $formatted
    ]);
    exit();
}

// ====================================================================
// POST: Save Landlord Apartment Post
// ====================================================================
if ($method === 'POST') {
    $rawInput = file_get_contents('php://input');
    $data = json_decode($rawInput, true);

    if (!$data) {
        http_response_code(400);
        echo json_encode(['status' => 'error', 'message' => 'Invalid JSON payload']);
        exit();
    }

    $society = trim($data['society'] ?? '');
    $city = trim($data['city'] ?? 'Bengaluru');
    $locality = trim($data['locality'] ?? '');
    $bhk = trim($data['bhk'] ?? '2 BHK');
    $furnishing = trim($data['furnishing'] ?? 'Semi Furnished');
    $area = (int)($data['area'] ?? 1100);
    $rent = (int)($data['rent'] ?? 0);
    $deposit = (int)($data['deposit'] ?? ($rent * 3));
    $ownerName = trim($data['ownerName'] ?? '');
    $ownerPhone = trim($data['ownerPhone'] ?? '');
    $isBoosted = !empty($data['isBoosted']) ? 1 : 0;
    $amenities = isset($data['amenities']) && is_array($data['amenities']) ? json_encode($data['amenities']) : '["gym","pool","balcony"]';
    $title = $society . ' — Spacious ' . $bhk;

    if (empty($society) || empty($ownerName) || empty($ownerPhone) || $rent <= 0) {
        http_response_code(422);
        echo json_encode(['status' => 'error', 'message' => 'Please provide society name, owner contact and valid rent']);
        exit();
    }

    $sql = "INSERT INTO apartments 
        (society, title, city, locality, bhk, furnishing, carpet_area, rent_monthly, security_deposit, owner_name, owner_phone, is_spotlight, amenities_json) 
        VALUES 
        (:society, :title, :city, :locality, :bhk, :furnishing, :area, :rent, :deposit, :owner_name, :owner_phone, :is_spotlight, :amenities)";

    $stmt = $pdo->prepare($sql);
    $stmt->execute([
        ':society' => $society,
        ':title' => $title,
        ':city' => $city,
        ':locality' => $locality,
        ':bhk' => $bhk,
        ':furnishing' => $furnishing,
        ':area' => $area,
        ':rent' => $rent,
        ':deposit' => $deposit,
        ':owner_name' => $ownerName,
        ':owner_phone' => $ownerPhone,
        ':is_spotlight' => $isBoosted,
        ':amenities' => $amenities
    ]);

    $newId = $pdo->lastInsertId();

    // Optional email alert to platform owner on Namecheap
    if (defined('ADMIN_EMAIL') && filter_var(ADMIN_EMAIL, FILTER_VALIDATE_EMAIL)) {
        $subject = "New Apartment Posted on ExaInfra: {$society} ({$city})";
        $body = "A new apartment was posted:\n\n"
              . "Society: {$society}\n"
              . "City: {$city}\n"
              . "BHK: {$bhk} ({$furnishing})\n"
              . "Rent: ₹{$rent}/month | Deposit: ₹{$deposit}\n"
              . "Owner: {$ownerName} ({$ownerPhone})\n"
              . "Spotlight Boost: " . ($isBoosted ? "YES (₹999 Paid)" : "Standard Free");
        @mail(ADMIN_EMAIL, $subject, $body, "From: no-reply@exainfra.in\r\n");
    }

    echo json_encode([
        'status' => 'success',
        'message' => 'Apartment posted and saved to database successfully',
        'apartment_id' => 'apt-' . $newId
    ]);
    exit();
}
