-- ====================================================================
-- ExaInfra Rentals & SaaS (exainfra.in) - Unified Production MySQL Schema
-- Direct Owner Rentals • Digital Lease Agreements • Landlord SaaS
-- ====================================================================

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+05:30";

-- --------------------------------------------------------
-- Table: users (Landlords & Tenants with Free Allowance Quotas)
-- --------------------------------------------------------
CREATE TABLE IF NOT EXISTS `users` (
  `id` INT AUTO_INCREMENT PRIMARY KEY,
  `name` VARCHAR(150) NOT NULL,
  `email` VARCHAR(191) NOT NULL UNIQUE,
  `phone` VARCHAR(50) NOT NULL,
  `role` ENUM('tenant', 'landlord') NOT NULL DEFAULT 'tenant',
  `free_posts_remaining` INT NOT NULL DEFAULT 5, -- 5 Free Property Postings for Landlords
  `free_chats_remaining` INT NOT NULL DEFAULT 20, -- 20 Free Landlord Inquiries for Tenants
  `is_premium` TINYINT(1) NOT NULL DEFAULT 0,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------
-- Table: apartments (Direct Owner Flat Listings)
-- --------------------------------------------------------
CREATE TABLE IF NOT EXISTS `apartments` (
  `id` INT AUTO_INCREMENT PRIMARY KEY,
  `user_id` INT DEFAULT NULL,
  `listing_type` VARCHAR(50) NOT NULL DEFAULT 'direct_owner',
  `society` VARCHAR(191) NOT NULL,
  `title` VARCHAR(255) NOT NULL,
  `city` VARCHAR(100) NOT NULL DEFAULT 'Bengaluru',
  `locality` VARCHAR(255) NOT NULL,
  `bhk` VARCHAR(50) NOT NULL,
  `furnishing` VARCHAR(50) NOT NULL,
  `carpet_area` INT NOT NULL DEFAULT 1100,
  `rent_monthly` INT NOT NULL,
  `security_deposit` INT NOT NULL,
  `owner_name` VARCHAR(150) NOT NULL,
  `owner_phone` VARCHAR(50) NOT NULL,
  `is_spotlight` TINYINT(1) NOT NULL DEFAULT 0,
  `status` ENUM('active', 'pending_verification', 'rented_out', 'hidden') DEFAULT 'active',
  `amenities_json` TEXT DEFAULT NULL,
  `image_url` VARCHAR(500) DEFAULT 'https://images.unsplash.com/photo-1545324418-cc1a3fa10c00?auto=format&fit=crop&w=800&q=80',
  `image_credit` VARCHAR(255) DEFAULT 'Photo: Verified Direct Owner Inspection',
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  INDEX (`user_id`),
  INDEX (`city`),
  INDEX (`bhk`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------
-- Table: chat_conversations (Direct Landlord-Tenant Messaging)
-- --------------------------------------------------------
CREATE TABLE IF NOT EXISTS `chat_conversations` (
  `id` INT AUTO_INCREMENT PRIMARY KEY,
  `apartment_id` INT NOT NULL,
  `landlord_name` VARCHAR(150) NOT NULL,
  `landlord_phone` VARCHAR(50) NOT NULL,
  `tenant_id` INT DEFAULT NULL,
  `tenant_name` VARCHAR(150) NOT NULL,
  `tenant_phone` VARCHAR(50) NOT NULL,
  `last_message` TEXT,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  INDEX (`apartment_id`),
  INDEX (`tenant_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------
-- Table: chat_messages (Message Thread)
-- --------------------------------------------------------
CREATE TABLE IF NOT EXISTS `chat_messages` (
  `id` INT AUTO_INCREMENT PRIMARY KEY,
  `conversation_id` INT NOT NULL,
  `sender_role` ENUM('tenant', 'landlord') NOT NULL,
  `sender_name` VARCHAR(150) NOT NULL,
  `message_text` TEXT NOT NULL,
  `sent_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  INDEX (`conversation_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------
-- Table: scheduled_visits (Physical & Video Property Tour Bookings)
-- --------------------------------------------------------
CREATE TABLE IF NOT EXISTS `scheduled_visits` (
  `id` INT AUTO_INCREMENT PRIMARY KEY,
  `apartment_id` INT NOT NULL,
  `visitor_name` VARCHAR(150) NOT NULL,
  `visitor_phone` VARCHAR(50) NOT NULL,
  `preferred_datetime` VARCHAR(100) NOT NULL,
  `visit_type` ENUM('in_person', 'whatsapp_video') DEFAULT 'in_person',
  `status` ENUM('confirmed', 'completed', 'rescheduled', 'cancelled') DEFAULT 'confirmed',
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  INDEX (`apartment_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------
-- Table: property_confirmations (Confirmed Bookings & ₹10K Token Reservations)
-- --------------------------------------------------------
CREATE TABLE IF NOT EXISTS `property_confirmations` (
  `id` INT AUTO_INCREMENT PRIMARY KEY,
  `apartment_id` INT NOT NULL,
  `tenant_name` VARCHAR(150) NOT NULL,
  `tenant_phone` VARCHAR(50) NOT NULL,
  `tenant_email` VARCHAR(191) NOT NULL,
  `token_deposit` INT NOT NULL DEFAULT 10000,
  `move_in_date` DATE NOT NULL,
  `confirmation_code` VARCHAR(50) NOT NULL UNIQUE,
  `status` ENUM('confirmed_token_paid', 'lease_signed', 'cancelled') DEFAULT 'confirmed_token_paid',
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  INDEX (`apartment_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------
-- Table: rental_agreements (11-Month Legal Lease Deeds & E-Stamps)
-- --------------------------------------------------------
CREATE TABLE IF NOT EXISTS `rental_agreements` (
  `id` INT AUTO_INCREMENT PRIMARY KEY,
  `agreement_code` VARCHAR(50) NOT NULL UNIQUE,
  `owner_name` VARCHAR(150) NOT NULL,
  `tenant_name` VARCHAR(150) NOT NULL,
  `property_address` TEXT NOT NULL,
  `monthly_rent` INT NOT NULL,
  `security_deposit` INT NOT NULL,
  `tenure` VARCHAR(50) DEFAULT '11 Months',
  `notice_period` VARCHAR(50) DEFAULT '1 Month',
  `has_estamp` TINYINT(1) DEFAULT 0,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------
-- Table: tenant_leads (Purchased Freedom Passes & Upgrades)
-- --------------------------------------------------------
CREATE TABLE IF NOT EXISTS `tenant_leads` (
  `id` INT AUTO_INCREMENT PRIMARY KEY,
  `tenant_name` VARCHAR(150) NOT NULL,
  `tenant_phone` VARCHAR(50) NOT NULL,
  `apartment_id` INT DEFAULT NULL,
  `pass_type` VARCHAR(100) NOT NULL DEFAULT 'tenant_freedom_pass',
  `amount_paid` DECIMAL(10,2) NOT NULL DEFAULT 399.00,
  `payment_status` VARCHAR(50) NOT NULL DEFAULT 'paid',
  `payment_method` VARCHAR(50) DEFAULT 'UPI',
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------
-- Table: landlord_units_saas (Landlord Property Management & UPI Ledger)
-- --------------------------------------------------------
CREATE TABLE IF NOT EXISTS `landlord_units_saas` (
  `id` INT AUTO_INCREMENT PRIMARY KEY,
  `unit_code` VARCHAR(50) NOT NULL UNIQUE,
  `society` VARCHAR(191) NOT NULL,
  `tenant_name` VARCHAR(150) NOT NULL,
  `tenant_phone` VARCHAR(50) NOT NULL,
  `monthly_rent` INT NOT NULL,
  `deposit_held` INT NOT NULL,
  `rent_status` ENUM('paid', 'due_soon', 'overdue') DEFAULT 'paid',
  `next_due_date` DATE NOT NULL,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------
-- Seed Users
-- --------------------------------------------------------
INSERT INTO `users` (`name`, `email`, `phone`, `role`, `free_posts_remaining`, `free_chats_remaining`, `is_premium`) VALUES
('Vikramaditya Sharma', 'vikram@landlord.com', '', 'landlord', 4, 20, 0),
('Aditya Saxena', 'aditya@tenant.com', '', 'tenant', 5, 18, 0);

-- --------------------------------------------------------
-- Seed Initial Direct Owner Apartments
-- --------------------------------------------------------
INSERT INTO `apartments` (`society`, `title`, `city`, `locality`, `bhk`, `furnishing`, `carpet_area`, `rent_monthly`, `security_deposit`, `owner_name`, `owner_phone`, `is_spotlight`, `amenities_json`, `image_url`, `image_credit`) VALUES
('Prestige Falcon City', 'Prestige Falcon City — High-Rise 3 BHK', 'Bengaluru', 'Kanakapura Road, Near Forum South Mall', '3 BHK', 'Fully Furnished', 1650, 52000, 156000, 'Suresh Prabhu', '', 1, '["gym","pool","pets","balcony"]', 'https://images.unsplash.com/photo-1545324418-cc1a3fa10c00?auto=format&fit=crop&w=800&q=80', 'Photo: Verified Direct Owner Inspection'),
('Sobha Dream Acres', 'Sobha Dream Acres — Garden View 2 BHK', 'Bengaluru', 'Panathur Main Road, Outer Ring Road', '2 BHK', 'Semi Furnished', 1050, 38000, 110000, 'Karthik Raman', '', 0, '["gym","pool","power-backup"]', 'https://images.unsplash.com/photo-1502672260266-1c1ef2d93688?auto=format&fit=crop&w=800&q=80', 'Photo: Direct Owner Verified'),
('Prestige Shantiniketan', 'Prestige Shantiniketan — Executive 3 BHK', 'Bengaluru', 'Whitefield Main Road, Near ITPL', '3 BHK', 'Fully Furnished', 1930, 65000, 200000, 'Priyanka Singhania', '', 1, '["gym","pool","clubhouse"]', 'https://images.unsplash.com/photo-1556911220-e15b29be8c8f?auto=format&fit=crop&w=800&q=80', 'Photo: Verified Direct Owner Inspection'),
('Godrej Eternity', 'Godrej Eternity — Serene 2 BHK with Green Balcony', 'Bengaluru', 'Holiday Village Road, Kanakapura', '2 BHK', 'Semi Furnished', 1120, 33000, 99000, 'Rajesh Varma', '', 0, '["gym","pool","pets"]', 'https://images.unsplash.com/photo-1522771739844-6a9f6d5f14af?auto=format&fit=crop&w=800&q=80', 'Photo: Direct Owner Verified'),
('Adarsh Palm Retreat', 'Adarsh Palm Retreat — Luxury 4 BHK Tower Villa', 'Bengaluru', 'Bellandur, Outer Ring Road Tech Corridor', '4+ BHK', 'Fully Furnished', 3200, 115000, 350000, 'Dr. Venkat Rao', '', 1, '["gym","pool","pets","concierge"]', 'https://images.unsplash.com/photo-1600585154340-be6161a56a0c?auto=format&fit=crop&w=800&q=80', 'Photo: Verified Direct Owner Inspection'),
('Salarpuria Sattva Senorita', 'Salarpuria Sattva Senorita — Sunlit 3 BHK', 'Bengaluru', 'Sarjapur Main Road, Near Wipro Corporate Office', '3 BHK', 'Semi Furnished', 1580, 54000, 160000, 'Nitin Deshpande', '', 0, '["gym","pool","power-backup"]', 'https://images.unsplash.com/photo-1512917774080-9991f1c4c750?auto=format&fit=crop&w=800&q=80', 'Photo: Direct Owner Verified'),
('Purva Fountain Square', 'Purva Fountain Square — Premium 2 BHK Flat', 'Bengaluru', 'Marathahalli, Old Airport Road', '2 BHK', 'Fully Furnished', 1240, 42000, 120000, 'Meenakshi Joshi', '', 0, '["gym","pool","gated"]', 'https://images.unsplash.com/photo-1560448204-e02f11c3d0e2?auto=format&fit=crop&w=800&q=80', 'Photo: Direct Owner Verified'),
('Brigade Metropolis', 'Brigade Metropolis — High-Floor 3 BHK', 'Bengaluru', 'Mahadevapura, Near Whitefield', '3 BHK', 'Semi Furnished', 1750, 58000, 175000, 'Vikramaditya Hegde', '', 0, '["gym","pool","pets"]', 'https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?auto=format&fit=crop&w=800&q=80', 'Photo: Direct Owner Verified');

COMMIT;
