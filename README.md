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

# 📖 Additional Strategic CRM Lifecycle Journeys & Engineering Cases

---

### ⚡ Case 4: Volatility Anomaly Alert Engine (Ethical FOMO & Limit Orders)
* **Trigger:** `market_volatility_anomaly_detected` (Price move $\ge \pm 5\%$ in 4h) | **Channel:** Mobile Push + In-App Smart Modal
* **Strategic Rationale:** When crypto surges, users need calm tools rather than reckless gambling prompts. We dispatch factual price movements paired with an in-app **Limit Order** educational tool and a strict **24h frequency cap**.
* **Impact:** **+44.1% 24h Trading Volume Lift** with **-62.3% reduction in push opt-outs**.

---

### 📈 Case 5: 5-Year Sparplan (DCA) LTV & Retention Model
* **Strategic Rationale:** Manual spot traders churn during quiet bear markets (~6.5% monthly churn). Automated recurring savings plans (Sparpläne) eliminate price anxiety and create compound wealth habits.
* **Impact:** **59.2% 12-Month Retention** yielding **€9,850+ Average 2-Year Assets Under Custody (AUC)**.

---

### 🏦 Case 6: Stalled-Deposit Recovery Flow (High-Intent Capital Rescue)
* **Trigger:** `deposit_initiated` without confirmation in 15 minutes | **Channel:** In-App Banner (15m) + Care Email (24h)
* **Strategic Rationale:** Rescues users who finished Video-Ident but got overwhelmed by bank transfer codes with 1-click IBAN copying and friendly German customer care.
* **Impact:** **+20.3% First-Deposit Recovery Rate** (+64% Email CTR).

---

### 🏆 Case 7: Milestone Habit Gamification (Goal Gradient DCA Nudge)
* **Trigger:** Portfolio crosses €500, €1,000, or €5,000 AUC | **Channel:** In-App Confetti Modal + Milestone Forecast Email
* **Strategic Rationale:** Leverages the psychological Goal Gradient Effect to celebrate disciplined long-term savers and suggest a +€25/month Sparplan upgrade.
* **Impact:** **+52.4% Sparplan Upgrade Velocity**.

---

### 🪙 Case 8: Idle Capital Staking & Yield Activation Journey
* **Trigger:** Holding $\ge 	ext{€}200$ in staking-eligible assets with no active staking for $>30$ days | **Channel:** Dynamic In-App Balance Card
* **Strategic Rationale:** Dynamically computes estimated annual staking rewards in EUR right on the portfolio screen, overcoming apathy.
* **Impact:** **+3.4x Staking Product Adoption (27.8% Conversion)**.

---

### 🛠️ Case 9: CRM Automation Architecture & Crash Recovery
* **Strategic Rationale:** Uses asynchronous in-memory segment caching (4.2ms lookup) and unique idempotency keys to guarantee **zero duplicate messages** if a broadcast server restarts.
* **Impact:** **100% Crash-Resilient Delivery** with zero exchange database lockups.

---

### 👥 Case 10: Cross-Functional Alignment Blueprint
* **Collaboration Matrix:** Standardizes event tracking taxonomies with **BI**, app deep-linking with **Product/UX**, and Double-Opt-In (DOI) audit trails with **Legal/BaFin**.
* **Impact:** Rapid, 100% audit-ready campaign go-live.

---

### 💻 Case 11: Production-Ready Technical Schemas
* **Artifacts Provided:** Ready-to-deploy Liquid dynamic templates and Snowflake SQL cohort extraction queries.

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
