import json

with open('/Users/chetanbisariya/.gemini/antigravity-ide/scratch/exainfra-in/direct_owner_apartments.json') as f:
    apartments_data = json.load(f)

apartments_json_str = json.dumps(apartments_data, indent=2)

js_content = f"""/**
 * ExaInfra Rentals & SaaS (exainfra.in) - Unified Engine
 * Direct Owner Rentals, Landlord & PG Management SaaS, and Legal Lease & Tax Studio
 */

document.addEventListener('DOMContentLoaded', () => {{

  // ====================================================================
  // 1. Direct Owner Verified Apartments Dataset
  // ====================================================================
  let defaultApartments = {apartments_json_str};

  let apartments = JSON.parse(localStorage.getItem('exainfra_owner_apartments_v6')) || defaultApartments;

  function saveApartments() {{
    localStorage.setItem('exainfra_owner_apartments_v6', JSON.stringify(apartments));
  }}

  // ====================================================================
  // 2. User State & Quota Management (5 Free Postings, 20 Free Inquiries)
  // ====================================================================
  let userState = JSON.parse(localStorage.getItem('exainfra_user_state_v6')) || {{
    role: 'tenant', // 'tenant' or 'landlord'
    tenant: {{
      name: 'Aditya Saxena',
      phone: '',
      email: 'aditya@tenant.com',
      inquiriesLeft: 20,
      inquiriesTotal: 20,
      isPro: false
    }},
    landlord: {{
      name: 'Anand Deshmukh',
      phone: '',
      email: 'anand@landlord.com',
      listingsLeft: 5,
      listingsTotal: 5,
      isPro: false
    }},
    savedSearches: [
      {{
        id: 's-1',
        title: '2-3 BHK in Bellandur / ORR under ₹55k',
        date: '23 Oct 2026',
        city: 'Bengaluru',
        bhk: '2 BHK, 3 BHK',
        budget: '₹55,000',
        matches: 4
      }}
    ],
    chatConversations: {{}},
    confirmedBookings: []
  }};

  function saveUserState() {{
    localStorage.setItem('exainfra_user_state_v6', JSON.stringify(userState));
    updateUserNavUI();
  }}

  function updateUserNavUI() {{
    const roleBadge = document.getElementById('userRoleNavBadge');
    const quotaText = document.getElementById('userQuotaNavText');
    const btnSwitchRole = document.getElementById('btnSwitchRoleNav');

    if (userState.role === 'tenant') {{
      if (roleBadge) {{
        roleBadge.textContent = userState.tenant.isPro ? 'TENANT PRO' : 'TENANT';
        roleBadge.className = userState.tenant.isPro ? 'nav-badge-pro' : 'nav-badge-tenant';
      }}
      if (quotaText) {{
        if (userState.tenant.isPro) {{
          quotaText.innerHTML = '⚡ <strong>Unlimited Inquiries</strong> (Freedom Pass)';
        }} else {{
          quotaText.innerHTML = `💬 <strong>${{userState.tenant.inquiriesLeft}}/${{userState.tenant.inquiriesTotal}}</strong> Free Inquiries Left`;
        }}
      }}
      if (btnSwitchRole) {{
        btnSwitchRole.textContent = 'Switch to Landlord View ➔';
      }}
    }} else {{
      if (roleBadge) {{
        roleBadge.textContent = userState.landlord.isPro ? 'LANDLORD PRO' : 'LANDLORD';
        roleBadge.className = userState.landlord.isPro ? 'nav-badge-pro' : 'nav-badge-landlord';
      }}
      if (quotaText) {{
        if (userState.landlord.isPro) {{
          quotaText.innerHTML = '🌟 <strong>Unlimited Postings</strong> (Pro SaaS Active)';
        }} else {{
          quotaText.innerHTML = `🏠 <strong>${{userState.landlord.listingsLeft}}/${{userState.landlord.listingsTotal}}</strong> Free Postings Left`;
        }}
      }}
      if (btnSwitchRole) {{
        btnSwitchRole.textContent = 'Switch to Tenant View ➔';
      }}
    }}
  }}

  updateUserNavUI();

  // Role Switcher Button
  const btnSwitchRoleNav = document.getElementById('btnSwitchRoleNav');
  if (btnSwitchRoleNav) {{
    btnSwitchRoleNav.addEventListener('click', (e) => {{
      e.preventDefault();
      userState.role = userState.role === 'tenant' ? 'landlord' : 'tenant';
      saveUserState();
      showToast(`Switched to ${{userState.role.toUpperCase()}} Mode!`);
    }});
  }}

  // ====================================================================
  // 3. Search & Filtering State
  // ====================================================================
  const activeFilters = {{
    city: 'Bengaluru',
    locality: 'all',
    bhk: 'all',
    furnishing: 'all',
    maxBudget: 150000,
    amenity: 'all',
    sort: 'featured'
  }};

  const apartmentsGrid = document.getElementById('apartmentsGrid');
  const searchResultCount = document.getElementById('searchResultCount');
  const emptyListingsState = document.getElementById('emptyListingsState');
  const filterCity = document.getElementById('filterCity');
  const filterBhk = document.getElementById('filterBhk');
  const filterFurnishing = document.getElementById('filterFurnishing');
  const filterMaxBudget = document.getElementById('filterMaxBudget');
  const budgetChipDisplay = document.getElementById('budgetChipDisplay');
  const sortResults = document.getElementById('sortResults');
  const btnResetFilters = document.getElementById('btnResetFilters');
  const btnResetEmptySearch = document.getElementById('btnResetEmptySearch');
  const btnExecuteSearch = document.getElementById('btnExecuteSearch');
  const bangaloreLocalityChips = document.querySelectorAll('#bangaloreLocalityChips .loc-chip');
  const amenityChips = document.querySelectorAll('.amenity-chip');

  function formatINR(number) {{
    return '₹' + number.toLocaleString('en-IN');
  }}

  function renderApartments() {{
    if (!apartmentsGrid) return;

    let filtered = apartments.filter(apt => {{
      // City filter
      if (activeFilters.city !== 'all' && apt.city.toLowerCase() !== activeFilters.city.toLowerCase()) {{
        return false;
      }}
      // Locality filter
      if (activeFilters.locality && activeFilters.locality !== 'all') {{
        const locLower = activeFilters.locality.toLowerCase();
        const matchesLoc = (apt.locality && apt.locality.toLowerCase().includes(locLower)) ||
                           (apt.title && apt.title.toLowerCase().includes(locLower)) ||
                           (apt.society && apt.society.toLowerCase().includes(locLower));
        if (!matchesLoc) {{
          return false;
        }}
      }}
      // BHK filter
      if (activeFilters.bhk !== 'all' && apt.bhk !== activeFilters.bhk) {{
        return false;
      }}
      // Furnishing filter
      if (activeFilters.furnishing !== 'all' && apt.furnishing !== activeFilters.furnishing) {{
        return false;
      }}
      // Budget filter
      if (apt.rent > activeFilters.maxBudget) {{
        return false;
      }}
      // Amenity filter
      if (activeFilters.amenity !== 'all') {{
        if (!apt.amenities.includes(activeFilters.amenity)) {{
          return false;
        }}
      }}
      return true;
    }});

    // Sorting
    if (activeFilters.sort === 'featured') {{
      filtered.sort((a, b) => (b.spotlight ? 1 : 0) - (a.spotlight ? 1 : 0));
    }} else if (activeFilters.sort === 'price-low') {{
      filtered.sort((a, b) => a.rent - b.rent);
    }} else if (activeFilters.sort === 'price-high') {{
      filtered.sort((a, b) => b.rent - a.rent);
    }} else if (activeFilters.sort === 'newest') {{
      filtered.sort((a, b) => a.postedDaysAgo - b.postedDaysAgo);
    }}

    if (searchResultCount) {{
      searchResultCount.textContent = filtered.length;
    }}

    if (filtered.length === 0) {{
      apartmentsGrid.style.display = 'none';
      if (emptyListingsState) emptyListingsState.style.display = 'block';
      return;
    }}

    apartmentsGrid.style.display = 'grid';
    if (emptyListingsState) emptyListingsState.style.display = 'none';

    apartmentsGrid.innerHTML = filtered.map(apt => {{
      const spotlightBadge = apt.spotlight ? `<span class="spotlight-badge">★ Spotlight</span>` : '';
      const reservedBadge = apt.isReserved ? `<span class="reserved-badge">🔒 Reserved</span>` : '';

      const amenitiesHtml = apt.amenities.slice(0, 3).map(am => {{
        let label = am.toUpperCase();
        if (am === 'gym') label = 'Fitness Gym';
        if (am === 'pool') label = 'Pool';
        if (am === 'pets') label = 'Pet Friendly';
        if (am === 'gated') label = '24/7 Gated';
        return `<span class="amenity-tag">${{label}}</span>`;
      }}).join('');

      return `
        <div class="apt-card-clean" data-id="${{apt.id}}">
          <div class="apt-img-box" onclick="window.openApartmentDetailModal('${{apt.id}}')">
            <img src="${{apt.image}}" alt="${{apt.title}}" class="apt-img" loading="lazy" decoding="async" onerror="this.onerror=null; this.src='https://images.unsplash.com/photo-1545324418-cc1a3fa10c00?auto=format&fit=crop&w=800&q=80';">
            
            <div class="card-source-badge-wrap">
              <span class="portal-source-pill exadirect">🟢 Direct Owner Verified</span>
              <span class="zero-broker-pill">ZERO BROKERAGE</span>
            </div>

            <div class="card-top-badges">
              ${{spotlightBadge}}
              ${{reservedBadge}}
            </div>

            <div class="photo-count-pill">📷 ${{apt.photoCount || 10}} Photos</div>
          </div>

          <div class="apt-card-body-clean">
            <div class="apt-financials-row">
              <div class="apt-rent-clean">${{formatINR(apt.rent)}} <span>/ month</span></div>
              <div class="apt-deposit-clean">Deposit: <strong>${{formatINR(apt.deposit)}}</strong></div>
            </div>

            <h3 class="apt-society-title" onclick="window.openApartmentDetailModal('${{apt.id}}')">
              ${{apt.title}}
            </h3>

            <div class="apt-location-clean">
              <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path><circle cx="12" cy="10" r="3"></circle></svg>
              <span>${{apt.locality}}, ${{apt.city}}</span>
            </div>

            <div class="apt-specs-strip">
              <div class="spec-block">
                <span>CONFIG</span>
                <strong>${{apt.bhk}}</strong>
              </div>
              <div class="spec-block">
                <span>FURNISHING</span>
                <strong>${{apt.furnishing}}</strong>
              </div>
              <div class="spec-block">
                <span>CARPET AREA</span>
                <strong>${{apt.area}} sq.ft</strong>
              </div>
            </div>

            <div class="apt-amenities-row">
              ${{amenitiesHtml}}
            </div>

            <div class="apt-owner-tagline">
              <span>Owner: <strong>${{apt.owner.name}}</strong></span>
              <span class="owner-verified-tag">✓ Direct Owner Verified</span>
            </div>

            <div class="direct-owner-actions-grid">
              <button class="btn btn-outline-clean btn-sm btn-action-chat" data-id="${{apt.id}}" title="Direct In-App Chat with Landlord">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"></path></svg>
                <span>Chat</span>
              </button>

              <button class="btn btn-outline-clean btn-sm btn-action-visit" data-id="${{apt.id}}" title="Schedule a Physical or Video Property Tour">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect><line x1="16" y1="2" x2="16" y2="6"></line><line x1="8" y1="2" x2="8" y2="6"></line><line x1="3" y1="10" x2="21" y2="10"></line></svg>
                <span>Visit</span>
              </button>

              <button class="btn btn-primary-clean btn-sm btn-action-confirm" data-id="${{apt.id}}" title="Confirm & Reserve with Refundable ₹10K Token">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M21 2l-2 2m-2-2l2 2M3 13l2-2m-2 2l2 2m7-9a4 4 0 1 1 0 8 4 4 0 0 1 0-8z"></path></svg>
                <span>Reserve</span>
              </button>
            </div>
          </div>
        </div>
      `;
    }}).join('');

    // Attach card action listeners
    document.querySelectorAll('.btn-action-chat').forEach(btn => {{
      btn.addEventListener('click', (e) => {{
        e.stopPropagation();
        const aptId = e.currentTarget.getAttribute('data-id');
        openInAppChatModal(aptId);
      }});
    }});

    document.querySelectorAll('.btn-action-visit').forEach(btn => {{
      btn.addEventListener('click', (e) => {{
        e.stopPropagation();
        const aptId = e.currentTarget.getAttribute('data-id');
        openApartmentDetailModal(aptId);
      }});
    }});

    document.querySelectorAll('.btn-action-confirm').forEach(btn => {{
      btn.addEventListener('click', (e) => {{
        e.stopPropagation();
        const aptId = e.currentTarget.getAttribute('data-id');
        openConfirmRentalModal(aptId);
      }});
    }});
  }}

  // Locality Chips
  bangaloreLocalityChips.forEach(chip => {{
    chip.addEventListener('click', () => {{
      bangaloreLocalityChips.forEach(c => c.classList.remove('active'));
      chip.classList.add('active');
      activeFilters.locality = chip.getAttribute('data-locality');
      renderApartments();
      const el = document.getElementById('explore-apartments');
      if (el) el.scrollIntoView({{ behavior: 'smooth' }});
    }});
  }});

  // Budget Slider
  if (filterMaxBudget && budgetChipDisplay) {{
    filterMaxBudget.addEventListener('input', () => {{
      activeFilters.maxBudget = parseInt(filterMaxBudget.value, 10);
      budgetChipDisplay.textContent = formatINR(activeFilters.maxBudget) + ' / mo';
    }});
  }}

  // Filter Dropdowns
  if (filterCity) {{
    filterCity.addEventListener('change', () => {{
      const chosen = filterCity.value;
      if (chosen !== 'Bengaluru' && chosen !== 'all') {{
        openCityComingSoonModal(chosen);
        filterCity.value = 'Bengaluru';
        activeFilters.city = 'Bengaluru';
      }} else {{
        activeFilters.city = chosen;
      }}
      renderApartments();
    }});
  }}

  if (filterBhk) {{
    filterBhk.addEventListener('change', () => {{
      activeFilters.bhk = filterBhk.value;
      renderApartments();
    }});
  }}

  if (filterFurnishing) {{
    filterFurnishing.addEventListener('change', () => {{
      activeFilters.furnishing = filterFurnishing.value;
      renderApartments();
    }});
  }}

  if (sortResults) {{
    sortResults.addEventListener('change', () => {{
      activeFilters.sort = sortResults.value;
      renderApartments();
    }});
  }}

  // Amenity Chips
  amenityChips.forEach(chip => {{
    chip.addEventListener('click', () => {{
      if (chip.classList.contains('active')) {{
        chip.classList.remove('active');
        activeFilters.amenity = 'all';
      }} else {{
        amenityChips.forEach(c => c.classList.remove('active'));
        chip.classList.add('active');
        activeFilters.amenity = chip.getAttribute('data-amenity');
      }}
      renderApartments();
    }});
  }});

  // Search Buttons
  if (btnExecuteSearch) {{
    btnExecuteSearch.addEventListener('click', () => {{
      renderApartments();
      const el = document.getElementById('explore-apartments');
      if (el) el.scrollIntoView({{ behavior: 'smooth' }});
      showToast(`Showing ${{searchResultCount.textContent}} verified direct owner properties!`);
    }});
  }}

  if (btnResetFilters) {{
    btnResetFilters.addEventListener('click', resetAllFilters);
  }}

  if (btnResetEmptySearch) {{
    btnResetEmptySearch.addEventListener('click', resetAllFilters);
  }}

  function resetAllFilters() {{
    activeFilters.city = 'Bengaluru';
    activeFilters.locality = 'all';
    activeFilters.bhk = 'all';
    activeFilters.furnishing = 'all';
    activeFilters.maxBudget = 150000;
    activeFilters.amenity = 'all';
    activeFilters.sort = 'featured';

    if (filterCity) filterCity.value = 'Bengaluru';
    if (filterBhk) filterBhk.value = 'all';
    if (filterFurnishing) filterFurnishing.value = 'all';
    if (filterMaxBudget) filterMaxBudget.value = '150000';
    if (budgetChipDisplay) budgetChipDisplay.textContent = '₹1,50,000 / mo';
    if (sortResults) sortResults.value = 'featured';

    bangaloreLocalityChips.forEach(c => {{
      if (c.getAttribute('data-locality') === 'all') c.classList.add('active');
      else c.classList.remove('active');
    }});

    amenityChips.forEach(c => c.classList.remove('active'));

    renderApartments();
    showToast('Filters reset to All Direct Owner Listings');
  }}

  // Initial Render
  renderApartments();

  // ====================================================================
  // 4. Modal Helpers & System
  // ====================================================================
  function openModal(modal) {{
    if (!modal) return;
    modal.classList.add('active');
    document.body.style.overflow = 'hidden';
  }}

  function closeModal(modal) {{
    if (!modal) return;
    modal.classList.remove('active');
    document.body.style.overflow = '';
  }}

  document.querySelectorAll('.modal-backdrop').forEach(backdrop => {{
    backdrop.addEventListener('click', (e) => {{
      if (e.target === backdrop) {{
        closeModal(backdrop);
      }}
    }});
  }});

  // ====================================================================
  // 5. Direct In-App Chat with Landlord (20 Free Inquiries Enforced)
  // ====================================================================
  let activeChatApt = null;
  const modalInAppChat = document.getElementById('modalInAppChat');
  const chatOwnerAvatar = document.getElementById('chatOwnerAvatar');
  const chatLandlordName = document.getElementById('chatLandlordName');
  const chatAptSnippet = document.getElementById('chatAptSnippet');
  const chatFreeQuotaText = document.getElementById('chatFreeQuotaText');
  const chatMessagesThread = document.getElementById('chatMessagesThread');
  const formSendChatMessage = document.getElementById('formSendChatMessage');
  const chatInputText = document.getElementById('chatInputText');
  const quickInquiryChips = document.getElementById('quickInquiryChips');
  const btnScheduleVisitFromChat = document.getElementById('btnScheduleVisitFromChat');
  const btnConfirmRentalFromChat = document.getElementById('btnConfirmRentalFromChat');
  const closeModalChat = document.getElementById('closeModalChat');

  if (closeModalChat) {{
    closeModalChat.addEventListener('click', () => closeModal(modalInAppChat));
  }}

  function openInAppChatModal(aptId) {{
    const apt = apartments.find(a => a.id === aptId);
    if (!apt) return;

    // Check Tenant Quota
    if (!userState.tenant.isPro && userState.tenant.inquiriesLeft <= 0) {{
      openQuotaUpgradeModal('tenant');
      return;
    }}

    activeChatApt = apt;

    // Init chat thread if not exists
    if (!userState.chatConversations[apt.id]) {{
      userState.chatConversations[apt.id] = [
        {{
          sender: 'landlord',
          time: 'Just now',
          text: `Namaste! I am ${{apt.owner.name}}, owner of the ${{apt.bhk}} in ${{apt.society}}. Feel free to ask about rent terms, deposit, or schedule a visit!`
        }}
      ];
      // Decrement inquiry quota on first new conversation
      if (!userState.tenant.isPro) {{
        userState.tenant.inquiriesLeft = Math.max(0, userState.tenant.inquiriesLeft - 1);
        saveUserState();
      }}
    }}

    if (chatOwnerAvatar) {{
      const initials = apt.owner.name.split(' ').map(n => n[0]).join('').substring(0, 2).toUpperCase();
      chatOwnerAvatar.textContent = initials || 'LL';
    }}
    if (chatLandlordName) chatLandlordName.textContent = apt.owner.name;
    if (chatAptSnippet) chatAptSnippet.innerHTML = `<strong>${{apt.society}}</strong> &bull; ${{formatINR(apt.rent)}}/mo &bull; Replies within 10 mins`;

    if (chatFreeQuotaText) {{
      if (userState.tenant.isPro) {{
        chatFreeQuotaText.textContent = 'Unlimited (Pro)';
        chatFreeQuotaText.className = 'text-green';
      }} else {{
        chatFreeQuotaText.textContent = `${{userState.tenant.inquiriesLeft}}/${{userState.tenant.inquiriesTotal}} Left`;
        chatFreeQuotaText.className = userState.tenant.inquiriesLeft <= 3 ? 'text-coral' : 'text-green';
      }}
    }}

    renderChatMessages();
    openModal(modalInAppChat);
  }}

  function renderChatMessages() {{
    if (!chatMessagesThread || !activeChatApt) return;
    const thread = userState.chatConversations[activeChatApt.id] || [];
    
    chatMessagesThread.innerHTML = thread.map(msg => `
      <div class="chat-bubble-clean ${{msg.sender === 'user' ? 'outgoing' : 'incoming'}}">
        <div class="bubble-body">${{msg.text}}</div>
        <div class="bubble-meta">${{msg.time || 'Today'}}</div>
      </div>
    `).join('');

    chatMessagesThread.scrollTop = chatMessagesThread.scrollHeight;
  }}

  if (formSendChatMessage) {{
    formSendChatMessage.addEventListener('submit', (e) => {{
      e.preventDefault();
      const text = chatInputText.value.trim();
      if (!text || !activeChatApt) return;

      // Add user message
      userState.chatConversations[activeChatApt.id].push({{
        sender: 'user',
        time: 'Just now',
        text: text
      }});
      chatInputText.value = '';
      renderChatMessages();
      saveUserState();

      // Landlord simulated reply after 800ms
      setTimeout(() => {{
        let reply = "Thank you for reaching out! Yes, you are welcome to visit the flat. Would this Saturday or Sunday morning work for you?";
        if (text.toLowerCase().includes('bachelor') || text.toLowerCase().includes('family')) {{
          reply = "Yes, bachelors and working IT professionals are completely welcome. We maintain a friendly, peaceful gated community.";
        }} else if (text.toLowerCase().includes('deposit') || text.toLowerCase().includes('negotiable')) {{
          reply = "The security deposit is set at standard terms, but we can finalize slightly flexible payment options upon in-person discussion.";
        }} else if (text.toLowerCase().includes('move-in') || text.toLowerCase().includes('immediate')) {{
          reply = "The apartment is ready for immediate move-in! Deep cleaning and painting have already been completed.";
        }}

        if (userState.chatConversations[activeChatApt.id]) {{
          userState.chatConversations[activeChatApt.id].push({{
            sender: 'landlord',
            time: 'Just now',
            text: reply
          }});
          renderChatMessages();
          saveUserState();
        }}
      }}, 850);
    }});
  }}

  if (quickInquiryChips) {{
    quickInquiryChips.querySelectorAll('.quick-chip-clean').forEach(chip => {{
      chip.addEventListener('click', () => {{
        const msg = chip.getAttribute('data-msg');
        if (chatInputText) {{
          chatInputText.value = msg;
          chatInputText.focus();
        }}
      }});
    }});
  }}

  if (btnScheduleVisitFromChat) {{
    btnScheduleVisitFromChat.addEventListener('click', () => {{
      closeModal(modalInAppChat);
      if (activeChatApt) {{
        openApartmentDetailModal(activeChatApt.id);
      }}
    }});
  }}

  if (btnConfirmRentalFromChat) {{
    btnConfirmRentalFromChat.addEventListener('click', () => {{
      closeModal(modalInAppChat);
      if (activeChatApt) {{
        openConfirmRentalModal(activeChatApt.id);
      }}
    }});
  }}

  // ====================================================================
  // 6. Apartment Detail & Visit Scheduler Modal
  // ====================================================================
  const modalApartmentDetail = document.getElementById('modalApartmentDetail');
  const detailModalContent = document.getElementById('detailModalContent');
  const closeModalDetail = document.getElementById('closeModalDetail');

  if (closeModalDetail) {{
    closeModalDetail.addEventListener('click', () => closeModal(modalApartmentDetail));
  }}

  window.openApartmentDetailModal = function(aptId) {{
    const apt = apartments.find(a => a.id === aptId);
    if (!apt || !detailModalContent) return;

    detailModalContent.innerHTML = `
      <div class="detail-header-clean">
        <div class="detail-title-col">
          <span class="source-tag-pill" style="background:#ECFDF5; color:#059669; font-weight:700;">🟢 Direct Owner Verified</span>
          <h2 style="font-size:1.5rem; font-weight:800; color:#0F172A; margin:0.4rem 0;">${{apt.title}}</h2>
          <p style="color:#64748B; font-size:0.9rem;">📍 ${{apt.locality}}, ${{apt.city}}</p>
        </div>
        <div class="detail-pricing-box">
          <div style="font-size:1.6rem; font-weight:800; color:#E11D48;">${{formatINR(apt.rent)}} <span style="font-size:0.85rem; color:#64748B;">/ month</span></div>
          <div style="font-size:0.85rem; color:#475569;">Deposit: <strong>${{formatINR(apt.deposit)}}</strong></div>
        </div>
      </div>

      <div class="detail-hero-media">
        <img src="${{apt.image}}" alt="${{apt.title}}" style="width:100%; height:320px; object-fit:cover; border-radius:12px;" onerror="this.onerror=null; this.src='https://images.unsplash.com/photo-1545324418-cc1a3fa10c00?auto=format&fit=crop&w=800&q=80';">
      </div>

      <div class="detail-specs-grid" style="display:grid; grid-template-columns:repeat(auto-fit, minmax(130px, 1fr)); gap:0.75rem; margin:1.25rem 0;">
        <div class="spec-tile" style="background:#F8FAFC; border:1px solid #E2E8F0; padding:0.75rem; border-radius:8px; text-align:center;">
          <span style="font-size:0.75rem; color:#64748B; display:block;">CONFIGURATION</span>
          <strong style="color:#0F172A;">${{apt.bhk}}</strong>
        </div>
        <div class="spec-tile" style="background:#F8FAFC; border:1px solid #E2E8F0; padding:0.75rem; border-radius:8px; text-align:center;">
          <span style="font-size:0.75rem; color:#64748B; display:block;">SUPER AREA</span>
          <strong style="color:#0F172A;">${{apt.area}} sq.ft</strong>
        </div>
        <div class="spec-tile" style="background:#F8FAFC; border:1px solid #E2E8F0; padding:0.75rem; border-radius:8px; text-align:center;">
          <span style="font-size:0.75rem; color:#64748B; display:block;">FURNISHING</span>
          <strong style="color:#0F172A;">${{apt.furnishing}}</strong>
        </div>
        <div class="spec-tile" style="background:#F8FAFC; border:1px solid #E2E8F0; padding:0.75rem; border-radius:8px; text-align:center;">
          <span style="font-size:0.75rem; color:#64748B; display:block;">AVAILABILITY</span>
          <strong style="color:#059669;">${{apt.availableFrom || 'Immediately'}}</strong>
        </div>
      </div>

      <div class="detail-owner-strip" style="background:#F0FDF4; border:1px solid #BBF7D0; padding:1rem; border-radius:10px; display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:0.75rem; margin-bottom:1.5rem;">
        <div>
          <span style="font-size:0.75rem; color:#166534; font-weight:700;">DIRECT OWNER</span>
          <h4 style="margin:0.2rem 0; color:#14532D; font-size:1.1rem;">${{apt.owner.name}}</h4>
          <span style="font-size:0.85rem; color:#166534;">Verified Phone: ${{apt.owner.phone}}</span>
        </div>
        <div style="display:flex; gap:0.5rem;">
          <button class="btn btn-secondary btn-sm" onclick="closeModal(document.getElementById('modalApartmentDetail')); openInAppChatModal('${{apt.id}}')">
            <span>💬 Chat with Owner</span>
          </button>
          <button class="btn btn-primary btn-sm" onclick="closeModal(document.getElementById('modalApartmentDetail')); openConfirmRentalModal('${{apt.id}}')">
            <span>🔑 Reserve Flat</span>
          </button>
        </div>
      </div>

      <div class="visit-scheduler-box" style="background:#F8FAFC; border:1px solid #E2E8F0; padding:1.25rem; border-radius:12px;">
        <h4 style="margin:0 0 0.5rem 0; font-size:1.05rem; font-weight:800; color:#0F172A;">Schedule Direct Property Visit</h4>
        <p style="font-size:0.85rem; color:#64748B; margin-bottom:1rem;">Select your preferred date & time slot. The owner will confirm the appointment directly via WhatsApp.</p>

        <form id="formScheduleDetailVisit">
          <div style="display:grid; grid-template-columns:1fr 1fr; gap:0.75rem; margin-bottom:0.75rem;">
            <div>
              <label style="font-size:0.8rem; font-weight:600; color:#475569; display:block; margin-bottom:0.25rem;">Visit Date *</label>
              <input type="date" id="visDate" class="form-control-clean" required min="${{new Date().toISOString().split('T')[0]}}">
            </div>
            <div>
              <label style="font-size:0.8rem; font-weight:600; color:#475569; display:block; margin-bottom:0.25rem;">Time Window *</label>
              <select id="visTime" class="form-control-clean">
                <option value="Morning (10:00 AM - 12:30 PM)">Morning (10:00 AM - 12:30 PM)</option>
                <option value="Afternoon (02:00 PM - 04:30 PM)">Afternoon (02:00 PM - 04:30 PM)</option>
                <option value="Evening (05:00 PM - 07:30 PM)" selected>Evening (05:00 PM - 07:30 PM)</option>
              </select>
            </div>
          </div>

          <div style="display:grid; grid-template-columns:1fr 1fr; gap:0.75rem; margin-bottom:1rem;">
            <div>
              <label style="font-size:0.8rem; font-weight:600; color:#475569; display:block; margin-bottom:0.25rem;">Tour Type</label>
              <select id="visType" class="form-control-clean">
                <option value="In-Person Physical Visit" selected>In-Person Physical Visit</option>
                <option value="WhatsApp Video Call Walkthrough">WhatsApp Video Call Walkthrough</option>
              </select>
            </div>
            <div>
              <label style="font-size:0.8rem; font-weight:600; color:#475569; display:block; margin-bottom:0.25rem;">Tentative Move-in Date</label>
              <input type="date" id="visMoveIn" class="form-control-clean">
            </div>
          </div>

          <button type="submit" class="btn btn-primary btn-full">
            <span>Confirm Visit Request & Notify Landlord &rarr;</span>
          </button>
        </form>
      </div>
    `;

    openModal(modalApartmentDetail);

    const formScheduleDetailVisit = document.getElementById('formScheduleDetailVisit');
    if (formScheduleDetailVisit) {{
      formScheduleDetailVisit.addEventListener('submit', (e) => {{
        e.preventDefault();
        const vDate = document.getElementById('visDate').value;
        const vTime = document.getElementById('visTime').value;
        const vType = document.getElementById('visType').value;

        closeModal(modalApartmentDetail);
        showToast(`📅 Visit Confirmed! ${{apt.owner.name}} notified for ${{vDate}} (${{vTime}}) via ${{vType}}.`);
      }});
    }}
  }};

  // ====================================================================
  // 7. Confirm Rental Property & Lock-in Token Modal
  // ====================================================================
  const modalConfirmProperty = document.getElementById('modalConfirmProperty');
  const confirmAptTitle = document.getElementById('confirmAptTitle');
  const confMonthlyRent = document.getElementById('confMonthlyRent');
  const confSecurityDeposit = document.getElementById('confSecurityDeposit');
  const formConfirmRental = document.getElementById('formConfirmRental');
  const confirmFormState = document.getElementById('confirmFormState');
  const confirmSuccessState = document.getElementById('confirmSuccessState');
  const certBookingCode = document.getElementById('certBookingCode');
  const certMoveInDate = document.getElementById('certMoveInDate');
  const closeModalConfirm = document.getElementById('closeModalConfirm');
  const btnGoToAgreementFromConfirm = document.getElementById('btnGoToAgreementFromConfirm');

  let activeConfirmApt = null;

  if (closeModalConfirm) {{
    closeModalConfirm.addEventListener('click', () => closeModal(modalConfirmProperty));
  }}

  function openConfirmRentalModal(aptId) {{
    const apt = apartments.find(a => a.id === aptId);
    if (!apt) return;

    activeConfirmApt = apt;
    if (confirmAptTitle) confirmAptTitle.textContent = `${{apt.society}} — ${{apt.title}}`;
    if (confMonthlyRent) confMonthlyRent.textContent = `${{formatINR(apt.rent)}} / mo`;
    if (confSecurityDeposit) confSecurityDeposit.textContent = formatINR(apt.deposit);

    if (confirmFormState) confirmFormState.style.display = 'block';
    if (confirmSuccessState) confirmSuccessState.style.display = 'none';

    // Set default move-in date to next month 1st
    const confMoveInDate = document.getElementById('confMoveInDate');
    if (confMoveInDate) {{
      const d = new Date();
      d.setMonth(d.getMonth() + 1);
      d.setDate(1);
      confMoveInDate.value = d.toISOString().split('T')[0];
    }}

    openModal(modalConfirmProperty);
  }}

  if (formConfirmRental) {{
    formConfirmRental.addEventListener('submit', (e) => {{
      e.preventDefault();
      if (!activeConfirmApt) return;

      const code = 'EXA-RENT-' + Math.floor(100000 + Math.random() * 900000);
      const moveIn = document.getElementById('confMoveInDate').value;

      activeConfirmApt.isReserved = true;
      saveApartments();
      renderApartments();

      userState.confirmedBookings.push({{
        aptId: activeConfirmApt.id,
        bookingCode: code,
        moveInDate: moveIn,
        tokenPaid: 10000
      }});
      saveUserState();

      if (confirmFormState) confirmFormState.style.display = 'none';
      if (confirmSuccessState) confirmSuccessState.style.display = 'block';
      if (certBookingCode) certBookingCode.textContent = code;
      if (certMoveInDate) certMoveInDate.textContent = moveIn;

      showToast(`🎉 Flat Reserved! Booking Token ₹10,000 processed in escrow.`);
    }});
  }}

  if (btnGoToAgreementFromConfirm) {{
    btnGoToAgreementFromConfirm.addEventListener('click', () => {{
      closeModal(modalConfirmProperty);
      const agrEl = document.getElementById('rental-agreement');
      if (agrEl) agrEl.scrollIntoView({{ behavior: 'smooth' }});
    }});
  }}

  // ====================================================================
  // 8. Landlord & PG Management SaaS Dashboard
  // ====================================================================
  const saasTabButtons = document.querySelectorAll('.saas-tab-btn');
  const saasPanes = {{
    rent: document.getElementById('saasTabRent'),
    leases: document.getElementById('saasTabLeases'),
    tickets: document.getElementById('saasTabTickets')
  }};

  saasTabButtons.forEach(btn => {{
    btn.addEventListener('click', () => {{
      saasTabButtons.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');

      const tabKey = btn.getAttribute('data-saas-tab');
      Object.keys(saasPanes).forEach(k => {{
        if (saasPanes[k]) {{
          saasPanes[k].style.display = (k === tabKey) ? 'block' : 'none';
        }}
      }});
    }});
  }});

  // Sneha Rao UPI Reminder Simulation
  const btnSendSnehaReminder = document.getElementById('btnSendSnehaReminder');
  if (btnSendSnehaReminder) {{
    btnSendSnehaReminder.addEventListener('click', () => {{
      btnSendSnehaReminder.innerHTML = `<span>Sent ✓</span>`;
      btnSendSnehaReminder.style.background = '#059669';
      btnSendSnehaReminder.disabled = true;

      showToast('💬 WhatsApp Rent Invoice with UPI link delivered to Sneha Rao ()');
    }});
  }}

  // Send WhatsApp Links to All Units
  const btnSimulateCollectAll = document.getElementById('btnSimulateCollectAll');
  if (btnSimulateCollectAll) {{
    btnSimulateCollectAll.addEventListener('click', () => {{
      btnSimulateCollectAll.innerHTML = `<span>Sending...</span>`;
      btnSimulateCollectAll.disabled = true;

      setTimeout(() => {{
        btnSimulateCollectAll.innerHTML = `<span>✓ Rent Links Sent to 4 Tenants</span>`;
        showToast('⚡ WhatsApp UPI payment links sent to all 4 tenant units!');
      }}, 900);
    }});
  }}

  // Maintenance Ticket Resolution
  const ticketCountBadge = document.getElementById('ticketCountBadge');
  window.resolveTicket = function(btn) {{
    const row = btn.closest('tr');
    if (row) {{
      const statusCell = row.children[4];
      if (statusCell) {{
        statusCell.innerHTML = `<span class="saas-badge-paid">✓ Resolved</span>`;
      }}
      btn.remove();
      if (ticketCountBadge) {{
        let count = parseInt(ticketCountBadge.textContent, 10) || 1;
        ticketCountBadge.textContent = Math.max(0, count - 1);
      }}
      showToast('✓ Maintenance ticket marked as Resolved!');
    }}
  }};

  // Log New Maintenance Issue
  const btnLogNewTicket = document.getElementById('btnLogNewTicket');
  const saasTicketsTableBody = document.getElementById('saasTicketsTableBody');
  if (btnLogNewTicket && saasTicketsTableBody) {{
    btnLogNewTicket.addEventListener('click', () => {{
      const issue = prompt("Enter tenant maintenance issue description:", "Balcony Geyser Heating Sensor Replacement");
      if (!issue) return;

      const newId = "TCK-" + Math.floor(800 + Math.random() * 100);
      const newRow = document.createElement('tr');
      newRow.innerHTML = `
        <td><strong>${{newId}}</strong></td>
        <td>UNIT-112 (Arjun)</td>
        <td>${{issue}}</td>
        <td>Today</td>
        <td><span class="saas-badge-due">⚙ In Progress</span></td>
        <td>
          <button class="btn btn-xs btn-primary" onclick="resolveTicket(this)">
            Mark Resolved ✓
          </button>
        </td>
      `;
      saasTicketsTableBody.prepend(newRow);
      if (ticketCountBadge) {{
        let count = parseInt(ticketCountBadge.textContent, 10) || 0;
        ticketCountBadge.textContent = count + 1;
      }}
      showToast(`✓ Ticket ${{newId}} created and assigned to vendor!`);
    }});
  }}

  // ====================================================================
  // 9. Legal Lease & Tax Studio (11-Month Leases & HRA Tax Receipts)
  // ====================================================================
  const btnToggleLeaseMode = document.getElementById('btnToggleLeaseMode');
  const btnToggleHraMode = document.getElementById('btnToggleHraMode');
  const studioLeaseView = document.getElementById('studioLeaseView');
  const studioHraView = document.getElementById('studioHraView');

  if (btnToggleLeaseMode && btnToggleHraMode) {{
    btnToggleLeaseMode.addEventListener('click', () => {{
      btnToggleLeaseMode.classList.add('active');
      btnToggleLeaseMode.style.background = 'var(--coral-500)';
      btnToggleLeaseMode.style.color = '#FFFFFF';

      btnToggleHraMode.classList.remove('active');
      btnToggleHraMode.style.background = 'none';
      btnToggleHraMode.style.color = '#475569';

      if (studioLeaseView) studioLeaseView.style.display = 'grid';
      if (studioHraView) studioHraView.style.display = 'none';
    }});

    btnToggleHraMode.addEventListener('click', () => {{
      btnToggleHraMode.classList.add('active');
      btnToggleHraMode.style.background = 'var(--coral-500)';
      btnToggleHraMode.style.color = '#FFFFFF';

      btnToggleLeaseMode.classList.remove('active');
      btnToggleLeaseMode.style.background = 'none';
      btnToggleLeaseMode.style.color = '#475569';

      if (studioLeaseView) studioLeaseView.style.display = 'none';
      if (studioHraView) studioHraView.style.display = 'grid';
    }});
  }}

  // 11-Month Lease Drafter Form
  const formAgreementDraft = document.getElementById('formAgreementDraft');
  const modalAgreementPreview = document.getElementById('modalAgreementPreview');
  const legalDocumentPaper = document.getElementById('legalDocumentPaper');
  const closeModalAgrPreview = document.getElementById('closeModalAgrPreview');
  const btnPrintAgreement = document.getElementById('btnPrintAgreement');
  const btnProceedAadhaarSign = document.getElementById('btnProceedAadhaarSign');

  if (closeModalAgrPreview) {{
    closeModalAgrPreview.addEventListener('click', () => closeModal(modalAgreementPreview));
  }}

  if (formAgreementDraft && legalDocumentPaper) {{
    formAgreementDraft.addEventListener('submit', (e) => {{
      e.preventDefault();

      const ownerName = document.getElementById('agrOwnerName').value;
      const tenantName = document.getElementById('agrTenantName').value;
      const propAddr = document.getElementById('agrPropertyAddress').value;
      const monthlyRent = parseInt(document.getElementById('agrMonthlyRent').value, 10);
      const deposit = parseInt(document.getElementById('agrDeposit').value, 10);
      const duration = document.getElementById('agrDuration').value;
      const notice = document.getElementById('agrNotice').value;

      legalDocumentPaper.innerHTML = `
        <div class="estamp-banner-clean">
          <div class="estamp-top-row">
            <div class="govt-seal">
              <strong>GOVERNMENT OF KARNATAKA</strong><br>
              <span>e-Stamp Certificate of Stamp Duty & Registration</span>
            </div>
            <div class="estamp-code">
              <strong>CERT NO: IN-KA29108420194098T</strong><br>
              <span>Stamp Duty Paid: ₹500.00 &bull; 24-Oct-2026</span>
            </div>
          </div>
          <div class="estamp-divider"></div>
          <div class="estamp-parties-row">
            <span>First Party: <strong>${{ownerName}}</strong> (Lessor)</span>
            <span>Second Party: <strong>${{tenantName}}</strong> (Lessee)</span>
          </div>
        </div>

        <div class="legal-body-text">
          <h3 style="text-align:center; text-transform:uppercase; font-size:1.25rem; font-weight:800; margin:1.5rem 0 1rem 0; letter-spacing:0.5px;">
            RESIDENTIAL RENTAL & LEASE AGREEMENT
          </h3>

          <p>
            THIS RESIDENTIAL LEASE AGREEMENT is made and entered into on this <strong>24th day of October 2026</strong>, by and between:
          </p>

          <p>
            <strong>${{ownerName}}</strong>, residing at Bangalore, Karnataka, hereinafter referred to as the <strong>"LESSOR" / OWNER</strong> (which expression shall include his/her legal heirs, successors and assigns) of the ONE PART;
          </p>
          <p style="text-align:center; font-weight:700;">- AND -</p>
          <p>
            <strong>${{tenantName}}</strong>, residing at Bangalore, Karnataka, hereinafter referred to as the <strong>"LESSEE" / TENANT</strong> (which expression shall include his/her legal heirs, successors and assigns) of the OTHER PART.
          </p>

          <h4 style="margin:1rem 0 0.5rem 0; font-size:1rem; font-weight:700; color:#0F172A;">1. SUBJECT PREMISES</h4>
          <p>The Lessor hereby lets out and the Lessee agrees to take on lease the premises situated at: <strong>${{propAddr}}</strong>.</p>

          <h4 style="margin:1rem 0 0.5rem 0; font-size:1rem; font-weight:700; color:#0F172A;">2. TENURE & LOCK-IN PERIOD</h4>
          <p>The lease shall be in effect for a tenure of <strong>${{duration}}</strong> commencing immediately. Both parties agree to a mandatory lock-in period of 3 months.</p>

          <h4 style="margin:1rem 0 0.5rem 0; font-size:1rem; font-weight:700; color:#0F172A;">3. MONTHLY RENT & UTILITIES</h4>
          <p>The Lessee shall pay to the Lessor a monthly rental of <strong>${{formatINR(monthlyRent)}}</strong> payable on or before the 5th day of every calendar month via UPI / Net Banking. Electricity and water consumption charges shall be paid directly by the Lessee.</p>

          <h4 style="margin:1rem 0 0.5rem 0; font-size:1rem; font-weight:700; color:#0F172A;">4. INTEREST-FREE SECURITY DEPOSIT</h4>
          <p>The Lessee has paid a sum of <strong>${{formatINR(deposit)}}</strong> as an interest-free refundable security deposit, refundable upon handover of keys subject to 1-month painting deduction.</p>

          <h4 style="margin:1rem 0 0.5rem 0; font-size:1rem; font-weight:700; color:#0F172A;">5. TERMINATION & NOTICE</h4>
          <p>Either party may terminate this agreement by providing a minimum of <strong>${{notice}}</strong> written notice.</p>

          <div class="legal-sign-grid" style="display:grid; grid-template-columns:1fr 1fr; gap:2rem; margin-top:2.5rem; padding-top:1.5rem; border-top:1px dashed #CBD5E1;">
            <div class="sign-col">
              <span style="font-size:0.8rem; color:#64748B;">LESSOR / OWNER SIGNATURE</span>
              <div style="font-family:'JetBrains Mono', monospace; font-size:1.1rem; color:#0F172A; margin:0.75rem 0 0.25rem 0; font-weight:700;">${{ownerName}}</div>
              <span style="font-size:0.75rem; color:#059669;">✓ Verified Direct Landlord Identity</span>
            </div>
            <div class="sign-col">
              <span style="font-size:0.8rem; color:#64748B;">LESSEE / TENANT SIGNATURE</span>
              <div style="font-family:'JetBrains Mono', monospace; font-size:1.1rem; color:#0F172A; margin:0.75rem 0 0.25rem 0; font-weight:700;">${{tenantName}}</div>
              <span style="font-size:0.75rem; color:#0284C7;">⏳ Ready for Aadhaar eSign</span>
            </div>
          </div>
        </div>
      `;

      openModal(modalAgreementPreview);
    }});
  }}

  if (btnPrintAgreement) {{
    btnPrintAgreement.addEventListener('click', () => {{
      window.print();
    }});
  }}

  if (btnProceedAadhaarSign) {{
    btnProceedAadhaarSign.addEventListener('click', () => {{
      btnProceedAadhaarSign.innerHTML = `<span>Simulating Aadhaar OTP...</span>`;
      btnProceedAadhaarSign.disabled = true;

      setTimeout(() => {{
        btnProceedAadhaarSign.innerHTML = `<span>✓ Agreement Digitally eSigned</span>`;
        btnProceedAadhaarSign.style.background = '#059669';
        showToast('🎉 Digital Lease Agreement successfully eSigned and E-Stamped!');
      }}, 1200);
    }});
  }}

  // 12-Month HRA Tax Receipts Generator
  const formHraGenerate = document.getElementById('formHraGenerate');
  const modalHraPreview = document.getElementById('modalHraPreview');
  const hraReceiptsContainer = document.getElementById('hraReceiptsContainer');
  const closeModalHraPreview = document.getElementById('closeModalHraPreview');
  const btnPrintHraReceipts = document.getElementById('btnPrintHraReceipts');

  if (closeModalHraPreview) {{
    closeModalHraPreview.addEventListener('click', () => closeModal(modalHraPreview));
  }}

  if (formHraGenerate && hraReceiptsContainer) {{
    formHraGenerate.addEventListener('submit', (e) => {{
      e.preventDefault();

      const tenant = document.getElementById('hraTenantName').value;
      const landlord = document.getElementById('hraLandlordName').value;
      const rentAmt = parseInt(document.getElementById('hraRentAmount').value, 10);
      const landlordPan = document.getElementById('hraLandlordPan').value.toUpperCase();
      const address = document.getElementById('hraAddress').value;
      const fy = document.getElementById('hraFinancialYear').value;

      const months = [
        {{ name: 'April', year: fy.split('-')[0] }},
        {{ name: 'May', year: fy.split('-')[0] }},
        {{ name: 'June', year: fy.split('-')[0] }},
        {{ name: 'July', year: fy.split('-')[0] }},
        {{ name: 'August', year: fy.split('-')[0] }},
        {{ name: 'September', year: fy.split('-')[0] }},
        {{ name: 'October', year: fy.split('-')[0] }},
        {{ name: 'November', year: fy.split('-')[0] }},
        {{ name: 'December', year: fy.split('-')[0] }},
        {{ name: 'January', year: fy.split('-')[1] }},
        {{ name: 'February', year: fy.split('-')[1] }},
        {{ name: 'March', year: fy.split('-')[1] }}
      ];

      hraReceiptsContainer.innerHTML = months.map((m, idx) => `
        <div class="hra-receipt-paper" style="background:#FFFFFF; border:1px solid #CBD5E1; border-radius:10px; padding:1.25rem; margin-bottom:1rem; box-shadow:0 2px 4px rgba(0,0,0,0.04);">
          <div style="display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid #E2E8F0; padding-bottom:0.6rem; margin-bottom:0.75rem;">
            <div>
              <span style="font-size:0.75rem; color:#64748B; font-weight:700;">HRA TAX RENT RECEIPT #${{idx + 1}}</span>
              <h4 style="margin:0; font-size:1.1rem; color:#0F172A; font-weight:800;">${{m.name}} ${{m.year}}</h4>
            </div>
            <div style="text-align:right;">
              <span style="font-size:0.75rem; color:#64748B;">Section 10(13A) Exemption</span>
              <div style="font-size:1.2rem; font-weight:800; color:#059669;">${{formatINR(rentAmt)}}</div>
            </div>
          </div>

          <p style="font-size:0.88rem; color:#334155; line-height:1.6; margin:0 0 0.75rem 0;">
            Received with thanks from <strong>${{tenant}}</strong> a sum of <strong>${{formatINR(rentAmt)}}</strong> towards house rent for the month of <strong>${{m.name}} ${{m.year}}</strong> for residential premises situated at: <strong>${{address}}</strong>.
          </p>

          <div style="display:flex; justify-content:space-between; align-items:flex-end; padding-top:0.5rem; border-top:1px dashed #E2E8F0;">
            <div>
              <span style="font-size:0.75rem; color:#64748B; display:block;">LANDLORD DECLARATION:</span>
              <strong style="font-size:0.9rem; color:#0F172A;">${{landlord}}</strong>
              <div style="font-size:0.75rem; color:#475569; font-family:'JetBrains Mono', monospace;">PAN: <strong>${{landlordPan}}</strong></div>
            </div>

            <div class="hra-stamp-box" style="border:2px solid #E11D48; padding:0.4rem 0.6rem; text-align:center; border-radius:4px; transform:rotate(-4deg); background:#FFF1F2;">
              <span style="font-size:0.65rem; color:#E11D48; font-weight:800; display:block;">REVENUE STAMP</span>
              <span style="font-size:0.8rem; font-weight:800; color:#E11D48;">₹1.00</span>
              <div style="font-size:0.65rem; color:#E11D48; font-style:italic;">${{landlord}}</div>
            </div>
          </div>
        </div>
      `).join('');

      openModal(modalHraPreview);
      showToast(`✓ Generated 12 official HRA rent receipts for ${{fy}}!`);
    }});
  }}

  if (btnPrintHraReceipts) {{
    btnPrintHraReceipts.addEventListener('click', () => {{
      window.print();
    }});
  }}

  // ====================================================================
  // 10. Pricing & Monetization Handlers
  // ====================================================================
  const btnBuyTenantFreedomPass = document.getElementById('btnBuyTenantFreedomPass');
  const btnBuyLandlordPro = document.getElementById('btnBuyLandlordPro');

  if (btnBuyTenantFreedomPass) {{
    btnBuyTenantFreedomPass.addEventListener('click', () => {{
      userState.tenant.isPro = true;
      userState.tenant.inquiriesLeft = 9999;
      userState.role = 'tenant';
      saveUserState();
      showToast('🎉 Tenant Freedom Pass Activated! Enjoy Unlimited Landlord Inquiries.');
    }});
  }}

  if (btnBuyLandlordPro) {{
    btnBuyLandlordPro.addEventListener('click', () => {{
      userState.landlord.isPro = true;
      userState.landlord.listingsLeft = 9999;
      userState.role = 'landlord';
      saveUserState();
      showToast('🎉 Landlord Pro SaaS Activated! Unlimited Postings & Automated Rent Invoicing Unlocked.');
    }});
  }}

  // Quota Upgrade Modal
  const modalQuotaUpgrade = document.getElementById('modalQuotaUpgrade');
  const quotaUpgradeTitle = document.getElementById('quotaUpgradeTitle');
  const quotaUpgradeDesc = document.getElementById('quotaUpgradeDesc');
  const upgradePackageCard = document.getElementById('upgradePackageCard');
  const btnSimulateBuyQuota = document.getElementById('btnSimulateBuyQuota');
  const btnQuotaPayText = document.getElementById('btnQuotaPayText');
  const closeModalQuota = document.getElementById('closeModalQuota');

  if (closeModalQuota) {{
    closeModalQuota.addEventListener('click', () => closeModal(modalQuotaUpgrade));
  }}

  let currentUpgradeRole = 'tenant';

  function openQuotaUpgradeModal(role = 'tenant') {{
    currentUpgradeRole = role;
    if (role === 'tenant') {{
      if (quotaUpgradeTitle) quotaUpgradeTitle.textContent = 'Free 20 Inquiries Exhausted';
      if (quotaUpgradeDesc) quotaUpgradeDesc.textContent = 'You have utilized all 20 free landlord inquiries. Unlock unlimited direct landlord contacts with the Tenant Freedom Pass.';
      if (upgradePackageCard) {{
        upgradePackageCard.innerHTML = `
          <div style="background:#F8FAFC; border:1px solid #CBD5E1; padding:1.25rem; border-radius:10px;">
            <div style="display:flex; justify-content:space-between; align-items:center;">
              <h4 style="margin:0; font-size:1.15rem; color:#0F172A;">Tenant Freedom Pass</h4>
              <span style="font-size:1.3rem; font-weight:800; color:#E11D48;">₹399</span>
            </div>
            <p style="font-size:0.85rem; color:#64748B; margin:0.5rem 0;">Unlimited direct landlord chats, physical visit bookings, and free HRA receipts.</p>
          </div>
        `;
      }}
      if (btnQuotaPayText) btnQuotaPayText.textContent = 'Get Tenant Freedom Pass (₹399) ➔';
    }} else {{
      if (quotaUpgradeTitle) quotaUpgradeTitle.textContent = 'Free 5 Listings Exhausted';
      if (quotaUpgradeDesc) quotaUpgradeDesc.textContent = 'You have used your 5 free direct property postings. Upgrade to Landlord Pro SaaS for unlimited listings and automated UPI rent collections.';
      if (upgradePackageCard) {{
        upgradePackageCard.innerHTML = `
          <div style="background:#F8FAFC; border:1px solid #CBD5E1; padding:1.25rem; border-radius:10px;">
            <div style="display:flex; justify-content:space-between; align-items:center;">
              <h4 style="margin:0; font-size:1.15rem; color:#0F172A;">Landlord Pro Annual SaaS</h4>
              <span style="font-size:1.3rem; font-weight:800; color:#E11D48;">₹999 / yr</span>
            </div>
            <p style="font-size:0.85rem; color:#64748B; margin:0.5rem 0;">Unlimited listings, spotlight badges, WhatsApp rent reminders, and tenant ticket tracking.</p>
          </div>
        `;
      }}
      if (btnQuotaPayText) btnQuotaPayText.textContent = 'Upgrade to Landlord Pro (₹999) ➔';
    }}

    openModal(modalQuotaUpgrade);
  }}

  if (btnSimulateBuyQuota) {{
    btnSimulateBuyQuota.addEventListener('click', () => {{
      closeModal(modalQuotaUpgrade);
      if (currentUpgradeRole === 'tenant') {{
        userState.tenant.isPro = true;
        userState.tenant.inquiriesLeft = 9999;
        showToast('🎉 Tenant Freedom Pass unlocked! You have Unlimited inquiries.');
      }} else {{
        userState.landlord.isPro = true;
        userState.landlord.listingsLeft = 9999;
        showToast('🎉 Landlord Pro activated! Unlimited property listings unlocked.');
      }}
      saveUserState();
    }});
  }}

  // ====================================================================
  // 11. Post Apartment Modal (5 Free Listings Enforced)
  // ====================================================================
  const modalPostApartment = document.getElementById('modalPostApartment');
  const formPostApartment = document.getElementById('formPostApartment');
  const btnTriggerPostProperty = document.getElementById('btnTriggerPostProperty');
  const closeModalPost = document.getElementById('closeModalPost');

  if (btnTriggerPostProperty) {{
    btnTriggerPostProperty.addEventListener('click', () => {{
      if (!userState.landlord.isPro && userState.landlord.listingsLeft <= 0) {{
        openQuotaUpgradeModal('landlord');
        return;
      }}
      openModal(modalPostApartment);
    }});
  }}

  if (closeModalPost) {{
    closeModalPost.addEventListener('click', () => closeModal(modalPostApartment));
  }}

  if (formPostApartment) {{
    formPostApartment.addEventListener('submit', (e) => {{
      e.preventDefault();

      if (!userState.landlord.isPro && userState.landlord.listingsLeft <= 0) {{
        closeModal(modalPostApartment);
        openQuotaUpgradeModal('landlord');
        return;
      }}

      const title = document.getElementById('postTitle') ? document.getElementById('postTitle').value : 'Luxury Flat in Bengaluru';
      const society = document.getElementById('postSociety') ? document.getElementById('postSociety').value : 'Exa Skyline Residency';
      const locality = document.getElementById('postLocality') ? document.getElementById('postLocality').value : 'Whitefield';
      const bhk = document.getElementById('postBhk') ? document.getElementById('postBhk').value : '2 BHK';
      const furnishing = document.getElementById('postFurnishing') ? document.getElementById('postFurnishing').value : 'Semi Furnished';
      const rent = parseInt(document.getElementById('postRent').value, 10) || 35000;
      const deposit = parseInt(document.getElementById('postDeposit').value, 10) || (rent * 3);
      const area = parseInt(document.getElementById('postArea').value, 10) || 1100;
      const ownerName = document.getElementById('postOwnerName') ? document.getElementById('postOwnerName').value : userState.landlord.name;
      const ownerPhone = document.getElementById('postOwnerPhone') ? document.getElementById('postOwnerPhone').value : userState.landlord.phone;

      const newApt = {{
        id: 'apt-exa-' + Date.now(),
        source: 'Direct Owner',
        sourceId: 'EXA-' + Math.floor(100 + Math.random() * 900),
        title: `${{society}} — ${{title}}`,
        society: society,
        city: 'Bengaluru',
        locality: locality,
        bhk: bhk,
        furnishing: furnishing,
        rent: rent,
        deposit: deposit,
        area: area,
        photoCount: 8,
        image: 'https://images.unsplash.com/photo-1545324418-cc1a3fa10c00?auto=format&fit=crop&w=800&q=80',
        imageCredit: 'Photo: Verified Direct Owner Inspection',
        amenities: ['gym', 'pool', 'gated'],
        owner: {{
          name: ownerName,
          phone: ownerPhone,
          type: 'Direct Owner',
          verified: true
        }},
        spotlight: true,
        postedDaysAgo: 0,
        availableFrom: 'Immediately',
        isReserved: false
      }};

      apartments.unshift(newApt);
      saveApartments();

      if (!userState.landlord.isPro) {{
        userState.landlord.listingsLeft = Math.max(0, userState.landlord.listingsLeft - 1);
        saveUserState();
      }}

      closeModal(modalPostApartment);
      renderApartments();

      const el = document.getElementById('explore-apartments');
      if (el) el.scrollIntoView({{ behavior: 'smooth' }});

      showToast(`🎉 Property "${{society}}" listed successfully! 100% Zero Brokerage.`);
    }});
  }}

  // ====================================================================
  // 12. City Coming Soon Modal
  // ====================================================================
  function openCityComingSoonModal(cityName) {{
    const modal = document.createElement('div');
    modal.className = 'modal-backdrop active';
    modal.innerHTML = `
      <div class="modal-box" style="text-align:center;">
        <button class="modal-close-btn" onclick="this.closest('.modal-backdrop').remove();">&times;</button>
        <span class="modal-badge-clean" style="margin-bottom:0.75rem;">EXPANSION ROADMAP</span>
        <h3 style="font-size:1.4rem; font-weight:800; color:#0F172A; margin:0.5rem 0;">ExaInfra is Coming to ${{cityName}} in Q1 2027!</h3>
        <p style="color:#64748B; font-size:0.9rem; margin-bottom:1.25rem;">
          We are currently fully live across <strong>Bengaluru (12 verified tech corridor hubs)</strong>. Drop your email to get early zero-brokerage access when we launch in ${{cityName}}.
        </p>
        <div style="display:flex; gap:0.5rem; max-width:360px; margin:0 auto 1.5rem auto;">
          <input type="email" placeholder="Enter your email" class="form-control-clean" style="flex:1;" value="user@domain.com">
          <button class="btn btn-primary" onclick="showToast('✓ You are on the VIP waitlist for ${{cityName}}!'); this.closest('.modal-backdrop').remove();">
            Join Waitlist
          </button>
        </div>
        <button class="btn btn-secondary btn-full" onclick="this.closest('.modal-backdrop').remove();">
          Browse Bengaluru Properties Instead &rarr;
        </button>
      </div>
    `;
    document.body.appendChild(modal);
  }}

  // ====================================================================
  // 13. Rent Estimator
  // ====================================================================
  const estLocality = document.getElementById('estLocality');
  const estBhk = document.getElementById('estBhk');
  const estFurnishing = document.getElementById('estFurnishing');
  const estCarpetArea = document.getElementById('estCarpetArea');
  const estAmenities = document.getElementById('estAmenities');
  const estRangeDisplay = document.getElementById('estRangeDisplay');
  const estYieldDisplay = document.getElementById('estYieldDisplay');

  function calculateRentEstimate() {{
    if (!estRangeDisplay) return;

    let baseRent = 30000;
    const bhk = estBhk ? estBhk.value : '2 BHK';
    if (bhk === '1 BHK') baseRent = 18000;
    else if (bhk === '2 BHK') baseRent = 35000;
    else if (bhk === '3 BHK') baseRent = 55000;
    else if (bhk === '4+ BHK') baseRent = 90000;

    const loc = estLocality ? estLocality.value : 'Bellandur';
    let locMultiplier = 1.0;
    if (loc.includes('Bellandur') || loc.includes('Indiranagar')) locMultiplier = 1.2;
    else if (loc.includes('Whitefield') || loc.includes('Koramangala')) locMultiplier = 1.15;
    else if (loc.includes('Electronic')) locMultiplier = 0.85;

    const furn = estFurnishing ? estFurnishing.value : 'Semi Furnished';
    let furnMultiplier = 1.0;
    if (furn === 'Fully Furnished') furnMultiplier = 1.25;
    else if (furn === 'Unfurnished') furnMultiplier = 0.85;

    const calculated = Math.round(baseRent * locMultiplier * furnMultiplier / 1000) * 1000;
    const low = Math.round(calculated * 0.9 / 1000) * 1000;
    const high = Math.round(calculated * 1.15 / 1000) * 1000;

    estRangeDisplay.textContent = `${{formatINR(low)}} - ${{formatINR(high)}} / mo`;
    if (estYieldDisplay) estYieldDisplay.textContent = '4.2% - 4.8% p.a.';
  }}

  [estLocality, estBhk, estFurnishing, estCarpetArea, estAmenities].forEach(el => {{
    if (el) el.addEventListener('change', calculateRentEstimate);
  }});

  // ====================================================================
  // 14. Toast Notification System
  // ====================================================================
  function showToast(message, type = 'emerald') {{
    const container = document.getElementById('toastContainer');
    if (!container) return;

    const toast = document.createElement('div');
    toast.className = `toast-item toast-${{type}}`;
    toast.innerHTML = `
      <div class="toast-content">${{message}}</div>
      <button class="toast-close" onclick="this.parentElement.remove()">&times;</button>
    `;

    container.appendChild(toast);
    setTimeout(() => {{
      toast.classList.add('fade-out');
      setTimeout(() => toast.remove(), 300);
    }}, 4000);
  }}

  window.showToast = showToast;
  window.openModal = openModal;
  window.closeModal = closeModal;
  window.openInAppChatModal = openInAppChatModal;
  window.openConfirmRentalModal = openConfirmRentalModal;

}});
"""

with open('/Users/chetanbisariya/.gemini/antigravity-ide/scratch/exainfra-in/app.js', 'w') as f:
    f.write(js_content)

print(f"Generated clean app.js ({len(js_content)} bytes) successfully.")
