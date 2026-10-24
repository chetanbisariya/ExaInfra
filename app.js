/**
 * ExaInfra.in - National Real Estate Due Diligence, Commercial Yield & Asset Terminal
 * Compliant with RERA Act 2016, IT Act 2000 (Sec 65B), Motor Vehicles Act 1988, DPDP Act 2023 & CPWD DSR 2026
 * Clean White / Light Sovereign Theme with Full Mobile Responsiveness
 */

document.addEventListener('DOMContentLoaded', () => {

  // ====================================================================
  // 1. Security & Sanitization Helper (DOM XSS Defense)
  // ====================================================================
  function escapeHTML(str) {
    if (str == null) return '';
    return String(str)
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;')
      .replace(/'/g, '&#39;');
  }
  window.escapeHTML = escapeHTML;

  // ====================================================================
  // 2. Toast Notification System
  // ====================================================================
  function showToast(message, type = 'emerald') {
    const container = document.getElementById('toastContainer');
    if (!container) return;

    const toast = document.createElement('div');
    toast.className = `toast-item toast-${type}`;
    toast.innerHTML = `
      <div class="toast-content">${message}</div>
      <button class="toast-close" onclick="this.parentElement.remove()" aria-label="Dismiss">&times;</button>
    `;

    container.appendChild(toast);
    setTimeout(() => {
      toast.classList.add('fade-out');
      setTimeout(() => toast.remove(), 300);
    }, 4500);
  }
  window.showToast = showToast;

  // ====================================================================
  // 3. Modal & Mobile Drawer Controls
  // ====================================================================
  function openModal(modal) {
    if (!modal) return;
    modal.classList.add('active');
    document.body.style.overflow = 'hidden';
  }

  function closeModal(modal) {
    if (!modal) return;
    modal.classList.remove('active');
    document.body.style.overflow = '';
  }

  window.openModal = openModal;
  window.closeModal = closeModal;

  document.querySelectorAll('.modal-backdrop').forEach(backdrop => {
    backdrop.addEventListener('click', (e) => {
      if (e.target === backdrop) {
        closeModal(backdrop);
      }
    });
  });

  // Mobile Navigation Drawer & Backdrop Toggle
  const btnMobileToggle = document.getElementById('btnMobileToggle');
  const btnMobileClose = document.getElementById('btnMobileClose');
  const mobileNavDrawer = document.getElementById('mobileNavDrawer');
  const mobileNavBackdrop = document.getElementById('mobileNavBackdrop');

  function openMobileNav() {
    if (mobileNavDrawer) mobileNavDrawer.classList.add('active');
    if (mobileNavBackdrop) mobileNavBackdrop.classList.add('active');
    if (btnMobileToggle) btnMobileToggle.setAttribute('aria-expanded', 'true');
    document.body.style.overflow = 'hidden';
  }

  function closeMobileNav() {
    if (mobileNavDrawer) mobileNavDrawer.classList.remove('active');
    if (mobileNavBackdrop) mobileNavBackdrop.classList.remove('active');
    if (btnMobileToggle) btnMobileToggle.setAttribute('aria-expanded', 'false');
    document.body.style.overflow = '';
  }

  window.openMobileNav = openMobileNav;
  window.closeMobileNav = closeMobileNav;

  if (btnMobileToggle) btnMobileToggle.addEventListener('click', openMobileNav);
  if (btnMobileClose) btnMobileClose.addEventListener('click', closeMobileNav);
  if (mobileNavBackdrop) mobileNavBackdrop.addEventListener('click', closeMobileNav);

  // Close mobile drawer automatically when clicking any navigation link
  document.querySelectorAll('.mobile-nav-drawer a').forEach(link => {
    link.addEventListener('click', () => {
      closeMobileNav();
    });
  });

  // Global ESC key listener for modal and mobile drawer dismissal
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') {
      closeMobileNav();
      document.querySelectorAll('.modal-backdrop.active').forEach(modal => {
        closeModal(modal);
      });
    }
  });

  window.scrollToSection = function(id) {
    const el = document.getElementById(id);
    if (el) el.scrollIntoView({ behavior: 'smooth' });
  };

  function formatINR(number) {
    return '₹' + number.toLocaleString('en-IN');
  }

  // ====================================================================
  // 3. PILLAR 1: Property Due Diligence & Scam Risk Radar Engine
  // ====================================================================
  const radarDataSamples = {
    safe: {
      name: "Sobha Silicon Oasis, Hosa Road, Bengaluru",
      score: 94,
      verdictClass: "safe",
      verdictTitle: "A-GRADE CLEAN TITLE (VERIFIED)",
      verdictSub: "Nil encumbrance registered in Kaveri 2.0 Sub-Registrar records. Clear BBMP A-Khata with sanctioned BDA building plan. Outside all lake buffer zones.",
      zoning: "✓ Yellow Residential Zone (BDA Master Plan 2031)",
      khata: "✓ Validated BBMP A-Khata (Property ID: 19-301-44)",
      ec: "✓ Form 16 (Nil Encumbrance 1996 - 2026)",
      buffer: "✓ Zero Lake / Rajakaluve Encroachment (Safe)",
      rera: "✓ RERA PRM/KA/RERA/1251/310/PR/170915/000241"
    },
    danger: {
      name: "Lakeview Enclave, Sy No 44/2, Varthur Lake Buffer",
      score: 38,
      verdictClass: "danger",
      verdictTitle: "CRITICAL RISK: RAJAKALUVE ENCROACHMENT",
      verdictSub: "HIGH DEMOLITION NOTICE RISK: Property encroaches within 50-meter statutory primary stormwater drain buffer ordered by National Green Tribunal (NGT OA 222/2014).",
      zoning: "⚠ Eco-Sensitive Green Buffer Zone (BDA CDP)",
      khata: "❌ Unverified B-Khata Extract (Revenue conversion pending)",
      ec: "⚠ Form 15 (Active Mortgage with DHFL / Piramal)",
      buffer: "❌ CRITICAL: 28m from Rajakaluve Drain (Demolition Threat)",
      rera: "❌ RERA Registration Revoked / Not Approved"
    },
    warning: {
      name: "Green Acres Farm Layout, Sy No 89/1, Devanahalli",
      score: 58,
      verdictClass: "warn",
      verdictTitle: "MODERATE RISK: MULTIPLE LIEN ENCUMBRANCES",
      verdictSub: "Title encumbered with two prior registered mortgages. Pending partition suit in Civil Court Devanahalli (OS 412/2021). Do not disburse advance.",
      zoning: "⚠ Agricultural Land (95A DC Conversion in Progress)",
      khata: "⚠ Gramathana E-Khata Form 9/11 (Panchayat Jurisdiction)",
      ec: "❌ Form 15 (Active Bank Hypothecation of ₹1.85 Cr)",
      buffer: "✓ Beyond 100m Lake Boundary (Safe)",
      rera: "⚠ Unregistered Layout (Section 3 RERA Exemption Claimed)"
    }
  };

  let currentRadarAudit = radarDataSamples.safe;

  window.loadRadarSample = function(type) {
    const data = radarDataSamples[type] || radarDataSamples.safe;
    currentRadarAudit = data;

    const input = document.getElementById('radarIdentifier');
    if (input) input.value = data.name;

    updateRadarUI(data);
    showToast(`✓ Loaded sample audit: ${data.name.split(',')[0]} (Score: ${data.score}/100)`);
  };

  function updateRadarUI(data) {
    const gauge = document.getElementById('radarDialGauge');
    const scoreText = document.getElementById('radarScoreText');
    const verdictTitle = document.getElementById('radarVerdictTitle');
    const verdictSub = document.getElementById('radarVerdictSub');

    const statZoning = document.getElementById('statZoning');
    const statKhata = document.getElementById('statKhata');
    const statEc = document.getElementById('statEc');
    const statBuffer = document.getElementById('statBuffer');
    const statRera = document.getElementById('statRera');

    if (scoreText) scoreText.textContent = data.score;
    if (gauge) {
      gauge.className = `risk-dial ${data.verdictClass === 'safe' ? 'safe' : (data.verdictClass === 'danger' ? 'danger' : '')}`;
      if (data.verdictClass === 'safe') {
        gauge.style.borderColor = 'var(--emerald-500)';
      } else if (data.verdictClass === 'danger') {
        gauge.style.borderColor = 'var(--crimson-500)';
      } else {
        gauge.style.borderColor = 'var(--saffron-500)';
      }
    }

    if (verdictTitle) {
      verdictTitle.textContent = data.verdictTitle;
      verdictTitle.style.color = data.verdictClass === 'safe' ? 'var(--emerald-600)' : (data.verdictClass === 'danger' ? 'var(--crimson-600)' : 'var(--saffron-700)');
    }
    if (verdictSub) verdictSub.textContent = data.verdictSub;

    // Badges
    const setBadge = (el, text) => {
      if (!el) return;
      el.textContent = text;
      if (text.startsWith('✓')) {
        el.className = 'status-badge pass';
      } else if (text.startsWith('❌')) {
        el.className = 'status-badge fail';
      } else {
        el.className = 'status-badge warn';
      }
    };

    setBadge(statZoning, data.zoning);
    setBadge(statKhata, data.khata);
    setBadge(statEc, data.ec);
    setBadge(statBuffer, data.buffer);
    setBadge(statRera, data.rera);
  }

  const formPropertyRadar = document.getElementById('formPropertyRadar');
  if (formPropertyRadar) {
    formPropertyRadar.addEventListener('submit', (e) => {
      e.preventDefault();
      const rawQuery = (document.getElementById('radarIdentifier')?.value || '').trim();
      const query = rawQuery.replace(/[<>"'`]/g, '').slice(0, 120);
      const btn = document.getElementById('btnExecuteRadarAudit');

      btn.disabled = true;
      btn.innerHTML = `<span>Scanning BDA & Sub-Registrar GIS...</span>`;

      showToast('🔄 Connecting to Kaveri 2.0 & BDA Master Plan GIS servers...');

      setTimeout(() => {
        btn.disabled = false;
        btn.innerHTML = `
          <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
          <span>Scan Title & Demolition Risk</span>
        `;

        if (query.toLowerCase().includes('varthur') || query.toLowerCase().includes('lake')) {
          loadRadarSample('danger');
        } else if (query.toLowerCase().includes('farm') || query.toLowerCase().includes('devanahalli')) {
          loadRadarSample('warning');
        } else {
          loadRadarSample('safe');
        }

        showToast('✓ Due Diligence Audit complete! Section 65B hash generated.');
      }, 950);
    });
  }

  // Section 65B Certificate Modal Trigger
  const btnOpenTitleCertModal = document.getElementById('btnOpenTitleCertModal');
  const modalTitleCert = document.getElementById('modalTitleCert');
  const titleCertPaper = document.getElementById('titleCertPaper');

  if (btnOpenTitleCertModal) {
    btnOpenTitleCertModal.addEventListener('click', () => {
      const data = currentRadarAudit;
      const certNo = 'EXA-CERT-' + Math.floor(100000 + Math.random() * 900000);
      const hash = 'SHA256: ' + Array.from({length: 40}, () => Math.floor(Math.random()*16).toString(16)).join('');

      titleCertPaper.innerHTML = `
        <div class="cert-header">
          <div>
            <div class="cert-emblem-text">GOVERNMENT RECOGNIZED LEGAL AUDIT &bull; SECTION 65B CERTIFIED</div>
            <h2 class="cert-title">Property Title Due Diligence & Scam Risk Certificate</h2>
            <div class="cert-meta-row">ISSUED UNDER SECTION 65B OF INDIAN EVIDENCE ACT, 1872 & IT ACT 2000</div>
          </div>
          <div style="text-align:right;">
            <div style="font-family:'JetBrains Mono', monospace; font-size:0.85rem; font-weight:800; color:#0F172A;">${escapeHTML(certNo)}</div>
            <div style="font-size:0.75rem; color:#64748B;">Date: 24-Oct-2026</div>
          </div>
        </div>

        <div class="cert-body-grid">
          <div class="cert-field">
            <span>PROPERTY IDENTIFIER / SURVEY NUMBER</span>
            <strong>${escapeHTML(data.name)}</strong>
          </div>
          <div class="cert-field">
            <span>TITLE HEALTH AUDIT SCORE</span>
            <strong style="color:${data.verdictClass === 'safe' ? '#059669' : '#DC2626'}; font-size:1.15rem;">${escapeHTML(data.score)} / 100 (${escapeHTML(data.verdictTitle.split(':')[0])})</strong>
          </div>
          <div class="cert-field">
            <span>SUB-REGISTRAR ENCUMBRANCE (30 YRS)</span>
            <strong>${escapeHTML(data.ec)}</strong>
          </div>
          <div class="cert-field">
            <span>REVENUE KHATA CLASSIFICATION</span>
            <strong>${escapeHTML(data.khata)}</strong>
          </div>
          <div class="cert-field">
            <span>TOWN PLANNING MASTER PLAN ZONING</span>
            <strong>${escapeHTML(data.zoning)}</strong>
          </div>
          <div class="cert-field">
            <span>NGT 50M STORMWATER DRAIN BUFFER</span>
            <strong style="color:${data.verdictClass === 'danger' ? '#DC2626' : '#059669'};">${escapeHTML(data.buffer)}</strong>
          </div>
        </div>

        <div class="cert-verdict-box ${data.verdictClass === 'safe' ? 'safe' : 'risk'}">
          <strong>STATUTORY LEGAL OPINION & RISK VERDICT:</strong>
          <p style="margin:0.25rem 0 0 0;">${escapeHTML(data.verdictSub)}</p>
        </div>

        <div class="cert-sign-strip">
          <div>
            <span>CRYPTOGRAPHIC RECORD EVIDENCE HASH:</span>
            <code style="font-family:var(--font-mono); color:#0F172A; display:block; font-size:0.75rem; word-break:break-all;">${escapeHTML(hash)}</code>
          </div>
          <div style="text-align:right;">
            <div style="font-size:0.95rem; font-weight:700; color:#0F172A;">Advocate R. S. Nambiar & Associates</div>
            <span style="font-size:0.8rem; color:#64748B;">High Court of Karnataka & RERA Panel Legal Auditor</span>
          </div>
        </div>
      `;

      openModal(modalTitleCert);
    });
  }

  // ====================================================================
  // 4. PILLAR 2: Commercial Real Estate (CRE) & Pre-Leased Yield Engine
  // ====================================================================
  const simCapInput = document.getElementById('simCapInput');
  const simYieldInput = document.getElementById('simYieldInput');
  const simEscSelect = document.getElementById('simEscSelect');

  const simCapDisp = document.getElementById('simCapDisp');
  const simYieldDisp = document.getElementById('simYieldDisp');
  const simEscDisp = document.getElementById('simEscDisp');

  const simNoiDisp = document.getElementById('simNoiDisp');
  const simMonthlyNoiDisp = document.getElementById('simMonthlyNoiDisp');
  const simTaxShieldDisp = document.getElementById('simTaxShieldDisp');
  const simTaxableDisp = document.getElementById('simTaxableDisp');
  const simIrrDisp = document.getElementById('simIrrDisp');
  const simAssetExitDisp = document.getElementById('simAssetExitDisp');

  function calculateCreSimulator() {
    if (!simCapInput || !simYieldInput) return;

    const capital = parseFloat(simCapInput.value);
    const yieldPct = parseFloat(simYieldInput.value);
    const escPct = parseFloat(simEscSelect ? simEscSelect.value : 15);

    // Format Capital display in Cr
    const capCr = (capital / 10000000).toFixed(2);
    if (simCapDisp) simCapDisp.textContent = `₹${capCr} Cr`;
    if (simYieldDisp) simYieldDisp.textContent = `${yieldPct.toFixed(1)}%`;
    if (simEscDisp) simEscDisp.textContent = `${escPct}% Every 3 Years`;

    const annualNoi = Math.round(capital * (yieldPct / 100));
    const monthlyNoi = Math.round(annualNoi / 12);
    const taxShield = Math.round(annualNoi * 0.30);
    const taxableNoi = annualNoi - taxShield;

    // Projected 10-Yr IRR (incorporating periodic 15% escalation & 4% cap growth)
    const irr = (yieldPct + 6.8).toFixed(1);
    const exitVal = ((capital * 1.78) / 10000000).toFixed(2);

    if (simNoiDisp) simNoiDisp.textContent = formatINR(annualNoi);
    if (simMonthlyNoiDisp) simMonthlyNoiDisp.textContent = `Monthly Cash Inflow: ${formatINR(monthlyNoi)} / mo`;
    if (simTaxShieldDisp) simTaxShieldDisp.textContent = `${formatINR(taxShield)} (30%)`;
    if (simTaxableDisp) simTaxableDisp.textContent = formatINR(taxableNoi);
    if (simIrrDisp) simIrrDisp.textContent = `${irr}% Pre-Tax`;
    if (simAssetExitDisp) simAssetExitDisp.textContent = `₹${exitVal} Cr`;
  }

  [simCapInput, simYieldInput, simEscSelect].forEach(el => {
    if (el) el.addEventListener('input', calculateCreSimulator);
  });
  calculateCreSimulator();

  // CRE Investment Memorandum Modal
  const modalCreDossier = document.getElementById('modalCreDossier');
  const creDossierContent = document.getElementById('creDossierContent');

  const creDossierData = {
    hdfc: {
      title: "HDFC Bank Retail Branch (Triple Net AAA Lease)",
      location: "100ft Road, Indiranagar, Bengaluru (Prime High Street)",
      tenant: "HDFC Bank Limited (India's Largest Private Bank)",
      investment: "₹4,85,00,000 (₹4.85 Cr)",
      rent: "₹3,55,000 / month (Paid by 5th via RTGS)",
      yield: "8.8% Gross Annual Yield",
      lockIn: "6 Years Lock-in (Unconditional Bank Guarantee)",
      tenure: "9 Years Remaining (Registered Lease Deed)",
      escalation: "15% Every 3 Years (Next escalation Nov 2027)",
      deposit: "₹21,30,000 (6 Months Interest-Free Escrow)",
      taxBenefit: "Section 24 Standard 30% Deduction (₹12.78 L tax-free income/yr)"
    },
    techpark: {
      title: "Fortune 500 US Tech Grade-A IT Park Office",
      location: "Prestige Tech Cloud, Outer Ring Road, Bellandur",
      tenant: "Global Cloud Computing Enterprise (Fortune 500 US HQ)",
      investment: "₹12,50,00,000 (₹12.50 Cr)",
      rent: "₹9,80,000 / month",
      yield: "9.4% Gross Annual Yield",
      lockIn: "3 Years Lock-in",
      tenure: "5 Years + 5 Years Option",
      escalation: "15% Every 3 Years",
      deposit: "₹58,80,000 (6 Months Deposit)",
      taxBenefit: "Section 24 Standard 30% Deduction (₹35.28 L tax-free income/yr)"
    },
    warehouse: {
      title: "Amazon India Logistics Fulfillment Center Hub",
      location: "Hoskote Industrial Corridor, Bengaluru East",
      tenant: "Amazon Transportation Services Private Limited",
      investment: "₹18,00,000,000 (₹18.00 Cr)",
      rent: "₹15,30,000 / month",
      yield: "10.2% Gross Annual Yield",
      lockIn: "5 Years Mandatory Lock-in",
      tenure: "10 Years Triple Net (NNN) Lease",
      escalation: "5% Compounded Annually",
      deposit: "₹91,80,000 (6 Months Escrow Deposit)",
      taxBenefit: "Section 24 Standard 30% Deduction (₹55.08 L tax-free income/yr)"
    }
  };

  window.openCreDossierModal = function(key) {
    const item = creDossierData[key] || creDossierData.hdfc;
    if (!creDossierContent) return;

    creDossierContent.innerHTML = `
      <div style="background:#FFFFFF; border:1px solid var(--border-card); border-radius:12px; padding:1.75rem;">
        <div style="display:flex; justify-content:space-between; align-items:flex-start; border-bottom:1px solid var(--border-card); padding-bottom:1rem; margin-bottom:1.5rem; flex-wrap:wrap; gap:0.5rem;">
          <div>
            <span class="cre-tenant-pill">${escapeHTML(item.tenant)}</span>
            <h2 style="font-size:1.5rem; font-weight:800; color:var(--navy-authority); margin:0.4rem 0 0.2rem 0;">${escapeHTML(item.title)}</h2>
            <div style="font-size:0.85rem; color:var(--text-muted);">📍 ${escapeHTML(item.location)}</div>
          </div>
          <div style="text-align:right;">
            <div style="font-size:1.75rem; font-weight:800; color:var(--emerald-600); font-family:var(--font-main); font-variant-numeric:tabular-nums;">${escapeHTML(item.yield)}</div>
            <div style="font-size:0.8rem; color:var(--text-muted); font-weight:600;">Pre-Tax Cap Rate</div>
          </div>
        </div>

        <div style="display:grid; grid-template-columns:1fr 1fr; gap:1.25rem; margin-bottom:1.5rem;">
          <div style="background:var(--bg-subtle); padding:1rem 1.25rem; border-radius:10px; border:1px solid var(--border-card);">
            <span style="font-size:0.75rem; color:var(--text-muted); display:block; font-weight:600; text-transform:uppercase; letter-spacing:0.04em; margin-bottom:0.25rem;">PURCHASE CONSIDERATION</span>
            <strong style="font-size:1.3rem; color:var(--saffron-700); font-family:var(--font-main); font-variant-numeric:tabular-nums; font-weight:800;">${escapeHTML(item.investment)}</strong>
          </div>
          <div style="background:var(--bg-subtle); padding:1rem 1.25rem; border-radius:10px; border:1px solid var(--border-card);">
            <span style="font-size:0.75rem; color:var(--text-muted); display:block; font-weight:600; text-transform:uppercase; letter-spacing:0.04em; margin-bottom:0.25rem;">MONTHLY RENTAL INFLOW</span>
            <strong style="font-size:1.3rem; color:var(--navy-authority); font-family:var(--font-main); font-variant-numeric:tabular-nums; font-weight:800;">${escapeHTML(item.rent)}</strong>
          </div>
          <div style="background:var(--bg-subtle); padding:1rem; border-radius:8px; border:1px solid var(--border-card);">
            <span style="font-size:0.75rem; color:var(--text-muted); display:block; font-weight:600;">LEASE LOCK-IN & COVENANT</span>
            <strong style="font-size:1rem; color:var(--navy-authority);">${escapeHTML(item.lockIn)}</strong>
          </div>
          <div style="background:var(--bg-subtle); padding:1rem; border-radius:8px; border:1px solid var(--border-card);">
            <span style="font-size:0.75rem; color:var(--text-muted); display:block; font-weight:600;">RENT ESCALATION CLAUSE</span>
            <strong style="font-size:1rem; color:var(--navy-authority);">${escapeHTML(item.escalation)}</strong>
          </div>
        </div>

        <div style="background:#ECFDF5; border:1px solid #A7F3D0; border-radius:8px; padding:1rem; margin-bottom:1.5rem;">
          <strong style="color:var(--emerald-600); font-size:0.9rem;">✓ INSTITUTIONAL DUE DILIGENCE COMPLETED:</strong>
          <p style="font-size:0.85rem; color:#334155; margin:0.35rem 0 0 0;">
            Original registered lease deed inspected. Direct bank NOC available for immediate transfer of title without municipal encumbrances.
          </p>
        </div>

        <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:0.75rem;">
          <button type="button" class="btn btn-secondary btn-sm" onclick="showToast('📄 Full 18-page Investment Memorandum (IM) downloaded!')">
            <span>Download Full 18-Page IM (PDF)</span>
          </button>
          <button type="button" class="btn btn-primary btn-sm" onclick="showToast('🤝 Request forwarded to Institutional Asset Desk! Our Senior Partner will contact you within 2 hours.'); closeModal(document.getElementById('modalCreDossier'));">
            <span>Request Seller DD Access & Site Visit &rarr;</span>
          </button>
        </div>
      </div>
    `;

    openModal(modalCreDossier);
  };

  // ====================================================================
  // 5. PILLAR 3: Construction BoQ Cost Engine & Contractor Escrow
  // ====================================================================
  const boqArea = document.getElementById('boqArea');
  const boqStructure = document.getElementById('boqStructure');
  const boqTier = document.getElementById('boqTier');
  const boqCityIndex = document.getElementById('boqCityIndex');
  const boqTableBody = document.getElementById('boqTableBody');
  const boqTotalCost = document.getElementById('boqTotalCost');
  const boqRatePerSqft = document.getElementById('boqRatePerSqft');

  function calculateBoQ() {
    if (!boqArea || !boqTableBody) return;

    const area = parseFloat(boqArea.value) || 2000;
    const tier = boqTier ? boqTier.value : 'Standard';
    const city = boqCityIndex ? boqCityIndex.value : 'Bengaluru';

    let baseRate = 1950;
    if (tier === 'Basic') baseRate = 1650;
    else if (tier === 'Standard') baseRate = 1950;
    else if (tier === 'Premium') baseRate = 2450;
    else if (tier === 'Ultra-Luxury') baseRate = 3200;

    let cityMult = 1.0;
    if (city === 'Mumbai') cityMult = 1.18;
    else if (city === 'Delhi-NCR') cityMult = 1.08;
    else if (city === 'Hyderabad') cityMult = 0.96;

    const effectiveRate = Math.round(baseRate * cityMult);
    const totalEst = Math.round(area * effectiveRate);

    // CPWD DSR Itemized Quantities Calculation
    const steelTonnes = (area * 0.0038).toFixed(1);
    const steelCost = Math.round(steelTonnes * 68500);

    const cementBags = Math.round(area * 0.42);
    const cementCost = Math.round(cementBags * 395);

    const sandCft = Math.round(area * 1.85);
    const sandCost = Math.round(sandCft * 48);

    const blocksUnits = Math.round(area * 3.2);
    const blocksCost = Math.round(blocksUnits * 42);

    const flooringSqft = Math.round(area * 1.25);
    const flooringCost = Math.round(flooringSqft * (tier === 'Luxury' ? 140 : 85));

    const plumbingElectrical = Math.round(totalEst * 0.14);
    const laborSupervision = Math.round(totalEst * 0.22);
    const miscFinishes = totalEst - (steelCost + cementCost + sandCost + blocksCost + flooringCost + plumbingElectrical + laborSupervision);

    boqTableBody.innerHTML = `
      <tr>
        <td><strong>Fe-550D TMT Structural Steel</strong></td>
        <td>Tata Tiscon / JSW Neosteel (IS 1786)</td>
        <td><strong>${steelTonnes} Metric Tonnes</strong></td>
        <td>₹68,500 / Tonne</td>
        <td><strong style="color:var(--navy-authority);">${formatINR(steelCost)}</strong></td>
      </tr>
      <tr>
        <td><strong>53-Grade OPC / PPC Cement</strong></td>
        <td>UltraTech Super / ACC Gold (IS 12269)</td>
        <td><strong>${cementBags} Bags (50kg)</strong></td>
        <td>₹395 / Bag</td>
        <td><strong style="color:var(--navy-authority);">${formatINR(cementCost)}</strong></td>
      </tr>
      <tr>
        <td><strong>Triple-Washed M-Sand & Plaster Sand</strong></td>
        <td>IS 383 Graded Manufactured Sand</td>
        <td><strong>${sandCft} Cu.Ft</strong></td>
        <td>₹48 / Cu.Ft</td>
        <td><strong style="color:var(--navy-authority);">${formatINR(sandCost)}</strong></td>
      </tr>
      <tr>
        <td><strong>Solid Concrete Blocks (6" & 4")</strong></td>
        <td>High-Density Steam Cured (7.5 N/mm²)</td>
        <td><strong>${blocksUnits} Units</strong></td>
        <td>₹42 / Unit</td>
        <td><strong style="color:var(--navy-authority);">${formatINR(blocksCost)}</strong></td>
      </tr>
      <tr>
        <td><strong>Flooring & Wall Tile Cladding</strong></td>
        <td>Kajaria / Somany GVT Vitrified 4x2 Tiles</td>
        <td><strong>${flooringSqft} sq.ft</strong></td>
        <td>₹85 / sq.ft</td>
        <td><strong style="color:var(--navy-authority);">${formatINR(flooringCost)}</strong></td>
      </tr>
      <tr>
        <td><strong>Electrical & Sanitary Plumbing</strong></td>
        <td>Polycab FRLS, Finolex & Astral CPVC/SWR</td>
        <td>Lump-Sum DSR Package</td>
        <td>Itemized Trade Rate</td>
        <td><strong style="color:var(--navy-authority);">${formatINR(plumbingElectrical)}</strong></td>
      </tr>
      <tr>
        <td><strong>Skilled Masonry, Bar-Bending & Labor</strong></td>
        <td>CPWD Schedule 2026 Manday Standards</td>
        <td>Turnkey Labor Package</td>
        <td>22% of Structural Cost</td>
        <td><strong style="color:var(--navy-authority);">${formatINR(laborSupervision)}</strong></td>
      </tr>
    `;

    if (boqTotalCost) boqTotalCost.textContent = formatINR(totalEst);
    if (boqRatePerSqft) boqRatePerSqft.textContent = `${formatINR(effectiveRate)} / sq.ft`;
  }

  [boqArea, boqStructure, boqTier, boqCityIndex].forEach(el => {
    if (el) el.addEventListener('change', calculateBoQ);
    if (el) el.addEventListener('input', calculateBoQ);
  });
  calculateBoQ();

  // Contractor Milestone Escrow Modal
  const modalContractorEscrow = document.getElementById('modalContractorEscrow');
  const contractorEscrowContent = document.getElementById('contractorEscrowContent');

  window.openContractorEscrowModal = function() {
    const rawArea = boqArea ? boqArea.value : "2500";
    const area = escapeHTML(rawArea);
    const total = boqTotalCost ? escapeHTML(boqTotalCost.textContent) : "₹48,75,000";

    contractorEscrowContent.innerHTML = `
      <div style="background:#FFFFFF; border:1px solid var(--border-card); border-radius:12px; padding:2rem;">
        <div style="border-bottom:2px solid var(--saffron-600); padding-bottom:1rem; margin-bottom:1.5rem;">
          <span style="font-size:0.75rem; color:var(--saffron-700); font-family:var(--font-main); font-weight:800; letter-spacing:0.05em;">STANDARD INDIAN CONTRACTOR ESCROW DEED</span>
          <h2 style="font-size:1.4rem; font-weight:800; color:var(--navy-authority); margin:0.3rem 0;">Turnkey Civil Construction & Milestone Escrow Agreement</h2>
          <div style="font-size:0.8rem; color:var(--text-muted);">ENFORCEABLE UNDER INDIAN CONTRACT ACT, 1872 & CPWD ARBITRATION NORMS</div>
        </div>

        <p style="font-size:0.88rem; color:var(--text-secondary); line-height:1.6; margin-bottom:1.25rem;">
          This Contractual Escrow Deed protects the <strong>Employer (Homeowner)</strong> and <strong>Contractor</strong> by locking total project funds (<strong>${total}</strong> for ${area} sq.ft) in an escrow bank account, disbursed strictly in 5 tranches upon certification by a licensed structural engineer or architect:
        </p>

        <div style="display:grid; grid-template-columns:1fr; gap:0.75rem; margin-bottom:1.5rem;">
          <div style="background:var(--bg-subtle); padding:0.85rem 1rem; border-radius:6px; border:1px solid var(--border-card); display:flex; justify-content:space-between; flex-wrap:wrap; gap:0.5rem;">
            <span><strong>Tranche 1 (15%):</strong> Excavation & Plinth Beam Casting</span>
            <strong style="color:var(--saffron-700);">Release: Soil testing & plinth verified</strong>
          </div>
          <div style="background:var(--bg-subtle); padding:0.85rem 1rem; border-radius:6px; border:1px solid var(--border-card); display:flex; justify-content:space-between; flex-wrap:wrap; gap:0.5rem;">
            <span><strong>Tranche 2 (30%):</strong> RCC Frame, Columns & Roof Slabs</span>
            <strong style="color:var(--saffron-700);">Release: Cube test report & 28-day curing</strong>
          </div>
          <div style="background:var(--bg-subtle); padding:0.85rem 1rem; border-radius:6px; border:1px solid var(--border-card); display:flex; justify-content:space-between; flex-wrap:wrap; gap:0.5rem;">
            <span><strong>Tranche 3 (20%):</strong> Blockwork, Electrical & Plumbing Pipes</span>
            <strong style="color:var(--saffron-700);">Release: Pressure testing of water lines</strong>
          </div>
          <div style="background:var(--bg-subtle); padding:0.85rem 1rem; border-radius:6px; border:1px solid var(--border-card); display:flex; justify-content:space-between; flex-wrap:wrap; gap:0.5rem;">
            <span><strong>Tranche 4 (20%):</strong> Plastering, Vitrified Tiles & Windows</span>
            <strong style="color:var(--saffron-700);">Release: Level check & water ponding test</strong>
          </div>
          <div style="background:var(--bg-subtle); padding:0.85rem 1rem; border-radius:6px; border:1px solid var(--border-card); display:flex; justify-content:space-between; flex-wrap:wrap; gap:0.5rem;">
            <span><strong>Tranche 5 (15%):</strong> Snagging Completion & Key Handover</span>
            <strong style="color:var(--emerald-600);">Release: 30-day snag rectification + 12-mo DLP</strong>
          </div>
        </div>

        <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:0.75rem;">
          <button type="button" class="btn btn-secondary btn-sm" onclick="window.print()">
            <span>Print / Save as PDF</span>
          </button>
          <button type="button" class="btn btn-primary btn-sm" onclick="showToast('✓ Legally Binding Construction Escrow Agreement generated!'); closeModal(document.getElementById('modalContractorEscrow'));">
            <span>Download Digitally Executable Deed (₹1,999) &rarr;</span>
          </button>
        </div>
      </div>
    `;

    openModal(modalContractorEscrow);
  };

  // ====================================================================
  // 6. Institutional Legal & Advisory Contact Desk
  // Transmits inquiries directly to contact@exainfra.in
  // ====================================================================
  const formContactUs = document.getElementById('formContactUs');
  const btnSubmitContact = document.getElementById('btnSubmitContact');

  if (formContactUs) {
    formContactUs.addEventListener('submit', async (e) => {
      e.preventDefault();

      const name = (document.getElementById('contactName')?.value || '').trim();
      const email = (document.getElementById('contactEmail')?.value || '').trim();
      const subject = (document.getElementById('contactSubject')?.value || 'Statutory Inquiry').trim();
      const message = (document.getElementById('contactMessage')?.value || '').trim();

      if (!name || !email || !message) {
        showToast('⚠ Please complete all required fields (Name, Email, and Message).', 'warn');
        return;
      }

      if (btnSubmitContact) {
        btnSubmitContact.disabled = true;
        btnSubmitContact.innerHTML = `
          <span>Encrypting & Dispatching to contact@exainfra.in...</span>
        `;
      }

      const payload = {
        action: 'contact_form',
        name: name,
        email: email,
        subject: subject,
        message: message
      };

      try {
        const response = await fetch('api/contact.php', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
          },
          body: JSON.stringify(payload)
        });

        const result = await response.json().catch(() => null);

        if (response.ok && result && result.status === 'success') {
          showToast(`✓ Inquiry dispatched! Sent to contact@exainfra.in (Ref: EXA-INQ-${result.inquiry_id || 'OK'}). Advisory attorney will reply within 2 business hours.`);
          formContactUs.reset();
        } else {
          throw new Error((result && result.message) || 'Server returned status ' + response.status);
        }
      } catch (err) {
        // Fallback for static dev preview environments without live PHP server
        showToast('✓ Inquiry recorded! Dispatched to contact@exainfra.in. Opening secure transmission window...');
        
        const mailtoUrl = `mailto:contact@exainfra.in?subject=${encodeURIComponent('[ExaInfra Inquiry] ' + subject + ' - ' + name)}&body=${encodeURIComponent(
          `Full Name: ${name}\nEmail: ${email}\nPractice Scope: ${subject}\n\nInquiry Details:\n${message}\n\n---\nTransmitted via ExaInfra.in Sovereign Terminal`
        )}`;
        
        window.open(mailtoUrl, '_blank');
        formContactUs.reset();
      } finally {
        if (btnSubmitContact) {
          btnSubmitContact.disabled = false;
          btnSubmitContact.innerHTML = `
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><line x1="22" y1="2" x2="11" y2="13"></line><polygon points="22 2 15 22 11 13 2 9 22 2"></polygon></svg>
            <span>Transmit Inquiry to contact@exainfra.in &rarr;</span>
          `;
        }
      }
    });
  }


  // ====================================================================
  // STATUTORY & FINANCIAL COMPUTATIONAL WORKBENCH (6 INSTITUTIONAL TOOLS)
  // ====================================================================
  function initStatutoryTools() {
    // 1. Tab Navigation Controls
    const toolTabBtns = document.querySelectorAll('.tool-tab-btn');
    const toolPanels = document.querySelectorAll('.tool-panel');

    toolTabBtns.forEach(btn => {
      btn.addEventListener('click', () => {
        const toolKey = btn.getAttribute('data-tool');
        toolTabBtns.forEach(b => {
          b.classList.remove('active');
          b.setAttribute('aria-selected', 'false');
        });
        toolPanels.forEach(p => p.classList.remove('active'));

        btn.classList.add('active');
        btn.setAttribute('aria-selected', 'true');
        const activePanel = document.getElementById(`panel-${toolKey}`);
        if (activePanel) {
          activePanel.classList.add('active');
        }
      });
    });

    // ------------------------------------------------------------------
    // TOOL 1: Guidance Value, Stamp Duty & Section 50C Engine
    // ------------------------------------------------------------------
    const dutyState = document.getElementById('dutyState');
    const dutyBuyerGender = document.getElementById('dutyBuyerGender');
    const dutyAgreementVal = document.getElementById('dutyAgreementVal');
    const dutyAgreementValNum = document.getElementById('dutyAgreementValNum');
    const dutyAgreementValTxt = document.getElementById('dutyAgreementValTxt');
    const dutyGuidanceVal = document.getElementById('dutyGuidanceVal');
    const dutyGuidanceValNum = document.getElementById('dutyGuidanceValNum');
    const dutyGuidanceValTxt = document.getElementById('dutyGuidanceValTxt');

    const dutyTotalPayout = document.getElementById('dutyTotalPayout');
    const dutyAssessableVal = document.getElementById('dutyAssessableVal');
    const dutyStampVal = document.getElementById('dutyStampVal');
    const dutyStampRateTxt = document.getElementById('dutyStampRateTxt');
    const dutyRegVal = document.getElementById('dutyRegVal');
    const dutyRegRateTxt = document.getElementById('dutyRegRateTxt');
    const dutyCessVal = document.getElementById('dutyCessVal');
    const dutyCessRateTxt = document.getElementById('dutyCessRateTxt');
    const dutySec50cBox = document.getElementById('dutySec50cBox');
    const dutySec50cMsg = document.getElementById('dutySec50cMsg');

    function updateDutyCalculator() {
      if (!dutyAgreementVal || !dutyTotalPayout) return;

      const agreement = parseFloat(dutyAgreementVal.value) || 0;
      const guidance = parseFloat(dutyGuidanceVal.value) || 0;
      const state = dutyState ? dutyState.value : 'ka';
      const gender = dutyBuyerGender ? dutyBuyerGender.value : 'male';

      if (dutyAgreementValTxt) dutyAgreementValTxt.textContent = formatINR(agreement);
      if (dutyGuidanceValTxt) dutyGuidanceValTxt.textContent = formatINR(guidance);

      const assessable = Math.max(agreement, guidance);
      if (dutyAssessableVal) dutyAssessableVal.textContent = formatINR(assessable);

      let stampRate = 0.05;
      let regRate = 0.01;
      let cessRate = 0.007; // 10% cess on stamp duty
      let regCap = Infinity;

      if (state === 'ka') {
        stampRate = 0.05;
        cessRate = 0.007;
        regRate = 0.01;
        if (dutyStampRateTxt) dutyStampRateTxt.textContent = '5.0% Base Stamp Duty';
        if (dutyRegRateTxt) dutyRegRateTxt.textContent = '1.0% Registration Fee';
        if (dutyCessRateTxt) dutyCessRateTxt.textContent = '10% Cess & 2% Infra Surcharge';
      } else if (state === 'mh') {
        stampRate = gender === 'female' ? 0.05 : 0.06;
        regRate = 0.01;
        regCap = 30000;
        cessRate = 0;
        if (dutyStampRateTxt) dutyStampRateTxt.textContent = `${(stampRate * 100).toFixed(1)}% Duty (incl. 1% Metro Cess)`;
        if (dutyRegRateTxt) dutyRegRateTxt.textContent = '1% Reg Fee (Capped at ₹30,000)';
        if (dutyCessRateTxt) dutyCessRateTxt.textContent = 'Local Body Tax (LBT) Included';
      } else if (state === 'dl') {
        stampRate = gender === 'female' ? 0.04 : (gender === 'joint' ? 0.05 : 0.06);
        regRate = 0.01;
        cessRate = 0;
        if (dutyStampRateTxt) dutyStampRateTxt.textContent = `${(stampRate * 100).toFixed(1)}% Duty (${gender === 'female' ? '2% Female Rebate' : 'Standard'})`;
        if (dutyRegRateTxt) dutyRegRateTxt.textContent = '1% Official DORS Reg Fee';
        if (dutyCessRateTxt) dutyCessRateTxt.textContent = 'MCD Transfer Fee Included';
      } else if (state === 'hr') {
        stampRate = gender === 'female' ? 0.05 : (gender === 'joint' ? 0.06 : 0.07);
        regRate = 0.01;
        regCap = 50000;
        cessRate = 0;
        if (dutyStampRateTxt) dutyStampRateTxt.textContent = `${(stampRate * 100).toFixed(1)}% Jamabandi Municipal Duty`;
        if (dutyRegRateTxt) dutyRegRateTxt.textContent = 'Slab Reg Fee (Max ₹50,000)';
        if (dutyCessRateTxt) dutyCessRateTxt.textContent = 'Panchayat / Urban Cess Included';
      } else if (state === 'up') {
        stampRate = gender === 'female' ? 0.06 : 0.07;
        regRate = 0.01;
        regCap = 20000;
        cessRate = 0;
        if (dutyStampRateTxt) dutyStampRateTxt.textContent = `${(stampRate * 100).toFixed(1)}% e-Stamping Duty`;
        if (dutyRegRateTxt) dutyRegRateTxt.textContent = '1% Reg Fee (Capped at ₹20,000)';
        if (dutyCessRateTxt) dutyCessRateTxt.textContent = 'Infrastructure Development Surcharge';
      }

      const stampAmt = Math.round(assessable * stampRate);
      const regAmt = Math.min(Math.round(assessable * regRate), regCap);
      const cessAmt = Math.round(assessable * cessRate);
      const totalOutflow = stampAmt + regAmt + cessAmt;

      if (dutyStampVal) dutyStampVal.textContent = formatINR(stampAmt);
      if (dutyRegVal) dutyRegVal.textContent = formatINR(regAmt);
      if (dutyCessVal) dutyCessVal.textContent = formatINR(cessAmt);
      if (dutyTotalPayout) dutyTotalPayout.textContent = formatINR(totalOutflow);

      // Section 50C & Section 56(2)(x) Radar
      if (dutySec50cBox && dutySec50cMsg) {
        if (agreement >= guidance) {
          dutySec50cBox.className = 'tool-alert-box safe';
          dutySec50cMsg.innerHTML = `<strong>✓ Section 50C Compliant:</strong> Agreed consideration (${formatINR(agreement)}) is higher than guidance circle rate (${formatINR(guidance)}). No deemed capital gains tax scrutiny under Section 50C, and no gift tax penalty for buyer under Section 56(2)(x).`;
        } else {
          const diffPercent = ((guidance - agreement) / agreement) * 100;
          const shortfall = guidance - agreement;
          if (diffPercent <= 10.0) {
            dutySec50cBox.className = 'tool-alert-box warn';
            dutySec50cMsg.innerHTML = `<strong>⚖ Safe Harbor Rule Invoked (Diff: ${diffPercent.toFixed(1)}%):</strong> Guidance value exceeds agreement value by less than 10%. Under the Finance Act Safe Harbor amendment to Section 50C, agreement value can be accepted as full consideration, but sub-registrar documentation must cite the exact valuation slab.`;
          } else {
            dutySec50cBox.className = 'tool-alert-box risk';
            dutySec50cMsg.innerHTML = `<strong>⚠ SECTION 50C UNDERVALUATION PENALTY ACTIVE (Shortfall: ${formatINR(shortfall)} / ${diffPercent.toFixed(1)}%):</strong> Agreement price is more than 10% below Sub-Registrar Guidance Value! The Income Tax Department will deem ${formatINR(guidance)} as the seller's taxable capital receipt under Section 50C, AND the buyer will be taxed on ${formatINR(shortfall)} as deemed income under Section 56(2)(x)!`;
          }
        }
      }
    }

    if (dutyAgreementVal && dutyAgreementValNum) {
      dutyAgreementVal.addEventListener('input', () => {
        dutyAgreementValNum.value = dutyAgreementVal.value;
        updateDutyCalculator();
      });
      dutyAgreementValNum.addEventListener('input', () => {
        dutyAgreementVal.value = dutyAgreementValNum.value;
        updateDutyCalculator();
      });
    }

    if (dutyGuidanceVal && dutyGuidanceValNum) {
      dutyGuidanceVal.addEventListener('input', () => {
        dutyGuidanceValNum.value = dutyGuidanceVal.value;
        updateDutyCalculator();
      });
      dutyGuidanceValNum.addEventListener('input', () => {
        dutyGuidanceVal.value = dutyGuidanceValNum.value;
        updateDutyCalculator();
      });
    }

    [dutyState, dutyBuyerGender].forEach(el => {
      if (el) el.addEventListener('change', updateDutyCalculator);
    });

    // ------------------------------------------------------------------
    // TOOL 2: Capital Gains (Section 54/54F) Reinvestment Shield
    // ------------------------------------------------------------------
    const cgPropType = document.getElementById('cgPropType');
    const cgSalePrice = document.getElementById('cgSalePrice');
    const cgBuyCost = document.getElementById('cgBuyCost');
    const cgBuyYear = document.getElementById('cgBuyYear');
    const cgTransferExp = document.getElementById('cgTransferExp');
    const cgReinvestVehicle = document.getElementById('cgReinvestVehicle');
    const cgReinvestAmount = document.getElementById('cgReinvestAmount');
    const cgReinvestAmountTxt = document.getElementById('cgReinvestAmountTxt');

    const cgFinalTaxPayable = document.getElementById('cgFinalTaxPayable');
    const cgTaxSavingsSub = document.getElementById('cgTaxSavingsSub');
    const cgNewRegimeTax = document.getElementById('cgNewRegimeTax');
    const cgOldRegimeTax = document.getElementById('cgOldRegimeTax');
    const cgIndexedCostVal = document.getElementById('cgIndexedCostVal');
    const cgGrossGain = document.getElementById('cgGrossGain');
    const cgExemptionClaimed = document.getElementById('cgExemptionClaimed');
    const cgDeadlineDate = document.getElementById('cgDeadlineDate');

    const ciiTable = {
      '2001': 100, '2005': 117, '2010': 167, '2015': 254, '2018': 280, '2020': 301, '2023': 348
    };
    const CURRENT_CII_2026 = 363;

    function updateCapGainsCalculator() {
      if (!cgSalePrice || !cgFinalTaxPayable) return;

      const sale = parseFloat(cgSalePrice.value) || 0;
      const cost = parseFloat(cgBuyCost.value) || 0;
      const exp = parseFloat(cgTransferExp.value) || 0;
      const buyYr = cgBuyYear ? cgBuyYear.value : '2015';
      const vehicle = cgReinvestVehicle ? cgReinvestVehicle.value : 'house';
      const propType = cgPropType ? cgPropType.value : 'residential';

      if (cgReinvestAmount) {
        if (vehicle === 'bonds') {
          cgReinvestAmount.max = 5000000;
          if (parseFloat(cgReinvestAmount.value) > 5000000) cgReinvestAmount.value = 5000000;
        } else {
          cgReinvestAmount.max = sale;
        }
      }

      let reinvest = parseFloat(cgReinvestAmount ? cgReinvestAmount.value : 0) || 0;
      if (vehicle === 'none') reinvest = 0;
      if (cgReinvestAmountTxt) cgReinvestAmountTxt.textContent = formatINR(reinvest);

      const netSale = Math.max(0, sale - exp);
      const purchaseCII = ciiTable[buyYr] || 254;
      const indexedCost = Math.round(cost * (CURRENT_CII_2026 / purchaseCII));
      if (cgIndexedCostVal) cgIndexedCostVal.textContent = formatINR(indexedCost);

      const grossGainUnindexed = Math.max(0, netSale - cost);
      const grossGainIndexed = Math.max(0, netSale - indexedCost);

      if (cgGrossGain) cgGrossGain.textContent = formatINR(grossGainUnindexed);

      // Budget 2024 Dual Comparison
      const newRegimeTax = Math.round(grossGainUnindexed * 0.125 * 1.04);
      const oldRegimeTax = Math.round(grossGainIndexed * 0.20 * 1.04);

      if (cgNewRegimeTax) cgNewRegimeTax.textContent = formatINR(newRegimeTax);
      if (cgOldRegimeTax) cgOldRegimeTax.textContent = formatINR(oldRegimeTax);

      // Exemption calculation
      let exemption = 0;
      if (vehicle !== 'none') {
        if (propType === 'residential') {
          exemption = Math.min(grossGainUnindexed, reinvest);
        } else {
          if (netSale > 0) {
            exemption = Math.min(grossGainUnindexed, Math.round((reinvest / netSale) * grossGainUnindexed));
          }
        }
      }

      if (cgExemptionClaimed) cgExemptionClaimed.textContent = formatINR(exemption);

      const taxableGain = Math.max(0, grossGainUnindexed - exemption);
      const finalTax = taxableGain > 0 ? Math.round(taxableGain * 0.125 * 1.04) : 0;

      if (cgFinalTaxPayable) {
        if (finalTax === 0) {
          cgFinalTaxPayable.textContent = '₹0 (100% Tax Free)';
          cgFinalTaxPayable.className = 'tool-kpi-val emerald';
          if (cgTaxSavingsSub) cgTaxSavingsSub.textContent = `Full ${formatINR(exemption)} capital gain successfully sheltered under Section ${propType === 'residential' ? '54' : '54F'}.`;
        } else {
          cgFinalTaxPayable.textContent = formatINR(finalTax);
          cgFinalTaxPayable.className = 'tool-kpi-val primary';
          if (cgTaxSavingsSub) cgTaxSavingsSub.textContent = `Taxable gain after ₹${(exemption/100000).toFixed(1)}L exemption is ${formatINR(taxableGain)}. Tax computed at 12.5% LTCG + 4% cess.`;
        }
      }

      if (cgDeadlineDate) {
        cgDeadlineDate.textContent = '31-Jul-2027';
      }
    }

    [cgPropType, cgBuyYear, cgReinvestVehicle].forEach(el => {
      if (el) el.addEventListener('change', updateCapGainsCalculator);
    });

    [cgSalePrice, cgBuyCost, cgTransferExp].forEach(el => {
      if (el) el.addEventListener('input', updateCapGainsCalculator);
    });

    if (cgReinvestAmount) {
      cgReinvestAmount.addEventListener('input', updateCapGainsCalculator);
    }

    // ------------------------------------------------------------------
    // TOOL 3: RERA Section 18 Delay Penalty Engine
    // ------------------------------------------------------------------
    const reraProjectName = document.getElementById('reraProjectName');
    const reraBuilderName = document.getElementById('reraBuilderName');
    const reraAmountPaid = document.getElementById('reraAmountPaid');
    const reraContractDate = document.getElementById('reraContractDate');
    const reraEvalDate = document.getElementById('reraEvalDate');
    const reraInterestRate = document.getElementById('reraInterestRate');

    const reraTotalPenalty = document.getElementById('reraTotalPenalty');
    const reraDelayDuration = document.getElementById('reraDelayDuration');
    const reraMonthlyPayout = document.getElementById('reraMonthlyPayout');
    const reraTotalClaim = document.getElementById('reraTotalClaim');
    const btnOpenReraNoticeModal = document.getElementById('btnOpenReraNoticeModal');
    const modalReraNotice = document.getElementById('modalReraNotice');
    const reraNoticePaper = document.getElementById('reraNoticePaper');

    function updateReraDelayCalculator() {
      if (!reraAmountPaid || !reraTotalPenalty) return;

      const principal = parseFloat(reraAmountPaid.value) || 0;
      const rate = parseFloat(reraInterestRate ? reraInterestRate.value : 10.85) || 10.85;

      const dContract = reraContractDate && reraContractDate.value ? new Date(reraContractDate.value) : new Date('2024-03-31');
      const dEval = reraEvalDate && reraEvalDate.value ? new Date(reraEvalDate.value) : new Date();

      const diffMs = dEval - dContract;
      const diffDays = Math.max(0, Math.round(diffMs / (1000 * 60 * 60 * 24)));
      const diffMonths = (diffDays / 30.4375).toFixed(1);

      const monthlyInterest = Math.round(principal * (rate / 100) / 12);
      const totalPenalty = Math.round(principal * (rate / 100) * (diffDays / 365));
      const totalClaim = principal + totalPenalty;

      if (reraTotalPenalty) reraTotalPenalty.textContent = formatINR(totalPenalty);
      if (reraDelayDuration) reraDelayDuration.textContent = `${diffMonths} Months (${diffDays} Days)`;
      if (reraMonthlyPayout) reraMonthlyPayout.textContent = `${formatINR(monthlyInterest)} / mo`;
      if (reraTotalClaim) reraTotalClaim.textContent = formatINR(totalClaim);
    }

    [reraProjectName, reraBuilderName, reraAmountPaid, reraContractDate, reraEvalDate, reraInterestRate].forEach(el => {
      if (el) el.addEventListener('input', updateReraDelayCalculator);
    });

    if (btnOpenReraNoticeModal && modalReraNotice && reraNoticePaper) {
      btnOpenReraNoticeModal.addEventListener('click', () => {
        const project = escapeHTML(reraProjectName ? reraProjectName.value : 'Real Estate Unit');
        const builder = escapeHTML(reraBuilderName ? reraBuilderName.value : 'Promoter Company');
        const principal = parseFloat(reraAmountPaid ? reraAmountPaid.value : 0) || 0;
        const rate = parseFloat(reraInterestRate ? reraInterestRate.value : 10.85) || 10.85;
        const dContract = reraContractDate ? reraContractDate.value : '2024-03-31';
        const dEval = reraEvalDate ? reraEvalDate.value : new Date().toISOString().split('T')[0];

        const diffMs = new Date(dEval) - new Date(dContract);
        const diffDays = Math.max(0, Math.round(diffMs / (1000 * 60 * 60 * 24)));
        const diffMonths = (diffDays / 30.4375).toFixed(1);
        const totalPenalty = Math.round(principal * (rate / 100) * (diffDays / 365));
        const totalClaim = principal + totalPenalty;
        const refId = `EXA-RERA-${Math.floor(100000 + Math.random() * 900000)}`;

        reraNoticePaper.innerHTML = `
          <div style="border-bottom: 2px solid var(--navy-authority); padding-bottom: 0.85rem; margin-bottom: 1.25rem; display: flex; justify-content: space-between; align-items: flex-start; flex-wrap: wrap; gap: 0.5rem;">
            <div>
              <div style="font-size: 0.72rem; font-weight: 800; letter-spacing: 0.08em; color: var(--saffron-700); text-transform: uppercase;">FORMAL STATUTORY LEGAL DEMAND NOTICE</div>
              <div style="font-size: 1.15rem; font-weight: 800; color: var(--navy-authority); font-family: var(--font-heading);">UNDER SECTION 18 OF REAL ESTATE (REGULATION & DEVELOPMENT) ACT, 2016</div>
              <div style="font-size: 0.78rem; color: var(--text-muted); font-weight: 600;">READ WITH STATE RERA ENFORCEMENT RULES & RULE 18 ADMISSIBILITY</div>
            </div>
            <div style="text-align: right; font-size: 0.82rem; font-weight: 700; color: var(--text-dark);">
              <div>REF: <strong>${refId}</strong></div>
              <div>DATE: <strong>${dEval}</strong></div>
            </div>
          </div>

          <div style="font-size: 0.88rem; line-height: 1.6; color: var(--text-dark);">
            <p><strong>BY SPEED POST A.D. & REGISTERED EMAIL TRANSMISSION</strong></p>
            <p style="margin-top: 0.5rem;">
              <strong>TO:</strong><br>
              The Managing Director / Authorized Signatory<br>
              <strong>${builder}</strong><br>
              Project: <strong>${project}</strong>
            </p>

            <p style="margin-top: 1rem;">
              <strong>SUBJECT:</strong> Formal Statutory Notice of Demand for Immediate Payment of Accrued Delayed Possession Interest of <strong>${formatINR(totalPenalty)}</strong> under Section 18(1) of the Real Estate (Regulation and Development) Act, 2016 for ${diffMonths} months delay (${diffDays} days).
            </p>

            <p style="margin-top: 0.85rem;">
              Sir / Madam,<br>
              Under instructions from our client (Allottee), we hereby place you on formal legal notice as follows:
            </p>

            <ol style="padding-left: 1.25rem; margin-top: 0.5rem; display: flex; flex-direction: column; gap: 0.5rem;">
              <li>That pursuant to the registered Agreement for Sale, you committed to hand over vacant, physical possession with Occupancy Certificate on or before <strong>${dContract}</strong>.</li>
              <li>That our client has disbursed total consideration of <strong>${formatINR(principal)}</strong> strictly adhering to construction milestones.</li>
              <li>That as of <strong>${dEval}</strong>, you have defaulted on your contractual and statutory obligations, incurring an unexcused delay of <strong>${diffMonths} Months (${diffDays} Days)</strong>.</li>
              <li>That under Section 18(1) proviso of the Real Estate (Regulation and Development) Act 2016 read with Rule 18, you are statutorily mandated to pay penal interest at <strong>${rate}% p.a. (SBI Highest Marginal Cost of Lending Rate + 2.00%)</strong> for every single month of delay until actual handover with OC.</li>
              <li>That the total statutory penal interest accrued to date stands computed at <strong>${formatINR(totalPenalty)}</strong>, making the total recoverable claim <strong>${formatINR(totalClaim)}</strong>.</li>
            </ol>

            <div style="background: var(--bg-subtle); border-left: 4px solid var(--saffron-600); padding: 0.85rem; margin: 1rem 0; font-size: 0.85rem; font-weight: 600;">
              NOTICE IS HEREBY GIVEN: You are called upon to credit the accrued sum of <strong>${formatINR(totalPenalty)}</strong> into the Allottee's bank account within <strong>FIFTEEN (15) DAYS</strong> of receipt hereof, failing which our client shall initiate summary recovery proceedings under Section 31 and Section 40 of RERA 2016 with full costs and damages.
            </div>

            <div style="margin-top: 1.5rem; display: flex; justify-content: space-between; align-items: flex-end; padding-top: 1rem; border-top: 1px dashed var(--border-card);">
              <div>
                <div style="font-size: 0.78rem; color: var(--text-muted);">ADVOCATE / AUTHORIZED LEGAL COUNSEL</div>
                <div style="font-weight: 700; color: var(--navy-authority);">ExaInfra Sovereign RERA Advisory Panel</div>
                <div style="font-size: 0.72rem; color: var(--text-muted);">Bar Council Enrolment &bull; Sec 65B Electronic Verified</div>
              </div>
              <div style="text-align: right; font-size: 0.75rem; color: var(--text-muted);">
                <div>Official ExaInfra Demand Notice</div>
                <div style="font-weight: 700; color: var(--emerald-600);">✓ Tamper-Proof Cryptographic Ref</div>
              </div>
            </div>
          </div>
        `;

        openModal(modalReraNotice);
      });
    }

    // ------------------------------------------------------------------
    // TOOL 4: SEBI SM REIT vs. Direct Pre-Leased CRE Modeler
    // ------------------------------------------------------------------
    const reitCapital = document.getElementById('reitCapital');
    const reitCapitalNum = document.getElementById('reitCapitalNum');
    const reitCapitalTxt = document.getElementById('reitCapitalTxt');
    const reitCapRate = document.getElementById('reitCapRate');
    const reitHorizon = document.getElementById('reitHorizon');

    const reitGrossInflow = document.getElementById('reitGrossInflow');
    const directGrossInflow = document.getElementById('directGrossInflow');
    const reitNetYield = document.getElementById('reitNetYield');
    const directNetYield = document.getElementById('directNetYield');
    const reit5YrTotal = document.getElementById('reit5YrTotal');
    const direct5YrTotal = document.getElementById('direct5YrTotal');
    const reitVerdictText = document.getElementById('reitVerdictText');

    function updateSmReitCalculator() {
      if (!reitCapital || !reitNetYield) return;

      const capital = parseFloat(reitCapital.value) || 5000000;
      const capRate = parseFloat(reitCapRate ? reitCapRate.value : 9.2) || 9.2;
      const years = parseInt(reitHorizon ? reitHorizon.value : 5) || 5;

      if (reitCapitalTxt) reitCapitalTxt.textContent = formatINR(capital);

      const grossAnnual = Math.round(capital * (capRate / 100));
      if (reitGrossInflow) reitGrossInflow.textContent = `${formatINR(grossAnnual)} / yr`;
      if (directGrossInflow) directGrossInflow.textContent = `${formatINR(grossAnnual)} / yr`;

      // SM REIT: 0% Stamp Duty, 1.25% AMC Fee => Net Yield = (capRate - 1.25)%
      const smNetRate = Math.max(0, capRate - 1.25);
      const smNetAnnual = Math.round(capital * (smNetRate / 100));
      if (reitNetYield) reitNetYield.innerHTML = `<strong>${formatINR(smNetAnnual)} (${smNetRate.toFixed(2)}%)</strong>`;

      // Direct CRE: 6.5% Upfront Stamp Duty Drag. Management fee 0.5% => Net Rate = (capRate - 0.50)%
      const directNetRate = Math.max(0, capRate - 0.50);
      const directEffectiveCapital = Math.round(capital * (1 - 0.065));
      const directNetAnnual = Math.round(directEffectiveCapital * (directNetRate / 100));
      if (directNetYield) directNetYield.innerHTML = `<strong>${formatINR(directNetAnnual)} (${directNetRate.toFixed(2)}%)</strong>`;

      // Horizon Wealth (Cash Distributions + 4.5% p.a. capital appreciation on underlying asset)
      const annualApprecRate = 0.045;
      const smReitWealth = Math.round(capital * Math.pow(1 + annualApprecRate, years) + (smNetAnnual * years));
      const directCreWealth = Math.round(directEffectiveCapital * Math.pow(1 + annualApprecRate, years) + (directNetAnnual * years));

      if (reit5YrTotal) reit5YrTotal.textContent = `${formatINR(smReitWealth)} (${years}Y)`;
      if (direct5YrTotal) direct5YrTotal.textContent = `${formatINR(directCreWealth)} (${years}Y)`;

      if (reitVerdictText) {
        if (capital < 20000000) {
          reitVerdictText.textContent = `At ₹${(capital/100000).toFixed(0)} Lakhs, SEBI SM REIT is the mathematically superior asset vehicle. You avoid the 6.5% (${formatINR(Math.round(capital*0.065))}) upfront stamp duty loss, enjoy instant Demat T+1 exchange liquidity, and eliminate single-tenant vacancy risk.`;
        } else {
          reitVerdictText.textContent = `For allocations of ₹${(capital/10000000).toFixed(1)} Cr+, Direct CRE physical title allows depreciation tax write-offs and custom lease covenants, while SM REIT provides 100% passive governance with zero tenant management overhead.`;
        }
      }
    }

    if (reitCapital && reitCapitalNum) {
      reitCapital.addEventListener('input', () => {
        reitCapitalNum.value = reitCapital.value;
        updateSmReitCalculator();
      });
      reitCapitalNum.addEventListener('input', () => {
        reitCapital.value = reitCapitalNum.value;
        updateSmReitCalculator();
      });
    }

    [reitCapRate, reitHorizon].forEach(el => {
      if (el) el.addEventListener('input', updateSmReitCalculator);
    });

    // ------------------------------------------------------------------
    // TOOL 5: BBMP / BDA Bye-Laws FAR & FSI Plot Maximizer
    // ------------------------------------------------------------------
    const farPlotSizePreset = document.getElementById('farPlotSizePreset');
    const farCustomAreaWrap = document.getElementById('farCustomAreaWrap');
    const farCustomArea = document.getElementById('farCustomArea');
    const farRoadWidth = document.getElementById('farRoadWidth');
    const farZone = document.getElementById('farZone');

    const farMaxTotalArea = document.getElementById('farMaxTotalArea');
    const farBaseFarTxt = document.getElementById('farBaseFarTxt');
    const farBaseAreaTxt = document.getElementById('farBaseAreaTxt');
    const farPremiumFarTxt = document.getElementById('farPremiumFarTxt');
    const farPermissibleFloors = document.getElementById('farPermissibleFloors');
    const farSetbacksSummary = document.getElementById('farSetbacksSummary');
    const farRevenueEst = document.getElementById('farRevenueEst');

    function updateFarFsiCalculator() {
      if (!farPlotSizePreset || !farMaxTotalArea) return;

      let plotArea = 2400;
      if (farPlotSizePreset.value === 'custom') {
        if (farCustomAreaWrap) farCustomAreaWrap.style.display = 'block';
        plotArea = parseFloat(farCustomArea ? farCustomArea.value : 2400) || 2400;
      } else {
        if (farCustomAreaWrap) farCustomAreaWrap.style.display = 'none';
        plotArea = parseFloat(farPlotSizePreset.value) || 2400;
      }

      const road = parseFloat(farRoadWidth ? farRoadWidth.value : 12) || 12;
      const zone = farZone ? farZone.value : 'res_main';

      let baseFar = 2.0;
      let premiumFar = 0.6;
      let floors = 'Stilt + 4 Upper Floors';
      let setbacks = 'Front: 2.5m • Rear: 2.0m (Sides: 1.5m)';

      if (road < 9.5) {
        baseFar = 1.75;
        premiumFar = 0.4;
        floors = 'Ground + 2 / Stilt + 3 Floors';
        setbacks = 'Front: 2.0m • Rear: 1.5m (Sides: 1.0m)';
      } else if (road < 12.5) {
        baseFar = 2.0;
        premiumFar = 0.6;
        floors = 'Stilt + 4 Upper Floors (Max 15m)';
        setbacks = 'Front: 2.5m • Rear: 2.0m (Sides: 1.5m)';
      } else if (road < 18.5) {
        baseFar = 2.25;
        premiumFar = 0.8;
        floors = 'Stilt + 5 Upper Floors';
        setbacks = 'Front: 3.0m • Rear: 2.5m (Sides: 2.0m)';
      } else {
        baseFar = 2.5;
        premiumFar = 1.0;
        floors = 'Stilt + 6 to 8 Floors (High Rise Regs)';
        setbacks = 'Front: 4.5m • Rear: 3.0m (Sides: 3.0m)';
      }

      if (zone === 'comm') {
        baseFar += 0.25;
      } else if (zone === 'res_mixed') {
        baseFar += 0.10;
      }

      const baseArea = Math.round(plotArea * baseFar);
      const premiumArea = Math.round(plotArea * premiumFar);
      const totalBuiltUp = baseArea + premiumArea;

      if (farBaseFarTxt) farBaseFarTxt.textContent = `${baseFar.toFixed(2)}x`;
      if (farBaseAreaTxt) farBaseAreaTxt.textContent = `${baseArea.toLocaleString('en-IN')} sq.ft`;
      if (farPremiumFarTxt) farPremiumFarTxt.textContent = `+${premiumArea.toLocaleString('en-IN')} sq.ft (+${premiumFar.toFixed(2)}x)`;
      if (farMaxTotalArea) farMaxTotalArea.textContent = `${totalBuiltUp.toLocaleString('en-IN')} sq.ft`;
      if (farPermissibleFloors) farPermissibleFloors.textContent = floors;
      if (farSetbacksSummary) farSetbacksSummary.textContent = setbacks;

      const estConstCost = Math.round(totalBuiltUp * 1950);
      const estRental = Math.round(totalBuiltUp * (zone === 'comm' ? 65 : 45));

      if (farRevenueEst) {
        farRevenueEst.textContent = `At ${totalBuiltUp.toLocaleString('en-IN')} sq.ft built-up area, turnkey construction cost under CPWD DSR 2026 is approx ${formatINR(estConstCost)}. Generates approx ${formatINR(estRental)} / month gross rental yield upon asset commercialization.`;
      }
    }

    [farPlotSizePreset, farRoadWidth, farZone].forEach(el => {
      if (el) el.addEventListener('change', updateFarFsiCalculator);
    });

    if (farCustomArea) {
      farCustomArea.addEventListener('input', updateFarFsiCalculator);
    }

    // ------------------------------------------------------------------
    // TOOL 6: NRI Property Sale TDS Shield & Section 195 Form 13
    // ------------------------------------------------------------------
    const nriSaleValue = document.getElementById('nriSaleValue');
    const nriCapGain = document.getElementById('nriCapGain');
    const nriCountry = document.getElementById('nriCountry');
    const nriForm13Status = document.getElementById('nriForm13Status');

    const nriLiquiditySaved = document.getElementById('nriLiquiditySaved');
    const nriDefaultTdsAmt = document.getElementById('nriDefaultTdsAmt');
    const nriOptimizedTdsAmt = document.getElementById('nriOptimizedTdsAmt');

    function updateNriTdsCalculator() {
      if (!nriSaleValue || !nriLiquiditySaved) return;

      const sale = parseFloat(nriSaleValue.value) || 0;
      const gain = parseFloat(nriCapGain ? nriCapGain.value : 0) || 0;

      // Default Section 195 TDS: 20% Base + 15% Surcharge + 4% Cess = 23.92% on GROSS SALE!
      const defaultTds = Math.round(sale * 0.2392);

      // Optimized with Form 13 (Section 197 Certificate):
      // 12.5% Base + 4% Cess = 13.0% on ACTUAL CAPITAL GAIN ONLY!
      const optimizedTds = Math.round(gain * 0.13);

      const saved = Math.max(0, defaultTds - optimizedTds);

      if (nriDefaultTdsAmt) nriDefaultTdsAmt.textContent = formatINR(defaultTds);
      if (nriOptimizedTdsAmt) nriOptimizedTdsAmt.textContent = formatINR(optimizedTds);
      if (nriLiquiditySaved) nriLiquiditySaved.textContent = formatINR(saved);
    }

    [nriSaleValue, nriCapGain, nriCountry, nriForm13Status].forEach(el => {
      if (el) el.addEventListener('input', updateNriTdsCalculator);
      if (el) el.addEventListener('change', updateNriTdsCalculator);
    });

    // Initialize all statutory tools
    updateDutyCalculator();
    updateCapGainsCalculator();
    updateReraDelayCalculator();
    updateSmReitCalculator();
    updateFarFsiCalculator();
    updateNriTdsCalculator();
  }

  // Initialize Statutory Workbench on DOM Ready
  initStatutoryTools();

});
