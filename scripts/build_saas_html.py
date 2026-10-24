# Build clean, high-converting index.html focused 100% on Landlord SaaS, Legal Leases & HRA Studio

html_content = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>ExaInfra — Landlord & PG Management SaaS, UPI Rent Collection & Legal Lease Studio</title>
  <meta name="description" content="India's leading property management SaaS for landlords and PG operators. Automate UPI rent collection, send instant WhatsApp receipts, resolve maintenance tickets, and execute court-admissible 11-month e-stamped lease deeds.">
  <meta name="keywords" content="landlord saas, upi rent collection, automated rent receipts whatsapp, rental agreement online, 11 month lease deed, karnataka e-stamp rental agreement, hra rent receipts generator, tenant maintenance ticket tracker">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="style.css">
</head>
<body>

  <!-- Top Announcement Banner -->
  <div class="aggregator-ticker-bar" id="aggregatorTicker">
    <div class="ticker-content">
      <div class="live-crawler-status">
        <span class="crawler-pulse-dot"></span>
        <span class="ticker-label">EXAINFRA SAAS:</span>
      </div>
      <div class="ticker-marquee">
        <span id="tickerText">⚡ Automated UPI Rent Collection &bull; Instant WhatsApp Payment Receipts &bull; Court-Admissible 11-Month E-Stamped Lease Deeds &bull; Free 12-Month HRA Tax Receipts Package</span>
      </div>
      <a href="#pricing-plans" class="btn btn-xs btn-scanner-refresh" style="text-decoration:none;">
        <span>Explore SaaS Pricing &rarr;</span>
      </a>
    </div>
  </div>

  <!-- Main Navigation Header -->
  <header class="navbar" id="siteNavbar">
    <div class="nav-container">
      <a href="#" class="brand-logo" id="brandLogo">
        <div class="brand-icon">
          <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4">
            <path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path>
            <polyline points="9 22 9 12 15 12 15 22"></polyline>
          </svg>
        </div>
        <div class="brand-name">
          <div class="logo-top-row">
            <span class="logo-main">EXA<span class="logo-accent">INFRA</span></span>
            <span class="logo-aggregator-badge" style="background:#0284C7; color:#FFFFFF;">LANDLORD SAAS</span>
          </div>
          <span class="logo-sub">PROPERTY MANAGEMENT & LEGAL LEASE STUDIO</span>
        </div>
      </a>

      <!-- Desktop Nav Links -->
      <nav class="nav-links" id="navLinks">
        <a href="#landlord-saas" class="nav-link-item active">SaaS Dashboard</a>
        <a href="#rental-agreement" class="nav-link-item">11-Month Lease Deeds</a>
        <a href="#hra-tax-studio" class="nav-link-item">HRA Tax Receipts</a>
        <a href="#rent-estimator" class="nav-link-item">Rent & Yield Estimator</a>
        <a href="#pricing-plans" class="nav-link-item">SaaS Plans</a>
        <a href="#how-it-works" class="nav-link-item">How It Works</a>
      </nav>

      <!-- Nav Action CTAs -->
      <div class="nav-user-actions" style="display:flex; align-items:center; gap:0.75rem;">
        <button class="btn btn-sm btn-secondary" id="btnNavAddUnit" style="font-weight:700;">
          <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><line x1="12" y1="5" x2="12" y2="19"></line><line x1="5" y1="12" x2="19" y2="12"></line></svg>
          <span>Add Tenant Unit</span>
        </button>

        <a href="#landlord-saas" class="btn btn-sm btn-primary" style="text-decoration:none; font-weight:700;">
          <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="3" width="20" height="14" rx="2" ry="2"></rect><line x1="8" y1="21" x2="16" y2="21"></line><line x1="12" y1="17" x2="12" y2="21"></line></svg>
          <span>Launch Dashboard</span>
        </a>
      </div>
    </div>
  </header>

  <!-- Hero Section -->
  <section class="hero-section" style="padding: 4.5rem 0 3.5rem 0; background: linear-gradient(180deg, #0B1329 0%, #0F172A 100%);">
    <div class="container hero-container" style="text-align: center; max-width: 960px; margin: 0 auto;">
      <div class="hero-header-box">
        <div class="hero-live-badge" style="display: inline-flex; align-items: center; gap: 0.5rem; background: rgba(14, 165, 233, 0.15); border: 1px solid rgba(14, 165, 233, 0.35); padding: 0.35rem 0.9rem; border-radius: var(--radius-full); margin-bottom: 1.25rem;">
          <span class="live-dot-green"></span>
          <span style="color: #38BDF8; font-size: 0.78rem; font-weight: 800; letter-spacing: 0.05em;">SMART LANDLORD & PG AUTOMATION SUITE &bull; COURT E-STAMP LEASES</span>
        </div>

        <h1 class="hero-main-title" style="font-size: 3rem; line-height: 1.15; font-weight: 800; color: #FFFFFF; margin-bottom: 1rem;">
          Automate Rent Collection with UPI. <span class="highlight-coral">Sign E-Stamped Leases.</span><br>
          <span class="hero-sub-gradient">Manage All Your Properties on One Intelligent SaaS.</span>
        </h1>

        <p class="hero-subtext" style="font-size: 1.08rem; color: #94A3B8; line-height: 1.6; max-width: 800px; margin: 0 auto 2rem auto;">
          Say goodbye to delayed rent payments, messy spreadsheets, and lost deposit records. ExaInfra dispatches automated WhatsApp UPI payment links, generates instant rent receipts, tracks tenant maintenance tickets, and crafts legally binding 11-month rental agreements with official State E-Stamp Duty.
        </p>

        <!-- Hero Primary Action Buttons -->
        <div style="display: flex; justify-content: center; gap: 1rem; flex-wrap: wrap; margin-bottom: 3rem;">
          <a href="#landlord-saas" class="btn btn-primary btn-lg" style="text-decoration: none; font-weight: 700; padding: 0.85rem 1.75rem;">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><rect x="2" y="3" width="20" height="14" rx="2" ry="2"></rect><line x1="8" y1="21" x2="16" y2="21"></line><line x1="12" y1="17" x2="12" y2="21"></line></svg>
            <span>Launch Landlord Dashboard</span>
          </a>

          <a href="#rental-agreement" class="btn btn-secondary btn-lg" style="text-decoration: none; font-weight: 700; padding: 0.85rem 1.75rem; background: #1E293B; border-color: #334155; color: #FFFFFF;">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line></svg>
            <span>Draft 11-Month E-Stamped Lease</span>
          </a>

          <a href="#hra-tax-studio" class="btn btn-secondary btn-lg" style="text-decoration: none; font-weight: 700; padding: 0.85rem 1.75rem; background: #064E3B; border-color: #059669; color: #34D399;">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect><line x1="16" y1="2" x2="16" y2="6"></line><line x1="8" y1="2" x2="8" y2="6"></line><line x1="3" y1="10" x2="21" y2="10"></line></svg>
            <span>Free 12-Month HRA Receipts</span>
          </a>
        </div>

        <!-- Hero KPI Metrics Strip -->
        <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 1rem; background: rgba(30, 41, 59, 0.7); border: 1px solid #334155; padding: 1.25rem; border-radius: 12px; backdrop-filter: blur(8px);">
          <div>
            <div style="font-size: 1.5rem; font-weight: 800; color: #38BDF8;">₹2.8 Cr+</div>
            <div style="font-size: 0.8rem; color: #94A3B8;">Monthly Rent Collected</div>
          </div>
          <div>
            <div style="font-size: 1.5rem; font-weight: 800; color: #10B981;">100% Legal</div>
            <div style="font-size: 0.8rem; color: #94A3B8;">State E-Stamp & eSign</div>
          </div>
          <div>
            <div style="font-size: 1.5rem; font-weight: 800; color: #F59E0B;">4,200+</div>
            <div style="font-size: 0.8rem; color: #94A3B8;">Active Units & Tenants</div>
          </div>
          <div>
            <div style="font-size: 1.5rem; font-weight: 800; color: #E11D48;">0% Commission</div>
            <div style="font-size: 0.8rem; color: #94A3B8;">Zero Brokerage Always</div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Core Pillars Feature Grid -->
  <section style="padding: 3.5rem 0; background: #0B1120; border-top: 1px solid #1E293B; border-bottom: 1px solid #1E293B;">
    <div class="container">
      <div style="text-align: center; max-width: 720px; margin: 0 auto 2.5rem auto;">
        <span class="saas-tag">COMPLETE RENTAL INFRASTRUCTURE</span>
        <h2 style="font-size: 2rem; font-weight: 800; color: #F8FAFC; margin-bottom: 0.5rem;">Everything a Modern Landlord or Tenant Needs</h2>
        <p style="color: #94A3B8; font-size: 0.95rem;">From rent payment automation to court-admissible lease deeds and employee tax compliance.</p>
      </div>

      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1.5rem;">
        <!-- Card 1 -->
        <div style="background: #1E293B; border: 1px solid #334155; padding: 1.5rem; border-radius: 12px;">
          <div style="width: 44px; height: 44px; border-radius: 8px; background: rgba(14, 165, 233, 0.15); display: flex; align-items: center; justify-content: center; margin-bottom: 1rem; color: #38BDF8;">
            <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="5" width="20" height="14" rx="2"></rect><line x1="2" y1="10" x2="22" y2="10"></line></svg>
          </div>
          <h3 style="font-size: 1.15rem; font-weight: 700; color: #FFFFFF; margin-bottom: 0.4rem;">Automated WhatsApp & UPI Invoicing</h3>
          <p style="font-size: 0.88rem; color: #94A3B8; line-height: 1.5;">Send smart UPI payment intent links directly to your tenants' WhatsApp on the 1st of every month with one click.</p>
        </div>

        <!-- Card 2 -->
        <div style="background: #1E293B; border: 1px solid #334155; padding: 1.5rem; border-radius: 12px;">
          <div style="width: 44px; height: 44px; border-radius: 8px; background: rgba(16, 185, 129, 0.15); display: flex; align-items: center; justify-content: center; margin-bottom: 1rem; color: #34D399;">
            <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line></svg>
          </div>
          <h3 style="font-size: 1.15rem; font-weight: 700; color: #FFFFFF; margin-bottom: 0.4rem;">11-Month Court E-Stamped Lease Deeds</h3>
          <p style="font-size: 0.88rem; color: #94A3B8; line-height: 1.5;">Official Karnataka State E-Stamp Duty certificate + Aadhaar OTP biometric eSign. Legally enforceable in Indian courts.</p>
        </div>

        <!-- Card 3 -->
        <div style="background: #1E293B; border: 1px solid #334155; padding: 1.5rem; border-radius: 12px;">
          <div style="width: 44px; height: 44px; border-radius: 8px; background: rgba(245, 158, 11, 0.15); display: flex; align-items: center; justify-content: center; margin-bottom: 1rem; color: #FBBF24;">
            <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect><line x1="16" y1="2" x2="16" y2="6"></line><line x1="8" y1="2" x2="8" y2="6"></line><line x1="3" y1="10" x2="21" y2="10"></line></svg>
          </div>
          <h3 style="font-size: 1.15rem; font-weight: 700; color: #FFFFFF; margin-bottom: 0.4rem;">12-Month HRA Tax Receipts Package</h3>
          <p style="font-size: 0.88rem; color: #94A3B8; line-height: 1.5;">100% Free Section 10(13A) compliant rent receipts with authentic ₹1 revenue stamp graphics and landlord PAN declarations.</p>
        </div>

        <!-- Card 4 -->
        <div style="background: #1E293B; border: 1px solid #334155; padding: 1.5rem; border-radius: 12px;">
          <div style="width: 44px; height: 44px; border-radius: 8px; background: rgba(225, 29, 72, 0.15); display: flex; align-items: center; justify-content: center; margin-bottom: 1rem; color: #FB7185;">
            <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"></path></svg>
          </div>
          <h3 style="font-size: 1.15rem; font-weight: 700; color: #FFFFFF; margin-bottom: 0.4rem;">Tenant Maintenance & Repair Tracker</h3>
          <p style="font-size: 0.88rem; color: #94A3B8; line-height: 1.5;">Track geyser, AC, and plumbing issues with instant vendor assignment and one-click resolution status updates.</p>
        </div>

        <!-- Card 5 -->
        <div style="background: #1E293B; border: 1px solid #334155; padding: 1.5rem; border-radius: 12px;">
          <div style="width: 44px; height: 44px; border-radius: 8px; background: rgba(139, 92, 246, 0.15); display: flex; align-items: center; justify-content: center; margin-bottom: 1rem; color: #A78BFA;">
            <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect><path d="M7 11V7a5 5 0 0 1 10 0v4"></path></svg>
          </div>
          <h3 style="font-size: 1.15rem; font-weight: 700; color: #FFFFFF; margin-bottom: 0.4rem;">Security Deposit Escrow & Ledgers</h3>
          <p style="font-size: 0.88rem; color: #94A3B8; line-height: 1.5;">Maintain clear records of deposits held, deductions for painting/wear, and automated refund settlement receipts.</p>
        </div>

        <!-- Card 6 -->
        <div style="background: #1E293B; border: 1px solid #334155; padding: 1.5rem; border-radius: 12px;">
          <div style="width: 44px; height: 44px; border-radius: 8px; background: rgba(14, 165, 233, 0.15); display: flex; align-items: center; justify-content: center; margin-bottom: 1rem; color: #38BDF8;">
            <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="12" y1="1" x2="12" y2="23"></line><path d="M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"></path></svg>
          </div>
          <h3 style="font-size: 1.15rem; font-weight: 700; color: #FFFFFF; margin-bottom: 0.4rem;">Rental Yield & Fair Pricing Intel</h3>
          <p style="font-size: 0.88rem; color: #94A3B8; line-height: 1.5;">Real-time corridor-based rent estimator for Bangalore and top Indian metros to maximize your rental yield.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- Section 1: Landlord & PG Management SaaS Dashboard -->
  <section class="saas-section" id="landlord-saas">
    <div class="container">
      <div class="saas-header-box">
        <span class="saas-tag">PROPRIETARY SAAS SUITE</span>
        <h2 class="saas-title">Smart Landlord & PG Management SaaS</h2>
        <p class="saas-subtitle">
          Automate monthly rent collection via UPI, send instant WhatsApp receipts, manage security deposit ledgers, and resolve tenant maintenance tickets from one clean dashboard.
        </p>
      </div>

      <!-- KPI Metrics Row -->
      <div class="saas-kpi-grid">
        <div class="saas-kpi-card">
          <div class="kpi-lbl">Managed Units</div>
          <div class="kpi-val" id="saasKpiUnits">4 Units</div>
          <div class="kpi-sub">✓ 100% Occupied</div>
        </div>
        <div class="saas-kpi-card">
          <div class="kpi-lbl">October Rent Collected</div>
          <div class="kpi-val" id="saasKpiCollected">₹1,45,000</div>
          <div class="kpi-sub">3 Units Paid via UPI</div>
        </div>
        <div class="saas-kpi-card">
          <div class="kpi-lbl">Pending Collection</div>
          <div class="kpi-val" style="color:#F59E0B;" id="saasKpiPending">₹38,000</div>
          <div class="kpi-sub" style="color:#F59E0B;">1 Unit Due Soon</div>
        </div>
        <div class="saas-kpi-card">
          <div class="kpi-lbl">Security Deposit Held</div>
          <div class="kpi-val" style="color:#38BDF8;" id="saasKpiDeposit">₹4,20,000</div>
          <div class="kpi-sub">Escrow Protected</div>
        </div>
      </div>

      <!-- SaaS Interactive Workbench -->
      <div class="saas-workbench-card">
        <div class="saas-nav-tabs">
          <button class="saas-tab-btn active" data-saas-tab="rent">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="5" width="20" height="14" rx="2"></rect><line x1="2" y1="10" x2="22" y2="10"></line></svg>
            <span>Rent Collection & UPI Invoices</span>
          </button>
          <button class="saas-tab-btn" data-saas-tab="leases">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line></svg>
            <span>Tenant Leases & Security Deposits</span>
          </button>
          <button class="saas-tab-btn" data-saas-tab="tickets">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"></path></svg>
            <span>Maintenance Tickets (<span id="ticketCountBadge">2</span>)</span>
          </button>
        </div>

        <div class="saas-tab-content">
          <!-- Tab 1: Rent Collection & Invoicing -->
          <div id="saasTabRent" class="saas-pane active">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:1rem; flex-wrap:wrap; gap:0.5rem;">
              <h4 style="font-size:1.05rem; font-weight:800; color:#F8FAFC; margin:0;">Active Monthly Tenant Ledger</h4>
              <div style="display:flex; gap:0.5rem;">
                <button class="btn btn-xs btn-secondary" id="btnAddUnitPrompt">
                  <span>+ Add Tenant Unit</span>
                </button>
                <button class="btn btn-xs btn-primary" id="btnSimulateCollectAll">
                  <span>⚡ Send WhatsApp Rent Links to All Units</span>
                </button>
              </div>
            </div>

            <div class="saas-table-wrap">
              <table class="saas-table">
                <thead>
                  <tr>
                    <th>Unit / Society</th>
                    <th>Tenant Details</th>
                    <th>Monthly Rent</th>
                    <th>Status</th>
                    <th>Due Date</th>
                    <th>Automated Action</th>
                  </tr>
                </thead>
                <tbody id="saasRentTableBody">
                  <tr>
                    <td><strong>UNIT-302</strong><br><span style="font-size:0.75rem; color:#94A3B8;">Prestige Falcon City (3 BHK)</span></td>
                    <td>Aditya Saxena<br><span style="font-size:0.75rem; color:#94A3B8;"></span></td>
                    <td><strong>₹48,000</strong></td>
                    <td><span class="saas-badge-paid">✓ Paid on Oct 05</span></td>
                    <td>05 Nov 2026</td>
                    <td>
                      <button class="btn-upi-action" style="background:#334155;" onclick="showToast('📄 WhatsApp Rent Receipt already delivered to Aditya Saxena')">
                        <span>View Receipt</span>
                      </button>
                    </td>
                  </tr>
                  <tr>
                    <td><strong>UNIT-104</strong><br><span style="font-size:0.75rem; color:#94A3B8;">Sobha Dream Acres (2 BHK)</span></td>
                    <td>Sneha Rao<br><span style="font-size:0.75rem; color:#94A3B8;"></span></td>
                    <td><strong>₹38,000</strong></td>
                    <td><span class="saas-badge-due">⚠ Due in 4 Days</span></td>
                    <td>28 Oct 2026</td>
                    <td>
                      <button class="btn-upi-action" id="btnSendSnehaReminder">
                        <span>Send UPI Link 💬</span>
                      </button>
                    </td>
                  </tr>
                  <tr>
                    <td><strong>UNIT-201</strong><br><span style="font-size:0.75rem; color:#94A3B8;">Godrej Eternity (2 BHK)</span></td>
                    <td>Rahul Mehta<br><span style="font-size:0.75rem; color:#94A3B8;"></span></td>
                    <td><strong>₹33,000</strong></td>
                    <td><span class="saas-badge-paid">✓ Paid on Oct 01</span></td>
                    <td>01 Nov 2026</td>
                    <td>
                      <button class="btn-upi-action" style="background:#334155;" onclick="showToast('📄 WhatsApp Rent Receipt already delivered to Rahul Mehta')">
                        <span>View Receipt</span>
                      </button>
                    </td>
                  </tr>
                  <tr>
                    <td><strong>UNIT-112</strong><br><span style="font-size:0.75rem; color:#94A3B8;">Raheja Residency (2 BHK)</span></td>
                    <td>Arjun Nambiar<br><span style="font-size:0.75rem; color:#94A3B8;"></span></td>
                    <td><strong>₹26,000</strong></td>
                    <td><span class="saas-badge-paid">✓ Paid on Oct 03</span></td>
                    <td>03 Nov 2026</td>
                    <td>
                      <button class="btn-upi-action" style="background:#334155;" onclick="showToast('📄 WhatsApp Rent Receipt already delivered to Arjun Nambiar')">
                        <span>View Receipt</span>
                      </button>
                    </td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>

          <!-- Tab 2: Leases & Deposits -->
          <div id="saasTabLeases" class="saas-pane" style="display:none;">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:1rem; flex-wrap:wrap; gap:0.5rem;">
              <h4 style="font-size:1.05rem; font-weight:800; color:#F8FAFC; margin:0;">Active Leases & Security Deposits</h4>
              <button class="btn btn-xs btn-primary" onclick="document.getElementById('rental-agreement').scrollIntoView({behavior:'smooth'})">
                <span>+ Draft New E-Stamped Lease</span>
              </button>
            </div>
            <div class="saas-table-wrap">
              <table class="saas-table">
                <thead>
                  <tr>
                    <th>Unit / Society</th>
                    <th>Tenant Name</th>
                    <th>Security Deposit</th>
                    <th>Lease Tenure</th>
                    <th>Expiry Date</th>
                    <th>Renewal Action</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td>UNIT-302 (Prestige)</td>
                    <td>Aditya Saxena</td>
                    <td><strong style="color:#38BDF8;">₹1,44,000</strong></td>
                    <td>11 Months</td>
                    <td>15 Aug 2027</td>
                    <td><button class="btn btn-xs btn-secondary" onclick="showToast('✓ Lease in good standing (10 months remaining)')">Check Status</button></td>
                  </tr>
                  <tr>
                    <td>UNIT-104 (Sobha)</td>
                    <td>Sneha Rao</td>
                    <td><strong style="color:#38BDF8;">₹1,10,000</strong></td>
                    <td>11 Months</td>
                    <td>30 Mar 2027</td>
                    <td><button class="btn btn-xs btn-secondary" onclick="showToast('✓ Lease in good standing (5 months remaining)')">Check Status</button></td>
                  </tr>
                  <tr>
                    <td>UNIT-201 (Godrej)</td>
                    <td>Rahul Mehta</td>
                    <td><strong style="color:#38BDF8;">₹99,000</strong></td>
                    <td>11 Months</td>
                    <td>31 Dec 2026</td>
                    <td><button class="btn btn-xs btn-primary" onclick="showToast('📋 Automated 11-Month Renewal deed prepared!')">Renew Lease</button></td>
                  </tr>
                  <tr>
                    <td>UNIT-112 (Raheja)</td>
                    <td>Arjun Nambiar</td>
                    <td><strong style="color:#38BDF8;">₹67,000</strong></td>
                    <td>11 Months</td>
                    <td>30 Jun 2027</td>
                    <td><button class="btn btn-xs btn-secondary" onclick="showToast('✓ Lease in good standing')">Check Status</button></td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>

          <!-- Tab 3: Maintenance Tickets -->
          <div id="saasTabTickets" class="saas-pane" style="display:none;">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:1rem; flex-wrap:wrap; gap:0.5rem;">
              <h4 style="font-size:1.05rem; font-weight:800; color:#F8FAFC; margin:0;">Tenant Repair & Maintenance Requests</h4>
              <button class="btn btn-xs btn-secondary" id="btnLogNewTicket">
                <span>+ Log New Maintenance Issue</span>
              </button>
            </div>
            <div class="saas-table-wrap">
              <table class="saas-table">
                <thead>
                  <tr>
                    <th>Ticket ID</th>
                    <th>Unit / Tenant</th>
                    <th>Issue Description</th>
                    <th>Reported Date</th>
                    <th>Status</th>
                    <th>Landlord Action</th>
                  </tr>
                </thead>
                <tbody id="saasTicketsTableBody">
                  <tr>
                    <td><strong>TCK-801</strong></td>
                    <td>UNIT-302 (Aditya)</td>
                    <td>Master Bedroom AC Servicing & Cooling Check</td>
                    <td>22 Oct 2026</td>
                    <td><span class="saas-badge-due">⚙ In Progress</span></td>
                    <td>
                      <button class="btn btn-xs btn-primary" onclick="resolveTicket(this)">
                        Mark Resolved ✓
                      </button>
                    </td>
                  </tr>
                  <tr>
                    <td><strong>TCK-802</strong></td>
                    <td>UNIT-104 (Sneha)</td>
                    <td>Kitchen RO Water Purifier Filter Replacement</td>
                    <td>23 Oct 2026</td>
                    <td><span class="saas-badge-due">⌛ Pending Vendor</span></td>
                    <td>
                      <button class="btn btn-xs btn-primary" onclick="resolveTicket(this)">
                        Mark Resolved ✓
                      </button>
                    </td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Section 2: Legal Lease Deeds & Tax Studio -->
  <section class="agreement-section" id="rental-agreement">
    <div class="container">
      <div class="text-center-wrapper" style="margin-bottom:2.5rem;">
        <span class="section-tag-light">LEGAL INFRASTRUCTURE & TAX STUDIO</span>
        <h2 class="section-title-clean">11-Month Digital Lease Deeds & Automated HRA Receipts</h2>
        <p class="section-desc-clean">
          Execute legally compliant, court-admissible rental agreements with State E-stamping, or generate 12-month HRA tax rent receipts with revenue stamps instantly.
        </p>

        <!-- Studio Mode Switcher -->
        <div style="display:inline-flex; background:#E2E8F0; padding:0.3rem; border-radius:var(--radius-full); margin-top:1rem;">
          <button class="btn btn-xs btn-primary studio-toggle-btn active" id="btnToggleLeaseMode" style="border-radius:var(--radius-full);">
            <span>📜 11-Month Lease Drafter</span>
          </button>
          <button class="btn btn-xs btn-secondary studio-toggle-btn" id="btnToggleHraMode" style="border-radius:var(--radius-full); background:none; border:none;">
            <span>🧾 Automated HRA Tax Receipts</span>
          </button>
        </div>
      </div>

      <!-- Mode A: Lease Agreement Drafter -->
      <div id="studioLeaseView" class="agreement-clean-layout">
        <div class="agr-info">
          <span class="section-tag-light">COURT-COMPLIANT LEASE</span>
          <h3 style="font-size:1.6rem; font-weight:800; color:#0F172A; margin:0.4rem 0 0.8rem 0;">Legally Binding E-Stamped Rental Agreement</h3>
          <p class="section-desc-clean" style="text-align: left; margin: 0 0 1.25rem 0;">
            Execute a legally binding rental deed from home. Pre-drafted with standard lock-in clauses, security deposit return rules, and official State Government e-stamping.
          </p>

          <div class="agr-perks-list">
            <div class="agr-perk">
              <span class="check-circle">✓</span>
              <div>
                <strong>Aadhaar OTP Biometric Signatures</strong>
                <p>Fully compliant under Section 10A of the Information Technology Act 2000.</p>
              </div>
            </div>
            <div class="agr-perk">
              <span class="check-circle">✓</span>
              <div>
                <strong>State Government Official E-Stamping</strong>
                <p>Delivered digitally with valid certificate serial number and bar code.</p>
              </div>
            </div>
            <div class="agr-perk">
              <span class="check-circle">✓</span>
              <div>
                <strong>Deposit Protection & Notice Clauses</strong>
                <p>Standardized 1-month notice and clear painting deduction provisions.</p>
              </div>
            </div>
          </div>
        </div>

        <div class="agr-form-wrapper">
          <div class="agr-card-clean">
            <div class="agr-card-header">
              <h4>Instant Rental Agreement Drafter</h4>
              <span class="agr-badge">₹1,299 E-Stamp Included</span>
            </div>

            <form id="formAgreementDraft" class="agr-form-clean">
              <div class="form-row-clean">
                <div class="form-group">
                  <label for="agrOwnerName">Owner Full Name *</label>
                  <input type="text" id="agrOwnerName" class="form-control-clean" value="Anand Deshmukh" required>
                </div>
                <div class="form-group">
                  <label for="agrTenantName">Tenant Full Name *</label>
                  <input type="text" id="agrTenantName" class="form-control-clean" value="Aditya Saxena" required>
                </div>
              </div>

              <div class="form-group">
                <label for="agrPropertyAddress">Rented Apartment Address *</label>
                <input type="text" id="agrPropertyAddress" class="form-control-clean" value="Flat 402, Tower B, Prestige Falcon City, Kanakapura Road, Bengaluru" required>
              </div>

              <div class="form-row-clean">
                <div class="form-group">
                  <label for="agrMonthlyRent">Monthly Rent (₹) *</label>
                  <input type="number" id="agrMonthlyRent" class="form-control-clean" value="48000" required>
                </div>
                <div class="form-group">
                  <label for="agrDeposit">Security Deposit (₹) *</label>
                  <input type="number" id="agrDeposit" class="form-control-clean" value="144000" required>
                </div>
              </div>

              <div class="form-row-clean">
                <div class="form-group">
                  <label for="agrDuration">Tenure</label>
                  <select id="agrDuration" class="form-control-clean">
                    <option value="11 Months" selected>11 Months (Standard)</option>
                    <option value="22 Months">22 Months</option>
                  </select>
                </div>
                <div class="form-group">
                  <label for="agrNotice">Notice Period</label>
                  <select id="agrNotice" class="form-control-clean">
                    <option value="1 Month" selected>1 Month</option>
                    <option value="2 Months">2 Months</option>
                  </select>
                </div>
              </div>

              <button type="submit" class="btn btn-primary btn-full btn-lg" id="btnPreviewAgreement">
                <span>View Legal Draft & E-Stamp Preview &rarr;</span>
              </button>
            </form>
          </div>
        </div>
      </div>

      <!-- Mode B: HRA Rent Receipts Generator -->
      <div id="studioHraView" class="agreement-clean-layout" style="display:none;" id="hra-tax-studio">
        <div class="agr-info">
          <span class="section-tag-light">TAX SAVINGS UTILITY</span>
          <h3 style="font-size:1.6rem; font-weight:800; color:#0F172A; margin:0.4rem 0 0.8rem 0;">Automated HRA Tax Rent Receipts</h3>
          <p class="section-desc-clean" style="text-align: left; margin: 0 0 1.25rem 0;">
            Claim House Rent Allowance (HRA) exemptions under Section 10(13A) of the Income Tax Act. Instantly generate a full 12-month receipt package with authentic revenue stamp graphics and landlord PAN declaration.
          </p>

          <div class="agr-perks-list">
            <div class="agr-perk">
              <span class="check-circle">✓</span>
              <div>
                <strong>100% Free for ExaInfra Users</strong>
                <p>Generate compliant PDF receipts for FY 2026-27 corporate payroll submission.</p>
              </div>
            </div>
            <div class="agr-perk">
              <span class="check-circle">✓</span>
              <div>
                <strong>Automated ₹1 Revenue Stamp Graphic</strong>
                <p>Legally mandatory for monthly rent payments exceeding ₹5,000 in cash/cheque.</p>
              </div>
            </div>
            <div class="agr-perk">
              <span class="check-circle">✓</span>
              <div>
                <strong>Landlord PAN Exemption Format</strong>
                <p>Formatted for annual rents over ₹1,00,000 as per CBDT tax regulations.</p>
              </div>
            </div>
          </div>
        </div>

        <div class="agr-form-wrapper">
          <div class="agr-card-clean">
            <div class="agr-card-header">
              <h4>Generate 12-Month HRA Receipts</h4>
              <span class="agr-badge" style="background:#ECFDF5; color:#059669;">100% Free Utility</span>
            </div>

            <form id="formHraGenerate" class="agr-form-clean">
              <div class="form-row-clean">
                <div class="form-group">
                  <label for="hraTenantName">Employee / Tenant Name *</label>
                  <input type="text" id="hraTenantName" class="form-control-clean" value="Aditya Saxena" required>
                </div>
                <div class="form-group">
                  <label for="hraLandlordName">Landlord Full Name *</label>
                  <input type="text" id="hraLandlordName" class="form-control-clean" value="Anand Deshmukh" required>
                </div>
              </div>

              <div class="form-row-clean">
                <div class="form-group">
                  <label for="hraRentAmount">Monthly Rent Paid (₹) *</label>
                  <input type="number" id="hraRentAmount" class="form-control-clean" value="48000" required>
                </div>
                <div class="form-group">
                  <label for="hraLandlordPan">Landlord PAN Number *</label>
                  <input type="text" id="hraLandlordPan" class="form-control-clean" value="ABCDE1234F" style="text-transform:uppercase;" required>
                </div>
              </div>

              <div class="form-group">
                <label for="hraAddress">Rented House Address *</label>
                <input type="text" id="hraAddress" class="form-control-clean" value="Flat 402, Tower B, Prestige Falcon City, Kanakapura Road, Bengaluru" required>
              </div>

              <div class="form-group">
                <label for="hraFinancialYear">Financial Year Period</label>
                <select id="hraFinancialYear" class="form-control-clean">
                  <option value="2026-2027" selected>FY 2026-27 (Apr 2026 - Mar 2027)</option>
                  <option value="2025-2026">FY 2025-26 (Apr 2025 - Mar 2026)</option>
                </select>
              </div>

              <button type="submit" class="btn btn-primary btn-full btn-lg" id="btnGenerateHraReceipts">
                <span>Generate Official 12-Month HRA Receipts Package &rarr;</span>
              </button>
            </form>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Section 3: Rent & Yield Intelligence Estimator -->
  <section class="estimator-section" id="rent-estimator">
    <div class="container">
      <div class="text-center-wrapper">
        <span class="section-tag-light">RENTAL YIELD & MARKET INTELLIGENCE</span>
        <h2 class="section-title-clean">Bangalore Fair Market Rent & Yield Calculator</h2>
        <p class="section-desc-clean">
          Accurate rental benchmarks for landlords and property investors across Bangalore's major tech clusters.
        </p>
      </div>

      <div class="estimator-workbench-clean">
        <div class="est-controls-clean">
          <div class="form-group">
            <label for="estLocality">Locality / Tech Corridor</label>
            <select id="estLocality" class="form-control-clean">
              <option value="Bellandur" selected>Bellandur & Outer Ring Road (ORR)</option>
              <option value="Whitefield">Whitefield & ITPL</option>
              <option value="Koramangala">Koramangala</option>
              <option value="Indiranagar">Indiranagar & Domlur</option>
              <option value="HSR">HSR Layout</option>
              <option value="Sarjapur">Sarjapur Road</option>
              <option value="Electronic">Electronic City Phase 1 & 2</option>
            </select>
          </div>

          <div class="form-row-clean">
            <div class="form-group">
              <label for="estBhk">Configuration</label>
              <select id="estBhk" class="form-control-clean">
                <option value="1 BHK">1 BHK</option>
                <option value="2 BHK" selected>2 BHK</option>
                <option value="3 BHK">3 BHK</option>
                <option value="4+ BHK">4+ BHK / Villa</option>
              </select>
            </div>
            <div class="form-group">
              <label for="estFurnishing">Furnishing</label>
              <select id="estFurnishing" class="form-control-clean">
                <option value="Unfurnished">Unfurnished</option>
                <option value="Semi Furnished" selected>Semi Furnished</option>
                <option value="Fully Furnished">Fully Furnished</option>
              </select>
            </div>
          </div>

          <div class="form-row-clean">
            <div class="form-group">
              <label for="estCarpetArea">Approx Carpet Area (sq.ft)</label>
              <input type="number" id="estCarpetArea" class="form-control-clean" value="1150">
            </div>
            <div class="form-group">
              <label for="estAmenities">Gated Society Amenities</label>
              <select id="estAmenities" class="form-control-clean">
                <option value="standard" selected>Standard (Security, Lift, Power Backup)</option>
                <option value="premium">Clubhouse, Pool, Gym, Tennis</option>
              </select>
            </div>
          </div>
        </div>

        <div class="est-result-card-clean">
          <div class="est-res-header">
            <span>ESTIMATED FAIR MONTHLY RENT</span>
            <div class="est-rent-range" id="estRangeDisplay">₹38,000 - ₹44,000 / mo</div>
            <p class="est-sub">Based on verified direct landlord transactions in Q3/Q4 2026.</p>
          </div>

          <div class="est-stats-grid">
            <div class="stat-cell">
              <span class="lbl">Expected Rental Yield</span>
              <strong class="val" id="estYieldDisplay">4.5% - 5.1% p.a.</strong>
            </div>
            <div class="stat-cell">
              <span class="lbl">Recommended Security Deposit</span>
              <strong class="val">3 - 4 Months Rent</strong>
            </div>
            <div class="stat-cell">
              <span class="lbl">Avg Time to Rent</span>
              <strong class="val">8 - 14 Days</strong>
            </div>
            <div class="stat-cell">
              <span class="lbl">Rental Trend</span>
              <strong class="val text-green">↑ +8.4% YoY</strong>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Section 4: Transparent SaaS Pricing Plans -->
  <section class="pricing-section" id="pricing-plans">
    <div class="container">
      <div class="text-center-wrapper">
        <span class="section-tag-light">TRANSPARENT MONETIZATION</span>
        <h2 class="section-title-clean">Affordable Plans for Landlords, PGs & Legal Leases</h2>
        <p class="section-desc-clean">
          Free to start. Upgrade only when you need automated rent collections, multi-unit ledgers, or court-stamped lease deeds.
        </p>
      </div>

      <div class="pricing-cards-grid">
        <!-- Landlord Starter Plan -->
        <div class="pricing-card">
          <h3 class="p-plan-name">Landlord Starter</h3>
          <p class="p-plan-desc">For individual homeowners managing 1 or 2 rental properties.</p>
          <div class="p-price-row">
            <span class="amt">₹0</span>
            <span class="dur">/ free forever</span>
          </div>
          <ul class="p-features-list">
            <li><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"></polyline></svg> Up to 2 Managed Tenant Units</li>
            <li><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"></polyline></svg> Manual UPI Payment Recording</li>
            <li><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"></polyline></svg> <strong>100% Free 12-Month HRA Tax Receipts</strong></li>
            <li><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"></polyline></svg> Fair Market Rent & Yield Calculator</li>
            <li><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"></polyline></svg> Basic PDF Agreement Templates</li>
          </ul>
          <button class="btn btn-secondary btn-full" onclick="document.getElementById('landlord-saas').scrollIntoView({behavior:'smooth'})">
            <span>Use Free Starter Plan</span>
          </button>
        </div>

        <!-- Landlord Pro SaaS (Popular) -->
        <div class="pricing-card popular">
          <div class="pricing-badge-popular">MOST POPULAR</div>
          <h3 class="p-plan-name">Landlord Pro SaaS</h3>
          <p class="p-plan-desc">For serious property owners and PG operators wanting complete automation.</p>
          <div class="p-price-row">
            <span class="amt">₹999</span>
            <span class="dur">/ year</span>
          </div>
          <ul class="p-features-list">
            <li><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"></polyline></svg> <strong>Unlimited Managed Tenant Units & PGs</strong></li>
            <li><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"></polyline></svg> <strong>Automated WhatsApp UPI Rent Links</strong></li>
            <li><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"></polyline></svg> Instant WhatsApp Automated Rent Receipts</li>
            <li><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"></polyline></svg> Tenant Maintenance & Repair Ticket Tracker</li>
            <li><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"></polyline></svg> Security Deposit Escrow Ledger & Expiry Alerts</li>
          </ul>
          <button class="btn btn-primary btn-full" id="btnBuyLandlordPro">
            <span>Activate Landlord Pro (₹999/yr)</span>
          </button>
        </div>

        <!-- Digital E-Stamped Lease Deed -->
        <div class="pricing-card">
          <h3 class="p-plan-name">Digital Lease Deed</h3>
          <p class="p-plan-desc">Official 11-month agreement with State Government e-stamp duty.</p>
          <div class="p-price-row">
            <span class="amt">₹1,299</span>
            <span class="dur">/ per agreement</span>
          </div>
          <ul class="p-features-list">
            <li><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"></polyline></svg> Legally Binding, Court-Admissible Format</li>
            <li><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"></polyline></svg> <strong>Official State E-Stamp Duty Certificate</strong></li>
            <li><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"></polyline></svg> Aadhaar Biometric OTP eSign for both parties</li>
            <li><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"></polyline></svg> Instant PDF download + WhatsApp delivery</li>
            <li><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"></polyline></svg> Basic draft option available at ₹499</li>
          </ul>
          <button class="btn btn-secondary btn-full" onclick="document.getElementById('rental-agreement').scrollIntoView({behavior:'smooth'})">
            <span>Draft E-Stamped Lease Now</span>
          </button>
        </div>
      </div>
    </div>
  </section>

  <!-- Section 5: How It Works -->
  <section class="how-it-works-clean" id="how-it-works">
    <div class="container">
      <div class="text-center-wrapper">
        <span class="section-tag-light">SIMPLE & RELIABLE</span>
        <h2 class="section-title-clean">How ExaInfra Transforms Rental Management</h2>
        <p class="section-desc-clean">
          Get started in under 3 minutes with zero technical setup required.
        </p>
      </div>

      <div class="how-steps-clean">
        <div class="step-card-clean">
          <div class="step-num-badge">1</div>
          <h4>Register Your Units</h4>
          <p>Add your apartments, society name, tenant contact info, and monthly rent amount in 60 seconds.</p>
        </div>
        <div class="step-card-clean">
          <div class="step-num-badge">2</div>
          <h4>Automate UPI Collections</h4>
          <p>System automatically triggers WhatsApp payment reminders with one-tap UPI intent links on due dates.</p>
        </div>
        <div class="step-card-clean">
          <div class="step-num-badge">3</div>
          <h4>Resolve Maintenance Tickets</h4>
          <p>Tenants log repair requests directly. Track vendor work and mark tickets resolved transparently.</p>
        </div>
        <div class="step-card-clean">
          <div class="step-num-badge">4</div>
          <h4>Execute E-Stamped Leases</h4>
          <p>Generate court-admissible 11-month rental agreements with Karnataka State E-Stamp Duty and Aadhaar eSign.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- Footer -->
  <footer class="footer-clean" style="background:#0F172A; border-top:1px solid #1E293B; padding:3rem 0; color:#94A3B8;">
    <div class="container" style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:1.5rem;">
      <div>
        <div style="font-size:1.25rem; font-weight:800; color:#FFFFFF; margin-bottom:0.25rem;">
          EXA<span style="color:#0284C7;">INFRA</span> SAAS
        </div>
        <p style="font-size:0.85rem; margin:0; color:#64748B;">India's Landlord Automation & Legal Lease Infrastructure.</p>
      </div>
      <div style="display:flex; gap:1.5rem; font-size:0.85rem;">
        <a href="#landlord-saas" style="color:#94A3B8; text-decoration:none;">SaaS Dashboard</a>
        <a href="#rental-agreement" style="color:#94A3B8; text-decoration:none;">11-Month Leases</a>
        <a href="#hra-tax-studio" style="color:#94A3B8; text-decoration:none;">HRA Receipts</a>
        <a href="#pricing-plans" style="color:#94A3B8; text-decoration:none;">Pricing Plans</a>
      </div>
      <div style="font-size:0.8rem; color:#64748B;">
        &copy; 2026 ExaInfra.in. All rights reserved. Built for Namecheap hosting.
      </div>
    </div>
  </footer>

  <!-- ====================================================================
       MODALS
       ==================================================================== -->

  <!-- MODAL 1: Add Managed Unit Modal -->
  <div class="modal-backdrop" id="modalAddUnit">
    <div class="modal-box">
      <button class="modal-close-btn" id="closeModalAddUnit" aria-label="Close modal">&times;</button>
      <div class="modal-header-clean">
        <span class="modal-badge-clean">LANDLORD WORKBENCH</span>
        <h3>Add New Managed Tenant Unit</h3>
        <p>Register a new apartment to automate monthly UPI rent collection and receipts.</p>
      </div>

      <form id="formAddUnit" class="modal-form-clean">
        <div class="form-row-clean">
          <div class="form-group">
            <label for="newUnitCode">Unit Number *</label>
            <input type="text" id="newUnitCode" class="form-control-clean" placeholder="e.g. UNIT-504" required>
          </div>
          <div class="form-group">
            <label for="newSociety">Society / Apartment Name *</label>
            <input type="text" id="newSociety" class="form-control-clean" placeholder="e.g. Prestige Falcon City" required>
          </div>
        </div>

        <div class="form-row-clean">
          <div class="form-group">
            <label for="newTenantName">Tenant Full Name *</label>
            <input type="text" id="newTenantName" class="form-control-clean" placeholder="e.g. Vikram Sharma" required>
          </div>
          <div class="form-group">
            <label for="newTenantPhone">Tenant WhatsApp Number *</label>
            <input type="tel" id="newTenantPhone" class="form-control-clean" placeholder="e.g. " required>
          </div>
        </div>

        <div class="form-row-clean">
          <div class="form-group">
            <label for="newMonthlyRent">Monthly Rent (₹) *</label>
            <input type="number" id="newMonthlyRent" class="form-control-clean" placeholder="e.g. 42000" required>
          </div>
          <div class="form-group">
            <label for="newDueDate">Monthly Due Day (1-31) *</label>
            <input type="number" id="newDueDate" class="form-control-clean" placeholder="e.g. 5" min="1" max="31" value="5" required>
          </div>
        </div>

        <button type="submit" class="btn btn-primary btn-full btn-lg">
          <span>Register Unit & Activate Invoicing &rarr;</span>
        </button>
      </form>
    </div>
  </div>

  <!-- MODAL 2: Rental Agreement Preview Modal -->
  <div class="modal-backdrop" id="modalAgreementPreview">
    <div class="modal-box modal-lg">
      <button class="modal-close-btn" id="closeModalAgrPreview" aria-label="Close modal">&times;</button>
      <div class="modal-header-clean">
        <span class="modal-badge-clean">LEGAL DRAFT PREVIEW</span>
        <h3>Official Residential Lease & Rental Deed</h3>
        <p>11-Month Standard Agreement with State E-Stamp Duty and Legal Enforceability.</p>
      </div>

      <div class="legal-paper-clean" id="legalDocumentPaper">
        <!-- Populated dynamically -->
      </div>

      <div class="legal-action-bar-clean">
        <button class="btn btn-secondary" id="btnPrintAgreement">
          <span>Print / Save as PDF</span>
        </button>
        <button class="btn btn-primary" id="btnProceedAadhaarSign">
          <span>Proceed to Aadhaar eSign (₹1,299) &rarr;</span>
        </button>
      </div>
    </div>
  </div>

  <!-- MODAL 3: HRA Rent Receipts Preview Modal -->
  <div class="modal-backdrop" id="modalHraPreview">
    <div class="modal-box modal-lg">
      <button class="modal-close-btn" id="closeModalHraPreview" aria-label="Close modal">&times;</button>
      <div class="modal-header-clean">
        <span class="modal-badge-clean" style="background:#ECFDF5; color:#059669;">HRA TAX RECEIPTS PACKAGE</span>
        <h3>12-Month Official Rent Receipts for HRA Exemption</h3>
        <p>Section 10(13A) compliant for employee payroll submission with ₹1 revenue stamp declaration.</p>
      </div>

      <div id="hraReceiptsContainer" style="max-height: 480px; overflow-y: auto; padding: 0.5rem;">
        <!-- Populated dynamically -->
      </div>

      <div class="legal-action-bar-clean">
        <button class="btn btn-secondary" id="btnPrintHraReceipts">
          <span>Print All 12 Receipts / Save PDF</span>
        </button>
        <button class="btn btn-primary" onclick="showToast('✓ 12-Month HRA Tax Receipt Package downloaded!'); closeModal(document.getElementById('modalHraPreview'));">
          <span>Download Signed PDF Batch &rarr;</span>
        </button>
      </div>
    </div>
  </div>

  <!-- Toast Notification Container -->
  <div class="toast-container" id="toastContainer"></div>

  <script src="app.js"></script>
</body>
</html>
"""

with open('/Users/chetanbisariya/.gemini/antigravity-ide/scratch/exainfra-in/index.html', 'w') as f:
    f.write(html_content)

print(f"Generated clean SaaS index.html ({len(html_content)} bytes) successfully.")
