html_content = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>ExaInfra.in — National Real Estate Due Diligence, Commercial Yield & Asset Terminal</title>
  <meta name="description" content="India's sovereign-standard intelligence terminal for property legal due diligence, commercial real estate (CRE) pre-leased yield modeling, CPWD-compliant construction cost BoQs, and Vahan 4.0 fleet asset compliance.">
  <meta name="keywords" content="property legal due diligence india, a khata verification bangalore, rajakaluve lake buffer checker, commercial real estate pre-leased yield india, cpwd construction cost calculator, vahan rc verification challan radar, rera litigation check">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="style.css">
</head>
<body>

  <!-- Top National Statutory Ticker Bar -->
  <div class="national-ticker-bar">
    <div class="container ticker-inner">
      <div class="compliance-status-pill">
        <span class="live-pulse-dot"></span>
        <span>STATUTORY COMPLIANCE NODE: <strong>ACTIVE</strong></span>
      </div>
      <div class="ticker-text">
        <span>Compliant with <strong>RERA Act 2016</strong> &bull; <strong>IT Act 2000 (Sec 65B)</strong> &bull; <strong>Motor Vehicles Act 1988</strong> &bull; <strong>DPDP Act 2023</strong> &bull; <strong>CPWD DSR 2026</strong> Standards</span>
      </div>
      <div class="ticker-node">
        <span>SERVER NODE: IN-BLR-CENTRAL-01</span>
      </div>
    </div>
  </div>

  <!-- Main Navigation Header -->
  <header class="navbar-terminal" id="mainNavbar">
    <div class="container nav-container">
      <a href="#" class="brand-wrap">
        <div class="brand-emblem">
          <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2">
            <path d="M12 2L2 7l10 5 10-5-10-5z"></path>
            <path d="M2 17l10 5 10-5"></path>
            <path d="M2 12l10 5 10-5"></path>
          </svg>
        </div>
        <div class="brand-text-col">
          <div class="brand-title">EXA<span>INFRA</span></div>
          <div class="brand-sub">NATIONAL ASSET & LEGAL TERMINAL</div>
        </div>
      </a>

      <!-- Desktop Nav Menu -->
      <nav class="nav-menu">
        <a href="#legal-radar" class="nav-link active">Property Scam Radar</a>
        <a href="#cre-terminal" class="nav-link">CRE Yield Terminal</a>
        <a href="#build-boq" class="nav-link">Construction BoQ</a>
        <a href="#vahan-fleet" class="nav-link">VAHAN & Fleet</a>
        <a href="#pricing-plans" class="nav-link">Statutory Plans</a>
        <a href="#regulatory-framework" class="nav-link">Regulatory Acts</a>
      </nav>

      <div class="nav-actions">
        <a href="#legal-radar" class="btn btn-primary btn-sm">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"></polygon></svg>
          <span>Instant Property Audit</span>
        </a>

        <!-- Mobile Hamburger Toggle -->
        <button class="mobile-toggle-btn" id="btnMobileToggle" aria-label="Toggle Navigation Menu">
          <span></span>
          <span></span>
          <span></span>
        </button>
      </div>
    </div>
  </header>

  <!-- Mobile Navigation Drawer -->
  <div class="mobile-nav-drawer" id="mobileNavDrawer">
    <div class="mobile-nav-header">
      <div class="brand-title">EXA<span style="color:var(--saffron-600);">INFRA</span></div>
      <button class="mobile-close-btn" id="btnMobileClose" aria-label="Close Mobile Menu">&times;</button>
    </div>
    <div class="mobile-nav-links">
      <a href="#legal-radar" class="mobile-link" onclick="closeMobileNav()">🛡️ Property Scam Radar</a>
      <a href="#cre-terminal" class="mobile-link" onclick="closeMobileNav()">🏢 CRE Yield Terminal</a>
      <a href="#build-boq" class="mobile-link" onclick="closeMobileNav()">🏗️ Construction BoQ</a>
      <a href="#vahan-fleet" class="mobile-link" onclick="closeMobileNav()">🚗 VAHAN & Fleet</a>
      <a href="#pricing-plans" class="mobile-link" onclick="closeMobileNav()">📊 Statutory Plans</a>
      <a href="#regulatory-framework" class="mobile-link" onclick="closeMobileNav()">⚖️ Regulatory Acts</a>
    </div>
    <div style="margin-top: 1.5rem;">
      <a href="#legal-radar" class="btn btn-primary btn-full" onclick="closeMobileNav()">
        <span>⚡ Instant Property Audit</span>
      </a>
    </div>
  </div>

  <!-- Hero Section: Institutional Sovereign Asset Terminal -->
  <section class="hero-terminal">
    <div class="container">
      <div class="hero-seal-badge">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><circle cx="12" cy="12" r="10"></circle><path d="M12 6v6l4 2"></path></svg>
        <span>REPUBLIC OF INDIA REGULATORY STANDARDS & IT ACT 2000 ADMISSIBLE</span>
      </div>

      <h1 class="hero-headline">
        National Real Estate Due Diligence,<br>
        <span class="highlight-saffron">Commercial Yield & Asset Compliance Terminal.</span>
      </h1>

      <p class="hero-description">
        ExaInfra is India's sovereign-standard intelligence engine for high-stakes property legal audits, commercial real estate (CRE) pre-leased yield modeling, CPWD-compliant construction cost BoQs, and Vahan 4.0 fleet asset verification.
      </p>

      <!-- 4 Pillars Interactive Tab Switcher in Hero -->
      <div class="hero-pillars-nav">
        <button class="pillar-tab-btn active" data-pillar="radar" onclick="scrollToSection('legal-radar')">
          <span>🛡️ Property Legal Radar</span>
        </button>
        <button class="pillar-tab-btn" data-pillar="cre" onclick="scrollToSection('cre-terminal')">
          <span>🏢 Commercial Real Estate Yield</span>
        </button>
        <button class="pillar-tab-btn" data-pillar="boq" onclick="scrollToSection('build-boq')">
          <span>🏗️ Construction BoQ & Escrow</span>
        </button>
        <button class="pillar-tab-btn" data-pillar="vahan" onclick="scrollToSection('vahan-fleet')">
          <span>🚗 VAHAN 4.0 Fleet Audit</span>
        </button>
      </div>

      <!-- Hero Live Metric Bar -->
      <div class="hero-metric-bar">
        <div class="metric-cell">
          <div class="metric-val">₹4,850 Cr+</div>
          <div class="metric-lbl">Asset Value Screened</div>
        </div>
        <div class="metric-cell">
          <div class="metric-val">28,400+</div>
          <div class="metric-lbl">Title & Khata Audits</div>
        </div>
        <div class="metric-cell">
          <div class="metric-val">8.8% - 10.4%</div>
          <div class="metric-lbl">Pre-Leased CRE Cap Rates</div>
        </div>
        <div class="metric-cell">
          <div class="metric-val">100% Legal</div>
          <div class="metric-lbl">Section 65B Certified Proof</div>
        </div>
      </div>
    </div>
  </section>

  <!-- ====================================================================
       PILLAR 1: Property Due Diligence & Scam Risk Radar
       ==================================================================== -->
  <section class="radar-section" id="legal-radar">
    <div class="container">
      <div class="section-header-block">
        <span class="section-tag">LEGAL INTELLIGENCE ENGINE</span>
        <h2 class="section-title">Property Due Diligence & Scam Risk Radar</h2>
        <p class="section-desc">
          Detect land scams, A/B-Khata fraud, 50m Rajakaluve lake buffer encroachment, 30-year encumbrances, and RERA builder insolvency before transferring advance funds.
        </p>
      </div>

      <div class="radar-terminal-card">
        <!-- Search & Query Form -->
        <form id="formPropertyRadar" class="radar-search-box">
          <div class="form-field-radar">
            <label for="radarPropType">Property Asset Class</label>
            <select id="radarPropType" class="form-control-terminal">
              <option value="Apartment / Flat" selected>Apartment / High-Rise Flat</option>
              <option value="Gated Villa">Gated Community Villa</option>
              <option value="Agricultural Land">Agricultural Land Plot</option>
              <option value="Commercial Plot">Commercial Commercial Plot</option>
            </select>
          </div>

          <div class="form-field-radar">
            <label for="radarCity">Jurisdiction / Authority</label>
            <select id="radarCity" class="form-control-terminal">
              <option value="Bengaluru (BBMP / BDA / BMRDA)" selected>Bengaluru (BBMP / BDA)</option>
              <option value="Mumbai (BMC / MMRDA)">Mumbai (BMC / MMRDA)</option>
              <option value="Delhi-NCR (DDA / RERA)">Delhi-NCR (DDA / RERA)</option>
              <option value="Hyderabad (GHMC / HMDA)">Hyderabad (GHMC / HMDA)</option>
              <option value="Pune (PMC / PMRDA)">Pune (PMC / PMRDA)</option>
            </select>
          </div>

          <div class="form-field-radar">
            <label for="radarIdentifier">Survey No / Khata / RERA Project Name</label>
            <input type="text" id="radarIdentifier" class="form-control-terminal" value="Prestige Falcon City, Sy No 84, Kanakapura" placeholder="e.g. Sy No 142/2, Khata 890 or Project Name" required>
          </div>

          <div class="form-field-radar">
            <button type="submit" class="btn btn-primary" id="btnExecuteRadarAudit" style="height:42px;">
              <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
              <span>Scan Title & Demolition Risk</span>
            </button>
          </div>
        </form>

        <!-- Sample Quick-Load Chips -->
        <div class="sample-queries-row">
          <span style="font-size:0.75rem; color:var(--text-muted); font-family:var(--font-mono); font-weight:700;">Try Realistic Scenarios:</span>
          <button type="button" class="sample-query-chip" onclick="loadRadarSample('safe')">
            ✓ Sobha Silicon Oasis (Clear A-Khata & Nil Encumbrance)
          </button>
          <button type="button" class="sample-query-chip" onclick="loadRadarSample('danger')">
            ⚠ Lakeview Enclave, Varthur (Demolition Risk - 50m Rajakaluve Encroachment)
          </button>
          <button type="button" class="sample-query-chip" onclick="loadRadarSample('warning')">
            ⚡ Green Acres Farm (Form 15 Multiple Mortgage Encumbrance)
          </button>
        </div>

        <!-- Live Audit Results Interface -->
        <div class="radar-results-grid" id="radarResultsContainer">
          <!-- Left: Risk Gauge -->
          <div class="gauge-card">
            <div class="risk-dial safe" id="radarDialGauge">
              <span class="dial-score" id="radarScoreText">94</span>
              <span class="dial-lbl" id="radarScoreLbl">TITLE HEALTH</span>
            </div>
            <h3 class="risk-verdict-title text-green" id="radarVerdictTitle" style="color:var(--emerald-600);">A-GRADE CLEAN TITLE</h3>
            <p style="font-size:0.85rem; color:var(--text-muted); line-height:1.4;" id="radarVerdictSub">
              Nil encumbrance registered under Sub-Registrar records. Clear BBMP A-Khata with approved BDA building plan.
            </p>
            <button type="button" class="btn btn-secondary btn-sm" id="btnOpenTitleCertModal" style="margin-top:1.25rem;">
              <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline></svg>
              <span>View Sec 65B Certificate</span>
            </button>
          </div>

          <!-- Right: 5-Point Statutory Matrix -->
          <div class="matrix-container" id="radarMatrixContainer">
            <!-- Row 1 -->
            <div class="matrix-row">
              <div class="matrix-info">
                <h4>1. Master Plan 2031 Land-Use Zoning</h4>
                <p>Checked against BDA Comprehensive Development Plan (CDP) GIS mapping.</p>
              </div>
              <span class="status-badge pass" id="statZoning">✓ Yellow Residential Zone</span>
            </div>

            <!-- Row 2 -->
            <div class="matrix-row">
              <div class="matrix-info">
                <h4>2. Khata Classification & Revenue Legality</h4>
                <p>Karnataka Land Revenue Act (Section 95A Conversion & E-Khata issuance).</p>
              </div>
              <span class="status-badge pass" id="statKhata">✓ Validated BBMP A-Khata</span>
            </div>

            <!-- Row 3 -->
            <div class="matrix-row">
              <div class="matrix-info">
                <h4>3. 30-Year Encumbrance Audit (EC 1996-2026)</h4>
                <p>Kaveri 2.0 Sub-Registrar mortgage, court attachment & sale lien index.</p>
              </div>
              <span class="status-badge pass" id="statEc">✓ Form 16 (Nil Encumbrance)</span>
            </div>

            <!-- Row 4 -->
            <div class="matrix-row">
              <div class="matrix-info">
                <h4>4. NGT Rajakaluve (Stormwater) & Lake Buffer Check</h4>
                <p>National Green Tribunal mandate: 50m Primary drain, 25m Secondary drain.</p>
              </div>
              <span class="status-badge pass" id="statBuffer">✓ Zero Encroachment (Safe)</span>
            </div>

            <!-- Row 5 -->
            <div class="matrix-row">
              <div class="matrix-info">
                <h4>5. RERA Registration & NCLT Insolvency Radar</h4>
                <p>Cross-referenced with Karnataka RERA project tribunal orders & IBC defaults.</p>
              </div>
              <span class="status-badge pass" id="statRera">✓ RERA PRM/KA/RERA/1251 (Active)</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- ====================================================================
       PILLAR 2: Commercial Real Estate (CRE) & Pre-Leased Yield Terminal
       ==================================================================== -->
  <section class="cre-section" id="cre-terminal">
    <div class="container">
      <div class="section-header-block">
        <span class="section-tag">INSTITUTIONAL GRADE YIELD ENGINE</span>
        <h2 class="section-title">Commercial Real Estate (CRE) Pre-Leased Terminal</h2>
        <p class="section-desc">
          Institutional investment analysis for pre-leased bank branches, grade-A tech parks, and logistics warehouses with 8.5% to 10.4% gross yields and long lock-in covenants.
        </p>
      </div>

      <!-- 3 Verified Institutional Commercial Assets -->
      <div class="cre-assets-grid">
        <!-- Asset 1: Bank Branch -->
        <div class="cre-card">
          <div class="cre-card-header">
            <div>
              <span class="cre-tenant-pill">AAA COVENANT &bull; BANK LEASE</span>
              <h3 class="cre-asset-title">HDFC Bank Retail Branch</h3>
              <div class="cre-location">
                <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path></svg>
                <span>100ft Road, Indiranagar, Bengaluru</span>
              </div>
            </div>
          </div>

          <div class="cre-card-body">
            <div class="cre-metrics-strip">
              <div class="cre-spec-item">
                <span>GROSS YIELD</span>
                <strong style="color:var(--emerald-600);">8.8% p.a.</strong>
              </div>
              <div class="cre-spec-item">
                <span>MONTHLY RENT</span>
                <strong>₹3,55,000</strong>
              </div>
              <div class="cre-spec-item">
                <span>TOTAL ASSET COST</span>
                <strong style="color:var(--saffron-600);">₹4.85 Cr</strong>
              </div>
              <div class="cre-spec-item">
                <span>LEASE TENURE</span>
                <strong>9 Yrs (6-Yr Lock-in)</strong>
              </div>
            </div>

            <div class="cre-covenant-tag">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"></polyline></svg>
              <span>15% Escalation Every 3 Years &bull; Security Deposit ₹21.3 L</span>
            </div>

            <button type="button" class="btn btn-secondary btn-full btn-sm" onclick="openCreDossierModal('hdfc')">
              <span>View Investment Memorandum (IM) &rarr;</span>
            </button>
          </div>
        </div>

        <!-- Asset 2: Tech Park IT Office -->
        <div class="cre-card">
          <div class="cre-card-header">
            <div>
              <span class="cre-tenant-pill" style="color:var(--blue-sky); border-color:var(--blue-sky); background:var(--blue-light);">FORTUNE 500 US TECH</span>
              <h3 class="cre-asset-title">Grade-A IT Park Office</h3>
              <div class="cre-location">
                <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path></svg>
                <span>Outer Ring Road (ORR), Bellandur, Bengaluru</span>
              </div>
            </div>
          </div>

          <div class="cre-card-body">
            <div class="cre-metrics-strip">
              <div class="cre-spec-item">
                <span>GROSS YIELD</span>
                <strong style="color:var(--emerald-600);">9.4% p.a.</strong>
              </div>
              <div class="cre-spec-item">
                <span>MONTHLY RENT</span>
                <strong>₹9,80,000</strong>
              </div>
              <div class="cre-spec-item">
                <span>TOTAL ASSET COST</span>
                <strong style="color:var(--saffron-600);">₹12.50 Cr</strong>
              </div>
              <div class="cre-spec-item">
                <span>LEASE TENURE</span>
                <strong>5 Yrs (3-Yr Lock-in)</strong>
              </div>
            </div>

            <div class="cre-covenant-tag">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"></polyline></svg>
              <span>10,500 sq.ft Furnished &bull; 6-Month Security Deposit Held</span>
            </div>

            <button type="button" class="btn btn-secondary btn-full btn-sm" onclick="openCreDossierModal('techpark')">
              <span>View Investment Memorandum (IM) &rarr;</span>
            </button>
          </div>
        </div>

        <!-- Asset 3: Logistics Warehouse -->
        <div class="cre-card">
          <div class="cre-card-header">
            <div>
              <span class="cre-tenant-pill" style="color:#7C3AED; border-color:#7C3AED; background:rgba(124,58,237,0.08);">E-COMMERCE MULTINATIONAL</span>
              <h3 class="cre-asset-title">Amazon Fulfillment Hub</h3>
              <div class="cre-location">
                <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path></svg>
                <span>Hoskote Industrial Logistics Corridor, Bengaluru</span>
              </div>
            </div>
          </div>

          <div class="cre-card-body">
            <div class="cre-metrics-strip">
              <div class="cre-spec-item">
                <span>GROSS YIELD</span>
                <strong style="color:var(--emerald-600);">10.2% p.a.</strong>
              </div>
              <div class="cre-spec-item">
                <span>MONTHLY RENT</span>
                <strong>₹15,30,000</strong>
              </div>
              <div class="cre-spec-item">
                <span>TOTAL ASSET COST</span>
                <strong style="color:var(--saffron-600);">₹18.00 Cr</strong>
              </div>
              <div class="cre-spec-item">
                <span>LEASE TENURE</span>
                <strong>10 Yrs (Triple Net NNN)</strong>
              </div>
            </div>

            <div class="cre-covenant-tag">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"></polyline></svg>
              <span>Zero Landlord Maintenance &bull; PE Institutional Structure</span>
            </div>

            <button type="button" class="btn btn-secondary btn-full btn-sm" onclick="openCreDossierModal('warehouse')">
              <span>View Investment Memorandum (IM) &rarr;</span>
            </button>
          </div>
        </div>
      </div>

      <!-- CRE Interactive Yield & IRR Modeling Simulator -->
      <div class="cre-simulator-card">
        <div>
          <h3 style="font-size:1.3rem; font-weight:800; color:var(--navy-authority); margin-bottom:0.4rem;">Institutional CRE Cash-Flow & Cap Rate Modeler</h3>
          <p style="font-size:0.88rem; color:var(--text-muted); margin-bottom:1.5rem;">
            Model gross rental yield, statutory 30% standard deduction under Section 24, and 10-year Internal Rate of Return (IRR).
          </p>

          <div class="sim-slider-box">
            <div class="sim-slider-hdr">
              <span>Capital Investment Deployment:</span>
              <strong id="simCapDisp">₹5.00 Cr</strong>
            </div>
            <input type="range" id="simCapInput" min="10000000" max="250000000" step="2500000" value="50000000" class="custom-range">
          </div>

          <div class="sim-slider-box">
            <div class="sim-slider-hdr">
              <span>Gross Rental Yield (% p.a.):</span>
              <strong id="simYieldDisp">8.8%</strong>
            </div>
            <input type="range" id="simYieldInput" min="6.0" max="12.0" step="0.2" value="8.8" class="custom-range">
          </div>

          <div class="sim-slider-box">
            <div class="sim-slider-hdr">
              <span>Contractual Rent Escalation:</span>
              <strong id="simEscDisp">15% Every 3 Years</strong>
            </div>
            <select id="simEscSelect" class="form-control-terminal">
              <option value="15" selected>15% Every 3 Years (Standard Indian CRE)</option>
              <option value="5">5% Compounded Annually</option>
              <option value="10">10% Every 3 Years</option>
            </select>
          </div>
        </div>

        <div class="sim-outputs-panel">
          <div class="sim-result-hero">
            <span>ANNUAL NET OPERATING INCOME (NOI)</span>
            <strong id="simNoiDisp">₹44,00,000</strong>
            <div style="font-size:0.82rem; color:var(--blue-sky); margin-top:0.25rem; font-weight:700;" id="simMonthlyNoiDisp">Monthly Cash Inflow: ₹3,66,667 / mo</div>
          </div>

          <div class="sim-grid-stats">
            <div class="sim-stat-box">
              <span>Section 24 Tax Shield</span>
              <strong style="color:var(--emerald-600);" id="simTaxShieldDisp">₹13,20,000 (30%)</strong>
            </div>
            <div class="sim-stat-box">
              <span>Taxable Rental Income</span>
              <strong id="simTaxableDisp">₹30,80,000</strong>
            </div>
            <div class="sim-stat-box">
              <span>10-Yr Projected IRR</span>
              <strong style="color:var(--saffron-700);" id="simIrrDisp">15.8% Pre-Tax</strong>
            </div>
            <div class="sim-stat-box">
              <span>Year 10 Asset Valuation</span>
              <strong id="simAssetExitDisp">₹8.95 Cr</strong>
            </div>
          </div>

          <button type="button" class="btn btn-primary btn-full" style="margin-top:1.25rem;" onclick="showToast('✓ Institutional CRE Financial Model exported to your clipboard & PDF!')">
            <span>Export Pro-Forma Financial Model (Excel / PDF)</span>
          </button>
        </div>
      </div>
    </div>
  </section>

  <!-- ====================================================================
       PILLAR 3: Smart Construction Cost BoQ Engine & Contractor Escrow
       ==================================================================== -->
  <section class="boq-section" id="build-boq">
    <div class="container">
      <div class="section-header-block">
        <span class="section-tag">CPWD DSR 2026 & NBC COMPLIANT</span>
        <h2 class="section-title">Smart Construction BoQ Engine & Contractor Escrow</h2>
        <p class="section-desc">
          Stop contractor overcharging and project abandonment. Calculate exact metric tonnes of steel, cement bags, and labor costs with a legally binding milestone-based escrow contract.
        </p>
      </div>

      <div class="boq-workbench">
        <!-- Input Row -->
        <div class="boq-inputs-row">
          <div class="form-field-radar">
            <label for="boqArea">Total Built-Up Area (sq.ft)</label>
            <input type="number" id="boqArea" class="form-control-terminal" value="2500" min="500" max="50000" step="100">
          </div>

          <div class="form-field-radar">
            <label for="boqStructure">Structure Type</label>
            <select id="boqStructure" class="form-control-terminal">
              <option value="G+1 Duplex" selected>G+1 Independent Duplex</option>
              <option value="G+2 Triplex">G+2 Triplex Home</option>
              <option value="G+3 Multi-Unit">G+3 Multi-Unit Building</option>
              <option value="Luxury Villa">Luxury Sprawling Villa</option>
            </select>
          </div>

          <div class="form-field-radar">
            <label for="boqTier">Finishing & Spec Tier</label>
            <select id="boqTier" class="form-control-terminal">
              <option value="Basic">Basic (₹1,650/sq.ft)</option>
              <option value="Standard" selected>Standard (₹1,950/sq.ft)</option>
              <option value="Premium">Premium (₹2,450/sq.ft)</option>
              <option value="Ultra-Luxury">Ultra-Luxury (₹3,200/sq.ft)</option>
            </select>
          </div>

          <div class="form-field-radar">
            <label for="boqCityIndex">City Material Index</label>
            <select id="boqCityIndex" class="form-control-terminal">
              <option value="Bengaluru" selected>Bengaluru (Base 1.0)</option>
              <option value="Mumbai">Mumbai (+18% Material)</option>
              <option value="Delhi-NCR">Delhi-NCR (+8% Transport)</option>
              <option value="Hyderabad">Hyderabad (-4% Labor)</option>
            </select>
          </div>
        </div>

        <!-- Live Dynamic BoQ Table -->
        <div class="boq-table-wrap">
          <table class="boq-table">
            <thead>
              <tr>
                <th>MATERIAL / TRADE SPECIFICATION</th>
                <th>GRADE & BRAND STANDARD</th>
                <th>ESTIMATED QUANTITY</th>
                <th>CPWD DSR 2026 RATE</th>
                <th>ESTIMATED AMOUNT (₹)</th>
              </tr>
            </thead>
            <tbody id="boqTableBody">
              <!-- Dynamically populated by JS -->
            </tbody>
          </table>
        </div>

        <!-- BoQ Total Card -->
        <div class="boq-total-card">
          <div class="boq-total-col">
            <span>TOTAL ESTIMATED TURNKEY CONSTRUCTION COST</span>
            <strong id="boqTotalCost">₹48,75,000</strong>
          </div>
          <div class="boq-total-col">
            <span>ESTIMATED RATE PER SQ.FT</span>
            <strong style="color:#FFFFFF; font-size:1.4rem;" id="boqRatePerSqft">₹1,950 / sq.ft</strong>
          </div>
          <div>
            <button type="button" class="btn btn-primary" onclick="openContractorEscrowModal()">
              <span>Generate Contractor Milestone Escrow Deed &rarr;</span>
            </button>
          </div>
        </div>

        <!-- 5-Phase Milestone Escrow Visualizer -->
        <div class="escrow-flow-card">
          <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:0.5rem;">
            <h4 style="font-size:1.1rem; font-weight:800; color:var(--navy-authority);">Standard Contractor Milestone Escrow Schedule</h4>
            <span style="font-size:0.75rem; color:var(--emerald-600); font-weight:700; font-family:var(--font-mono);">
              🛡️ FUNDS HELD IN PROTECTED ESCROW UNTIL ARCHITECT VERIFICATION
            </span>
          </div>

          <div class="escrow-steps-grid">
            <div class="escrow-step-item">
              <div class="step-pct">15%</div>
              <div class="step-phase">Foundation & Plinth</div>
              <div class="step-trigger">Soil excavation, PCC, footings and plinth beam casting completed.</div>
            </div>
            <div class="escrow-step-item">
              <div class="step-pct">30%</div>
              <div class="step-phase">RCC Superstructure</div>
              <div class="step-trigger">Ground and upper floor columns, beams and slab de-shuttering done.</div>
            </div>
            <div class="escrow-step-item">
              <div class="step-pct">20%</div>
              <div class="step-phase">Brickwork & Conduits</div>
              <div class="step-trigger">External block walls, internal partitions and electrical pipings.</div>
            </div>
            <div class="escrow-step-item">
              <div class="step-pct">20%</div>
              <div class="step-phase">Plastering & Flooring</div>
              <div class="step-trigger">Internal/external plaster, vitrified tiles, sanitary fixtures.</div>
            </div>
            <div class="escrow-step-item">
              <div class="step-pct">15%</div>
              <div class="step-phase">Snagging & Handover</div>
              <div class="step-trigger">Doors, windows, final 2 coats Asian Paints, deep cleaning & keys.</div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- ====================================================================
       PILLAR 4: VAHAN & Fleet Asset Compliance Terminal
       ==================================================================== -->
  <section class="vahan-section" id="vahan-fleet">
    <div class="container">
      <div class="section-header-block">
        <span class="section-tag">PARIVAHAN & MORTH INTEROPERABLE</span>
        <h2 class="section-title">VAHAN 4.0 & Fleet Asset Compliance Terminal</h2>
        <p class="section-desc">
          Instant multi-state vehicle RC verification, bank loan hypothecation NOC audit, blacklisted vehicle radar, and real-time pending traffic e-challan ledger.
        </p>
      </div>

      <div class="vahan-terminal-card">
        <!-- Plate Lookup Input -->
        <div class="vahan-lookup-bar">
          <div class="plate-input-wrap">
            <span class="ind-badge">IND</span>
            <input type="text" id="vahanPlateInput" class="plate-input" value="KA-01-MJ-4920" placeholder="e.g. KA-01-MJ-4920" maxlength="13">
          </div>
          <button type="button" class="btn btn-primary" id="btnRunVahanAudit" style="white-space:nowrap;">
            <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
            <span>Scan Vahan RC & Challans</span>
          </button>
        </div>

        <div style="text-align:center; margin-bottom:1.5rem;">
          <span style="font-size:0.75rem; color:var(--text-muted); font-family:var(--font-mono); font-weight:700; margin-right:0.5rem;">Quick Demos:</span>
          <button type="button" class="sample-query-chip" onclick="loadVahanSample('clean')">
            ✓ KA-01-MJ-4920 (Clear Title, NOC Ready, 0 Challans)
          </button>
          <button type="button" class="sample-query-chip" onclick="loadVahanSample('hypo')">
            ⚠ MH-02-CP-9901 (Active Bank Hypothecation & 2 Pending Challans)
          </button>
        </div>

        <!-- Vahan Results Display -->
        <div class="vahan-results-box" id="vahanResultsContainer">
          <div class="vahan-vehicle-header">
            <div>
              <span style="font-size:0.75rem; font-family:var(--font-mono); color:var(--saffron-700); font-weight:800;">REGISTRATION RECORD (VAHAN 4.0)</span>
              <h3 style="font-size:1.4rem; font-weight:800; color:var(--navy-authority); margin:0.2rem 0;" id="vahanModelName">TOYOTA INNOVA CRYSTA 2.4 VX (7-STR)</h3>
              <div style="font-size:0.82rem; color:var(--text-muted);">Registered at RTO: <strong>KA-01 (Koramangala, Bengaluru)</strong></div>
            </div>
            <div style="text-align:right;">
              <span class="status-badge pass" id="vahanNocBadge">✓ Hypothecation Clear (No Bank Lien)</span>
              <div style="font-size:0.75rem; color:var(--text-muted); margin-top:0.35rem;" id="vahanRegDate">Reg Date: 14-Nov-2022</div>
            </div>
          </div>

          <!-- Specs Grid -->
          <div class="vahan-grid-details">
            <div class="vahan-cell">
              <span>VEHICLE CLASS</span>
              <strong id="vahanClass">Motor Cab / Commercial</strong>
            </div>
            <div class="vahan-cell">
              <span>FUEL & EMISSION</span>
              <strong id="vahanFuel">Diesel &bull; BS-VI OBD-II</strong>
            </div>
            <div class="vahan-cell">
              <span>FITNESS VALIDITY</span>
              <strong style="color:var(--emerald-600);" id="vahanFitness">Valid upto 13-Nov-2027</strong>
            </div>
            <div class="vahan-cell">
              <span>INSURANCE & PUCC</span>
              <strong style="color:var(--emerald-600);" id="vahanInsurance">Active (ICICI Lombard)</strong>
            </div>
          </div>

          <!-- Challans Sub-Table -->
          <div style="background:#FFFFFF; border:1px solid var(--border-card); border-radius:var(--radius-sm); padding:1rem;">
            <div style="display:flex; justify-content:space-between; align-items:center;">
              <h4 style="font-size:0.95rem; font-weight:800; color:var(--navy-authority); margin:0;" id="vahanChallanTitle">Pending Traffic e-Challan Radar (0 Violations)</h4>
              <span class="status-badge pass" id="vahanChallanBadge">✓ All Dues Cleared</span>
            </div>

            <div id="vahanChallanTableWrap" style="margin-top:0.75rem;">
              <p style="font-size:0.85rem; color:var(--text-muted); margin:0;">Zero outstanding traffic enforcement penalties recorded across State Traffic Police & Parivahan servers.</p>
            </div>
          </div>

          <div style="display:flex; justify-content:space-between; align-items:center; margin-top:1.5rem; flex-wrap:wrap; gap:0.75rem;">
            <div style="font-size:0.8rem; color:var(--text-muted);">
              <span>Cryptographic Hash: </span>
              <code style="color:var(--saffron-700); font-family:var(--font-mono); font-weight:700;">SHA256: 7f8b91a2e34c90d8e271...</code>
            </div>
            <button type="button" class="btn btn-secondary btn-sm" onclick="openVahanReportModal()">
              <span>Download Pre-Purchase VAHAN Title NOC (PDF) &rarr;</span>
            </button>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- ====================================================================
       STATUTORY PRICING & PLANS
       ==================================================================== -->
  <section class="pricing-terminal-section" id="pricing-plans">
    <div class="container">
      <div class="section-header-block">
        <span class="section-tag">TRANSPARENT REGULATORY FEES</span>
        <h2 class="section-title">Institutional Pricing & Intelligence Tiers</h2>
        <p class="section-desc">
          Statutory audits, high-yield commercial property intelligence, and CPWD construction tools. Zero recurring lock-ins.
        </p>
      </div>

      <div class="pricing-cards-grid">
        <!-- Tier 1: Property Radar -->
        <div class="pricing-card-terminal featured">
          <div class="featured-pill">MOST VALUABLE</div>
          <h3 class="p-tier-name">Property Legal Audit</h3>
          <p class="p-tier-desc">Complete 30-year title diligence, A/B-Khata & lake buffer check before token payment.</p>
          <div class="p-price-block">
            <span class="amt">₹2,499</span>
            <span class="dur">/ per property audit</span>
          </div>
          <ul class="p-features-list">
            <li><svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"></polyline></svg> 30-Year Encumbrance Audit (EC 1996-2026)</li>
            <li><svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"></polyline></svg> BDA/BBMP 50m Lake & Drain Buffer Check</li>
            <li><svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"></polyline></svg> A-Khata vs B-Khata Authenticity Verification</li>
            <li><svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"></polyline></svg> RERA Litigation & Builder NCLT Default Check</li>
            <li><svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"></polyline></svg> <strong>Official Section 65B Certified Legal Dossier</strong></li>
          </ul>
          <button type="button" class="btn btn-primary btn-full" onclick="showToast('✓ Selected Property Legal Audit. Running real-time title checks...')">
            <span>Order Property Audit (₹2,499)</span>
          </button>
        </div>

        <!-- Tier 2: CRE Terminal -->
        <div class="pricing-card-terminal">
          <h3 class="p-tier-name">CRE Yield Terminal</h3>
          <p class="p-tier-desc">For HNIs and NRIs investing in 8.5% - 10.5% pre-leased institutional commercial assets.</p>
          <div class="p-price-block">
            <span class="amt">₹9,999</span>
            <span class="dur">/ annual membership</span>
          </div>
          <ul class="p-features-list">
            <li><svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"></polyline></svg> Verified Pre-Leased Commercial Opportunities</li>
            <li><svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"></polyline></svg> Triple Net (NNN) Bank & Tech Park Leases</li>
            <li><svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"></polyline></svg> Cap Rate, NOI & 10-Yr Post-Tax IRR Models</li>
            <li><svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"></polyline></svg> Section 24 Statutory 30% Tax Shield Optimization</li>
            <li><svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"></polyline></svg> Direct Seller Introduction with Zero Brokerage</li>
          </ul>
          <button type="button" class="btn btn-secondary btn-full" onclick="showToast('✓ Activated Institutional CRE Yield Terminal Membership!')">
            <span>Join CRE Terminal (₹9,999/yr)</span>
          </button>
        </div>

        <!-- Tier 3: Construction BoQ -->
        <div class="pricing-card-terminal">
          <h3 class="p-tier-name">BoQ & Contractor Escrow</h3>
          <p class="p-tier-desc">For home builders and developers preventing contractor fraud & cost escalations.</p>
          <div class="p-price-block">
            <span class="amt">₹1,999</span>
            <span class="dur">/ per construction project</span>
          </div>
          <ul class="p-features-list">
            <li><svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"></polyline></svg> Itemized CPWD DSR 2026 Bill of Quantities</li>
            <li><svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"></polyline></svg> Exact Steel (Tonnes) & Cement (Bags) Calculator</li>
            <li><svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"></polyline></svg> 5-Phase Milestone Escrow Payment Schedule</li>
            <li><svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"></polyline></svg> <strong>Court-Binding Contractor Escrow Agreement</strong></li>
            <li><svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"></polyline></svg> Anti-Snagging 15% Retention Matrix</li>
          </ul>
          <button type="button" class="btn btn-secondary btn-full" onclick="openContractorEscrowModal()">
            <span>Generate Escrow Agreement (₹1,999)</span>
          </button>
        </div>

        <!-- Tier 4: VAHAN Fleet -->
        <div class="pricing-card-terminal">
          <h3 class="p-tier-name">VAHAN Fleet Compliance</h3>
          <p class="p-tier-desc">For used car buyers, transport businesses & fleet operators.</p>
          <div class="p-price-block">
            <span class="amt">₹499</span>
            <span class="dur">/ per vehicle check</span>
          </div>
          <ul class="p-features-list">
            <li><svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"></polyline></svg> Real-Time VAHAN 4.0 RC Status Audit</li>
            <li><svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"></polyline></svg> Bank Hypothecation (Loan NOC) Verification</li>
            <li><svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"></polyline></svg> All-India Multi-State Traffic e-Challan Radar</li>
            <li><svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"></polyline></svg> RTO Blacklist & NCRB Theft Screening</li>
            <li><svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"></polyline></svg> Fleet Bulk API Option at ₹4,999/yr</li>
          </ul>
          <button type="button" class="btn btn-secondary btn-full" onclick="showToast('✓ Single VAHAN Vehicle Audit generated!')">
            <span>Verify Vehicle (₹499)</span>
          </button>
        </div>
      </div>
    </div>
  </section>

  <!-- ====================================================================
       INDIAN STATUTORY & REGULATORY FRAMEWORK
       ==================================================================== -->
  <section class="compliance-section" id="regulatory-framework">
    <div class="container">
      <div class="section-header-block">
        <span class="section-tag">LEGAL ENFORCEABILITY IN INDIAN COURTS</span>
        <h2 class="section-title">Strict Adherence to Indian Statutory Laws</h2>
        <p class="section-desc">
          Every audit, contract, and calculation on ExaInfra conforms to verified central and state legislation, supreme court guidelines, and ministry protocols.
        </p>
      </div>

      <div class="compliance-grid">
        <div class="comp-card">
          <span class="comp-act-badge">SECTION 65B &bull; INDIAN EVIDENCE ACT, 1872</span>
          <h3 class="comp-title">Electronic Record Court Admissibility</h3>
          <p class="comp-desc">
            All ExaInfra title audits, encumbrance extractions, and verification reports include automated Section 65B cryptographic hash certificates, admissible as direct evidence in Indian district and High Courts.
          </p>
        </div>

        <div class="comp-card">
          <span class="comp-act-badge">RERA ACT 2016 &bull; SECTIONS 3, 11, 14</span>
          <h3 class="comp-title">Real Estate Regulatory Oversight</h3>
          <p class="comp-desc">
            Audits cross-reference state RERA portals to detect unapproved floor additions, altered master layouts, sanctioned plan deviations, and promoter escrow account defaults.
          </p>
        </div>

        <div class="comp-card">
          <span class="comp-act-badge">DPDP ACT 2023 &bull; DATA PROTECTION</span>
          <h3 class="comp-title">Digital Personal Data Protection</h3>
          <p class="comp-desc">
            Sovereign compliance with India's DPDP Act 2023. All vehicular and land record queries use consent-driven zero-knowledge tokens with 256-bit TLS bank-grade encryption.
          </p>
        </div>

        <div class="comp-card">
          <span class="comp-act-badge">NGT ORDER OA NO. 222/2014 &bull; BUFFER ZONES</span>
          <h3 class="comp-title">National Green Tribunal Mandate</h3>
          <p class="comp-desc">
            Enforces strict 75m lake boundary and 50m Rajakaluve (primary stormwater drain) buffer zone rules, safeguarding buyers from BBMP/BDA encroachment demolition notices.
          </p>
        </div>

        <div class="comp-card">
          <span class="comp-act-badge">MOTOR VEHICLES ACT 1988 &bull; VAHAN 4.0</span>
          <h3 class="comp-title">MoRTH Vehicle Interoperability</h3>
          <p class="comp-desc">
            Standardized data architecture compliant with Central Motor Vehicles Rules 1989 (CMVR), Section 51 (Hypothecation endorsement) and Parivahan e-Challan protocol.
          </p>
        </div>

        <div class="comp-card">
          <span class="comp-act-badge">CPWD DSR 2026 &bull; NBC 2016</span>
          <h3 class="comp-title">National Building Code Standards</h3>
          <p class="comp-desc">
            Construction material specifications, concrete mix designs, and Bill of Quantities (BoQ) are derived directly from Central Public Works Department (CPWD) schedule of rates.
          </p>
        </div>
      </div>
    </div>
  </section>

  <!-- Footer -->
  <footer class="footer-terminal">
    <div class="container">
      <div class="footer-top">
        <div class="footer-col">
          <div class="brand-title" style="margin-bottom:0.75rem; color:#FFFFFF;">EXA<span style="color:var(--saffron-500);">INFRA</span></div>
          <p style="font-size:0.85rem; color:#94A3B8; line-height:1.6; margin-bottom:1rem;">
            India's sovereign intelligence terminal for real estate due diligence, commercial yield assets, construction BoQ estimation, and vehicular asset compliance.
          </p>
          <div style="font-size:0.75rem; color:#64748B; font-family:var(--font-mono);">
            DATA JURISDICTION: REPUBLIC OF INDIA &bull; MEITY STANDARDS
          </div>
        </div>

        <div class="footer-col">
          <h4>Due Diligence</h4>
          <ul>
            <li><a href="#legal-radar">30-Year EC Audit</a></li>
            <li><a href="#legal-radar">A-Khata vs B-Khata</a></li>
            <li><a href="#legal-radar">Rajakaluve Lake Buffer</a></li>
            <li><a href="#legal-radar">RERA Project Checks</a></li>
            <li><a href="#legal-radar">Sec 65B Certificates</a></li>
          </ul>
        </div>

        <div class="footer-col">
          <h4>CRE & Asset Tools</h4>
          <ul>
            <li><a href="#cre-terminal">Pre-Leased Bank Branches</a></li>
            <li><a href="#cre-terminal">Grade-A IT Park Offices</a></li>
            <li><a href="#cre-terminal">Cap Rate & IRR Modeler</a></li>
            <li><a href="#build-boq">CPWD Construction BoQ</a></li>
            <li><a href="#vahan-fleet">VAHAN 4.0 RC & Challans</a></li>
          </ul>
        </div>

        <div class="footer-col">
          <h4>Compliance & Legal</h4>
          <p style="font-size:0.82rem; color:#94A3B8; margin-bottom:1rem;">
            ExaInfra operates strictly under Section 65B of the Indian Evidence Act, 1872 and the Information Technology Act, 2000.
          </p>
          <div style="font-size:0.78rem; color:var(--saffron-500); font-family:var(--font-mono);">
            CERTIFIED SOVEREIGN CLOUD ARCHITECTURE
          </div>
        </div>
      </div>

      <div class="footer-bottom">
        <div>
          &copy; 2026 ExaInfra.in. All Rights Reserved. Engineered for Indian Statutory & Regulatory Standards.
        </div>
        <div style="display:flex; gap:1.5rem;">
          <a href="#regulatory-framework" style="color:#94A3B8; text-decoration:none;">Statutory Acts</a>
          <a href="#pricing-plans" style="color:#94A3B8; text-decoration:none;">Pricing Policy</a>
          <a href="#" style="color:#94A3B8; text-decoration:none;">Privacy (DPDP Act)</a>
        </div>
      </div>
    </div>
  </footer>

  <!-- ====================================================================
       INTERACTIVE MODALS
       ==================================================================== -->

  <!-- MODAL 1: Section 65B Property Legal Title Audit Certificate -->
  <div class="modal-backdrop" id="modalTitleCert">
    <div class="modal-box modal-lg">
      <button class="modal-close-btn" onclick="closeModal(document.getElementById('modalTitleCert'))">&times;</button>
      <div class="cert-paper" id="titleCertPaper">
        <!-- Injected dynamically -->
      </div>
      <div style="display:flex; justify-content:flex-end; gap:0.75rem; margin-top:1.25rem; flex-wrap:wrap;">
        <button type="button" class="btn btn-secondary btn-sm" onclick="window.print()">
          <span>Print / Save as PDF</span>
        </button>
        <button type="button" class="btn btn-primary btn-sm" onclick="showToast('✓ Section 65B Digital Certificate downloaded!'); closeModal(document.getElementById('modalTitleCert'));">
          <span>Download Signed Dossier</span>
        </button>
      </div>
    </div>
  </div>

  <!-- MODAL 2: CRE Investment Memorandum (IM) Dossier -->
  <div class="modal-backdrop" id="modalCreDossier">
    <div class="modal-box modal-lg">
      <button class="modal-close-btn" onclick="closeModal(document.getElementById('modalCreDossier'))">&times;</button>
      <div id="creDossierContent">
        <!-- Injected dynamically -->
      </div>
    </div>
  </div>

  <!-- MODAL 3: CPWD Contractor Milestone Escrow Agreement -->
  <div class="modal-backdrop" id="modalContractorEscrow">
    <div class="modal-box modal-lg">
      <button class="modal-close-btn" onclick="closeModal(document.getElementById('modalContractorEscrow'))">&times;</button>
      <div id="contractorEscrowContent">
        <!-- Injected dynamically -->
      </div>
    </div>
  </div>

  <!-- MODAL 4: VAHAN 4.0 Vehicle Title & NOC Certificate -->
  <div class="modal-backdrop" id="modalVahanReport">
    <div class="modal-box modal-lg">
      <button class="modal-close-btn" onclick="closeModal(document.getElementById('modalVahanReport'))">&times;</button>
      <div id="vahanReportContent">
        <!-- Injected dynamically -->
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

print(f"Generated clean white & mobile index.html ({len(html_content)} bytes) successfully.")
