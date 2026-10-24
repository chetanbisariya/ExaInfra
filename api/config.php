<?php
/**
 * ExaInfra Rentals (exainfra.in) - Database Configuration
 * Compatible with Namecheap Shared Hosting (cPanel MySQL) & Local Dev (SQLite)
 */

header('Content-Type: application/json; charset=UTF-8');
header('Access-Control-Allow-Origin: *');
header('Access-Control-Allow-Methods: GET, POST, OPTIONS');
header('Access-Control-Allow-Headers: Content-Type, Authorization');

// Security Headers (Defense in depth)
header('X-Content-Type-Options: nosniff');
header('X-Frame-Options: DENY');
header('X-XSS-Protection: 1; mode=block');
header('Referrer-Policy: strict-origin-when-cross-origin');

if ($_SERVER['REQUEST_METHOD'] === 'OPTIONS') {
    http_response_code(200);
    exit();
}

// ====================================================================
// NAMECHEAP cPANEL MYSQL CREDENTIALS
// Fill these in after creating your database in cPanel -> MySQL Databases
// ====================================================================
define('DB_HOST', 'localhost'); // Namecheap standard is 'localhost'
define('DB_NAME', 'yourcpanel_exainfra'); // e.g., chetan_exainfra
define('DB_USER', 'yourcpanel_dbuser');   // e.g., chetan_dbuser
define('DB_PASS', 'YOUR_STRONG_PASSWORD');

// Official Admin notification & Contact email
define('ADMIN_EMAIL', 'contact@exainfra.in');

function getDbConnection() {
    static $pdo = null;
    if ($pdo !== null) {
        return $pdo;
    }

    // Try MySQL first if credentials have been configured
    if (DB_NAME !== 'yourcpanel_exainfra' && DB_PASS !== 'YOUR_STRONG_PASSWORD') {
        try {
            $dsn = "mysql:host=" . DB_HOST . ";dbname=" . DB_NAME . ";charset=utf8mb4";
            $pdo = new PDO($dsn, DB_USER, DB_PASS, [
                PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
                PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
                PDO::ATTR_EMULATE_PREPARES => false,
            ]);
            return $pdo;
        } catch (PDOException $e) {
            // If MySQL connection fails, fall back to SQLite for seamless resilience
            error_log("MySQL Connection failed: " . $e->getMessage());
        }
    }

    // Fallback: Local file-based SQLite database (works out of the box with zero setup!)
    try {
        $dbPath = __DIR__ . '/exainfra.sqlite';
        $pdo = new PDO("sqlite:" . $dbPath);
        $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
        $pdo->setAttribute(PDO::ATTR_DEFAULT_FETCH_MODE, PDO::FETCH_ASSOC);

        // Auto-create tables if sqlite file is new
        $pdo->exec("
            CREATE TABLE IF NOT EXISTS apartments (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                society TEXT NOT NULL,
                title TEXT NOT NULL,
                city TEXT NOT NULL,
                locality TEXT NOT NULL,
                bhk TEXT NOT NULL,
                furnishing TEXT NOT NULL,
                carpet_area INTEGER DEFAULT 1000,
                rent_monthly INTEGER NOT NULL,
                security_deposit INTEGER NOT NULL,
                owner_name TEXT NOT NULL,
                owner_phone TEXT NOT NULL,
                is_spotlight INTEGER DEFAULT 0,
                status TEXT DEFAULT 'active',
                amenities_json TEXT,
                image_url TEXT DEFAULT 'assets/apartment_living.jpg',
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP
            );

            CREATE TABLE IF NOT EXISTS tenant_leads (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                tenant_name TEXT NOT NULL,
                tenant_phone TEXT NOT NULL,
                apartment_id INTEGER,
                pass_type TEXT DEFAULT 'tenant_freedom_pass',
                amount_paid REAL DEFAULT 399.00,
                payment_status TEXT DEFAULT 'paid',
                payment_method TEXT DEFAULT 'UPI',
                transaction_ref TEXT,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP
            );

            CREATE TABLE IF NOT EXISTS scheduled_visits (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                apartment_id INTEGER NOT NULL,
                visitor_name TEXT NOT NULL,
                visitor_phone TEXT NOT NULL,
                preferred_datetime TEXT NOT NULL,
                visit_type TEXT DEFAULT 'physical',
                status TEXT DEFAULT 'confirmed',
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP
            );

            CREATE TABLE IF NOT EXISTS rental_agreements (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                owner_name TEXT NOT NULL,
                tenant_name TEXT NOT NULL,
                property_address TEXT NOT NULL,
                monthly_rent INTEGER NOT NULL,
                security_deposit INTEGER NOT NULL,
                tenure TEXT DEFAULT '11 Months',
                notice_period TEXT DEFAULT '1 Month',
                stamp_duty_amount REAL DEFAULT 500.00,
                total_fee REAL DEFAULT 1299.00,
                aadhaar_sign_status TEXT DEFAULT 'draft',
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP
            );
        ");

        return $pdo;
    } catch (PDOException $e) {
        http_response_code(500);
        echo json_encode(['error' => 'Database initialization failed: ' . $e->getMessage()]);
        exit();
    }
}
