import json

with open('/Users/chetanbisariya/.gemini/antigravity-ide/scratch/exainfra-in/direct_owner_apartments.json') as f:
    apts = json.load(f)

# Build index.html
html_content = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>ExaInfra Rentals & SaaS — Direct Owner Rentals, Legal Leases & Landlord Management</title>
  <meta name="description" content="India's complete rental & landlord platform. Zero-brokerage direct owner flats, court-compliant 11-month e-stamped lease deeds, automated HRA rent receipts, and UPI rent collection SaaS.">
  <meta name="keywords" content="direct owner flats, zero brokerage bangalore, rental agreement online, e-stamp rent agreement, hra rent receipts, landlord management saas, upi rent collection">
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
        <span class="ticker-label">EXAINFRA ALL-IN-ONE:</span>
      </div>
      <div class="ticker-marquee">
        <span id="tickerText">100% Direct Owner Verified Flats &bull; 5 Free Property Postings for Landlords &bull; 20 Free Tenant Inquiries &bull; 11-Month Digital Lease Deeds &bull; Automated UPI Rent Collection</span>
      </div>
      <a href="#pricing-plans" class="btn btn-xs btn-scanner-refresh" style="text-decoration:none;">
        <span>Explore Pricing & Plans &rarr;</span>
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
            <span class="logo-aggregator-badge" style="background:#0F172A; color:#38BDF8; border-color:#334155;">SAAS & RENTALS</span>
          </div>
          <span class="logo-sub">DIRECT OWNERS &bull; LEGAL LEASES &bull; LANDLORD SAAS</span>
        </div>
      </a>

      <!-- Desktop Nav Links -->
      <nav class="nav-links" id="navLinks">
        <a href="#explore-apartments" class="nav-link-item active">Direct Owner Flats</a>
        <a href="#rental-agreement" class="nav-link-item">Digital Lease & HRA</a>
        <a href="#landlord-saas" class="nav-link-item">Landlord SaaS Dashboard</a>
        <a href="#rent-estimator" class="nav-link-item">Rent Estimator</a>
        <a href="#pricing-plans" class="nav-link-item">Pricing & Plans</a>
        <a href="#how-it-works" class="nav-link-item">How It Works</a>
      </nav>

      <!-- Right Action Controls -->
      <div class="nav-actions">
        <!-- City Selector -->
        <div class="city-selector">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path><circle cx="12" cy="10" r="3"></circle></svg>
          <select id="quickCitySelect" class="city-select-dropdown" aria-label="Select City">
            <option value="Bengaluru" selected>Bengaluru</option>
            <option value="Mumbai">Mumbai</option>
            <option value="Delhi-NCR">Delhi-NCR</option>
            <option value="Hyderabad">Hyderabad</option>
            <option value="Pune">Pune</option>
            <option value="all">All Metros</option>
          </select>
        </div>

        <!-- Saved Searches Button -->
        <button class="btn btn-nav-ghost" id="btnOpenSavedSearches" title="View Saved Searches">
          <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M19 21l-7-5-7 5V5a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2z"></path></svg>
          <span>Saved (<span id="savedSearchesCount">1</span>)</span>
        </button>

        <!-- User Account / Role Widget -->
        <button class="user-account-btn" id="btnUserAccount" title="Manage Account & Free Quotas">
          <div class="user-avatar" id="navAvatar">👤</div>
          <div class="user-meta-nav">
            <span class="user-name-text" id="navUserName">Aditya (Tenant)</span>
            <span class="user-quota-badge" id="navQuotaBadge">💬 18/20 Free Chats</span>
          </div>
        </button>

        <!-- Landlord Post Button -->
        <button class="btn btn-primary btn-post-flat" id="btnNavPostApartment">
          <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><line x1="12" y1="5" x2="12" y2="19"></line><line x1="5" y1="12" x2="19" y2="12"></line></svg>
          <span id="navPostBtnText">Post Flat (5 Free)</span>
        </button>

        <button class="mobile-menu-btn" id="mobileMenuBtn" aria-label="Open mobile navigation">
          <span></span><span></span><span></span>
        </button>
      </div>
    </div>
  </header>

  <!-- Hero Section -->
  <section class="hero-section">
    <div class="container hero-container">
      <div class="hero-header-box">
        <div class="hero-live-badge">
          <span class="live-dot-green"></span>
          <span>100% DIRECT OWNER NETWORK &bull; ZERO BROKERAGE &bull; LEGAL LEASES &bull; LANDLORD SAAS</span>
        </div>

        <h1 class="hero-main-title">
          Rent Direct From Owners. <span class="highlight-coral">Sign Digital Leases.</span><br>
          <span class="hero-sub-gradient">Automate Your Rental Properties with SaaS.</span>
        </h1>
        <p class="hero-subtext">
          ExaInfra is India's all-in-one rental ecosystem: zero-brokerage direct flats, e-stamped 11-month legal rental agreements, automated HRA receipts, and UPI rent collection SaaS for landlords.
        </p>

        <!-- 3 Core Pillars Tabs -->
        <div style="display:flex; justify-content:center; gap:0.75rem; flex-wrap:wrap; margin-top:1.5rem;">
          <a href="#explore-apartments" class="btn btn-secondary" style="text-decoration:none; font-weight:700;">
            <span>🏠 Browse Direct Owner Flats</span>
          </a>
          <a href="#rental-agreement" class="btn btn-secondary" style="text-decoration:none; font-weight:700;">
            <span>📜 11-Month Lease & HRA Studio</span>
          </a>
          <a href="#landlord-saas" class="btn btn-primary" style="text-decoration:none; font-weight:700;">
            <span>💼 Landlord SaaS Dashboard</span>
          </a>
        </div>
      </div>

      <!-- Search Workbench -->
      <div class="search-workbench-card">
        <!-- Search Type Tabs -->
        <div class="search-tabs-header">
          <button class="tab-btn active" data-type="rent">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path></svg>
            <span>Full Apartments (Direct Rent)</span>
          </button>
          <button class="tab-btn" data-type="flatmates">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path><circle cx="9" cy="7" r="4"></circle><path d="M23 21v-2a4 4 0 0 0-3-3.87"></path><path d="M16 3.13a4 4 0 0 1 0 7.75"></path></svg>
            <span>Flatmates / Co-Living</span>
          </button>
          <button class="tab-btn" data-type="commercial">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="3" width="20" height="14" rx="2" ry="2"></rect><line x1="8" y1="21" x2="16" y2="21"></line><line x1="12" y1="17" x2="12" y2="21"></line></svg>
            <span>Commercial Office</span>
          </button>
        </div>

        <!-- Bangalore Locality Quick Filters -->
        <div class="blr-locality-filter-bar">
          <span class="ps-label">Bengaluru Corridors:</span>
          <div class="blr-filter-chips" id="bangaloreLocalityChips">
            <button class="loc-chip active" data-locality="all">All Bangalore</button>
            <button class="loc-chip" data-locality="Outer Ring Road">Bellandur & ORR</button>
            <button class="loc-chip" data-locality="Whitefield">Whitefield & ITPL</button>
            <button class="loc-chip" data-locality="Koramangala">Koramangala</button>
            <button class="loc-chip" data-locality="Indiranagar">Indiranagar</button>
            <button class="loc-chip" data-locality="HSR">HSR Layout</button>
            <button class="loc-chip" data-locality="Sarjapur">Sarjapur Road</button>
            <button class="loc-chip" data-locality="Marathahalli">Marathahalli</button>
            <button class="loc-chip" data-locality="Electronic City">Electronic City</button>
            <button class="loc-chip" data-locality="Kanakapura">Kanakapura Road</button>
          </div>
        </div>

        <!-- Search Inputs Grid -->
        <div class="search-inputs-grid">
          <!-- City -->
          <div class="search-input-field">
            <label for="filterCity">Location / City</label>
            <div class="input-wrap">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path><circle cx="12" cy="10" r="3"></circle></svg>
              <select id="filterCity">
                <option value="Bengaluru" selected>Bengaluru (Prime Tech Corridors)</option>
                <option value="Mumbai">Mumbai</option>
                <option value="Delhi-NCR">Delhi-NCR</option>
                <option value="Hyderabad">Hyderabad</option>
                <option value="Pune">Pune</option>
                <option value="all">All Top Indian Metros</option>
              </select>
            </div>
          </div>

          <!-- Configuration (BHK) -->
          <div class="search-input-field">
            <label for="filterBhk">Apartment Size (BHK)</label>
            <div class="input-wrap">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path></svg>
              <select id="filterBhk">
                <option value="all">All Configurations</option>
                <option value="1 BHK">1 BHK Flat</option>
                <option value="2 BHK">2 BHK Flat</option>
                <option value="3 BHK">3 BHK Flat</option>
                <option value="4+ BHK">4+ BHK / Villa</option>
              </select>
            </div>
          </div>

          <!-- Furnishing Status -->
          <div class="search-input-field">
            <label for="filterFurnishing">Furnishing Status</label>
            <div class="input-wrap">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="7" width="20" height="14" rx="2" ry="2"></rect><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"></path></svg>
              <select id="filterFurnishing">
                <option value="all">Any Furnishing</option>
                <option value="Fully Furnished">Fully Furnished</option>
                <option value="Semi Furnished">Semi Furnished</option>
              </select>
            </div>
          </div>

          <!-- Monthly Budget Range -->
          <div class="search-input-field budget-box">
            <div class="budget-header">
              <label for="filterMaxBudget">Max Monthly Budget</label>
              <span class="budget-chip" id="budgetChipDisplay">₹1,50,000 / mo</span>
            </div>
            <input type="range" id="filterMaxBudget" min="15000" max="150000" step="5000" value="150000" class="custom-range-slider">
          </div>
        </div>

        <!-- Search Action Bar -->
        <div class="search-footer-action-bar">
          <div class="quick-amenity-tags">
            <span class="q-tag-label">Must Have:</span>
            <button class="amenity-chip" data-amenity="gym">Gym</button>
            <button class="amenity-chip" data-amenity="pool">Swimming Pool</button>
            <button class="amenity-chip" data-amenity="pets">Pet Friendly</button>
            <button class="amenity-chip" data-amenity="gated">Gated Society</button>
          </div>

          <div class="search-btns-group">
            <button class="btn btn-save-search" id="btnSaveSearchAlert" title="Save this search to get instant alerts">
              <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M19 21l-7-5-7 5V5a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2z"></path></svg>
              <span>Save Search Alert</span>
            </button>
            <button class="btn btn-secondary" id="btnResetFilters">Reset</button>
            <button class="btn btn-primary btn-search-execute" id="btnExecuteSearch">
              <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
              <span>Search Direct Owner Flats</span>
            </button>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Section 1: Explore Direct Owner Apartments -->
  <section class="listings-section" id="explore-apartments">
    <div class="container">
      <div class="listings-header-clean">
        <div class="lh-left">
          <h2>Direct Owner Verified Rentals</h2>
          <p class="lh-sub">100% Zero Brokerage. Connect with verified landlords via direct in-app chat, schedule visits, and reserve flats online.</p>
        </div>
        <div class="lh-right">
          <span class="results-badge-clean"><span id="searchResultCount">12</span> Properties Available</span>
          <div class="sort-wrap-clean">
            <label for="sortResults">Sort:</label>
            <select id="sortResults" class="sort-select-clean">
              <option value="featured">Verified Spotlight</option>
              <option value="price-low">Rent: Low to High</option>
              <option value="price-high">Rent: High to Low</option>
              <option value="newest">Newly Listed</option>
            </select>
          </div>
        </div>
      </div>

      <!-- Apartments Grid -->
      <div class="apartments-grid" id="apartmentsGrid">
        <!-- Rendered dynamically by app.js -->
      </div>

      <!-- Empty State -->
      <div class="empty-listings-state" id="emptyListingsState" style="display: none;">
        <div class="empty-icon-box">🏠</div>
        <h3>No direct owner flats match your exact filters</h3>
        <p>Try resetting the budget slider or selecting "All Bangalore" to view all verified properties.</p>
        <button class="btn btn-secondary" id="btnResetEmptySearch">Reset All Filters</button>
      </div>
    </div>
  </section>

  <!-- Section 2: Landlord & PG Management SaaS Dashboard -->
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
              <button class="btn btn-xs btn-primary" id="btnSimulateCollectAll">
                <span>⚡ Send WhatsApp Rent Links to All Units</span>
              </button>
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
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:1rem;">
              <h4 style="font-size:1.05rem; font-weight:800; color:#F8FAFC; margin:0;">Active Leases & Security Deposits</h4>
              <button class="btn btn-xs btn-secondary" onclick="openModal(document.getElementById('modalAgreementPreview'))">
                <span>+ Draft New Lease Agreement</span>
              </button>
            </div>
            <div class="saas-table-wrap">
              <table class="saas-table">
                <thead>
                  <tr>
                    <th>Unit</th>
                    <th>Tenant</th>
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
                    <td><button class="btn btn-xs btn-secondary" onclick="showToast('✓ Lease in good standing')">Check Status</button></td>
                  </tr>
                  <tr>
                    <td>UNIT-201 (Godrej)</td>
                    <td>Rahul Mehta</td>
                    <td><strong style="color:#38BDF8;">₹99,000</strong></td>
                    <td>11 Months</td>
                    <td>31 Dec 2026</td>
                    <td><button class="btn btn-xs btn-primary" onclick="showToast('📋 Automated 11-Month Renewal draft generated!')">Renew Lease</button></td>
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
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:1rem;">
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
                      <button class="btn btn-xs btn-primary" onclick="this.parentElement.previousElementSibling.innerHTML='<span class=\\'saas-badge-paid\\'>✓ Resolved</span>'; this.remove(); showToast('✓ Ticket marked as Resolved!');">
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
                      <button class="btn btn-xs btn-primary" onclick="this.parentElement.previousElementSibling.innerHTML='<span class=\\'saas-badge-paid\\'>✓ Resolved</span>'; this.remove(); showToast('✓ Ticket marked as Resolved!');">
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

  <!-- Section 3: Legal Lease Agreements & HRA Tax Receipts Studio -->
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
      <div id="studioHraView" class="agreement-clean-layout" style="display:none;">
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
                <strong>100% Free for ExaInfra Tenants</strong>
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

              <button type="submit" class="btn btn-primary btn-full btn-lg">
                <span>Generate & Preview 12 Monthly HRA Receipts &rarr;</span>
              </button>
            </form>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Section 4: AI Rental Valuation & Rent Estimator -->
  <section class="estimator-section" id="rent-estimator">
    <div class="container">
      <div class="estimator-clean-card">
        <div class="est-header-clean">
          <span class="section-tag-light">AI RENTAL VALUATION</span>
          <h2>How Much Can You Rent Your Flat For?</h2>
          <p>Instant market rent prediction based on real verified Bengaluru society lease deeds.</p>
        </div>

        <div class="est-clean-grid">
          <div class="est-controls-clean">
            <div class="form-group">
              <label for="estLocality">Bangalore Tech Locality</label>
              <select id="estLocality" class="form-control-clean">
                <option value="Whitefield">Whitefield / ITPL Corridor</option>
                <option value="Indiranagar">Indiranagar 100ft / 12th Main</option>
                <option value="Koramangala" selected>Koramangala 3rd/4th Block</option>
                <option value="Bellandur">Bellandur & Outer Ring Road</option>
                <option value="HSR Layout">HSR Layout (Sectors 1-7)</option>
                <option value="Sarjapur">Sarjapur Road</option>
                <option value="Kanakapura">Kanakapura Road</option>
                <option value="Electronic City">Electronic City Phase 1</option>
              </select>
            </div>

            <div class="form-group">
              <label for="estBhk">Configuration</label>
              <select id="estBhk" class="form-control-clean">
                <option value="1">1 BHK Apartment</option>
                <option value="2" selected>2 BHK Apartment</option>
                <option value="3">3 BHK Apartment</option>
                <option value="4">4+ BHK / Penthouse</option>
              </select>
            </div>

            <div class="form-group">
              <label for="estFurnish">Furnishing Level</label>
              <select id="estFurnish" class="form-control-clean">
                <option value="unfurnished">Unfurnished</option>
                <option value="semi" selected>Semi-Furnished</option>
                <option value="fully">Fully Furnished</option>
              </select>
            </div>

            <div class="form-group">
              <label for="estArea">Carpet Area: <span id="estAreaDisplay">1,250 sq.ft</span></label>
              <input type="range" id="estArea" min="500" max="3500" step="50" value="1250" class="custom-range-slider">
            </div>
          </div>

          <div class="est-results-clean">
            <span class="est-result-label">ESTIMATED FAIR MARKET RENT</span>
            <div class="est-rent-display" id="estRentDisplay">₹42,000 - ₹48,000</div>
            <div class="est-deposit-display" id="estDepositDisplay">Typical Security Deposit: <strong>₹1.2L - ₹1.5L</strong></div>

            <div class="est-breakdown-list">
              <div class="est-breakdown-item">
                <span>Projected Annual Rental Income:</span>
                <strong id="estAnnualYield">₹5,40,000 / yr</strong>
              </div>
              <div class="est-breakdown-item">
                <span>Average Tenant Find Time:</span>
                <strong class="text-green">7 to 10 Days</strong>
              </div>
              <div class="est-breakdown-item">
                <span>Rental Yield (Bengaluru Avg):</span>
                <strong>4.8% per annum</strong>
              </div>
            </div>

            <button class="btn btn-primary btn-full" id="btnEstPostFlat">
              <span>Post This Flat for Free (5 Free Posts) &rarr;</span>
            </button>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Section 5: Transparent Pricing & SaaS Monetization Plans -->
  <section class="pricing-section" id="pricing-plans">
    <div class="container">
      <div class="text-center-wrapper">
        <span class="section-tag-light">TRANSPARENT MONETIZATION</span>
        <h2 class="section-title-clean">Affordable Plans for Renters, Landlords & Leases</h2>
        <p class="section-desc-clean">
          Free to start. Upgrade only when you need unlimited power, automated rent collections, or court-stamped lease deeds.
        </p>
      </div>

      <div class="pricing-cards-grid">
        <!-- Tenant Freedom Pass -->
        <div class="pricing-card popular">
          <div class="pricing-badge-popular">MOST POPULAR</div>
          <h3 class="p-plan-name">Tenant Freedom Pass</h3>
          <p class="p-plan-desc">For active renters seeking direct owner apartments without broker commissions.</p>
          <div class="p-price-row">
            <span class="amt">₹399</span>
            <span class="dur">/ one-time</span>
          </div>
          <ul class="p-features-list">
            <li><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"></polyline></svg> 20 Free Inquiries included by default</li>
            <li><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"></polyline></svg> <strong>Unlimited Direct Landlord Chats & Calls</strong></li>
            <li><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"></polyline></svg> Priority Physical & Video Visit Scheduling</li>
            <li><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"></polyline></svg> Free 12-Month HRA Tax Receipts Package</li>
            <li><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"></polyline></svg> ₹300 Discount on E-Stamped Digital Lease</li>
          </ul>
          <button class="btn btn-primary btn-full" id="btnBuyTenantFreedomPass">
            <span>Get Tenant Freedom Pass (₹399)</span>
          </button>
        </div>

        <!-- Landlord Pro SaaS -->
        <div class="pricing-card">
          <h3 class="p-plan-name">Landlord Pro SaaS</h3>
          <p class="p-plan-desc">For homeowners and PG operators managing multiple rental units.</p>
          <div class="p-price-row">
            <span class="amt">₹999</span>
            <span class="dur">/ year</span>
          </div>
          <ul class="p-features-list">
            <li><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"></polyline></svg> <strong>5 Free Property Postings included forever</strong></li>
            <li><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"></polyline></svg> Unlimited Property Postings on ExaInfra</li>
            <li><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"></polyline></svg> Verified Spotlight Badge (5x more inquiries)</li>
            <li><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"></polyline></svg> Automated UPI Rent Collection & Reminders</li>
            <li><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"></polyline></svg> Tenant Maintenance & Repair Ticket Tracker</li>
          </ul>
          <button class="btn btn-secondary btn-full" id="btnBuyLandlordPro">
            <span>Upgrade to Landlord Pro (₹999)</span>
          </button>
        </div>

        <!-- Digital Lease Agreement -->
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
            <li><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"></polyline></svg> Basic PDF draft option available at ₹499</li>
          </ul>
          <button class="btn btn-secondary btn-full" onclick="document.getElementById('rental-agreement').scrollIntoView({behavior:'smooth'})">
            <span>Draft Rental Agreement Now</span>
          </button>
        </div>
      </div>
    </div>
  </section>

  <!-- Section 6: How It Works -->
  <section class="how-it-works-clean" id="how-it-works">
    <div class="container">
      <div class="text-center-wrapper">
        <span class="section-tag-light">SIMPLE & TRANSPARENT</span>
        <h2 class="section-title-clean">How ExaInfra Powers Your Rental Journey</h2>
        <p class="section-desc-clean">Direct connections, verified owners, and frictionless digital infrastructure.</p>
      </div>

      <div class="steps-clean-grid">
        <div class="step-clean-box">
          <div class="step-clean-num">1</div>
          <h3>Browse Direct Owner Flats</h3>
          <p>Explore 100% direct homeowner listings in prime Bangalore societies with verified rents, high-res photos, and zero brokerage fees.</p>
        </div>

        <div class="step-clean-box">
          <div class="step-clean-num">2</div>
          <h3>Chat Direct & Book Free Tour</h3>
          <p>Use your <strong>20 free inquiries</strong> to chat directly with landlords, schedule in-person visits or WhatsApp video walkthroughs.</p>
        </div>

        <div class="step-clean-box">
          <div class="step-clean-num">3</div>
          <h3>Digital Lease & UPI Management</h3>
          <p>Execute an official 11-month e-stamped rental deed, reserve your flat with a ₹10K token, and manage monthly rent via automated UPI.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- Site Footer -->
  <footer class="site-footer">
    <div class="container">
      <div class="footer-columns">
        <div class="footer-col brand-col">
          <div class="brand-logo">
            <div class="brand-icon">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path><polyline points="9 22 9 12 15 12 15 22"></polyline></svg>
            </div>
            <div class="brand-name">
              <span class="logo-main">EXA<span class="logo-accent">INFRA</span></span>
              <span class="logo-sub">RENTALS.IN</span>
            </div>
          </div>
          <p class="footer-desc">
            India's direct owner rental platform, legal lease deed studio, and landlord property management SaaS.
          </p>
          <div class="footer-contact">
            <p><strong>Support Helpline:</strong>  (Mon - Sat, 9 AM - 8 PM)</p>
            <p><strong>Email:</strong> help@exainfra.in</p>
          </div>
        </div>

        <div class="footer-col">
          <h4>Direct Rental Corridors</h4>
          <ul class="footer-links">
            <li><a href="#explore-apartments">Bellandur & Outer Ring Road Flats</a></li>
            <li><a href="#explore-apartments">Whitefield & ITPL Tech Hub</a></li>
            <li><a href="#explore-apartments">Koramangala 3rd & 4th Block</a></li>
            <li><a href="#explore-apartments">Indiranagar 100ft Road</a></li>
            <li><a href="#explore-apartments">HSR Layout Sectors 1-7</a></li>
          </ul>
        </div>

        <div class="footer-col">
          <h4>Legal & SaaS Services</h4>
          <ul class="footer-links">
            <li><a href="#rental-agreement">11-Month Digital Rental Agreement</a></li>
            <li><a href="#rental-agreement">Free HRA Tax Rent Receipts Generator</a></li>
            <li><a href="#landlord-saas">Landlord & PG Management Dashboard</a></li>
            <li><a href="#pricing-plans">Tenant Freedom Pass (₹399)</a></li>
            <li><a href="#pricing-plans">Landlord Pro Annual SaaS (₹999)</a></li>
          </ul>
        </div>

        <div class="footer-col">
          <h4>Customer Guarantees</h4>
          <ul class="footer-links">
            <li><a href="#explore-apartments">Zero Brokerage Guarantee</a></li>
            <li><a href="#explore-apartments">Landlords: 5 Free Property Postings</a></li>
            <li><a href="#explore-apartments">Tenants: 20 Free Landlord Inquiries</a></li>
            <li><a href="#explore-apartments">Aadhaar E-Stamped Deeds</a></li>
            <li><a href="#explore-apartments">Refundable ₹10,000 Token Escrow</a></li>
          </ul>
        </div>
      </div>

      <div class="footer-bottom-strip">
        <p>&copy; 2026 ExaInfra Rentals Technologies Private Limited (exainfra.in). All rights reserved.</p>
        <div class="footer-trust-tags">
          <span>🔒 256-Bit SSL Secured</span>
          <span>⚖ IT Act 2000 Compliant</span>
          <span>⚡ Instant UPI Enabled</span>
        </div>
      </div>
    </div>
  </footer>

  <!-- ==========================================================================
       MODALS
       ========================================================================== -->

  <!-- MODAL 1: Post Apartment Modal (5 Free Quota) -->
  <div class="modal-backdrop" id="modalPostApartment">
    <div class="modal-box modal-lg">
      <button class="modal-close-btn" id="closeModalPost" aria-label="Close modal">&times;</button>
      
      <div class="modal-header-clean">
        <span class="modal-badge-clean">DIRECT LANDLORD PORTAL</span>
        <h3>Post Your Apartment for Rent</h3>
        <p>Landlords get <strong class="text-coral">5 Free Property Postings</strong>. Verified tenants will contact you directly via in-app chat.</p>
      </div>

      <form id="formPostApartment" class="modal-form-clean">
        <div class="form-row-clean">
          <div class="form-group">
            <label for="postTitle">Property Listing Title *</label>
            <input type="text" id="postTitle" class="form-control-clean" placeholder="e.g. Prestige Falcon City — High-Rise 3 BHK" required>
          </div>
          <div class="form-group">
            <label for="postSociety">Apartment / Society Name *</label>
            <input type="text" id="postSociety" class="form-control-clean" placeholder="e.g. Prestige Falcon City" required>
          </div>
        </div>

        <div class="form-row-clean">
          <div class="form-group">
            <label for="postCity">City *</label>
            <select id="postCity" class="form-control-clean" required>
              <option value="Bengaluru" selected>Bengaluru</option>
              <option value="Mumbai">Mumbai</option>
              <option value="Delhi-NCR">Delhi-NCR</option>
              <option value="Hyderabad">Hyderabad</option>
              <option value="Pune">Pune</option>
            </select>
          </div>
          <div class="form-group">
            <label for="postLocality">Locality / Area *</label>
            <input type="text" id="postLocality" class="form-control-clean" placeholder="e.g. Kanakapura Road, Near Metro" required>
          </div>
        </div>

        <div class="form-row-clean">
          <div class="form-group">
            <label for="postBhk">Configuration *</label>
            <select id="postBhk" class="form-control-clean" required>
              <option value="1 BHK">1 BHK</option>
              <option value="2 BHK" selected>2 BHK</option>
              <option value="3 BHK">3 BHK</option>
              <option value="4+ BHK">4+ BHK / Penthouse</option>
            </select>
          </div>
          <div class="form-group">
            <label for="postFurnishing">Furnishing *</label>
            <select id="postFurnishing" class="form-control-clean" required>
              <option value="Semi Furnished" selected>Semi Furnished</option>
              <option value="Fully Furnished">Fully Furnished</option>
              <option value="Unfurnished">Unfurnished</option>
            </select>
          </div>
          <div class="form-group">
            <label for="postArea">Carpet Area (sq.ft) *</label>
            <input type="number" id="postArea" class="form-control-clean" placeholder="1250" value="1250" required>
          </div>
        </div>

        <div class="form-row-clean">
          <div class="form-group">
            <label for="postRent">Monthly Rent (₹) *</label>
            <input type="number" id="postRent" class="form-control-clean" placeholder="45000" value="45000" required>
          </div>
          <div class="form-group">
            <label for="postDeposit">Security Deposit (₹) *</label>
            <input type="number" id="postDeposit" class="form-control-clean" placeholder="135000" value="135000" required>
          </div>
        </div>

        <div class="form-row-clean">
          <div class="form-group">
            <label for="postOwnerName">Owner Full Name *</label>
            <input type="text" id="postOwnerName" class="form-control-clean" value="Vikramaditya Sharma" required>
          </div>
          <div class="form-group">
            <label for="postOwnerPhone">Mobile / WhatsApp Number *</label>
            <input type="tel" id="postOwnerPhone" class="form-control-clean" value="" required>
          </div>
        </div>

        <button type="submit" class="btn btn-primary btn-full btn-lg" id="btnSubmitPostApartment">
          <span>Publish Free Listing (Uses 1 of 5 Free Posts) &rarr;</span>
        </button>
      </form>
    </div>
  </div>

  <!-- MODAL 2: Apartment Detail & Visit Modal -->
  <div class="modal-backdrop" id="modalApartmentDetail">
    <div class="modal-box modal-lg">
      <button class="modal-close-btn" id="closeModalDetail" aria-label="Close modal">&times;</button>
      <div class="detail-modal-layout" id="detailModalContent">
        <!-- Rendered dynamically -->
      </div>
    </div>
  </div>

  <!-- MODAL 3: In-App Chat with Landlord (20 Free Chats) -->
  <div class="modal-backdrop" id="modalInAppChat">
    <div class="modal-box modal-lg chat-clean-modal">
      <button class="modal-close-btn" id="closeModalChat" aria-label="Close modal">&times;</button>
      
      <div class="chat-header-clean">
        <div class="chat-avatar-clean" id="chatOwnerAvatar">SP</div>
        <div class="chat-info-clean">
          <div class="chat-name-badge-row">
            <h4 id="chatLandlordName">Suresh Prabhu</h4>
            <span class="source-tag-pill" id="chatSourceTag" style="background:#ECFDF5; color:#059669;">Direct Owner Verified</span>
          </div>
          <p id="chatAptSnippet">Prestige Falcon City &bull; ₹52,000/mo &bull; Replies in 10 mins</p>
        </div>
        <div class="chat-quota-counter-clean">
          <span class="q-lbl">Free Inquiries:</span>
          <strong id="chatFreeQuotaText" class="text-coral">18/20 Left</strong>
        </div>
      </div>

      <div class="quick-inquiry-chips-clean" id="quickInquiryChips">
        <button class="quick-chip-clean" data-msg="Hi, is this apartment available for immediate move-in?">Immediate Move-in?</button>
        <button class="quick-chip-clean" data-msg="Are bachelors or working professionals allowed?">Bachelors allowed?</button>
        <button class="quick-chip-clean" data-msg="Can we schedule a physical visit this Saturday/Sunday?">Visit this weekend?</button>
        <button class="quick-chip-clean" data-msg="Is the security deposit slightly negotiable?">Deposit negotiable?</button>
      </div>

      <div class="chat-messages-thread-clean" id="chatMessagesThread">
        <!-- Dynamic chat bubbles -->
      </div>

      <form id="formSendChatMessage" class="chat-input-clean">
        <input type="text" id="chatInputText" class="chat-input-text" placeholder="Type your message to the owner..." required autocomplete="off">
        <button type="submit" class="btn btn-primary btn-chat-send" id="btnSendChatMsg">
          <span>Send</span>
          <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><line x1="22" y1="2" x2="11" y2="13"></line><polygon points="22 2 15 22 11 13 2 9 22 2"></polygon></svg>
        </button>
      </form>

      <div class="chat-bottom-actions">
        <button class="btn btn-secondary btn-sm" id="btnScheduleVisitFromChat">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect><line x1="16" y1="2" x2="16" y2="6"></line><line x1="8" y1="2" x2="8" y2="6"></line><line x1="3" y1="10" x2="21" y2="10"></line></svg>
          <span>Schedule Visit</span>
        </button>
        <button class="btn btn-emerald btn-sm" id="btnConfirmRentalFromChat">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg>
          <span>Confirm & Reserve Flat</span>
        </button>
      </div>
    </div>
  </div>

  <!-- MODAL 4: User Account & Role Switcher -->
  <div class="modal-backdrop" id="modalUserAccount">
    <div class="modal-box">
      <button class="modal-close-btn" id="closeModalAccount" aria-label="Close modal">&times;</button>
      
      <div class="modal-header-clean">
        <span class="modal-badge-clean">USER ACCOUNT</span>
        <h3>Manage Account & Roles</h3>
        <p>Switch between Tenant and Landlord mode to test free allowances.</p>
      </div>

      <div class="account-card-clean">
        <div class="acc-user-row">
          <div class="acc-avatar-large">👤</div>
          <div>
            <h4 id="accUserName">Aditya Saxena</h4>
            <p id="accUserEmail">aditya@tenant.com &bull; </p>
          </div>
        </div>

        <div class="role-selector-pills">
          <button class="role-pill-btn active" id="btnSwitchTenantRole" data-role="tenant">
            <span>Tenant Mode (Search & Chat)</span>
          </button>
          <button class="role-pill-btn" id="btnSwitchLandlordRole" data-role="landlord">
            <span>Landlord Mode (Post Flats)</span>
          </button>
        </div>

        <div class="quota-progress-clean">
          <div class="qp-labels">
            <span id="accQuotaLabel">Free Landlord Inquiries Remaining:</span>
            <strong id="accQuotaValue" class="text-green">18 of 20 Free Chats</strong>
          </div>
          <div class="qp-bar-track">
            <div class="qp-bar-fill" id="accQuotaBar" style="width: 90%;"></div>
          </div>
          <p class="qp-note" id="accQuotaNote">Tenants get 20 free inquiries to direct owners. Upgrade to ₹399 Freedom Pass for unlimited access.</p>
        </div>

        <button class="btn btn-secondary btn-full" id="btnTriggerAccountUpgrade">
          <span id="btnAccountUpgradeText">Upgrade to ₹399 Tenant Freedom Pass</span>
        </button>
      </div>
    </div>
  </div>

  <!-- MODAL 5: Saved Searches Modal -->
  <div class="modal-backdrop" id="modalSavedSearches">
    <div class="modal-box">
      <button class="modal-close-btn" id="closeModalSaved" aria-label="Close modal">&times;</button>
      <div class="modal-header-clean">
        <span class="modal-badge-clean">SAVED SEARCH ALERTS</span>
        <h3>Your Instant Property Alerts</h3>
        <p>Receive WhatsApp & email notifications the second a direct owner posts a flat matching your criteria.</p>
      </div>
      <div class="saved-searches-list-clean" id="savedSearchesContainer">
        <!-- Rendered dynamically -->
      </div>
    </div>
  </div>

  <!-- MODAL 6: Confirm Rental Property & Lock-in Token -->
  <div class="modal-backdrop" id="modalConfirmProperty">
    <div class="modal-box">
      <button class="modal-close-btn" id="closeModalConfirm" aria-label="Close modal">&times;</button>
      
      <div class="modal-header-clean">
        <span class="modal-badge-clean">RESERVATION PROTOCOL</span>
        <h3>Confirm & Reserve Rental Flat</h3>
        <p id="confirmAptTitle">Prestige Falcon City — Luxury 3 BHK</p>
      </div>

      <div id="confirmFormState">
        <div class="confirm-summary-box-clean">
          <div class="c-clean-row">
            <span>Monthly Rent:</span>
            <strong id="confMonthlyRent">₹52,000 / mo</strong>
          </div>
          <div class="c-clean-row">
            <span>Security Deposit:</span>
            <strong id="confSecurityDeposit">₹1,56,000</strong>
          </div>
          <div class="c-clean-row highlight">
            <span>Refundable Lock-in Token:</span>
            <strong class="text-green">₹10,000</strong>
          </div>
          <p class="c-note-clean">🔒 Fully refundable token locks the apartment exclusively for you for 7 days while the digital lease deed is signed.</p>
        </div>

        <form id="formConfirmRental" class="modal-form-clean">
          <div class="form-row-clean">
            <div class="form-group">
              <label for="confTenantName">Full Name *</label>
              <input type="text" id="confTenantName" class="form-control-clean" value="Aditya Saxena" required>
            </div>
            <div class="form-group">
              <label for="confTenantPhone">WhatsApp Number *</label>
              <input type="tel" id="confTenantPhone" class="form-control-clean" value="" required>
            </div>
          </div>

          <div class="form-row-clean">
            <div class="form-group">
              <label for="confMoveInDate">Move-in Date *</label>
              <input type="date" id="confMoveInDate" class="form-control-clean" required>
            </div>
            <div class="form-group">
              <label for="confTenantEmail">Email Address *</label>
              <input type="email" id="confTenantEmail" class="form-control-clean" value="aditya@tenant.com" required>
            </div>
          </div>

          <button type="submit" class="btn btn-primary btn-full btn-lg" id="btnPayTokenConfirm">
            <span>Pay ₹10,000 Token & Reserve Flat &rarr;</span>
          </button>
        </form>
      </div>

      <!-- Success State -->
      <div id="confirmSuccessState" class="confirm-success-clean" style="display: none;">
        <div class="success-seal-clean">✓</div>
        <h3>Rental Property Confirmed & Reserved!</h3>
        <p>Your flat reservation is confirmed. The landlord has been notified to hold the keys.</p>

        <div class="cert-clean-box">
          <div class="cert-row">
            <span>Booking Code:</span>
            <strong id="certBookingCode" class="text-coral">EXA-RENT-791055</strong>
          </div>
          <div class="cert-row">
            <span>Move-in Date:</span>
            <strong id="certMoveInDate">1st of Next Month</strong>
          </div>
        </div>

        <a href="#rental-agreement" class="btn btn-primary btn-full" id="btnGoToAgreementFromConfirm">
          <span>Proceed to 11-Month Digital Agreement &rarr;</span>
        </a>
      </div>
    </div>
  </div>

  <!-- MODAL 7: Quota Upgrade Modal -->
  <div class="modal-backdrop" id="modalQuotaUpgrade">
    <div class="modal-box">
      <button class="modal-close-btn" id="closeModalQuota" aria-label="Close modal">&times;</button>
      
      <div class="modal-header-clean">
        <span class="modal-badge-warn-clean">QUOTA LIMIT REACHED</span>
        <h3 id="quotaUpgradeTitle">Free Allowance Utilized</h3>
        <p id="quotaUpgradeDesc">You have utilized your free quota allowance.</p>
      </div>

      <div class="upgrade-package-clean" id="upgradePackageCard">
        <!-- Rendered dynamically -->
      </div>

      <button class="btn btn-primary btn-full btn-lg" id="btnSimulateBuyQuota">
        <span id="btnQuotaPayText">Upgrade Now &rarr;</span>
      </button>
    </div>
  </div>

  <!-- MODAL 8: Rental Agreement Preview Modal -->
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

  <!-- MODAL 9: HRA Rent Receipts Preview Modal -->
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

print("Generated clean index.html successfully.")
