# Namecheap Shared Hosting (cPanel) Deployment Guide for exainfra.in

This guide explains how to deploy **exainfra.in** to your **Namecheap Shared Hosting** (Stellar / Stellar Plus) account and connect the MySQL customer database.

---

## Step 1: Create Your MySQL Database in cPanel

1. Log into your **Namecheap Account** and open **cPanel**.
2. Under the **Databases** section, click on **MySQL Databases**.
3. Under **Create New Database**, enter a name like `exainfra` (your full name will be `youruser_exainfra`) and click **Create Database**.
4. Scroll down to **Add New User**:
   - Username: `dbuser` (e.g., `youruser_dbuser`)
   - Password: Click **Password Generator** (copy this password)
   - Click **Create User**.
5. Scroll down to **Add User To Database**:
   - Select your user and your database.
   - Click **Add**.
   - Check the box **ALL PRIVILEGES** and click **Make Changes**.

---

## Step 2: Import the Database Tables via phpMyAdmin

1. In cPanel, click **phpMyAdmin** (under Databases).
2. On the left sidebar, click on your newly created database (`youruser_exainfra`).
3. Click the **Import** tab at the top.
4. Click **Choose File** and select:
   `api/schema.sql` (from your project folder).
5. Scroll to the bottom and click **Import** (or **Go**).
   > ✅ All 4 customer tables (`apartments`, `tenant_leads`, `scheduled_visits`, `rental_agreements`) will be created instantly with seed listings!

---

## Step 3: Enter Database Credentials in `api/config.php`

Open [`api/config.php`](api/config.php) and update lines 24–27 with your cPanel database info:

```php
define('DB_HOST', 'localhost');                  // Keep as localhost on Namecheap
define('DB_NAME', 'youruser_exainfra');          // Your cPanel DB Name
define('DB_USER', 'youruser_dbuser');            // Your cPanel DB User
define('DB_PASS', 'YOUR_COPIED_PASSWORD');       // Your DB Password
define('ADMIN_EMAIL', 'help@exainfra.in');       // Email to receive instant alerts
```

---

## Step 4: Upload Your Files to Namecheap `public_html`

1. In cPanel, open **File Manager**.
2. Double-click the **`public_html`** directory (this is your root website folder for `exainfra.in`).
3. Upload all the files from this project:
   - `index.html`
   - `style.css`
   - `app.js`
   - `assets/` (folder with images)
   - `api/` (folder with `config.php`, `apartments.php`, `leads.php`)
4. Visit `https://exainfra.in` in your browser!

---

## 📊 How to View Customer Data & Revenue in phpMyAdmin

- Whenever someone posts a flat, it appears in the **`apartments`** table.
- Whenever someone buys the ₹399 Tenant Pass, it logs in the **`tenant_leads`** table with their name, phone number, and payment status.
- You can click **Export &rarr; Format: CSV (or Microsoft Excel)** in phpMyAdmin at any time to download your full customer lead list!

---

## 💾 Zero-Storage Architecture: Saving Disk Space on Namecheap

Because Namecheap shared hosting plans (Stellar / Stellar Plus) have disk space limits and inode quotas, **ExaInfra uses a zero-storage aggregator design**:
1. **No local image accumulation**: Instead of storing hundreds of megabytes of heavy apartment photos on your hosting disk, listings store high-speed remote CDN image references (`image_url`) and outbound redirect URLs (`external_url`).
2. **Instant external redirection**: Every card features a prominent 1-click **"View on [NoBroker / Housing / MagicBricks / 99acres] ↗"** redirect button that sends prospective tenants directly to the original verified listing on the respective aggregator's website.
3. **Microscopic database footprint**: Only textual and financial metadata (society, BHK, rent, deposit, locality, owner contact) is stored in MySQL, taking less than 1–2 megabytes for thousands of listings. Your Namecheap server never runs out of disk space or hits inode limits!
