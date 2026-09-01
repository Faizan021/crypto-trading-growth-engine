# ⚡ Faizex Digital | CRM Lifecycle Marketing & Retention OS
### Multi-Channel Customer Journeys (Email, Push, In-App), Onboarding Optimization, A/B Testing Experiments, and Sparplan Retention for Regulated Trading Platforms

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://crypto-trading-growth-engine.streamlit.app)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![CRM Stack: Braze & Liquid](https://img.shields.io/badge/CRM%20Stack-Braze%20%7C%20Liquid%20%7C%20SQL-blueviolet.svg)](https://www.braze.com/)
[![Compliance: BaFin & GDPR](https://img.shields.io/badge/Compliance-BaFin%20%7C%20GDPR-green.svg)](https://www.bafin.de/)

> [!IMPORTANT]
> **PORTFOLIO & EDUCATIONAL NOTICE:**  
> **"Faizex"** is a custom portfolio case study platform created by **Faizan Ahmed** to demonstrate end-to-end CRM campaign management, lifecycle journey design, behavioral segmentation, and data-driven A/B testing in a regulated European trading environment.

---

# 🎯 Executive CRM Lifecycle Overview

```mermaid
flowchart TD
    subgraph Trigger_Layer ["1. Behavioral & Market Triggers"]
        A["User Signed Up (KYC Pending)"] --> D["CRM Journey Orchestrator (Braze)"]
        B["First Spot Order Filled"] --> D
        C["Market Volatility Breakout (±5%)"] --> D
    end

    subgraph Segmentation_Layer ["2. Dynamic Segmentation & Personalization"]
        D --> E{"Audience Lifecycle Stage"}
        E -->|Unverified| F["Onboarding Friction-Breaker Journey"]
        E -->|Spot Trader| G["Sparplan DCA Conversion Journey"]
        E -->|Dormant >60D| H["Market Signal Win-Back Journey"]
    end

    subgraph Multichannel_Layer ["3. Multi-Channel Touchpoints"]
        F --> I["Interactive 3-Step Email + Deep-Link"]
        G --> J["In-App Post-Trade Modal + DCA Nudge"]
        H --> K["Targeted Push Notification + Fatigue Guard"]
    end
```

---

# 🔬 Creative Email A/B Testing Experiments (Side-by-Side)

---

### ✉️ Case 1: Transactional Confirmation & Momentum Builder
* **Trigger:** `user_registration_submitted` | **Channel:** Transactional Email (High Deliverability)
* **Strategic Context:** Transactional confirmations command a **68.2% open rate** (the highest in the customer lifecycle). Treating this email as a plain administrative chore wastes the moment of peak customer motivation.

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
* **Trigger:** `email_confirmed_kyc_pending` | **Channel:** Multichannel (Email + Push + IAM)
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
* **Trigger:** Monthly Broadcast (`active_and_onboarding_subscribers`) | **Channel:** Dynamic Rich HTML Email
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
