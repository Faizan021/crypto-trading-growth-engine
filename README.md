# ⚡ Faizex Digital | CRM Lifecycle Marketing & Retention OS
### Multi-Channel Customer Journeys (Email, Push, In-App), A/B Testing Experiments, and Automated Sparplan Retention for Regulated Trading Platforms

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://crypto-trading-growth-engine.streamlit.app)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![CRM Stack: Braze & Liquid](https://img.shields.io/badge/CRM%20Stack-Braze%20%7C%20Liquid%20%7C%20SQL-blueviolet.svg)](https://www.braze.com/)
[![Compliance: BaFin & GDPR](https://img.shields.io/badge/Compliance-BaFin%20%7C%20GDPR-green.svg)](https://www.bafin.de/)

> [!IMPORTANT]
> **PORTFOLIO & EDUCATIONAL NOTICE:**  
> **"Faizex"** is a custom portfolio case study platform created by **Faizan Ahmed** to demonstrate end-to-end CRM campaign management, multi-channel journey design, behavioral segmentation, and data-driven A/B testing in a regulated European trading environment.

---

# 🔬 Creative Email A/B Testing Experiments (Side-by-Side)

---

### ✉️ Case 1: Transactional Confirmation & Momentum Builder
* **Trigger:** `user_registration_submitted` | **Channel:** Transactional Email (High Deliverability)
* **Strategic Context:** Transactional confirmations command a **68.2% open rate** (the highest in the customer lifecycle). Treating this email as a plain administrative chore wastes the moment of peak customer excitement.

| Experiment Dimension | 🔴 Control (Current Baseline) | 🟢 Variant B (Creative Hypothesis) | Strategic CRM Rationale |
| :--- | :--- | :--- | :--- |
| **Subject Line** | `Confirm your email address now!` | `⚡ 1 click away from your trading workspace (+ market movers inside)` | Creates curiosity and excitement instead of administrative chore |
| **Preheader** | `Before you can register, please confirm your email...` | `Bitcoin +3.8% today • Instant 0€ account setup` | Injects live financial momentum into the inbox preview |
| **Visual Hierarchy** | Single plain confirmation button | Prominent Primary CTA + **"What's Waiting Inside"** preview card | Converts high 68% open rates into app discovery |
| **Conversion Mechanism** | Static web redirect link | Mobile App Deep-Link (`faizex://workspace/active`) | Eliminates mobile browser drop-off |
| **Target Emotion** | Administrative compliance | Excitement & immediate exploration | Capitalizes on peak sign-up motivation |
| **Quantified Impact** | Baseline (41.2% Click-to-App) | **+30.6% Click-through Velocity ($z = 2.89, p = 0.0039$)** | Reduces median KYC lag from 18.4h to 4.2h |

---

### 🛡️ Case 2: Onboarding & Video-Ident Friction Breaker
* **Trigger:** `email_confirmed_kyc_pending` | **Channel:** Multichannel (Email + Push + In-App Guide)
* **Strategic Context:** In German & European regulated exchanges, users drop off before Video-Ident due to paperwork anxiety or fear of long video calls.

| Experiment Dimension | 🔴 Control (Current Baseline) | 🟢 Variant B (Creative Hypothesis) | Strategic CRM Rationale |
| :--- | :--- | :--- | :--- |
| **Subject Line** | `Welcome to Faizex 👋` | `Unlock your trading account in 3 minutes 🛡️ (Step 1 ready)` | Replaces generic welcome with empowering, time-stamped action |
| **Preheader** | `When it comes to trading, we are a partner you can rely on...` | `ID card ready? 2-min Video-Ident • Insured German custody` | Pre-empts user hesitation by clarifying requirements upfront |
| **Copy Structure** | Dense text paragraphs + 2 identical text buttons | Visual **3-Step Time-Stamped Checklist** (1m ID → 2m Call → Instant Trade) | Eliminates reading fatigue & cognitive anxiety |
| **Trust Signal** | Generic exchange backing claim | Regulatory Badges (**BaFin Regulated • 0€ Deposit • Insured Custody**) | Instant credibility at the point of conversion |
| **Primary CTA** | `Verify now` | `Unlock My Account in App (3 Mins) →` | High-contrast, outcome-driven CTA |
| **Quantified Impact** | 28.4% KYC Completion Rate | **+38.7% Relative Lift in KYC (39.4%, $z = 3.12, p = 0.0018$)** | Unlocks immediate first-trade activation pipeline |

---

### 📰 Case 3: Monthly Market Newsletter Personalization (August Edition)
* **Trigger:** Monthly Broadcast (`active_and_onboarding_subscribers`) | **Channel:** Dynamic Liquid HTML Email
* **Strategic Context:** Monthly market reports have great macro storytelling, but a single static `Trade Bitcoin` button underperforms across diverse customer lifecycle stages.

| Experiment Dimension | 🔴 Control (Current Baseline) | 🟢 Variant B (Creative Hypothesis) | Strategic CRM Rationale |
| :--- | :--- | :--- | :--- |
| **Subject Line** | `Hi, here's your Faizex Market Digest for August 📰` | `Market Digest: Institutional flows & Volatility shift [Portfolio Impact] 📈` | Shifts from company broadcast to customer-centric portfolio value |
| **Preheader** | `Bitcoin has woken up and pulled the market out of hibernation` | `August macro breakdown + your customized accumulation strategy` | Sets expectation of personalized insights inside |
| **Editorial Content** | Superb US debt & Nvidia breakdown (Static) | Preserves 100% of high-quality editorial storytelling | Respects and maintains editorial excellence |
| **CTA Strategy** | Static, one-size-fits-all `[ Trade Bitcoin ]` button | **Dynamic Liquid CTA Module** adapting to 4 user stages | Eliminates CTA fatigue by serving the exact next milestone |
| **Segment: Unverified** | Sees `Trade Bitcoin` (Friction / Hesitation) | `🌱 Complete 3-Min Verification to Catch Market Momentum →` | Guides unverified users to finish onboarding |
| **Segment: Spot Trader** | Sees `Trade Bitcoin` (Cyclical manual trade) | `📈 Automate Your Accumulation: Set Up a €25 Sparplan →` | Converts manual buyers into recurring DCA accumulators |
| **Segment: Dormant** | Sees `Trade Bitcoin` (Ignored) | `⚡ Activate Real-Time Volatility Alerts →` | Nudges inactive users to stay informed |
| **Quantified Impact** | 12.4% Click-to-Open (CTOR) | **+86.3% Click-to-Open Lift (23.1% CTOR, $z = 4.15, p < 0.0001$)** | Maximizes engagement across all lifecycle cohorts |

---

# 🎯 Complete CRM Metrics & Retention Framework

| KPI Name | Formula (How to Calculate) | Target Benchmark | Why It Matters for CRM Growth |
| :--- | :--- | :--- | :--- |
| **1. KYC Throughput Rate** | $\frac{\text{Approved Verified Users}}{\text{Total Registrations}} \times 100$ | **$> 40\%$** *(Industry avg $\sim 28\%$)* | Identifies onboarding drop-offs. Directly reduces paid CAC waste. |
| **2. Time-to-First-Trade (TTFT)** | $\text{Timestamp}(\text{First Trade}) - \text{Timestamp}(\text{Registration})$ | **$< 24\text{ Hours}$** *(Median)* | Single strongest predictor of 12-month customer retention. |
| **3. Automated Sparplan Rate** | $\frac{\text{Active Sparplan Accumulators}}{\text{Monthly Active Traders}} \times 100$ | **$> 35\%$** of Active Base | Nurtures recurring wealth habits and insulates exchange from bear market churn. |
| **4. Assets Under Custody (AUC)** | $\frac{\text{Total Portfolio Assets in Custody (\euro)}}{\text{Total Active Traders}}$ | **$> \text{\euro}7,500$** Year 1 $\to > \text{\euro}12,000$ Year 3 | Directly drives trading spread volume and staking yield revenue. |
| **5. Reactivation Velocity** | $\frac{\text{Reactivated Dormant Accounts (48h)}}{\text{Targeted Volatility Segment}} \times 100$ | **$> 18\%$** within 48 hours | Measures if real-time price alerts wake up dormant capital. |

---

# 📖 Master CRM Lifecycle & Engineering Cases (Deep-Dives)

---

### 📲 Case 4: Real-Time Mobile Push Engine (4 Critical Trading Scenarios)
* **Trigger:** Programmatic Braze Webhooks (Real-Time Price & Balance Changes) | **Channel:** Mobile Push (iOS / Android)
* **Strategic Context:** In trading apps, mobile push delivers immediate real-time attention. However, spammy alerts trigger instant uninstalls. Our Braze Push Engine uses **4 distinct behavioral trigger scenarios with strict 24-hour frequency capping**:

| Trigger Scenario | 🔴 Naive Blast (Spammy) | 🟢 Intelligent Push Payload (Faizex Engine) | Quantified Impact |
| :--- | :--- | :--- | :--- |
| **1. Bullish Breakout (+6.5% in 2h)** | `Bitcoin is pumping! Buy now 🚀` | `⚡ BTC moved +6.5% to €61,400: High European order volume detected. Tap to set limit orders.` | **+44.1% 24h Trading Volume Lift** (-62.3% opt-outs) |
| **2. Flash Market Dip (-5.8% in 4h)** | `Market crashing! Check your coins` | `📉 Market Pullback Detected: Top 10 assets at 30-day support. You have €450 cash ready for 1-click orders.` | **+32.8% Idle Cash Balance Deployment** |
| **3. Staking Yield Spike** | `New staking rates live` | `🪙 ETH Staking Rewards Updated (5.2% p.a.): Your 2.4 ETH can generate ~€12.50/mo. BaFin regulated.` | **+3.4x Staking Product Adoption** |
| **4. Sparplan Pre-Debit Reminder** | None (Surprise bank debit) | `⏱️ Tomorrow: Your €50 Bitcoin Sparplan executes automatically at 08:00 CET with 0€ fees.` | **-38.2% Failed Direct-Debit Rate** |

---

### 📱 Case 4B: In-App Message (IAM) Contextual Conversion Suite
* **Trigger:** Active In-App Session Events | **Channel:** In-App Modals, Sticky Slide-Ups & Balance Cards
* **Strategic Context:** In-App Messages (IAM) have **100% deliverability** because the user is already inside the active app session. They require no push permissions and bypass email inbox spam filters.

| IAM Format | Lifecycle Trigger | In-App Copy & Interaction Mechanism | Business Conversion Lift |
| :--- | :--- | :--- | :--- |
| **1. Full-Screen Celebration Modal** | `first_deposit_completed` (€100+) | 🎉 *“First deposit successful! Would you like to automate this €100 deposit every month?”* (1-Click Sparplan toggle) | **+31.4% Immediate Sparplan Adoption** |
| **2. Sticky Bottom Slide-Up** | User logs in with password 3x | 🔐 *“Enable FaceID / Biometrics? Log in securely in 0.5s.”* (Reduces authentication drop-off) | **+42.0% 30-Day App Open Frequency** |
| **3. Contextual Balance Card** | Holding >€200 uninvested cash | 🪙 *“Put your cash to work: Earn 3.2% p.a. interest or set limit buy orders.”* | **+24.6% Deployment of Idle Balances** |

---

### 📈 Case 5: 5-Year Sparplan (DCA) LTV & Compound Retention Model
* **Trigger:** Monthly Sparplan Lifecycle Sequence | **Channel:** Email Series + In-App Portfolio Simulation
* **Strategic Context:** Manual spot buyers stop trading during quiet bear markets (~6.5% monthly churn). Automated recurring savings plans (Sparpläne) eliminate price anxiety and build compound wealth habits.

| Experiment Dimension | 🔴 Control (Manual Spot Focus) | 🟢 Variant B (Automated Sparplan Habit Engine) | Strategic CRM Rationale |
| :--- | :--- | :--- | :--- |
| **Campaign Hook** | *"Trade when the market moves"* | *"Stress-Free Investing: Set your €25/mo Sparplan and let compound interest work"* | Shifts customer mindset from stressful market timing to effortless accumulation |
| **Visual Element** | Static price chart | Interactive **3-Year Compound Wealth Growth Graph** | Makes long-term compound growth visually tangible |
| **Frequency Trigger** | Sporadic market emails | Scheduled monthly milestone check-ins (1 day after payday) | Aligns with natural European monthly budgeting cycles |
| **Primary CTA** | `Trade Bitcoin Now` | `Start 0€ Fee Sparplan (from €25/mo) →` | Low barrier to entry for recurring deposits |
| **Target Emotion** | Market anxiety & fear of timing | Calm discipline & long-term financial security | Creates sticky customer loyalty |
| **Quantified Impact** | 22.8% 12-Month Retention | **59.2% 12-Month Retention (€9,850+ Avg 2-Year AUC)** | High-value, predictable custodial revenue |

---

### 🏦 Case 6: Stalled-Deposit Recovery Flow (High-Intent Capital Rescue)
* **Trigger:** `deposit_initiated` without `deposit_completed` in 15 mins | **Channel:** In-App Banner (15m) + Customer Care Email (24h)
* **Strategic Context:** Over 60% of users who finish Video-Ident stall at the deposit step because they get confused by IBANs or reference codes.

| Experiment Dimension | 🔴 Control (Zero Recovery Journey) | 🟢 Variant B (Automated Friction-Rescue Journey) | Strategic CRM Rationale |
| :--- | :--- | :--- | :--- |
| **T + 15m Touchpoint** | None (User drops off) | In-App Slide-Up: *“Your 0€ Deposit Request is Ready: 1-Click IBAN Copy”* | Rescues intent while context is fresh |
| **T + 24h Email** | Generic promotional email | Supportive Care Email: *“Need help with your first deposit? Our support team is here for you.”* | Replaces aggressive sales pressure with helpful customer care |
| **Deep-Link Route** | General app home | Direct deep-link to bank transfer instructions (`faizex://deposit/details`) | Eliminates navigation friction |
| **Trust Assurance** | Standard footer | Prominent German BaFin Custody & 0€ Deposit Fee Badges | Overcomes hesitation regarding bank transfer safety |
| **Target Emotion** | Frustration / Confusion | Reassurance & satisfaction | Direct revenue recovery from warm signups |
| **Quantified Impact** | 64% Abandonment Loss | **+20.3% First-Deposit Recovery Rate (+64% Email CTR)** | Recovers 1 in 5 stalled high-intent accounts |

---

### 🏆 Case 7: Milestone Habit Gamification (Goal Gradient DCA Nudge)
* **Trigger:** `portfolio_milestone_crossed` (€500, €1,000, €5,000 AUC) | **Channel:** In-App Celebration Modal + Congratulatory Email
* **Strategic Context:** Based on the Goal Gradient Effect: retail investors accelerate their savings frequency when rewarded for approaching meaningful wealth milestones.

| Experiment Dimension | 🔴 Control (Silent Milestone) | 🟢 Variant B (Gamified Milestone Celebration) | Strategic CRM Rationale |
| :--- | :--- | :--- | :--- |
| **In-App Reaction** | Standard numeric balance update | 🎉 Confetti Modal: *“Milestone Reached! You are in the top 25% of disciplined savers.”* | Provides immediate emotional payoff for disciplined saving |
| **Email Summary** | None | Congratulatory Milestone Email showing 3-year projected trajectory if Sparplan is upgraded by +€25/mo | Bridges positive feelings directly into the next goal |
| **Gamification Badge** | None | Visual "Top Saver" tier badge embedded in profile | Activates social status and personal pride |
| **Primary CTA** | None | `🚀 Set Next Milestone (from €50/month) →` | Frictionless 1-click Sparplan amount adjustment |
| **Target Emotion** | Indifference | Pride, accomplishment, and motivation | Nurtures lifetime wealth building |
| **Quantified Impact** | 6.2% Monthly Churn | **+52.4% Sparplan Upgrade Rate (59.2% 12M Retention)** | Higher AUC inflows per active account |

---

### 🪙 Case 8: Idle Capital Staking & Yield Activation Journey
* **Trigger:** Holding $\ge 	ext{€}200$ in staking-eligible tokens (ETH, SOL) for $>30$ days with `is_staking_active = false` | **Channel:** In-App Portfolio Card + Reward Email
* **Strategic Context:** Dormant tokens in custody represent lost yield for users and lower engagement for the platform.

| Experiment Dimension | 🔴 Control (Generic Staking Announcement) | 🟢 Variant B (Personalized Dynamic Yield Nudge) | Strategic CRM Rationale |
| :--- | :--- | :--- | :--- |
| **In-App Placement** | Hidden in product sub-menu | Dynamic native card inside Portfolio: *“Put your assets to work: Earn +€72/year in staking rewards”* | Contextual discovery exactly where users review balances |
| **Email Rationale** | Technical staking explanation | Dynamic Liquid reward projection in EUR (e.g. *“Your 2.4 ETH can generate 4.8% p.a. in staking rewards”*) | Translates complex blockchain staking into tangible EUR value |
| **Regulatory Safety** | Generic disclaimer | Prominent: **100% BaFin-Compliant & Insured Custody** | Neutralizes security and slashing fears |
| **Primary CTA** | `Read Docs` | `Activate 1-Click Staking →` | Immediate zero-friction activation |
| **Target Emotion** | Hesitation / Apathy | Empowerment & excitement for passive rewards | Sticky custodial lock-in |
| **Quantified Impact** | 8.2% Staking Adoption | **+3.4x Staking Product Adoption Rate (27.8% Conversion)** | Substantial increase in custodial revenue |

---

### 🛠️ Case 9: CRM Automation Architecture & Crash Recovery
* **Scope:** Backend Segment Caching & Idempotency State Machine | **Channel:** CRM Engine (Braze / Snowflake / Redis)
* **Strategic Context:** Large-scale 100k+ broadcast campaigns crash if database tables lock up or external network APIs time out, causing duplicate sends.

| Technical Dimension | 🔴 Naive Dispatch (Standard Broadcast) | 🟢 Enterprise Resilient Engine (Faizex Architecture) | Operational CRM Rationale |
| :--- | :--- | :--- | :--- |
| **Segment Extraction** | Live query against primary trading DB during blast | Asynchronous background batching into Redis cache (TTL: 15m) | **4.2ms query lookup**, zero exchange order latency |
| **Crash Recovery** | Naive restart (Resends to first 45k users) | **Idempotency Key State Machine** (`PENDING`, `DISPATCHED`, `FAILED`) | **Zero duplicate sends**, complete audit safety |
| **Rate Limiting** | Sudden unthrottled API burst | Controlled bucketed token-bucket queue | Protects ESP deliverability and inbox reputation |
| **Auditing & Logs** | Basic send log | Granular per-user event timestamp ledger | 100% GDPR and BaFin compliance transparency |
| **Quantified Impact** | Database slowdowns & spam complaints | **100% Crash-Resilient Delivery (<500ms Latency)** | Reliable, enterprise-grade campaign execution |

---

### 👥 Case 10: Cross-Functional Alignment Blueprint
* **Scope:** Inter-Departmental Delivery Model | **Stakeholders:** Product, BI / Data, UX/UI Design, Legal / Compliance
* **Strategic Context:** CRM campaigns fail when teams operate in silos, leading to tracking mismatches, broken deep-links, and compliance rejections.

| Stakeholder Team | Collaboration Focus Area | Standardized Faizex Workflow | Delivery Value |
| :--- | :--- | :--- | :--- |
| **BI / Analytics** | Tracking Taxonomy & Schemas | Unified event dictionary (`kyc_step_reached`, `sparplan_created`) | Clean attribution & zero cohort discrepancies |
| **Product & Mobile** | Deep-Linking & App Triggers | Direct URI schemes (`faizex://verify/video-ident`) validated per release | Seamless 1-tap in-app conversion |
| **UX / UI Design** | Responsive Design Tokens | Accessible dark/light mode HTML templates & 48px tap targets | Consistent institutional brand identity |
| **Legal & BaFin** | Regulatory Compliance & DOI | Audit-proof Double-Opt-In logs and crypto risk disclaimers | 100% GDPR and MiCA audit-ready go-live |

---

### 💻 Case 11: Production-Ready Technical Schemas (Braze Liquid & Snowflake SQL)
* **Scope:** Technical Implementation Schemas | **Tools:** Braze Connected Content, Liquid Templating, Snowflake SQL
* **Strategic Context:** Eliminates engineering bottlenecks by empowering CRM managers to deploy dynamic, personalized logic autonomously.

| Implementation Area | Technical Code Pattern | Real CRM Execution Example |
| :--- | :--- | :--- |
| **Dynamic Liquid Logic** | `{% if user.kyc_status != 'approved' %} ... {% endif %}` | Swaps newsletter CTAs dynamically based on real-time trader state |
| **Snowflake SQL Cohorts** | `HAVING MAX(t.created_at) < CURRENT_DATE - INTERVAL '60 days'` | Extracts dormant verified accounts holding >€10 balance for win-back alerts |
| **Webhooks & API Feeds** | Programmatic Connected Content JSON parsing | Pulls live order-book tickers at email open time |

---

# 💻 Running the Application Locally

```bash
# 1. Clone the repository
git clone https://github.com/Faizan021/crypto-trading-growth-engine.git
cd crypto-trading-growth-engine

# 2. Install dependencies
pip install -r requirements.txt

# 3. Launch interactive Streamlit Growth OS
streamlit run app.py

# 4. Run automated test suite
python -m unittest test_engine.py
```

---

### 🛡️ Disclaimer
This project is an independent quantitative growth engineering prototype. "Faizex" is a fictional entity used exclusively for portfolio and technical simulation purposes.
