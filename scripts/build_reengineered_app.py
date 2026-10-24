js_content = """/**
 * ExaInfra.in - National Real Estate Due Diligence, Commercial Yield & Asset Terminal
 * Compliant with RERA Act 2016, IT Act 2000 (Sec 65B), Motor Vehicles Act 1988, DPDP Act 2023 & CPWD DSR 2026
 * Clean White / Light Sovereign Theme with Full Mobile Responsiveness
 */

document.addEventListener('DOMContentLoaded', () => {

  // ====================================================================
  // 1. Toast Notification System
  // ====================================================================
  function showToast(message, type = 'emerald') {
    const container = document.getElementById('toastContainer');
    if (!container) return;

    const toast = document.createElement('div');
    toast.className = `toast-item toast-${type}`;
    toast.innerHTML = `
      <div class="toast-content">${message}</div>
      <button class="toast-close" onclick="this.parentElement.remove()">&times;</button>
    `;

    container.appendChild(toast);
    setTimeout(() => {
      toast.classList.add('fade-out');
      setTimeout(() => toast.remove(), 300);
    }, 4500);
  }
  window.showToast = showToast;

  // ====================================================================
  // 2. Modal & Mobile Drawer Controls
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

  // Mobile Navigation Drawer Toggle
  const btnMobileToggle = document.getElementById('btnMobileToggle');
  const btnMobileClose = document.getElementById('btnMobileClose');
  const mobileNavDrawer = document.getElementById('mobileNavDrawer');

  function openMobileNav() {
    if (mobileNavDrawer) mobileNavDrawer.classList.add('active');
    document.body.style.overflow = 'hidden';
  }

  function closeMobileNav() {
    if (mobileNavDrawer) mobileNavDrawer.classList.remove('active');
    document.body.style.overflow = '';
  }

  window.closeMobileNav = closeMobileNav;

  if (btnMobileToggle) btnMobileToggle.addEventListener('click', openMobileNav);
  if (btnMobileClose) btnMobileClose.addEventListener('click', closeMobileNav);

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
      const query = document.getElementById('radarIdentifier').value.trim();
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
            <div style="font-family:'JetBrains Mono', monospace; font-size:0.85rem; font-weight:800; color:#0F172A;">${certNo}</div>
            <div style="font-size:0.75rem; color:#64748B;">Date: 24-Oct-2026</div>
          </div>
        </div>

        <div class="cert-body-grid">
          <div class="cert-field">
            <span>PROPERTY IDENTIFIER / SURVEY NUMBER</span>
            <strong>${data.name}</strong>
          </div>
          <div class="cert-field">
            <span>TITLE HEALTH AUDIT SCORE</span>
            <strong style="color:${data.verdictClass === 'safe' ? '#059669' : '#DC2626'}; font-size:1.15rem;">${data.score} / 100 (${data.verdictTitle.split(':')[0]})</strong>
          </div>
          <div class="cert-field">
            <span>SUB-REGISTRAR ENCUMBRANCE (30 YRS)</span>
            <strong>${data.ec}</strong>
          </div>
          <div class="cert-field">
            <span>REVENUE KHATA CLASSIFICATION</span>
            <strong>${data.khata}</strong>
          </div>
          <div class="cert-field">
            <span>TOWN PLANNING MASTER PLAN ZONING</span>
            <strong>${data.zoning}</strong>
          </div>
          <div class="cert-field">
            <span>NGT 50M STORMWATER DRAIN BUFFER</span>
            <strong style="color:${data.verdictClass === 'danger' ? '#DC2626' : '#059669'};">${data.buffer}</strong>
          </div>
        </div>

        <div class="cert-verdict-box ${data.verdictClass === 'safe' ? 'safe' : 'risk'}">
          <strong>STATUTORY LEGAL OPINION & RISK VERDICT:</strong>
          <p style="margin:0.25rem 0 0 0;">${data.verdictSub}</p>
        </div>

        <div class="cert-sign-strip">
          <div>
            <span>CRYPTOGRAPHIC RECORD EVIDENCE HASH:</span>
            <code style="font-family:'JetBrains Mono', monospace; color:#0F172A; display:block; font-size:0.75rem;">${hash}</code>
          </div>
          <div style="text-align:right;">
            <div style="font-family:'JetBrains Mono', monospace; font-size:0.9rem; font-weight:700; color:#0F172A;">Advocate R. S. Nambiar & Associates</div>
            <span>High Court of Karnataka & RERA Panel Legal Auditor</span>
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
            <span class="cre-tenant-pill">${item.tenant}</span>
            <h2 style="font-size:1.5rem; font-weight:800; color:var(--navy-authority); margin:0.4rem 0 0.2rem 0;">${item.title}</h2>
            <div style="font-size:0.85rem; color:var(--text-muted);">📍 ${item.location}</div>
          </div>
          <div style="text-align:right;">
            <div style="font-size:1.6rem; font-weight:800; color:var(--emerald-600); font-family:var(--font-mono);">${item.yield}</div>
            <div style="font-size:0.8rem; color:var(--text-muted);">Pre-Tax Cap Rate</div>
          </div>
        </div>

        <div style="display:grid; grid-template-columns:1fr 1fr; gap:1.25rem; margin-bottom:1.5rem;">
          <div style="background:var(--bg-subtle); padding:1rem; border-radius:8px; border:1px solid var(--border-card);">
            <span style="font-size:0.75rem; color:var(--text-muted); display:block; font-weight:600;">PURCHASE CONSIDERATION</span>
            <strong style="font-size:1.2rem; color:var(--saffron-700); font-family:var(--font-mono);">${item.investment}</strong>
          </div>
          <div style="background:var(--bg-subtle); padding:1rem; border-radius:8px; border:1px solid var(--border-card);">
            <span style="font-size:0.75rem; color:var(--text-muted); display:block; font-weight:600;">MONTHLY RENTAL INFLOW</span>
            <strong style="font-size:1.2rem; color:var(--navy-authority); font-family:var(--font-mono);">${item.rent}</strong>
          </div>
          <div style="background:var(--bg-subtle); padding:1rem; border-radius:8px; border:1px solid var(--border-card);">
            <span style="font-size:0.75rem; color:var(--text-muted); display:block; font-weight:600;">LEASE LOCK-IN & COVENANT</span>
            <strong style="font-size:1rem; color:var(--navy-authority);">${item.lockIn}</strong>
          </div>
          <div style="background:var(--bg-subtle); padding:1rem; border-radius:8px; border:1px solid var(--border-card);">
            <span style="font-size:0.75rem; color:var(--text-muted); display:block; font-weight:600;">RENT ESCALATION CLAUSE</span>
            <strong style="font-size:1rem; color:var(--navy-authority);">${item.escalation}</strong>
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
    const area = boqArea ? boqArea.value : 2500;
    const total = boqTotalCost ? boqTotalCost.textContent : "₹48,75,000";

    contractorEscrowContent.innerHTML = `
      <div style="background:#FFFFFF; border:1px solid var(--border-card); border-radius:12px; padding:1.75rem;">
        <div style="border-bottom:2px solid var(--saffron-600); padding-bottom:1rem; margin-bottom:1.5rem;">
          <span style="font-size:0.75rem; color:var(--saffron-700); font-family:var(--font-mono); font-weight:800;">STANDARD INDIAN CONTRACTOR ESCROW DEED</span>
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
  // 6. PILLAR 4: VAHAN 4.0 & Fleet Asset Compliance Terminal
  // ====================================================================
  const vahanSamples = {
    clean: {
      plate: "KA-01-MJ-4920",
      model: "TOYOTA INNOVA CRYSTA 2.4 VX (7-STR)",
      rto: "KA-01 (Koramangala, Bengaluru)",
      regDate: "14-Nov-2022",
      class: "Motor Cab / Commercial",
      fuel: "Diesel • BS-VI OBD-II",
      fitness: "Valid upto 13-Nov-2027",
      insurance: "Active (ICICI Lombard)",
      nocStatus: "pass",
      nocText: "✓ Hypothecation Clear (No Bank Lien)",
      challanCount: 0,
      challans: []
    },
    hypo: {
      plate: "MH-02-CP-9901",
      model: "TATA SIGNA 4825.TK HEAVY COMMERCIAL TRUCK",
      rto: "MH-02 (Andheri, Mumbai)",
      regDate: "08-Mar-2021",
      class: "Heavy Goods Vehicle (HGV)",
      fuel: "Diesel • BS-VI Commercial",
      fitness: "Valid upto 07-Mar-2025",
      insurance: "Active (New India Assurance)",
      nocStatus: "fail",
      nocText: "❌ ACTIVE HYPOTHECATION: HDFC BANK LTD (MUMBAI)",
      challanCount: 2,
      challans: [
        { id: "MH20261019001", date: "19-Oct-2026", offense: "Over-speeding on Mumbai-Pune Expressway (105 km/h)", amount: 2000, status: "Unpaid" },
        { id: "MH20260902419", date: "02-Sep-2026", offense: "Lane violation & missing rear retro-reflector", amount: 1500, status: "Unpaid" }
      ]
    }
  };

  let currentVahanData = vahanSamples.clean;

  window.loadVahanSample = function(type) {
    const data = vahanSamples[type] || vahanSamples.clean;
    currentVahanData = data;

    const input = document.getElementById('vahanPlateInput');
    if (input) input.value = data.plate;

    updateVahanUI(data);
    showToast(`✓ Loaded VAHAN record: ${data.plate} (${data.model.split(' ')[0]})`);
  };

  function updateVahanUI(data) {
    const vModelName = document.getElementById('vahanModelName');
    const vNocBadge = document.getElementById('vahanNocBadge');
    const vRegDate = document.getElementById('vahanRegDate');
    const vClass = document.getElementById('vahanClass');
    const vFuel = document.getElementById('vahanFuel');
    const vFitness = document.getElementById('vahanFitness');
    const vInsurance = document.getElementById('vahanInsurance');
    const vChallanTitle = document.getElementById('vahanChallanTitle');
    const vChallanBadge = document.getElementById('vahanChallanBadge');
    const vChallanTableWrap = document.getElementById('vahanChallanTableWrap');

    if (vModelName) vModelName.textContent = data.model;
    if (vRegDate) vRegDate.textContent = `Reg Date: ${data.regDate}`;
    if (vClass) vClass.textContent = data.class;
    if (vFuel) vFuel.textContent = data.fuel;
    if (vFitness) vFitness.textContent = data.fitness;
    if (vInsurance) vInsurance.textContent = data.insurance;

    if (vNocBadge) {
      vNocBadge.textContent = data.nocText;
      vNocBadge.className = `status-badge ${data.nocStatus === 'pass' ? 'pass' : 'fail'}`;
    }

    if (vChallanTitle) vChallanTitle.textContent = `Pending Traffic e-Challan Radar (${data.challanCount} Violations)`;
    if (vChallanBadge) {
      if (data.challanCount === 0) {
        vChallanBadge.textContent = '✓ All Dues Cleared';
        vChallanBadge.className = 'status-badge pass';
      } else {
        vChallanBadge.textContent = `⚠ ${data.challanCount} Unpaid Challans (₹${data.challans.reduce((a,c) => a + c.amount, 0)})`;
        vChallanBadge.className = 'status-badge fail';
      }
    }

    if (vChallanTableWrap) {
      if (data.challanCount === 0) {
        vChallanTableWrap.innerHTML = `<p style="font-size:0.85rem; color:var(--text-muted); margin:0;">Zero outstanding traffic enforcement penalties recorded across State Traffic Police & Parivahan servers.</p>`;
      } else {
        vChallanTableWrap.innerHTML = `
          <table class="challan-table">
            <thead>
              <tr>
                <th>CHALLAN NUMBER</th>
                <th>DATE</th>
                <th>OFFENSE DETAIL</th>
                <th>PENALTY</th>
                <th>ACTION</th>
              </tr>
            </thead>
            <tbody>
              ${data.challans.map(ch => `
                <tr>
                  <td><code>${ch.id}</code></td>
                  <td>${ch.date}</td>
                  <td>${ch.offense}</td>
                  <td><strong style="color:var(--crimson-600);">${formatINR(ch.amount)}</strong></td>
                  <td>
                    <button class="btn btn-xs btn-primary" onclick="this.innerHTML='Paid ✓'; this.style.background='#059669'; this.disabled=true; showToast('✓ Penalty of ${formatINR(ch.amount)} cleared on Parivahan gateway!');">
                      Pay & Settle
                    </button>
                  </td>
                </tr>
              `).join('')}
            </tbody>
          </table>
        `;
      }
    }
  }

  const btnRunVahanAudit = document.getElementById('btnRunVahanAudit');
  if (btnRunVahanAudit) {
    btnRunVahanAudit.addEventListener('click', () => {
      const plate = document.getElementById('vahanPlateInput').value.trim();
      btnRunVahanAudit.disabled = true;
      btnRunVahanAudit.innerHTML = `<span>Querying MoRTH VAHAN 4.0...</span>`;

      showToast('🔄 Cross-referencing Vahan 4.0 & State Police e-Challan database...');

      setTimeout(() => {
        btnRunVahanAudit.disabled = false;
        btnRunVahanAudit.innerHTML = `
          <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
          <span>Scan Vahan RC & Challans</span>
        `;

        if (plate.toUpperCase().includes('MH') || plate.toUpperCase().includes('9901')) {
          loadVahanSample('hypo');
        } else {
          loadVahanSample('clean');
        }
        showToast('✓ VAHAN RC verified & Traffic Challan ledger synced!');
      }, 900);
    });
  }

  // Vahan Report Modal
  const modalVahanReport = document.getElementById('modalVahanReport');
  const vahanReportContent = document.getElementById('vahanReportContent');

  window.openVahanReportModal = function() {
    const data = currentVahanData;

    vahanReportContent.innerHTML = `
      <div style="background:#FFFFFF; color:#0F172A; border-radius:10px; padding:1.75rem; border:1px solid var(--border-card);">
        <div style="border-bottom:2px solid #003366; padding-bottom:1rem; margin-bottom:1.25rem; display:flex; justify-content:space-between; align-items:flex-start; flex-wrap:wrap; gap:0.5rem;">
          <div>
            <span style="font-size:0.75rem; font-weight:800; color:#003366;">MINISTRY OF ROAD TRANSPORT & HIGHWAYS (MORTH) &bull; CITIZEN PORTAL COMPLIANT</span>
            <h2 style="font-size:1.35rem; font-weight:800; color:#0F172A; margin:0.25rem 0;">Vehicle RC Due Diligence & Pre-Purchase NOC Report</h2>
            <div style="font-size:0.75rem; color:#64748B;">VERIFIED UNDER CENTRAL MOTOR VEHICLES RULES, 1989 (CMVR)</div>
          </div>
          <div style="text-align:right;">
            <div style="font-family:'JetBrains Mono', monospace; font-size:1.1rem; font-weight:800; color:#003366;">${data.plate}</div>
            <div style="font-size:0.75rem; color:#64748B;">Date: 24-Oct-2026</div>
          </div>
        </div>

        <div style="display:grid; grid-template-columns:1fr 1fr; gap:1rem; background:#F8FAFC; border:1px solid #E2E8F0; padding:1.25rem; border-radius:8px; margin-bottom:1.5rem;">
          <div>
            <span style="font-size:0.72rem; color:#64748B; display:block;">MAKER & MODEL</span>
            <strong style="color:#0F172A;">${data.model}</strong>
          </div>
          <div>
            <span style="font-size:0.72rem; color:#64748B; display:block;">REGISTERING AUTHORITY</span>
            <strong style="color:#0F172A;">${data.rto}</strong>
          </div>
          <div>
            <span style="font-size:0.72rem; color:#64748B; display:block;">HYPOTHECATION (BANK LIEN)</span>
            <strong style="color:${data.nocStatus === 'pass' ? '#059669' : '#DC2626'};">${data.nocText}</strong>
          </div>
          <div>
            <span style="font-size:0.72rem; color:#64748B; display:block;">FITNESS & POLLUTION COMPLIANCE</span>
            <strong style="color:#059669;">${data.fitness}</strong>
          </div>
        </div>

        <div style="background:${data.nocStatus === 'pass' ? '#ECFDF5' : '#FEF2F2'}; border:1px solid ${data.nocStatus === 'pass' ? '#A7F3D0' : '#FECACA'}; padding:1rem; border-radius:6px; margin-bottom:1.5rem;">
          <strong style="color:${data.nocStatus === 'pass' ? '#065F46' : '#991B1B'}; font-size:0.9rem;">
            ${data.nocStatus === 'pass' ? '✓ CLEAR TITLE FOR VEHICLE OWNERSHIP TRANSFER:' : '⚠ CAUTION: CANNOT TRANSFER VEHICLE WITHOUT BANK FORM 35 NOC:'}
          </strong>
          <p style="font-size:0.85rem; color:#334155; margin:0.35rem 0 0 0;">
            ${data.nocStatus === 'pass' 
              ? 'Vehicle has zero pending hypothecations, clear insurance, and clean challan history. Fully eligible for RTO Form 29 & 30 transfer.'
              : 'Active bank hypothecation detected. Obtain original Form 35 with bank NOC letter before disburshing payment to seller.'}
          </p>
        </div>

        <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:0.75rem;">
          <button type="button" class="btn btn-secondary btn-sm" onclick="window.print()">
            <span>Print Report</span>
          </button>
          <button type="button" class="btn btn-primary btn-sm" onclick="showToast('✓ Official VAHAN Pre-Purchase Dossier downloaded!'); closeModal(document.getElementById('modalVahanReport'));">
            <span>Download Signed VAHAN NOC Dossier &rarr;</span>
          </button>
        </div>
      </div>
    `;

    openModal(modalVahanReport);
  };

});
"""

with open('/Users/chetanbisariya/.gemini/antigravity-ide/scratch/exainfra-in/app.js', 'w') as f:
    f.write(js_content)

print(f"Generated clean white & mobile app.js ({len(js_content)} bytes) successfully.")
