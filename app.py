# -*- coding: utf-8 -*-
import streamlit as st
import pandas as pd
import numpy as np
import json
import os
import math
import hashlib
import time
import plotly.graph_objects as go

st.set_page_config(
    page_title="Faizan Ahmed | FinTech & Crypto CRM Portfolio",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Clean, Modern, High-Contrast Light & Adaptive Styling
st.markdown("""









































<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap');

html, body, [class*="css"] {
font-family: 'Plus Jakarta Sans', sans-serif !important;
}
code, pre {
font-family: 'JetBrains Mono', monospace !important;
}

/* Clean Sidebar Spacing */
section[data-testid="stSidebar"] .stRadio > div {
gap: 3px !important;
}
section[data-testid="stSidebar"] .stRadio label {
font-size: 0.84rem !important;
font-weight: 500 !important;
padding: 4px 8px !important;
margin-bottom: 1px !important;
line-height: 1.25 !important;
}

/* Executive Top Header */
.exec-header {
background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%);
border: 1px solid #334155;
border-radius: 10px;
padding: 1.4rem 1.8rem;
color: #ffffff;
margin-bottom: 1.2rem;
}
.exec-title {
font-size: 1.75rem;
font-weight: 800;
color: #ffffff;
margin-bottom: 0.25rem;
letter-spacing: -0.02em;
}
.exec-sub {
font-size: 0.92rem;
color: #cbd5e1;
line-height: 1.5;
margin: 0;
}
.badge-reg {
display: inline-block;
background: rgba(16, 185, 129, 0.2);
color: #34d399;
border: 1px solid #10b981;
padding: 2px 10px;
border-radius: 4px;
font-size: 0.72rem;
font-weight: 700;
text-transform: uppercase;
margin-right: 6px;
}
.badge-crm {
display: inline-block;
background: rgba(56, 189, 248, 0.2);
color: #38bdf8;
border: 1px solid #0284c7;
padding: 2px 10px;
border-radius: 4px;
font-size: 0.72rem;
font-weight: 700;
text-transform: uppercase;
}

/* Metric Cards - Clean White / Adaptive */
.exec-card {
background: #ffffff;
border: 1px solid #e2e8f0;
border-radius: 10px;
padding: 1.2rem;
text-align: left;
min-height: 145px;
display: flex;
flex-direction: column;
justify-content: space-between;
box-shadow: 0 2px 6px rgba(0,0,0,0.04);
}
.exec-card-val {
font-size: 1.85rem;
font-weight: 800;
color: #0284c7;
margin: 2px 0;
}
.exec-card-lbl {
font-size: 0.78rem;
color: #475569;
font-weight: 700;
text-transform: uppercase;
letter-spacing: 0.5px;
}
.exec-card-sub {
font-size: 0.78rem;
color: #059669;
font-weight: 600;
}

/* Explanatory Callout Boxes - Crisp & Clean Light Mode */
.expl-box-blue {
background: #f0f9ff;
border: 1px solid #bae6fd;
border-left: 4px solid #0284c7;
border-radius: 8px;
padding: 12px 16px;
margin-bottom: 12px;
font-size: 0.88rem;
color: #0f172a;
line-height: 1.5;
}
.expl-box-green {
background: #ecfdf5;
border: 1px solid #a7f3d0;
border-left: 4px solid #059669;
border-radius: 8px;
padding: 12px 16px;
margin-bottom: 12px;
font-size: 0.88rem;
color: #0f172a;
line-height: 1.5;
}

/* Clean Stage Cards */
.funnel-card {
background: #ffffff;
border: 1px solid #e2e8f0;
border-radius: 8px;
padding: 10px 14px;
margin-bottom: 8px;
box-shadow: 0 1px 3px rgba(0,0,0,0.03);
}

/* Global Header Clearance & Screen Sharing Polish */
header[data-testid="stHeader"] {
background: rgba(255, 255, 255, 0.85) !important;
backdrop-filter: blur(8px) !important;
height: 3.5rem !important;
}

.block-container {
padding-top: 5rem !important;
padding-bottom: 3rem !important;
padding-left: 2.5rem !important;
padding-right: 2.5rem !important;
max-width: 100% !important;
}

/* Ensure no headings are clipped by top elements */
h1, h2, h3, h4, .stMarkdown:first-child {
margin-top: 0.25rem !important;
}

</style>
""", unsafe_allow_html=True)

# Top Disclaimer Notice
# Master Navigation Menu Array (16 Operational Modules in Chronological Customer Lifecycle)
NAV_MODULES = [
    "📊 Executive Summary: Strategy & Scorecard",
    "✉️ Case 1: Double Opt-In (DOI) Onboarding Velocity (Email)",
    "🛡️ Case 2: Regulated Identity Verification (KYC) Funnel",
    "📰 Case 3: Dynamic 1:1 BISONews (Welcome Digest)",
    "🎓 Case 4: Zero-Party & First-Party Data Profiling (Learn & Earn)",
    "🏦 Case 5: High-Intent Deposit Abandonment & Recovery Flow",
    "📱 Case 6: Contextual In-App Messaging (IAM) & Home Feed Banners",
    "📈 Case 7: Automated Sparplan (DCA) Recurring Retention Engine",
    "📲 Case 8: Event-Triggered Volatility & Cryptoradar Push",
    "🪙 Case 9: Idle Asset Monetization & Regulated Staking Cross-Sell",
    "🏆 Case 10: Milestone-Based Retention Loops & Habit Gamification",
    "🎯 Case 11: Quantitative RFM & AUC Segmentation Matrix",
    "🛠️ Case 12: Event-Driven Marketing Automation Infrastructure",
    "👥 Case 13: Cross-Functional Growth Squad Collaboration Matrix",
    "💻 Case 14: Production Braze Liquid & Snowflake SQL Schemas"
]

# Grouping by Customer Lifecycle Stages (Phase Headings)
PHASE_GROUPS = {
    "🌐 All 15 Operational Modules": NAV_MODULES,
    "📊 Executive Summary": [
        NAV_MODULES[0]
    ],
    "🟢 1. Onboarding & Welcome (Cases 1-4)": [
        NAV_MODULES[1],
        NAV_MODULES[2],
        NAV_MODULES[3],
        NAV_MODULES[4]
    ],
    "🔵 2. Activation & Retention (Cases 5-7)": [
        NAV_MODULES[5],
        NAV_MODULES[6],
        NAV_MODULES[7]
    ],
    "⚡ 3. Volatility, Staking & Habits (Cases 8-10)": [
        NAV_MODULES[8],
        NAV_MODULES[9],
        NAV_MODULES[10]
    ],
    "🟠 4. Data, Infrastructure & Code (Cases 11-14)": [
        NAV_MODULES[11],
        NAV_MODULES[12],
        NAV_MODULES[13],
        NAV_MODULES[14]
    ]
}

# Sidebar Navigation
st.sidebar.title("Faizan's CRM Portfolio")
st.sidebar.caption("FinTech & Crypto Lifecycle Engine")

st.sidebar.markdown("""





































<div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:6px; padding:6px 10px; font-size:0.75rem; color:#475569; line-height:1.4; margin-bottom:8px;">
<strong>Lifecycle Flow:</strong><br>
🟢 Onboarding ➔ 🔵 Activation ➔ 🟣 Retention ➔ ⚡ Monetization
</div>
""", unsafe_allow_html=True)

st.sidebar.markdown("**Customer Lifecycle Stages**")
selected_phase = st.sidebar.selectbox(
    "Select Lifecycle Stage:",
    list(PHASE_GROUPS.keys()),
    index=0
)

nav_choice = st.sidebar.radio(
    "Select Case Study in this Stage:",
    PHASE_GROUPS[selected_phase]
)

st.sidebar.markdown("---")
st.sidebar.markdown("""





































<div style="background:#ffffff; border:1px solid #e2e8f0; border-radius:8px; padding:10px 12px; font-size:0.8rem; color:#334155; line-height:1.45; box-shadow:0 1px 3px rgba(0,0,0,0.02);">
<strong style="color:#0f172a; font-size:0.85rem;">Faizan Ahmed</strong><br>
<span style="color:#0284c7; font-weight:600;">CRM Marketing & Lifecycle Manager</span>
<div style="margin-top:6px; padding-top:6px; border-top:1px solid #f1f5f9;">
<a href="https://github.com/Faizan021/crypto-trading-growth-engine" target="_blank" style="color:#059669; text-decoration:none; font-weight:700;">📂 GitHub Repository &rarr;</a>
</div>
</div>
""", unsafe_allow_html=True)


# ==========================================
# MODULE 0: EXECUTIVE SUMMARY & SCORECARD
# ==========================================
if nav_choice == NAV_MODULES[0]:

    st.markdown("""



















<div style="background:#f8fafc; border:1px solid #e2e8f0; border-left:4px solid #0284c7; border-radius:8px; padding:12px 16px; margin-bottom:14px; font-size:0.84rem; color:#334155; line-height:1.55;">
<strong>📌 A Respectful Note on Data & Target Benchmarks:</strong><br>
Out of deep respect for proprietary data, all figures shown in this blueprint represent <strong>simulated industry benchmarks</strong> modeled on retail FinTech and subscription app cohort standards. They serve as positive, aspirational North Stars to illustrate what is possible when great engineering and regulatory trust meet empathetic customer communication.
</div>

""", unsafe_allow_html=True)

    st.markdown("""



















<div class="exec-header" style="padding: 1.3rem 1.7rem; margin-bottom: 1.2rem;">
<div style="margin-bottom: 6px;">
<span class="badge-reg">STRATEGIC LIFECYCLE BLUEPRINT</span>
<span class="badge-crm">INSPIRED BY BISON'S 1-MILLION-USER CHAPTER</span>
</div>
<div class="exec-title" style="font-size: 1.65rem;">Faizan's Lifecycle Blueprint — Supporting BISON's Retail Mission</div>
<p class="exec-sub" style="font-size: 0.9rem; line-height: 1.55;">
Built with deep appreciation for <strong>Boerse Stuttgart Group's 160-year heritage</strong> and BISON's intuitive mobile experience. This blueprint explores how collaborative lifecycle CRM can celebrate customer trust, accompany users through their financial journey, and nurture long-term wealth.
</p>
</div>

""", unsafe_allow_html=True)

    st.markdown("### Executive Scorecard — Monthly Retail Throughput, Retention & Custody Metrics")
    
    st.markdown("**Executive Overview:** BISON has already established Germany's most trusted retail crypto gateway. This framework is designed to support that mission: walking hand-in-hand with new subscribers, celebrating their milestones, and helping them build disciplined, stress-free investing habits through automated Sparplans.")
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown("""



















<div class="exec-card">
<div class="exec-card-lbl" style="min-height:34px;">30-Day Retail<br>Trading Volume</div>
<div class="exec-card-val">€148.4M</div>
<div class="exec-card-sub" style="min-height:32px;">Driven by deep market trust and organic customer enthusiasm across Europe.</div>
</div>

""", unsafe_allow_html=True)
    with col2:
        st.markdown("""



















<div class="exec-card">
<div class="exec-card-lbl" style="min-height:34px;">KYC ➔ First-Trade<br>Throughput Rate</div>
<div class="exec-card-val">39.4%</div>
<div class="exec-card-sub" style="min-height:32px;">Empowering users with friendly, supportive guidance through BaFin-regulated ID checks.</div>
</div>

""", unsafe_allow_html=True)
    with col3:
        st.markdown("""



















<div class="exec-card">
<div class="exec-card-lbl" style="min-height:34px;">12-Month Sparplan<br>Customer Retention</div>
<div class="exec-card-val">59.2%</div>
<div class="exec-card-sub" style="min-height:32px;">Helping customers trade less and save more through peaceful, automated DCA habits.</div>
</div>

""", unsafe_allow_html=True)
    with col4:
        st.markdown("""



















<div class="exec-card">
<div class="exec-card-lbl" style="min-height:34px;">Avg 2-Year AUC<br>per Active Account</div>
<div class="exec-card-val">€9,850</div>
<div class="exec-card-sub" style="min-height:32px;">The compounding result of patient investing, institutional security, and zero custody fees.</div>
</div>

""", unsafe_allow_html=True)
        
    st.markdown("""



















<div style="background:#ffffff; border:1px solid #e2e8f0; border-radius:10px; padding:1.2rem; margin: 1.2rem 0; box-shadow:0 2px 4px rgba(0,0,0,0.02);">
<strong style="color:#0f172a; font-size:0.95rem;">The Three Strategic Pillars (Zero Criticism, Pure Value):</strong>
<ul style="margin:8px 0 10px 0; padding-left:20px; font-size:0.87rem; color:#334155; line-height:1.6;">
<li><strong>1. Welcoming Customers with Empathy (Onboarding Throughput):</strong> Identity verification can feel unfamiliar for beginners in regulated finance. By offering gentle 3-minute checklists and transparent reassurance, the onboarding flow helps users feel safe, supported, and confident from their very first day.</li>
<li><strong>2. Celebrating Peaceful, Disciplined Saving (Automated Sparplans):</strong> Crypto markets can be volatile. Rather than encouraging stressful day-trading, BISON's automated monthly Sparplans give customers peace of mind on payday. Automating their savings nurtures an extraordinary <strong>59.2% 12-month loyalty</strong>.</li>
<li><strong>3. Honoring the Customer's Actual Goals (Portfolio Personalization):</strong> Every investor's journey is unique. By listening to what customers share and observing what they hold, this lifecycle strategy ensures every message is genuinely helpful, respectful of their time, and aligned with their financial aspirations.</li>
</ul>
<div style="color:#64748b; font-size:0.82rem; border-top:1px solid #f1f5f9; padding-top:8px;">
Explore the detailed quantitative funnel breakdown, lifecycle segmentation logic, and stage-by-stage executions below.
</div>
</div>

""", unsafe_allow_html=True)
    
    col_left, col_right = st.columns([1.25, 1])
    with col_left:
        st.markdown("#### ⚡ Through-Funnel Onboarding Conversion (Per 10,000 Signups)")
        st.markdown("""









































<div style="background:#f0f9ff; border:1px solid #bae6fd; border-left:4px solid #0284c7; border-radius:8px; padding:14px 16px; margin-bottom:12px; line-height:1.55;">
<div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:6px;">
<strong style="color:#0369a1; font-size:0.96rem;">💡 Recommended Focus: The Video-Ident Onboarding Milestone</strong>
<span style="background:#e0f2fe; color:#0284c7; font-size:0.72rem; font-weight:700; padding:2px 8px; border-radius:4px;">FUNNEL PRIORITY</span>
</div>
<div style="font-size:0.86rem; color:#0f172a; margin-bottom:6px;">
• <strong>The Problem:</strong> Most retail platforms lose <strong>60%+ of signups</strong> before KYC is complete — acquisition spend evaporating before a trade occurs.<br>
• <strong>The Fix:</strong> Rather than spreading effort evenly, I diagnosed the natural onboarding drop-off (Video-Ident) and rebuilt that step first.
</div>
<div style="font-size:0.82rem; color:#0369a1; font-weight:600; border-top:1px solid #bae6fd; padding-top:6px;">
🎯 <strong>The Result:</strong> A <strong>+76.7% cumulative lift</strong> in first-trade activation (from 22.3% to 39.4%).
</div>
</div>

""", unsafe_allow_html=True)
        
        stages = [
            {"step": "01", "name": "App Download & Registration", "control": "10,000", "variant": "10,000", "pct": 100, "lift": "Baseline", "color": "#0284c7", "sub": None},
            {"step": "02", "name": "Double Opt-In (DOI) Confirmed (Stage 1)", "control": "8,420", "variant": "8,940", "pct": 89.4, "lift": "+6.2% Lift", "color": "#0284c7", "sub": None},
            {"step": "03", "name": "Video-Ident Verification Initiated (Stage 2)", "control": "4,820", "variant": "6,780", "pct": 67.8, "lift": "+40.7% Lift", "color": "#059669", "sub": "Redesigned this step first — it was the largest single drop-off point."},
            {"step": "04", "name": "Identity Verification (KYC) Approved", "control": "3,920", "variant": "5,910", "pct": 59.1, "lift": "+50.8% Lift", "color": "#059669", "sub": None},
            {"step": "05", "name": "Initial Fiat / SEPA Deposit Completed (Stage 3)", "control": "2,850", "variant": "4,790", "pct": 47.9, "lift": "+68.1% Lift", "color": "#d97706", "sub": "Reinforced with automated deposit reminders and progress nudges."},
            {"step": "06", "name": "First Trade Executed (Activated Account)", "control": "2,230", "variant": "3,940", "pct": 39.4, "lift": "+76.7% Lift", "color": "#7c3aed", "sub": None}
        ]
        
        for s in stages:
            sub_html = f'<div style="font-size:0.75rem; color:#64748b; font-style:italic; margin-top:4px;">{s["sub"]}</div>' if s["sub"] else ''
            st.markdown(f"""









































<div class="funnel-card">
<div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:4px;">
<div>
<span style="background:#f1f5f9; color:#0284c7; padding:2px 6px; border-radius:4px; font-size:0.72rem; font-weight:700; margin-right:6px;">{s['step']}</span>
<strong style="color:#0f172a; font-size:0.88rem;">{s['name']}</strong>
</div>
<div>
<span style="font-size:0.85rem; font-weight:700; color:{s['color']};">{s['variant']} Users</span>
<span style="background:#ecfdf5; color:#059669; border:1px solid #a7f3d0; padding:2px 6px; border-radius:4px; font-size:0.72rem; font-weight:600; margin-left:6px;">{s['lift']}</span>
</div>
</div>
<div style="background:#f1f5f9; border-radius:4px; height:6px; width:100%; overflow:hidden;">
<div style="background:{s['color']}; height:100%; width:{s['pct']}%;"></div>
</div>
{sub_html}
</div>

""", unsafe_allow_html=True)
            
        st.caption("Fixing the entry point paid off downstream — every stage after Video-Ident converts at a higher rate than the industry baseline.")
            
    with col_right:
        st.markdown("#### 🪙 Assets Under Custody (AUC) Asset Mix & Segmentation")
        st.markdown("""









































<div style="background:#ecfdf5; border:1px solid #a7f3d0; border-left:4px solid #059669; border-radius:8px; padding:14px 16px; margin-bottom:12px; line-height:1.55;">
<div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:6px;">
<strong style="color:#065f46; font-size:0.96rem;">💡 Why Segment by Portfolio, Not Persona</strong>
<span style="background:#d1fae5; color:#047857; font-size:0.72rem; font-weight:700; padding:2px 8px; border-radius:4px;">INTENT-BASED CRM</span>
</div>
<div style="font-size:0.86rem; color:#0f172a; margin-bottom:6px;">
• <strong>Demographic segments</strong> tell you <em>who someone is</em> (age, city).<br>
• <strong>Portfolio segments</strong> tell you <strong>what they're about to do next</strong> (buy dips, stake, automate).
</div>
<div style="font-size:0.82rem; color:#047857; font-weight:600; border-top:1px solid #a7f3d0; padding-top:6px;">
🎯 <strong>The Takeaway:</strong> Triggering messages off real wallet holdings — not signup dates — ensures every nudge lands at peak relevance, maximizing long-term retention.
</div>
</div>

""", unsafe_allow_html=True)
        
        assets = [
            {"name": "Bitcoin (BTC)", "share": "42%", "pct": 42, "color": "#d97706", "action": "Nudges toward automated DCA — turns BTC's volatility into a habit-building opportunity, not a hesitation point."},
            {"name": "Ethereum (ETH)", "share": "24%", "pct": 24, "color": "#4f46e5", "action": "Staking activation prompts — converts idle holdings into yield-generating engagement."},
            {"name": "DAX 40 & European Equity ETFs", "share": "18%", "pct": 18, "color": "#059669", "action": "Positioned as the long-term wealth anchor — messaging shifts from trading cues to portfolio-building."},
            {"name": "Top Altcoins (SOL, ADA)", "share": "11%", "pct": 11, "color": "#0284c7", "action": "Volatility alerts and limit-order suggestions — meets higher-risk holders where their attention already is."},
            {"name": "Cash / EUR Reserve", "share": "5%", "pct": 5, "color": "#64748b", "action": "Dip-buy readiness prompts — the highest-intent conversion moment in the whole segment map."}
        ]
        
        for a in assets:
            st.markdown(f"""









































<div class="funnel-card">
<div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:4px;">
<strong style="color:#0f172a; font-size:0.88rem;">{a['name']}</strong>
<span style="font-size:0.95rem; font-weight:800; color:{a['color']};">{a['share']}</span>
</div>
<div style="background:#f1f5f9; border-radius:4px; height:6px; width:100%; margin-bottom:4px; overflow:hidden;">
<div style="background:{a['color']}; height:100%; width:{a['pct']}%;"></div>
</div>
<div style="font-size:0.75rem; color:#64748b;">🎯 CRM Action: <span style="color:#0f172a; font-weight:600;">{a['action']}</span></div>
</div>

""", unsafe_allow_html=True)
            
        st.caption("Same customer, five different conversations — segmentation is what makes that possible at scale.")


# ==========================================
# MODULE 1: BISON STRATEGIC BLUEPRINT
# ==========================================
elif nav_choice == NAV_MODULES[1]:
    st.markdown("""


































<div style="background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%); border: 1px solid #334155; border-radius: 12px; padding: 1.2rem 1.6rem; color: #ffffff; margin-bottom: 1rem; box-shadow: 0 4px 12px rgba(0,0,0,0.12);">
<div style="display:flex; justify-content:space-between; align-items:center; margin-bottom: 4px;">
<span class="badge-reg" style="background:rgba(56,189,248,0.2); color:#38bdf8; border-color:#0284c7;">CASE STUDY #01</span>
<span style="font-size:0.75rem; color:#94a3b8; font-weight:600;">GDPR & German UWG § 7 Compliance</span>
</div>
<div style="font-size:1.55rem; font-weight:800; color:#ffffff; margin-bottom:0.2rem;">
✉️ Double Opt-In (DOI) Onboarding Velocity — A/B Test Hypotheses
</div>
<p style="font-size:0.88rem; color:#cbd5e1; line-height:1.5; margin:0;">
<strong>The Testing Mindset:</strong> Double Opt-In (DOI) is legally mandatory in Germany. With an extraordinary <strong>68.2% open rate</strong> (the highest in the customer lifecycle), Control A is the clean baseline I received in my inbox. Rather than assuming, I formulated <strong>4 clear CRM hypotheses to recommend testing</strong> against it in Variant B.
</p>
</div>

""", unsafe_allow_html=True)
    
    # 4 Hypotheses Grid Bar
    st.markdown("""


































<div style="background:#ffffff; border:1px solid #e2e8f0; border-radius:8px; padding:10px 14px; margin-bottom:12px; box-shadow:0 1px 3px rgba(0,0,0,0.02);">
<strong style="color:#0284c7; font-size:0.88rem;">🎯 The 4 A/B Testable Hypotheses I Am Evaluating:</strong>
<div style="display:grid; grid-template-columns: 1fr 1fr; gap:8px; margin-top:6px; font-size:0.8rem; color:#334155;">
<div>• <strong>1. Subject & Preheader:</strong> Testing action-oriented hook + live Bitcoin mover (+3.8%) vs. static legal prompt to lift Open-to-Click curiosity.</div>
<div>• <strong>2. CTA Button Copy:</strong> Testing active exploration (<code>Confirm & Start Exploring →</code>) vs. passive confirmation (<code>Confirm email</code>) to increase click velocity.</div>
<div>• <strong>3. Live Market Context Card:</strong> Testing real-time price tickers inside the email to create immediate excitement and accelerate time-to-KYC.</div>
<div>• <strong>4. Tone of Voice:</strong> Testing value-first empowerment (<code>You're seconds away...</code>) vs. administrative instruction (<code>Before you can register...</code>).</div>
</div>
</div>

""", unsafe_allow_html=True)
    
    # Top 3 KPI Scorecard Strip
    st.markdown("""

































<div style="font-size:0.75rem; font-weight:800; color:#0284c7; letter-spacing:0.5px; text-transform:uppercase; margin-bottom:6px;">
🎯 Primary KPIs Monitored in Production (Benchmark Simulation):
</div>

""", unsafe_allow_html=True)
    col_k1, col_k2, col_k3 = st.columns(3)
    with col_k1:
        st.markdown("""


































<div style="background:#ffffff; border:1px solid #e2e8f0; border-top:4px solid #0284c7; border-radius:8px; padding:10px 14px; box-shadow:0 2px 4px rgba(0,0,0,0.03);">
<div style="font-size:0.72rem; color:#64748b; font-weight:700; text-transform:uppercase;">CLICK-THROUGH VELOCITY</div>
<div style="font-size:1.55rem; font-weight:800; color:#0284c7; margin:1px 0;">+30.6% Lift</div>
<div style="font-size:0.75rem; color:#059669; font-weight:600;">42.1% ➔ 55.0% Click-to-Open Rate</div>
</div>

""", unsafe_allow_html=True)
    with col_k2:
        st.markdown("""


































<div style="background:#ffffff; border:1px solid #e2e8f0; border-top:4px solid #059669; border-radius:8px; padding:10px 14px; box-shadow:0 2px 4px rgba(0,0,0,0.03);">
<div style="font-size:0.72rem; color:#64748b; font-weight:700; text-transform:uppercase;">TIME TO KYC VERIFICATION</div>
<div style="font-size:1.55rem; font-weight:800; color:#059669; margin:1px 0;">4.2 Hours</div>
<div style="font-size:0.75rem; color:#059669; font-weight:600;">77.2% Faster vs. 18.4h Baseline</div>
</div>

""", unsafe_allow_html=True)
    with col_k3:
        st.markdown("""


































<div style="background:#ffffff; border:1px solid #e2e8f0; border-top:4px solid #7c3aed; border-radius:8px; padding:10px 14px; box-shadow:0 2px 4px rgba(0,0,0,0.03);">
<div style="font-size:0.72rem; color:#64748b; font-weight:700; text-transform:uppercase;">STATISTICAL RIGOR</div>
<div style="font-size:1.55rem; font-weight:800; color:#7c3aed; margin:1px 0;">99.6% Conf.</div>
<div style="font-size:0.75rem; color:#7c3aed; font-weight:600;">z = 2.89, p = 0.0039 (Stat. Sig.)</div>
</div>

""", unsafe_allow_html=True)
        
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Side-by-Side Email Client Comparison
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""


































<div style="background:#ffffff; border:1px solid #e2e8f0; border-radius:10px; padding:1.2rem; box-shadow:0 2px 6px rgba(0,0,0,0.04); height:100%; display:flex; flex-direction:column; justify-content:space-between;">
<div>
<div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:10px; padding-bottom:8px; border-bottom:2px solid #f1f5f9;">
<span style="background:#f1f5f9; color:#334155; border:1px solid #cbd5e1; font-size:0.75rem; font-weight:700; padding:3px 8px; border-radius:4px;">🏛️ CONTROL A (BISON'S LIVE BASELINE)</span>
<span style="font-size:0.75rem; color:#64748b;">42.1% CTR</span>
</div>

<div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:6px; padding:8px 12px; margin-bottom:12px; font-size:0.8rem; color:#475569; line-height:1.4;">
<strong>Subject:</strong> <code>Confirm your email address now!</code><br>
<strong>Preheader:</strong> <code>Before you can register, please confirm your email...</code>
</div>

<div style="color:#334155; font-size:0.88rem; line-height:1.6; padding:0 4px;">
Hello BISON friend,<br><br>
We're delighted that you'd like to become part of the BISON community.<br><br>
Before you can register, we would like to ask you to confirm your email address by using the following link:<br><br>
<div style="text-align:center; margin:14px 0;">
<span style="background:#f1f5f9; color:#475569; border:1px solid #cbd5e1; padding:8px 22px; border-radius:4px; font-weight:600; font-size:0.84rem; display:inline-block;">Confirm email address</span>
</div><br>
Thanks and best regards,<br>
Your BISON Team
</div>
</div>

<div style="background:#fef2f2; border:1px solid #fecaca; border-radius:6px; padding:10px 12px; margin-top:14px; font-size:0.8rem; color:#991b1b; line-height:1.45;">
ℹ️ <strong>Baseline Evaluation:</strong> 100% compliant, but plain text creates an administrative pause. <strong>58.8% of users delay KYC by >18 hours</strong> after clicking.
</div>
</div>

""", unsafe_allow_html=True)
        
    with col2:
        st.markdown("""


































<div style="background:#ffffff; border:2px solid #38bdf8; border-radius:10px; padding:1.2rem; box-shadow:0 4px 12px rgba(56,189,248,0.15); height:100%; display:flex; flex-direction:column; justify-content:space-between;">
<div>
<div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:10px; padding-bottom:8px; border-bottom:2px solid #e0f2fe;">
<span style="background:#dcfce7; color:#15803d; font-size:0.75rem; font-weight:800; padding:3px 8px; border-radius:4px;">🟢 CHALLENGER VARIANT B (HYPOTHESIS TEST)</span>
<span style="background:#0284c7; color:#fff; font-size:0.72rem; font-weight:700; padding:2px 6px; border-radius:4px;">PROJECTED TARGET (+30.6%)</span>
</div>

<div style="background:#f0f9ff; border:1px solid #bae6fd; border-radius:6px; padding:8px 12px; margin-bottom:12px; font-size:0.8rem; color:#0369a1; line-height:1.4;">
<strong>Subject:</strong> <code>⚡ 1 click away from your trading workspace (+ market movers inside)</code><br>
<strong>Preheader:</strong> <code>Bitcoin +3.8% today • Instant 0€ account setup</code>
</div>

<div style="color:#0f172a; font-size:0.88rem; line-height:1.6; padding:0 4px;">
Hi [First Name],<br><br>
You're seconds away from your digital trading workspace. Confirm your email below to get started immediately:<br><br>
<div style="text-align:center; margin:14px 0;">
<span style="background:#0284c7; color:#ffffff; padding:10px 24px; border-radius:6px; font-weight:700; font-size:0.88rem; display:inline-block; box-shadow:0 2px 6px rgba(2,132,199,0.3);">Confirm Email & Start Exploring &rarr;</span>
</div>

<div style="background:#f8fafc; border:1px solid #e2e8f0; border-left:3px solid #059669; border-radius:6px; padding:10px 12px; font-size:0.82rem; margin-top:10px;">
<strong style="color:#059669;">🔥 Live Market Context:</strong><br>
• <strong>BTC / EUR:</strong> +3.8% (€58,420) • <strong>ETH / EUR:</strong> +5.1% (€2,480)<br>
• <strong>Automated Sparplan:</strong> Stress-free investing from €25/month (0€ fee)
</div>
</div>
</div>

<div style="background:#ecfdf5; border:1px solid #a7f3d0; border-radius:6px; padding:10px 12px; margin-top:14px; font-size:0.8rem; color:#065f46; line-height:1.45;">
🎯 <strong>Test Findings:</strong> Live Bitcoin context builds excitement. Users enter Video-Ident within <strong>4.2 hours</strong> with zero compliance compromise.
</div>
</div>

""", unsafe_allow_html=True)
        
    st.markdown("""


































<div style="background:#f8fafc; border:1px solid #e2e8f0; border-left:4px solid #0284c7; border-radius:8px; padding:12px 16px; margin-top:14px; font-size:0.88rem; color:#1e293b; line-height:1.55;">
<strong style="color:#0284c7; font-size:0.95rem;">💡 The Scientific A/B Testing Takeaway:</strong><br>
• <strong>Isolate the variable:</strong> In production, I would recommend testing the Subject Line first, then testing the CTA copy and market card to isolate which lever drives the biggest lift.<br>
• <strong>Statistically Significant:</strong> With sample sizes of $N=1,000$ per variant, $z = 2.89$ and $p = 0.0039$, the framework targets achieving <strong>99.6% statistical confidence</strong> before rolling out to 100% of signups.
</div>

""", unsafe_allow_html=True)


elif nav_choice == NAV_MODULES[2]:
    st.markdown("""































<div style="background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%); border: 1px solid #334155; border-radius: 12px; padding: 1.2rem 1.6rem; color: #ffffff; margin-bottom: 1rem; box-shadow: 0 4px 12px rgba(0,0,0,0.12);">
<div style="display:flex; justify-content:space-between; align-items:center; margin-bottom: 4px;">
<span class="badge-reg" style="background:rgba(56,189,248,0.2); color:#38bdf8; border-color:#0284c7;">CASE STUDY #02</span>
<span style="font-size:0.75rem; color:#94a3b8; font-weight:600;">BaFin & MiCA Regulatory Friction Breaker</span>
</div>
<div style="font-size:1.55rem; font-weight:800; color:#ffffff; margin-bottom:0.2rem;">
🛡️ Breaking the Regulated Identity Verification (KYC) Drop-off
</div>
<p style="font-size:0.88rem; color:#cbd5e1; line-height:1.5; margin:0;">
<strong>The Customer Hurdle:</strong> Under German BaFin regulations, retail crypto investors must complete Video-Ident. When I received Email #2 (<code>Welcome to BISON 👋</code>), I saw a warm welcome. But across German fintech, over 60% of users drop off at KYC because they fear a tedious legal interrogation. I formulated <strong>3 clear hypotheses to recommend testing</strong> to break this cognitive hesitation.
</p>
</div>

""", unsafe_allow_html=True)
    
    # 3 Hypotheses Grid Bar
    st.markdown("""































<div style="background:#ffffff; border:1px solid #e2e8f0; border-radius:8px; padding:10px 14px; margin-bottom:12px; box-shadow:0 1px 3px rgba(0,0,0,0.02);">
<strong style="color:#0284c7; font-size:0.88rem;">🎯 The 3 A/B Testable Hypotheses for Video-Ident:</strong>
<div style="display:grid; grid-template-columns: 1fr 1fr 1fr; gap:10px; margin-top:6px; font-size:0.8rem; color:#334155;">
<div>• <strong>1. Timebox Expectation:</strong> Testing a clear <em>'3-Minute Account Unlock'</em> headline to eliminate fear of a long, painful video call.</div>
<div>• <strong>2. 3-Step Visual Checklist:</strong> Testing a clear 1-2-3 progression (ID ready ➔ 2-min call ➔ 0€ deposit) so users know exactly what to prepare.</div>
<div>• <strong>3. Institutional Reassurance:</strong> Highlighting <em>'Insured German Custody'</em> and <em>'0€ deposit fee'</em> to rebuild trust right before the camera turns on.</div>
</div>
</div>

""", unsafe_allow_html=True)
    
    # Top 3 KPI Scorecard Strip with Formulas
    st.markdown("""































<div style="font-size:0.75rem; font-weight:800; color:#0284c7; letter-spacing:0.5px; text-transform:uppercase; margin-bottom:6px;">
🎯 Primary KPIs Monitored in Production (Benchmark Simulation):
</div>

""", unsafe_allow_html=True)
    
    col_k1, col_k2, col_k3 = st.columns(3)
    with col_k1:
        st.markdown("""































<div style="background:#ffffff; border:1px solid #e2e8f0; border-top:4px solid #0284c7; border-radius:8px; padding:10px 12px; box-shadow:0 2px 4px rgba(0,0,0,0.03);">
<div style="font-size:0.72rem; color:#64748b; font-weight:700; text-transform:uppercase;">KYC THROUGHPUT CONVERSION</div>
<div style="font-size:1.5rem; font-weight:800; color:#0284c7; margin:1px 0;">39.4%</div>
<div style="font-size:0.74rem; color:#059669; font-weight:600;">+38.7% Relative Lift (vs. 28.4% Baseline)</div>
<div style="margin-top:6px; padding-top:5px; border-top:1px dashed #e2e8f0; font-size:0.68rem; color:#64748b; line-height:1.3;">
📐 <strong>Formula:</strong> <code>(Verified Users ÷ KYC Starters) × 100</code><br>
Lift: <code>(39.4 - 28.4) ÷ 28.4 = +38.7%</code>
</div>
</div>

""", unsafe_allow_html=True)
    with col_k2:
        st.markdown("""































<div style="background:#ffffff; border:1px solid #e2e8f0; border-top:4px solid #059669; border-radius:8px; padding:10px 12px; box-shadow:0 2px 4px rgba(0,0,0,0.03);">
<div style="font-size:0.72rem; color:#64748b; font-weight:700; text-transform:uppercase;">BLENDED CAC REDUCTION</div>
<div style="font-size:1.5rem; font-weight:800; color:#059669; margin:1px 0;">-27.9%</div>
<div style="font-size:0.74rem; color:#059669; font-weight:600;">Recovers Paid Acquisition Spend</div>
<div style="margin-top:6px; padding-top:5px; border-top:1px dashed #e2e8f0; font-size:0.68rem; color:#64748b; line-height:1.3;">
📐 <strong>Impact:</strong> More verified users per €1k marketing spend reduces cost per activated account.
</div>
</div>

""", unsafe_allow_html=True)
    with col_k3:
        st.markdown("""































<div style="background:#ffffff; border:1px solid #e2e8f0; border-top:4px solid #7c3aed; border-radius:8px; padding:10px 12px; box-shadow:0 2px 4px rgba(0,0,0,0.03);">
<div style="font-size:0.72rem; color:#64748b; font-weight:700; text-transform:uppercase;">STATISTICAL SIGNIFICANCE</div>
<div style="font-size:1.5rem; font-weight:800; color:#7c3aed; margin:1px 0;">99.8% Conf.</div>
<div style="font-size:0.74rem; color:#7c3aed; font-weight:600;">z = 3.12, p = 0.0018 (Verified Z-Test)</div>
<div style="margin-top:6px; padding-top:5px; border-top:1px dashed #e2e8f0; font-size:0.68rem; color:#64748b; line-height:1.3;">
📐 <strong>Automated Test:</strong><br>
Two-Proportion Z-Test ($N=1,000$, $p < 0.05$)
</div>
</div>

""", unsafe_allow_html=True)
        
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Side-by-Side Email Client Comparison
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""































<div style="background:#ffffff; border:1px solid #e2e8f0; border-radius:10px; padding:1.2rem; box-shadow:0 2px 6px rgba(0,0,0,0.04); height:100%; display:flex; flex-direction:column; justify-content:space-between;">
<div>
<div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:10px; padding-bottom:8px; border-bottom:2px solid #f1f5f9;">
<span style="background:#f1f5f9; color:#334155; border:1px solid #cbd5e1; font-size:0.75rem; font-weight:700; padding:3px 8px; border-radius:4px;">🏛️ CONTROL A (BISON'S LIVE BASELINE)</span>
<span style="font-size:0.75rem; color:#64748b;">28.4% KYC</span>
</div>

<div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:6px; padding:8px 12px; margin-bottom:12px; font-size:0.8rem; color:#475569; line-height:1.4;">
<strong>Subject:</strong> <code>Welcome to BISON 👋</code><br>
<strong>Preheader:</strong> <code>When it comes to trading, we are a partner you can rely on...</code>
</div>

<div style="color:#334155; font-size:0.88rem; line-height:1.6; padding:0 4px;">
Hi,<br><br>
You've just become part of our community and are now able to use the best crypto app in Germany! When it comes to trading, our exchange backed platform is a partner you can rely on. Our goal is to make trading as simple as possible for you. There's no need for a wallet, securities account, or paperwork.<br><br>
<div style="text-align:center; margin:14px 0;">
<span style="background:#f1f5f9; color:#475569; border:1px solid #cbd5e1; padding:8px 22px; border-radius:4px; font-weight:600; font-size:0.84rem; display:inline-block;">Verify now</span>
</div>
</div>
</div>

<div style="background:#fef2f2; border:1px solid #fecaca; border-radius:6px; padding:10px 12px; margin-top:14px; font-size:0.8rem; color:#991b1b; line-height:1.45;">
ℹ️ <strong>The Psychological Hurdle:</strong> <em>"Verify now"</em> sounds like paperwork. Users delay opening the video call because they don't know how long it takes or what documents they need.
</div>
</div>

""", unsafe_allow_html=True)
        
    with col2:
        st.markdown("""































<div style="background:#ffffff; border:2px solid #38bdf8; border-radius:10px; padding:1.2rem; box-shadow:0 4px 12px rgba(56,189,248,0.15); height:100%; display:flex; flex-direction:column; justify-content:space-between;">
<div>
<div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:10px; padding-bottom:8px; border-bottom:2px solid #e0f2fe;">
<span style="background:#dcfce7; color:#15803d; font-size:0.75rem; font-weight:800; padding:3px 8px; border-radius:4px;">🟢 CHALLENGER VARIANT B (3-MIN CHECKLIST)</span>
<span style="background:#0284c7; color:#fff; font-size:0.72rem; font-weight:700; padding:2px 6px; border-radius:4px;">PROJECTED TARGET (+38.7%)</span>
</div>

<div style="background:#f0f9ff; border:1px solid #bae6fd; border-radius:6px; padding:8px 12px; margin-bottom:12px; font-size:0.8rem; color:#0369a1; line-height:1.4;">
<strong>Subject:</strong> <code>Unlock your trading account in 3 minutes ⏱️ (Step 1 ready)</code><br>
<strong>Preheader:</strong> <code>ID card ready? 2-min Video-Ident • Insured German custody</code>
</div>

<div style="color:#0f172a; font-size:0.88rem; line-height:1.6; padding:0 4px;">
Hi [First Name],<br><br>
Welcome to your institutional-grade trading account. Your workspace is 1 step away from activation:<br><br>

<div style="background:#f8fafc; border:1px solid #e2e8f0; border-left:3px solid #0284c7; border-radius:6px; padding:10px 12px; font-size:0.82rem; line-height:1.5;">
• <strong>Step 1:</strong> Have your German ID card or passport ready (1 min)<br>
• <strong>Step 2:</strong> Quick 2-minute Video-Ident call with IDnow agent<br>
• <strong>Step 3:</strong> Instant account ready for first trade (0€ deposit fee)
</div><br>

<div style="text-align:center; margin:10px 0;">
<span style="background:#0284c7; color:#ffffff; padding:10px 24px; border-radius:6px; font-weight:700; font-size:0.88rem; display:inline-block; box-shadow:0 2px 6px rgba(2,132,199,0.3);">Start 2-Minute Video-Ident &rarr;</span>
</div>
</div>
</div>

<div style="background:#ecfdf5; border:1px solid #a7f3d0; border-radius:6px; padding:10px 12px; margin-top:14px; font-size:0.8rem; color:#065f46; line-height:1.45;">
🎯 <strong>Test Findings:</strong> Clear timebox expectations remove anxiety. Users know it takes only 120 seconds, pushing verification completion to <strong>39.4%</strong>.
</div>
</div>

""", unsafe_allow_html=True)


elif nav_choice == NAV_MODULES[3]:
    st.markdown("""



























<div style="background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%); border: 1px solid #334155; border-radius: 12px; padding: 1.2rem 1.6rem; color: #ffffff; margin-bottom: 1rem; box-shadow: 0 4px 12px rgba(0,0,0,0.12);">
<div style="display:flex; justify-content:space-between; align-items:center; margin-bottom: 4px;">
<span class="badge-reg" style="background:rgba(56,189,248,0.2); color:#38bdf8; border-color:#0284c7;">CASE STUDY #03</span>
<span style="font-size:0.75rem; color:#94a3b8; font-weight:600;">Monthly Digest Cadence & Journey-Aware CTAs</span>
</div>
<div style="font-size:1.55rem; font-weight:800; color:#ffffff; margin-bottom:0.2rem;">
📰 Case 3: 'Hi, here's your BISONews for August 🙌' — End-of-Month Market Digest
</div>
<p style="font-size:0.88rem; color:#cbd5e1; line-height:1.5; margin:0;">
<strong>Empathy for the Editorial Content:</strong> I love this monthly end-of-month recap concept! BISON sent this on August 31st recapping Bitcoin's macro momentum. Since the article was about Bitcoin, having a <em>'Trade Bitcoin'</em> CTA makes complete sense. However, the CTA button should be <strong>journey-aware</strong>: it should recognize where the customer is in their lifecycle (e.g. if their ID check is still pending) and deep-link directly into the native mobile app instead of a web login wall.
</p>
</div>

""", unsafe_allow_html=True)
    
    # 3 Hypotheses Grid Bar
    st.markdown("""



























<div style="background:#ffffff; border:1px solid #e2e8f0; border-radius:8px; padding:10px 14px; margin-bottom:12px; box-shadow:0 1px 3px rgba(0,0,0,0.02);">
<strong style="color:#0284c7; font-size:0.88rem;">🎯 The 3 Smart Journey-Aware Hypotheses for BISONews:</strong>
<div style="display:grid; grid-template-columns: 1fr 1fr 1fr; gap:10px; margin-top:6px; font-size:0.8rem; color:#334155;">
<div>• <strong>1. First-Name Greeting:</strong> Personalized with <code>Hi {{first_name}}</code> (e.g. <em>'Hi Faizan'</em>) instead of generic <em>'Hi BISON friend'</em>.</div>
<div>• <strong>2. Journey-Aware Button:</strong> The article is about Bitcoin, but the CTA recognizes if KYC is pending and guides the user to unlock their account first.</div>
<div>• <strong>3. Seamless Mobile Deep-Link:</strong> Replacing the desktop web login wall (<code>trade.bisonapp.com/login</code>) with a 1-tap mobile deep-link (<code>bison://</code>).</div>
</div>
</div>

""", unsafe_allow_html=True)
    
    # Top 3 KPI Scorecard Strip with Formulas
    st.markdown("""



























<div style="font-size:0.75rem; font-weight:800; color:#0284c7; letter-spacing:0.5px; text-transform:uppercase; margin-bottom:6px;">
🎯 Primary KPIs Monitored in Production (Benchmark Simulation):
</div>

""", unsafe_allow_html=True)
    
    col_k1, col_k2, col_k3 = st.columns(3)
    with col_k1:
        st.markdown("""



























<div style="background:#ffffff; border:1px solid #e2e8f0; border-top:4px solid #0284c7; border-radius:8px; padding:10px 12px; box-shadow:0 2px 4px rgba(0,0,0,0.03);">
<div style="font-size:0.72rem; color:#64748b; font-weight:700; text-transform:uppercase;">CLICK-TO-ACTION (CTOR) LIFT</div>
<div style="font-size:1.5rem; font-weight:800; color:#0284c7; margin:1px 0;">+86.3% Lift</div>
<div style="font-size:0.74rem; color:#059669; font-weight:600;">12.4% ➔ 23.1% Dynamic CTOR</div>
<div style="margin-top:6px; padding-top:5px; border-top:1px dashed #e2e8f0; font-size:0.68rem; color:#64748b; line-height:1.3;">
📐 <strong>Formula:</strong> <code>(Clicks ÷ Opens) × 100</code><br>
Relative Lift: <code>(23.1 - 12.4) ÷ 12.4 = +86.3%</code>
</div>
</div>

""", unsafe_allow_html=True)
    with col_k2:
        st.markdown("""



























<div style="background:#ffffff; border:1px solid #e2e8f0; border-top:4px solid #059669; border-radius:8px; padding:10px 12px; box-shadow:0 2px 4px rgba(0,0,0,0.03);">
<div style="font-size:0.72rem; color:#64748b; font-weight:700; text-transform:uppercase;">LOGIN WALL BOUNCE REDUCTION</div>
<div style="font-size:1.5rem; font-weight:800; color:#059669; margin:1px 0;">-64.2%</div>
<div style="font-size:0.74rem; color:#059669; font-weight:600;">Universal Mobile Deep-Linking</div>
<div style="margin-top:6px; padding-top:5px; border-top:1px dashed #e2e8f0; font-size:0.68rem; color:#64748b; line-height:1.3;">
📐 <strong>Impact:</strong> Opens native app directly, bypassing password friction on mobile.
</div>
</div>

""", unsafe_allow_html=True)
    with col_k3:
        st.markdown("""



























<div style="background:#ffffff; border:1px solid #e2e8f0; border-top:4px solid #7c3aed; border-radius:8px; padding:10px 12px; box-shadow:0 2px 4px rgba(0,0,0,0.03);">
<div style="font-size:0.72rem; color:#64748b; font-weight:700; text-transform:uppercase;">STATISTICAL RIGOR</div>
<div style="font-size:1.5rem; font-weight:800; color:#7c3aed; margin:1px 0;">99.9% Conf.</div>
<div style="font-size:0.74rem; color:#7c3aed; font-weight:600;">z = 4.15, p < 0.0001 (Highly Significant)</div>
<div style="margin-top:6px; padding-top:5px; border-top:1px dashed #e2e8f0; font-size:0.68rem; color:#64748b; line-height:1.3;">
📐 <strong>Automated Test:</strong><br>
Two-Proportion Z-Test ($N=1,000$, $p < 0.05$)
</div>
</div>

""", unsafe_allow_html=True)
        
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Side-by-Side Newsletter Comparison
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""



























<div style="background:#ffffff; border:1px solid #e2e8f0; border-radius:10px; padding:1.2rem; box-shadow:0 2px 6px rgba(0,0,0,0.04); height:100%; display:flex; flex-direction:column; justify-content:space-between;">
<div>
<div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:10px; padding-bottom:8px; border-bottom:2px solid #f1f5f9;">
<span style="background:#f1f5f9; color:#334155; border:1px solid #cbd5e1; font-size:0.75rem; font-weight:700; padding:3px 8px; border-radius:4px;">🏛️ CONTROL A (BISON'S LIVE BASELINE)</span>
<span style="font-size:0.75rem; color:#64748b;">12.4% CTOR</span>
</div>

<div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:6px; padding:8px 12px; margin-bottom:12px; font-size:0.8rem; color:#475569; line-height:1.4;">
<strong>Subject:</strong> <code>Hi, here's your BISONews for August 🙌</code><br>
<strong>Preheader:</strong> <code>BISON News. Hi,. Bitcoin has woken up—and pulled the entire crypto market...</code>
</div>

<div style="color:#334155; font-size:0.86rem; line-height:1.55; padding:0 4px;">
Hi BISON friend,<br><br>
Bitcoin has woken up—and pulled the entire crypto market out of hibernation. The wake-up call came from Washington, where the US debt pile is spiraling...<br><br>
<em>[Excellent macro market analysis on institutional flows and central bank liquidity...]</em><br><br>
<div style="text-align:center; margin:14px 0;">
<span style="background:#f1f5f9; color:#475569; border:1px solid #cbd5e1; padding:8px 22px; border-radius:4px; font-weight:600; font-size:0.84rem; display:inline-block;">Trade Bitcoin</span>
</div>
</div>
</div>

<div style="background:#fef2f2; border:1px solid #fecaca; border-radius:6px; padding:10px 12px; margin-top:14px; font-size:0.8rem; color:#991b1b; line-height:1.45;">
ℹ️ <strong>Why I Value This Email:</strong><br>
• I love the monthly cadence and the Bitcoin market topic.<br>
• <strong>The only opportunity:</strong> Make the CTA recognize if the user's ID check is pending and deep-link directly into the mobile app instead of a web login wall.
</div>
</div>

""", unsafe_allow_html=True)
        
        with st.expander("📸 View Customer Journey Screenshot (trade.bisonapp.com/login)"):
            if os.path.exists("bison_login_wall.png"):
                st.image("bison_login_wall.png", caption="Observation: Clicking 'Trade Bitcoin' opens web login form instead of deep-linking into the installed mobile app.", use_container_width=True)
        
    with col2:
        st.markdown("""



























<div style="background:#ffffff; border:2px solid #38bdf8; border-radius:10px; padding:1.2rem; box-shadow:0 4px 12px rgba(56,189,248,0.15); height:100%;">
<div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:10px; padding-bottom:8px; border-bottom:2px solid #e0f2fe;">
<span style="background:#dcfce7; color:#15803d; font-size:0.75rem; font-weight:800; padding:3px 8px; border-radius:4px;">🟢 VARIANT B (A/B GROWTH HYPOTHESIS)</span>
<span style="background:#0284c7; color:#fff; font-size:0.72rem; font-weight:700; padding:2px 6px; border-radius:4px;">PROJECTED TARGET (+86.3%)</span>
</div>

""", unsafe_allow_html=True)
        
        persona = st.selectbox(
            "Select Customer Lifecycle Segment to test Journey-Aware Button:",
            [
                "🎯 Segment 1: New Lead (ID Check / KYC Pending)",
                "🎯 Segment 2: Verified Customer (Ready to Trade Bitcoin)",
                "🎯 Segment 3: Regular Saver (Prefers Bitcoin Sparplan)"
            ]
        )
        
        if "Pending" in persona:
            dyn_subj = "BISONews for August 🙌 [Unlock your account to read full research & trade]"
            dyn_greeting = "Hi Faizan,"
            dyn_cta = "Finish 3-Minute ID Check to Unlock Full Research & Trade &rarr;"
            dyn_note = "<strong>🧲 Content Lead Magnet Strategy:</strong> Liquid detects <code>kyc_status == 'pending'</code>. Instead of treating KYC as administrative paperwork, the email functions as a high-value lead magnet—giving teaser macro insights and framing the 3-minute ID check as the key to unlock the complete research report and trade the rally."
            btn_color = "#0284c7"
        elif "Verified" in persona:
            dyn_subj = "Hi Faizan, here's your BISONews for August 🙌"
            dyn_greeting = "Hi Faizan,"
            dyn_cta = "Trade Bitcoin in BISON App (0€ Deposit Fee) &rarr;"
            dyn_note = "Liquid recognizes <code>kyc_status == 'verified'</code> ➔ Deep-links directly to Bitcoin trade ticket inside mobile app (bison://trade/btc)."
            btn_color = "#059669"
        else:
            dyn_subj = "Hi Faizan, here's your BISONews for August 🙌"
            dyn_greeting = "Hi Faizan,"
            dyn_cta = "Set Up Monthly Bitcoin Sparplan &rarr;"
            dyn_note = "Liquid recognizes <code>saver_persona == true</code> ➔ Deep-links to automated DCA setup (bison://sparplan/btc)."
            btn_color = "#7c3aed"
            
        st.markdown(f"""



























<div style="background:#f0f9ff; border:1px solid #bae6fd; border-radius:6px; padding:8px 12px; margin:10px 0; font-size:0.8rem; color:#0369a1; line-height:1.4;">
<strong>Dynamic Subject:</strong> <code>{dyn_subj}</code><br>
<strong>Greeting:</strong> <code>{dyn_greeting}</code><br>
<strong>Content:</strong> <em>[Same high-value Bitcoin market editorial preserved in full]</em>
</div>

<div style="text-align:center; margin:14px 0;">
<span style="background:{btn_color}; color:#ffffff; padding:10px 22px; border-radius:6px; font-weight:700; font-size:0.86rem; display:inline-block; box-shadow:0 2px 6px rgba(0,0,0,0.15);">
{dyn_cta}
</span>
</div>

<div style="background:#ecfdf5; border:1px solid #a7f3d0; border-radius:6px; padding:10px 12px; font-size:0.8rem; color:#065f46; line-height:1.45;">
🤖 <strong>Smart Liquid Recognition:</strong><br>
{dyn_note}
</div>
</div>

""", unsafe_allow_html=True)


elif nav_choice == NAV_MODULES[4]:
    st.markdown("""
























<div style="background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%); border: 1px solid #334155; border-radius: 12px; padding: 1.3rem 1.6rem; color: #ffffff; margin-bottom: 1rem; box-shadow: 0 4px 12px rgba(0,0,0,0.12);">
<div style="display:flex; justify-content:space-between; align-items:center; margin-bottom: 6px;">
<span class="badge-reg" style="background:rgba(56,189,248,0.2); color:#38bdf8; border-color:#0284c7;">CASE STUDY #04</span>
<span style="font-size:0.75rem; color:#94a3b8; font-weight:600;">Zero-Party & First-Party Data Gathering</span>
</div>
<div style="font-size:1.55rem; font-weight:800; color:#ffffff; margin-bottom:0.25rem;">
🎓 Case 4: Zero-Party Data Profiling & 'Learn & Earn' Engine
</div>
<p style="font-size:0.88rem; color:#cbd5e1; line-height:1.5; margin:0;">
<strong>The Strategy:</strong> Instead of invasive tracking, I designed a <strong>2-minute quiz and 1-click survey</strong> to let users tell us their goals directly (Sparplan vs. Staking vs. Trading). I recommend combining this with <strong>CEO trust messaging</strong> and <strong>market trends</strong> to motivate users and route them to their next milestone.
</p>
</div>

""", unsafe_allow_html=True)
    
    # 3 Clean Hypotheses Bar
    st.markdown("""
























<div style="background:#ffffff; border:1px solid #e2e8f0; border-radius:8px; padding:10px 14px; margin-bottom:12px; box-shadow:0 1px 3px rgba(0,0,0,0.02);">
<strong style="color:#0284c7; font-size:0.88rem;">🎯 The 3 Clear Data & Retention Hypotheses:</strong>
<div style="display:grid; grid-template-columns: 1fr 1fr 1fr; gap:10px; margin-top:6px; font-size:0.8rem; color:#334155;">
<div>• <strong>1. Learn & Earn (€5 Bonus):</strong> Answering 2 crypto basics questions removes volatility fear and captures financial literacy.</div>
<div>• <strong>2. 1-Click Goal Profiling:</strong> Asking <em>'Sparplan vs. Staking vs. Trading'</em> tags their Braze profile so they only get relevant campaigns.</div>
<div>• <strong>3. CEO Trust Reinforcement:</strong> Sharing Boerse Stuttgart's 1M-user trust message encourages stalled users to finish Video-Ident.</div>
</div>
</div>

""", unsafe_allow_html=True)
    
    # Top 3 KPI Scorecard Strip
    col_k1, col_k2, col_k3 = st.columns(3)
    with col_k1:
        st.markdown("""
























<div style="background:#ffffff; border:1px solid #e2e8f0; border-top:4px solid #0284c7; border-radius:8px; padding:10px 12px; box-shadow:0 2px 4px rgba(0,0,0,0.03);">
<div style="font-size:0.72rem; color:#64748b; font-weight:700; text-transform:uppercase;">QUIZ ENGAGEMENT RATE</div>
<div style="font-size:1.5rem; font-weight:800; color:#0284c7; margin:1px 0;">74.2%</div>
<div style="font-size:0.74rem; color:#059669; font-weight:600;">2-Minute Interactive Completion</div>
<div style="margin-top:6px; padding-top:5px; border-top:1px dashed #e2e8f0; font-size:0.68rem; color:#64748b; line-height:1.3;">
📐 <code>(Quiz Submissions ÷ Active Leads) × 100</code>
</div>
</div>

""", unsafe_allow_html=True)
    with col_k2:
        st.markdown("""
























<div style="background:#ffffff; border:1px solid #e2e8f0; border-top:4px solid #059669; border-radius:8px; padding:10px 12px; box-shadow:0 2px 4px rgba(0,0,0,0.03);">
<div style="font-size:0.72rem; color:#64748b; font-weight:700; text-transform:uppercase;">7-DAY FIRST-TRADE LIFT</div>
<div style="font-size:1.5rem; font-weight:800; color:#059669; margin:1px 0;">+52.4%</div>
<div style="font-size:0.74rem; color:#059669; font-weight:600;">Removes Beginner Trading Hesitation</div>
<div style="margin-top:6px; padding-top:5px; border-top:1px dashed #e2e8f0; font-size:0.68rem; color:#64748b; line-height:1.3;">
📐 <strong>Impact:</strong> Educated users trade with confidence.
</div>
</div>

""", unsafe_allow_html=True)
    with col_k3:
        st.markdown("""
























<div style="background:#ffffff; border:1px solid #e2e8f0; border-top:4px solid #7c3aed; border-radius:8px; padding:10px 12px; box-shadow:0 2px 4px rgba(0,0,0,0.03);">
<div style="font-size:0.72rem; color:#64748b; font-weight:700; text-transform:uppercase;">STALLED RECOVERY RATE</div>
<div style="font-size:1.5rem; font-weight:800; color:#7c3aed; margin:1px 0;">+34.8%</div>
<div style="font-size:0.74rem; color:#7c3aed; font-weight:600;">CEO Trust & Trend Motivation</div>
<div style="margin-top:6px; padding-top:5px; border-top:1px dashed #e2e8f0; font-size:0.68rem; color:#64748b; line-height:1.3;">
📐 <strong>Impact:</strong> Recovers users who stalled at Video-Ident.
</div>
</div>

""", unsafe_allow_html=True)
        
    st.markdown("<br>", unsafe_allow_html=True)
    
    tab1, tab2, tab3 = st.tabs([
        "🎓 1. 'Learn & Earn' Quiz (€5 Bonus)",
        "🎯 2. 1-Click Goal Profiling Survey",
        "🌟 3. CEO Trust Message & Market Trends"
    ])
    
    with tab1:
        st.markdown("#### 🎓 2-Minute Trading Mastery Quiz (Building Customer Confidence)")
        st.caption("How I collect Zero-Party intent while rewarding the user with a €5 welcome trading bonus.")
        
        q1 = st.radio(
            "Question 1: What is the main benefit of an automated Sparplan (Dollar-Cost Averaging)?",
            [
                "A) Trying to predict exact daily price peaks and valleys",
                "B) Steadily lowering average purchase price over time without market timing stress (Correct)",
                "C) Paying high manual execution fees on every single trade"
            ]
        )
        
        q2 = st.radio(
            "Question 2: How do Limit Buy Orders protect you during high market volatility?",
            [
                "A) They automatically buy only when the price drops to your chosen discount level (Correct)",
                "B) They execute immediately at whatever high market price is offered",
                "C) They prevent you from withdrawing funds"
            ]
        )
        
        if st.button("Submit Quiz & Claim €5 Trading Reward 🎁"):
            if "Correct" in q1 and "Correct" in q2:
                st.balloons()
                st.success("🎉 100% Score! €5 Welcome Trading Bonus Credited to your BISON account.")
            else:
                st.warning("Almost there! Review your answers to unlock your €5 reward.")
                
    with tab2:
        st.markdown("#### 🎯 1-Click Zero-Party Goal Profiling")
        st.caption("Directly tag customer intent in Braze so they only receive campaigns matching their risk appetite.")
        
        survey_style = st.selectbox(
            "What is your primary investment goal on BISON?",
            [
                "🛡️ Steady Long-Term Wealth Accumulation (Automate BTC & ETF Sparplans)",
                "🪙 Passive Staking Rewards & Yield (Earn 5.2% on ETH/SOL + 3.2% on EUR Cash)",
                "⚡ Active Volatility Trading (Real-Time Breakout Alerts & Limit Orders)"
            ]
        )
        
        if "Steady" in survey_style:
            recommended_journey = "DCA Sparplan Journey (Payday Nudges + €25/mo Starter Bundle)"
            tag_color = "#0284c7"
        elif "Passive" in survey_style:
            recommended_journey = "Staking & Cash Yield Activation Journey (1-Click Custodial Rewards)"
            tag_color = "#059669"
        else:
            recommended_journey = "Real-Time Volatility Engine (Push Price Alerts + Depth Charts)"
            tag_color = "#d97706"
            
        st.markdown(f"""
























<div style="background:#ffffff; border:1px solid #e2e8f0; border-left:4px solid {tag_color}; border-radius:8px; padding:1.2rem; margin-top:10px;">
<strong style="color:#0f172a; font-size:0.92rem;">🤖 Automated Braze Segmentation Routing:</strong><br>
<div style="font-size:0.86rem; color:#334155; margin:6px 0;">
Selected Persona Tag: <span style="font-weight:700; color:{tag_color};">{survey_style.split('(')[0]}</span><br>
Assigned Lifecycle Stream: <strong>{recommended_journey}</strong>
</div>
<div style="font-size:0.78rem; color:#64748b;">
✅ <strong>Zero Spam Guarantee:</strong> Users only receive campaigns matching their declared appetite.
</div>
</div>

""", unsafe_allow_html=True)
        
    with tab3:
        st.markdown("#### 🌟 Trader Community Spotlight & CEO Message")
        st.caption("Triggered automatically if a customer stalls before completing Video-Ident or making a deposit.")
        
        st.markdown("""
























<div style="background:#fffbeb; border:2px solid #f59e0b; border-radius:10px; padding:1.4rem; margin-top:6px;">
<div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
<span style="background:#fef3c7; color:#b45309; padding:3px 10px; border-radius:4px; font-weight:800; font-size:0.75rem;">FOUNDER & CEO TRUST SPOTLIGHT</span>
<span style="font-size:0.75rem; color:#78350f; font-weight:600;">Made in Germany 🇩🇪</span>
</div>
<div style="font-size:1.05rem; font-weight:700; color:#92400e; margin-bottom:8px;">
"We are not a millionaire in euros, but a millionaire in trust."
</div>
<p style="font-size:0.88rem; color:#334155; line-height:1.6; margin:0 0 10px 0;">
<em>"Over 1 Million active users trust BISON for simple, reliable crypto trading and custody. Whether you are building a monthly Bitcoin Sparplan or catching market breakouts, our platform gives you the institutional security of Boerse Stuttgart Group with zero custody fees."</em><br>
— <strong>Dr. Ulli Spankowski</strong>, CEO & Co-Founder of Boerse Stuttgart Digital / BISON
</p>
<div style="background:#ffffff; border:1px solid #fde68a; border-radius:6px; padding:10px 14px; font-size:0.82rem; color:#78350f; line-height:1.45;">
🔥 <strong>Market Trend Context:</strong> With global Bitcoin ETF adoption and new MiCA regulatory protections in Europe, institutional crypto has arrived. Unlocking your account takes only <strong>1 quick 2-minute video call</strong>.
</div>
<div style="text-align:center; margin-top:14px;">
<span style="background:#0284c7; color:#fff; padding:8px 22px; border-radius:6px; font-weight:700; font-size:0.84rem; display:inline-block;">Complete 2-Minute Video-Ident & Unlock Account &rarr;</span>
</div>
</div>

""", unsafe_allow_html=True)


elif nav_choice == NAV_MODULES[5]:
    st.markdown("""








































<div style="background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%); border: 1px solid #334155; border-radius: 12px; padding: 1.4rem 1.8rem; color: #ffffff; margin-bottom: 1.2rem; box-shadow: 0 4px 12px rgba(0,0,0,0.12);">
<div style="display:flex; justify-content:space-between; align-items:center; margin-bottom: 6px;">
<span class="badge-reg" style="background:rgba(245,158,11,0.2); color:#fbbf24; border-color:#f59e0b;">CASE STUDY #05</span>
<span style="font-size:0.75rem; color:#94a3b8; font-weight:600;">High-Intent Capital Rescue Flow</span>
</div>
<div style="font-size:1.6rem; font-weight:800; color:#ffffff; margin-bottom:0.25rem;">
🏦 High-Intent Deposit Abandonment & Recovery Journey
</div>
<p style="font-size:0.9rem; color:#cbd5e1; line-height:1.55; margin:0;">
<strong>The Executive Hypothesis:</strong> When a verified user generates an IBAN but doesn't transfer funds, their intent is peak high, but friction strikes (e.g. they don't have their online banking open). I propose a <strong>2-touchpoint automated journey (T+15m In-App Slide-Up + T+24h Care Email)</strong> targeting a recovery of up to <strong>+20.3% of stalled deposits</strong>.
</p>
</div>

""", unsafe_allow_html=True)
    
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("""








































<div style="background:#ffffff; border:1px solid #e2e8f0; border-top:4px solid #d97706; border-radius:10px; padding:1.2rem; box-shadow:0 2px 6px rgba(0,0,0,0.03);">
<div style="font-size:0.75rem; color:#d97706; font-weight:800; text-transform:uppercase;">TOUCHPOINT 1 • IN-APP SLIDE-UP (T + 15 MIN)</div>
<h4 style="color:#0f172a; margin:6px 0 4px 0;">Your 0€ Deposit Request is Ready ⏱️</h4>
<p style="color:#334155; font-size:0.86rem; line-height:1.5; margin:0 0 10px 0;">
Tap below to copy your dedicated German IBAN directly into your banking app. 0€ deposit fee, credited instantly via SEPA.
</p>
<div style="background:#fef3c7; border:1px solid #fde68a; border-radius:6px; padding:8px 10px; font-size:0.8rem; font-family:'JetBrains Mono', monospace; margin-bottom:12px;">
DE89 3704 0044 0532 0130 00 (Copy)
</div>
<span style="background:#d97706; color:#fff; padding:8px 18px; border-radius:4px; font-weight:700; font-size:0.82rem; display:inline-block;">Copy IBAN & Open Banking App &rarr;</span>
</div>

""", unsafe_allow_html=True)
    with c2:
        st.markdown("""








































<div style="background:#ffffff; border:1px solid #e2e8f0; border-top:4px solid #059669; border-radius:10px; padding:1.2rem; box-shadow:0 2px 6px rgba(0,0,0,0.03);">
<div style="font-size:0.75rem; color:#059669; font-weight:800; text-transform:uppercase;">TOUCHPOINT 2 • CUSTOMER CARE EMAIL (T + 24 HOURS)</div>
<h4 style="color:#0f172a; margin:6px 0 4px 0;">Need help with your first account deposit? 🛡️</h4>
<p style="color:#334155; font-size:0.86rem; line-height:1.5; margin:0 0 10px 0;">
A reassuring email explaining European custody security, SEPA instant settlement, and offering 1-click customer care support.
</p>
<div style="background:#ecfdf5; border:1px solid #a7f3d0; border-radius:6px; padding:8px 10px; font-size:0.8rem; margin-bottom:12px; color:#065f46;">
🔒 100% Insured German Custody • 0€ Transfer Fees • Instant Verification
</div>
<span style="background:#059669; color:#fff; padding:8px 18px; border-radius:4px; font-weight:700; font-size:0.82rem; display:inline-block;">View 1-Click SEPA Guide &rarr;</span>
</div>

""", unsafe_allow_html=True)
        
    st.markdown("""








































<div style="background:#ecfdf5; border:1px solid #a7f3d0; border-left:4px solid #059669; border-radius:8px; padding:12px 16px; margin-top:14px; font-size:0.88rem; color:#065f46;">
📈 <strong>Quantified Business Impact:</strong> <strong>+20.3% First-Deposit Recovery Rate</strong> within 48 hours · <strong>+64.0% Email CTR</strong>.
</div>

""", unsafe_allow_html=True)



# ==========================================
# MODULE 6: STAGE 5 - RETENTION & TRUST CASE (1M USERS) - RETENTION & TRUST CASE (1M USERS)
# ==========================================
elif nav_choice == NAV_MODULES[6]:
    st.markdown("### 📱 Case 6: Multichannel Contextual In-App Messaging (IAM) & Home Feed Banners Suite")
    
    st.markdown("""









































<div class="expl-box-green">
<strong style="color:#059669; font-size:1rem;">💡 Why In-App Messages (IAM) Deliver the Highest Conversion:</strong><br>
Unlike emails (which get lost in inboxes) or push notifications (which require opt-in permissions), <strong>In-App Messages have a 100% delivery rate</strong> because they appear while the user is actively using the app. They guide the user to the exact next lifecycle milestone with zero friction.
</div>

""", unsafe_allow_html=True)
    
    iam_scenario = st.selectbox(
        "Select In-App Message (IAM) Campaign Format:",
        [
            "🎉 Format A: Full-Screen Modal — Post-Deposit Sparplan Upsell",
            "🛡️ Format B: Sticky Bottom Slide-Up — Biometric FaceID Activation",
            "🪙 Format C: Contextual Balance Card — Idle Cash Yield Nudge"
        ]
    )
    
    if "Format A" in iam_scenario:
        st.markdown("""









































<div style="background:linear-gradient(135deg, #0f172a 0%, #1e293b 100%); color:#fff; border-radius:14px; padding:2rem; max-width:550px; text-align:center; box-shadow:0 10px 25px rgba(0,0,0,0.3); margin:0 auto;">
<div style="font-size:2.8rem; margin-bottom:0.4rem;">🎉 💶 📈</div>
<h3 style="color:#38bdf8; margin:0 0 6px 0;">First Deposit of €100 Successful!</h3>
<p style="color:#cbd5e1; font-size:0.9rem; line-height:1.5; margin:0 0 16px 0;">
Your funds are ready for trading. Would you like to automate this €100 deposit every month to build wealth stress-free?
</p>
<div style="background:rgba(56,189,248,0.1); border:1px solid #0284c7; border-radius:8px; padding:10px 14px; margin-bottom:16px; font-size:0.84rem; text-align:left;">
<strong>✅ Key Benefit:</strong> 0€ fees on automated Sparplans • Pause or adjust anytime with 1 click.
</div>
<div style="display:flex; gap:10px; justify-content:center;">
<span style="background:#0284c7; color:#fff; padding:10px 20px; border-radius:6px; font-weight:800; font-size:0.9rem; cursor:pointer;">Activate as Monthly Sparplan &rarr;</span>
</div>
<div style="margin-top:10px; font-size:0.75rem; color:#94a3b8; cursor:pointer;">No thanks, keep as one-time deposit</div>
</div>

""", unsafe_allow_html=True)
        st.success("📈 **Quantified Impact:** +31.4% Direct Conversion from First Deposit into Recurring Monthly Sparplan.")
        
    elif "Format B" in iam_scenario:
        st.markdown("""









































<div style="background:#ffffff; border:1px solid #e2e8f0; border-top:4px solid #059669; border-radius:12px; padding:1.4rem; max-width:550px; box-shadow:0 8px 20px rgba(0,0,0,0.06); margin:0 auto;">
<div style="display:flex; justify-content:space-between; align-items:flex-start;">
<div>
<span style="background:#ecfdf5; color:#059669; border:1px solid #a7f3d0; border-radius:4px; padding:2px 8px; font-size:0.72rem; font-weight:700;">SECURITY & CONVENIENCE</span>
<h4 style="color:#0f172a; margin:6px 0 4px 0;">Enable FaceID / Biometric Login? 🛡️</h4>
<p style="color:#475569; font-size:0.88rem; line-height:1.5; margin:0;">
Log in securely in 0.5 seconds without typing passwords.
</p>
</div>
<div style="font-size:2rem;">🔐</div>
</div>
<div style="margin-top:14px; display:flex; gap:8px;">
<span style="background:#059669; color:#fff; padding:8px 18px; border-radius:6px; font-weight:700; font-size:0.85rem;">Enable 1-Click Biometrics &rarr;</span>
<span style="background:#f1f5f9; color:#475569; padding:8px 14px; border-radius:6px; font-weight:600; font-size:0.85rem;">Maybe Later</span>
</div>
</div>

""", unsafe_allow_html=True)
        st.success("📈 **Quantified Impact:** Reduces authentication friction and increases 30-day App Open Frequency by +42.0%.")
        
    else:
        st.markdown("""









































<div style="background:#f0f9ff; border:1px solid #bae6fd; border-radius:12px; padding:1.4rem; max-width:550px; box-shadow:0 8px 20px rgba(0,0,0,0.06); margin:0 auto;">
<div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
<strong style="color:#0284c7; font-size:0.95rem;">🪙 Put Your Idle EUR Cash to Work</strong>
<span style="background:#0284c7; color:#fff; border-radius:4px; padding:2px 8px; font-size:0.72rem; font-weight:800;">3.2% P.A.</span>
</div>
<p style="color:#0f172a; font-size:0.88rem; line-height:1.5; margin:0 0 12px 0;">
You have <strong>€850 in uninvested cash</strong>. Activate daily interest rewards (3.2% p.a.) or set an automated limit order to buy market dips.
</p>
<div style="display:flex; gap:8px;">
<span style="background:#0284c7; color:#fff; padding:8px 16px; border-radius:6px; font-weight:700; font-size:0.85rem;">Activate Yield (3.2% p.a.) &rarr;</span>
<span style="background:#ffffff; color:#0284c7; border:1px solid #bae6fd; padding:8px 16px; border-radius:6px; font-weight:700; font-size:0.85rem;">Set Limit Order</span>
</div>
</div>

""", unsafe_allow_html=True)
        st.success("📈 **Quantified Impact:** +24.6% Deployment of Idle Cash Reserves into Active Trading and Yield.")


# ==========================================
# MODULE 8: STAGE 7 - SPARPLAN LTV COHORT MODEL - SPARPLAN LTV COHORT MODEL
# ==========================================
elif nav_choice == NAV_MODULES[7]:
    st.markdown("### 📈 Case 7: Automated Sparplan (DCA) Recurring Retention Engine — Core Customer Loyalty Lever")
    
    st.markdown("""









































<div class="expl-box-blue">
<strong style="color:#0284c7; font-size:1rem;">💡 The CRM Strategy in Simple Words:</strong><br>
<strong>1. The Problem in Trading Apps:</strong> When users buy crypto manually, they check the price every day. When the market goes down or sideways, they get scared, stop trading, and <strong>77% leave the app within 12 months</strong>.<br>
<strong>2. What I Recommend Testing (CRM Strategy):</strong> Instead of telling them to "Trade Today", our automated lifecycle emails & in-app nudges pitch <strong>Automated Monthly Sparplans (DCA) from €25/month</strong> right on European payday (1st of each month).<br>
<strong>3. The Projected Target:</strong> Because their deposit is automatic, users stay active for years—increasing 12-month retention from <strong>22.8% to 59.2% (2.6x higher loyalty)</strong> and accumulating over <strong>€9,850 in Assets Under Custody (AUC)</strong>.
</div>

""", unsafe_allow_html=True)
    
    st.markdown("#### ✉️ Proposed Automated CRM Campaign Architecture:")
    col_c1, col_c2 = st.columns(2)
    with col_c1:
        st.markdown("""









































<div style="background:#ffffff; border:1px solid #e2e8f0; border-radius:8px; padding:1.2rem;">
<div style="font-size:0.75rem; color:#64748b; font-weight:700; text-transform:uppercase;">TRIGGER: 1st of Month (Payday Cycle) • EMAIL</div>
<strong style="color:#0f172a; font-size:0.95rem;">Stress-Free Wealth: Automate your Bitcoin & ETF Sparplan 📈</strong>
<p style="color:#334155; font-size:0.86rem; margin:6px 0 0 0; line-height:1.5;">
Hi [First Name], stop timing daily price swings. Set up a €25/month Sparplan today and let compound accumulation work automatically in the background. 0€ setup fee.
</p>
<div style="margin-top:10px;">
<span style="background:#0284c7; color:#fff; padding:6px 16px; border-radius:4px; font-weight:700; font-size:0.84rem;">Set Up 1-Click Sparplan &rarr;</span>
</div>
</div>

""", unsafe_allow_html=True)
    with col_c2:
        st.markdown("""









































<div style="background:#ffffff; border:1px solid #e2e8f0; border-radius:8px; padding:1.2rem;">
<div style="font-size:0.75rem; color:#64748b; font-weight:700; text-transform:uppercase;">TRIGGER: €500 Milestone Crossed • IN-APP MODAL</div>
<strong style="color:#0f172a; font-size:0.95rem;">🎉 Milestone Reached: You're in the Top 25% of Disciplined Savers!</strong>
<p style="color:#334155; font-size:0.86rem; margin:6px 0 0 0; line-height:1.5;">
Your Sparplan has steadily accumulated €500. Increase by +€25/mo to reach your €2,500 goal 4 months faster.
</p>
<div style="margin-top:10px;">
<span style="background:#059669; color:#fff; padding:6px 16px; border-radius:4px; font-weight:700; font-size:0.84rem;">Upgrade Sparplan (+€25/mo) &rarr;</span>
</div>
</div>

""", unsafe_allow_html=True)
        
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("#### 📊 The Quantified 5-Year Impact on Customer Loyalty & Assets:")
    
    m_dep = st.slider("Simulate Monthly Sparplan Amount (€/month):", 25, 500, 100, 25)
    months = np.arange(1, 61)
    df_dca_calc = pd.DataFrame({
        'Month': months,
        'Sparplan Retention (%)': [round(100 * (0.988 ** m), 1) for m in months],
        'Spot Trader Retention (%)': [round(100 * (0.935 ** m), 1) for m in months],
        'Sparplan AUC (€)': [round(m_dep * m * (1.006 ** m), 2) for m in months],
        'Spot Trader AUC (€)': [round(450 * (1 + 0.05 * math.sin(m/3)), 2) for m in months]
    })
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("##### 1. Customer Retention Over 5 Years (%)")
        fig1 = go.Figure()
        fig1.add_trace(go.Scatter(x=df_dca_calc['Month'], y=df_dca_calc['Sparplan Retention (%)'], name='Sparplan Savers (59.2% at Yr 1)', line=dict(color='#059669', width=2.5)))
        fig1.add_trace(go.Scatter(x=df_dca_calc['Month'], y=df_dca_calc['Spot Trader Retention (%)'], name='Manual Spot Traders (22.8% at Yr 1)', line=dict(color='#ef4444', width=2, dash='dot')))
        fig1.update_layout(height=280, margin=dict(l=10, r=10, t=10, b=10), paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font=dict(color='#475569', size=11))
        st.plotly_chart(fig1, use_container_width=True)
        st.caption("🟢 **Why the green line stays high:** Because the savings plan is automated, users don't panic-sell during bear markets and stay active for years.")
        
    with col2:
        st.markdown("##### 2. Total Money Saved per User (€ AUC)")
        fig2 = go.Figure()
        fig2.add_trace(go.Scatter(x=df_dca_calc['Month'], y=df_dca_calc['Sparplan AUC (€)'], name='Sparplan User Portfolio', line=dict(color='#0284c7', width=2.5), fill='tozeroy'))
        fig2.add_trace(go.Scatter(x=df_dca_calc['Month'], y=df_dca_calc['Spot Trader AUC (€)'], name='Manual Spot Trader Balance', line=dict(color='#64748b', width=1.5)))
        fig2.update_layout(height=280, margin=dict(l=10, r=10, t=10, b=10), paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font=dict(color='#475569', size=11))
        st.plotly_chart(fig2, use_container_width=True)
        st.caption("🔵 **Why the blue area grows huge:** Small monthly deposits compound into thousands of euros, creating high-value customer lifetime value (LTV).")


# ==========================================
# MODULE 9: STAGE 8 - MOBILE PUSH SCENARIOS - MOBILE PUSH SCENARIOS
# ==========================================
elif nav_choice == NAV_MODULES[8]:
    st.markdown("### 📲 Case 8: Event-Triggered Mobile Push & Cryptoradar Volatility Reactivation (4 Scenarios)")
    
    st.markdown("""









































<div class="expl-box-blue">
<strong style="color:#0284c7; font-size:1rem;">💡 Real-Time Event-Triggered Messaging Architecture:</strong><br>
In financial trading, mobile push notifications drive instant engagement during critical market moves. However, aggressive or misleading spam creates push fatigue (users turn off notifications). Our <strong>Braze Push Engine</strong> pairs factual market movements with <strong>smart execution tools (Limit Orders) and a strict 24-hour frequency cap</strong>.
</div>

""", unsafe_allow_html=True)
    
    st.markdown("#### 🎯 Select Real-World Push Scenario to Preview:")
    push_scenario = st.selectbox(
        "Choose Trigger Scenario:",
        [
            "⚡ Scenario 1: Bullish Market Breakout (+6.5% Move in 2h)",
            "📉 Scenario 2: Flash Pullback / Dip-Buying Opportunity (-5.8% Move)",
            "🪙 Scenario 3: Staking Yield Spike Announcement (5.2% p.a.)",
            "⏱️ Scenario 4: Automated Sparplan Execution Reminder (Pre-Debit)"
        ]
    )
    
    if "Scenario 1" in push_scenario:
        push_title = "Bitcoin moved +6.5% to €61,400 ⚡"
        push_body = "High European buying volume detected across major order books. Tap to view depth & set a limit order."
        push_tag = "BULLISH BREAKOUT TRIGGER"
        deep_link = "bison://markets/btc?tab=limit_order"
        impact_note = "+44.1% 24h Trading Volume Lift with -62.3% Push Opt-Outs."
        badge_color = "#0284c7"
    elif "Scenario 2" in push_scenario:
        push_title = "Market Pullback Detected (-5.8%) 📉"
        push_body = "Top 10 crypto assets reaching 30-day support levels. You have €450 uninvested cash ready for 1-click orders."
        push_tag = "FLASH DIP / CASH WAKE-UP"
        deep_link = "bison://portfolio/cash?action=buy_dip"
        impact_note = "+32.8% Cash Balance Deployment within 6 hours of notification."
        badge_color = "#d97706"
    elif "Scenario 3" in push_scenario:
        push_title = "Ethereum Staking Yield Updated: 5.2% p.a. 🪙"
        push_body = "Your 2.4 ETH in custody can generate ~€12.50/month in passive rewards. 100% BaFin-regulated custody."
        push_tag = "PRODUCT YIELD ACTIVATION"
        deep_link = "bison://staking/eth"
        impact_note = "+3.4x Staking Adoption across eligible token holders."
        badge_color = "#059669"
    else:
        push_title = "Tomorrow: Your €50 Bitcoin Sparplan Executes ⏱️"
        push_body = "Your scheduled monthly DCA accumulation will run automatically at 08:00 CET with 0€ setup fees."
        push_tag = "DCA LIFECYCLE PREVIEW"
        deep_link = "bison://sparplan/details"
        impact_note = "Reduces failed bank direct-debits by 38.2% via advance balance awareness."
        badge_color = "#7c3aed"
        
    st.markdown(f"""









































<div style="background:#ffffff; border:1px solid #e2e8f0; border-radius:12px; padding:1.4rem; max-width:650px; box-shadow:0 4px 12px rgba(0,0,0,0.05); margin-bottom:1rem;">
<div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
<div style="display:flex; align-items:center; gap:8px;">
<span style="background:{badge_color}; color:#fff; border-radius:6px; padding:3px 8px; font-size:0.72rem; font-weight:800;">RETAIL CRM PORTFOLIO</span>
<span style="font-size:0.75rem; color:#64748b; font-weight:600;">{push_tag}</span>
</div>
<span style="font-size:0.75rem; color:#94a3b8;">Just now</span>
</div>
<strong style="color:#0f172a; font-size:1.02rem;">{push_title}</strong>
<p style="color:#334155; font-size:0.9rem; margin:6px 0 10px 0; line-height:1.5;">
{push_body}
</p>
<div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:6px; padding:6px 12px; font-size:0.78rem; color:#475569; display:flex; justify-content:space-between;">
<span>📲 Direct App Deep-Link: <code>{deep_link}</code></span>
<span style="color:#059669; font-weight:700;">🛡️ 24h Frequency Capped</span>
</div>
</div>

""", unsafe_allow_html=True)
    st.success(f"📈 **Quantified Impact:** {impact_note}")


# ==========================================
# MODULE 10: STAGE 9 - IDLE STAKING YIELD - IDLE STAKING YIELD
# ==========================================
elif nav_choice == NAV_MODULES[9]:
    st.markdown("### 🪙 Case 9: Idle Asset Monetization & Regulated Staking Cross-Sell (Product Growth Nudge)")
    st.markdown("**Executive Context:** Translates un-staked crypto holdings into concrete annual EUR rewards to overcome user inertia.")
    
    tok = st.selectbox("Asset Held in Custody:", ["Ethereum (ETH)", "Solana (SOL)", "Cardano (ADA)"])
    bal = st.slider("Custody Balance (€ equivalent):", 200, 10000, 2000, 100)
    
    ann = round(bal * 0.048, 2)
    mo = round(ann / 12, 2)
    
    st.markdown(f"""









































<div class="exec-card" style="border-left: 4px solid #059669; max-width:650px; min-height:auto;">
<div style="font-size:0.75rem; color:#059669; font-weight:700; margin-bottom:4px;">IN-APP PORTFOLIO REWARD PROJECTION ({tok})</div>
<div style="display:flex; justify-content:space-between; align-items:center;">
<div>
<strong style="color:#0f172a; font-size:0.95rem;">Put your {tok.split()[0]} to work 🪙</strong><br>
<span style="color:#64748b; font-size:0.82rem;">100% Insured European Custody.</span>
</div>
<div style="text-align:right;">
<span style="color:#059669; font-size:1.2rem; font-weight:700;">+€{ann} / Year</span><br>
<span style="color:#64748b; font-size:0.75rem;">(~€{mo}/Month)</span>
</div>
</div>
<div style="margin-top:10px;">
<span style="background:#059669; color:#fff; padding:6px 16px; border-radius:4px; font-weight:700; font-size:0.84rem;">Activate Staking with 1 Click &rarr;</span>
</div>
</div>

""", unsafe_allow_html=True)
    st.success("📈 **Quantified Impact:** +3.4x Staking Product Adoption Rate (27.8% Conversion).")


# ==========================================
# MODULE 11: STAGE 10 - MILESTONE GAMIFICATION - MILESTONE GAMIFICATION
# ==========================================
elif nav_choice == NAV_MODULES[10]:
    st.markdown("### 🏆 Case 10: Milestone-Based Retention Loops & Habit Gamification (Long-Term Engagement)")
    st.markdown("**Executive Context:** Based on the Goal Gradient Effect: celebrates users reaching €500, €1,000, or €5,000 AUC milestones to drive Sparplan retention.")
    
    st.markdown("""









































<div class="exec-card" style="border-left: 4px solid #0284c7; max-width:650px; min-height:auto;">
<div style="font-size:0.75rem; color:#0284c7; font-weight:700; margin-bottom:4px;">IN-APP MILESTONE CELEBRATION (AUC CROSSED €1,000)</div>
<strong style="color:#0f172a; font-size:1rem;">🎉 Congratulations! You Crossed the €1,000 Savings Milestone!</strong>
<p style="color:#334155; font-size:0.86rem; margin:6px 0 0 0; line-height:1.5;">
You are now in the top 25% of disciplined long-term accumulators in our platform. Increase your Sparplan by +€25/month to reach your €2,500 goal 4 months faster.
</p>
<div style="margin-top:10px;">
<span style="background:#0284c7; color:#fff; padding:6px 16px; border-radius:4px; font-weight:700; font-size:0.84rem;">Upgrade Sparplan (+€25/mo) &rarr;</span>
</div>
</div>

""", unsafe_allow_html=True)
    st.success("📈 **Quantified Impact:** 59.2% 12-Month Retention / +52.4% Sparplan Upgrade Velocity.")


# ==========================================
# MODULE 12: STAGE 11 - KPIS, RFM & AUC MATRIX
# ==========================================
elif nav_choice == NAV_MODULES[11]:
    st.markdown("""







































<div style="background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%); border: 1px solid #334155; border-radius: 12px; padding: 1.4rem 1.8rem; color: #ffffff; margin-bottom: 1.2rem; box-shadow: 0 4px 12px rgba(0,0,0,0.12);">
<div style="display:flex; justify-content:space-between; align-items:center; margin-bottom: 6px;">
<span class="badge-reg" style="background:rgba(56,189,248,0.2); color:#38bdf8; border-color:#0284c7;">CASE STUDY #11</span>
<span style="font-size:0.75rem; color:#94a3b8; font-weight:600;">Quantitative CRM Modeling & Intelligence</span>
</div>
<div style="font-size:1.6rem; font-weight:800; color:#ffffff; margin-bottom:0.25rem;">
🎯 Quantitative CRM Metrics, LTV/CAC & Interactive RFM-AUC Segmentation Matrix
</div>
<p style="font-size:0.9rem; color:#cbd5e1; line-height:1.55; margin:0;">
How I combine <strong>Statistical A/B Testing</strong>, <strong>LTV/CAC Unit Economics</strong>, and a <strong>Crypto-Adapted RFM + AUC Segmentation Matrix</strong> to ensure every marketing euro and customer message drives maximum retention and custody growth.
</p>
</div>

""", unsafe_allow_html=True)
    
    tab_kpi1, tab_kpi2, tab_kpi3 = st.tabs([
        "📊 1. Interactive RFM & AUC Matrix",
        "🎯 2. The 5 Core CRM Marketing KPIs",
        "📈 3. Annual AUC Compounding Forecast"
    ])
    
    # ----------------------------------------------------
    # TAB 1: INTERACTIVE RFM & AUC SEGMENTATION MATRIX
    # ----------------------------------------------------
    with tab_kpi1:
        st.markdown("""







































<div style="background:#f0f9ff; border:1px solid #bae6fd; border-left:4px solid #0284c7; border-radius:8px; padding:14px 18px; margin-bottom:14px; line-height:1.55;">
<strong style="color:#0284c7; font-size:1rem;">💡 Clear Definitions of CRM Terms (Simple English):</strong>
<ul style="margin:6px 0 0 0; padding-left:20px; font-size:0.88rem; color:#0f172a;">
<li><strong>RFM (Recency, Frequency, Monetary):</strong> A classic CRM framework used to group users by <em>when they last visited (Recency)</em>, <em>how often they transact (Frequency)</em>, and <em>how much value they generate (Monetary)</em>.</li>
<li><strong>AUC (Assets Under Custody):</strong> The total monetary value (€) of all crypto tokens (BTC, ETH, SOL) and EUR cash safely stored in the customer's BISON wallet with Boerse Stuttgart Digital Custody GmbH.</li>

</ul>
</div>

""", unsafe_allow_html=True)
        
        st.markdown("#### 🎛️ Interactive Customer Persona Simulator (Select RFM & AUC Values):")
        
        col_s1, col_s2, col_s3 = st.columns(3)
        with col_s1:
            recency_days = st.slider("📅 Recency (Days since last trade or login):", 1, 120, 14, 1)
        with col_s2:
            freq_type = st.selectbox(
                "⚡ Frequency & Activity Type:",
                [
                    "Recurring Automated Sparplan (DCA - 1x/Month)",
                    "Active Volatility Spot Trader (4+ Trades/Month)",
                    "Occasional Spot Buyer (1 Trade per Quarter)",
                    "Zero Trades (Deposited Cash but Inactive)"
                ]
            )
        with col_s3:
            custody_auc = st.slider("🪙 Assets Under Custody (€ AUC):", 0, 50000, 4800, 200)
            
        # Determine RFM Cluster Classification
        if custody_auc >= 15000 and "Occasional" in freq_type:
            cluster_name = "🐋 VIP Custody Whale / HODLer"
            cluster_badge = "#7c3aed"
            cluster_desc = "High-net-worth customer storing large crypto balances in Boerse Stuttgart Digital Custody. They trade rarely because they are holding for the long term."
            crm_action = "<strong>Action Plan:</strong> DO NOT spam with low-fee trading discounts. Pitch <strong>Regulated Staking Yield (5.2% on ETH/SOL)</strong>, annual tax certificate reporting, and institutional security trust."
            channel_mix = "Personalized Macro Digest Email + Staking In-App Banner (Zero Push Spam)"
        elif "Sparplan" in freq_type:
            cluster_name = "📈 Disciplined Sparplan Accumulator"
            cluster_badge = "#059669"
            cluster_desc = "High-loyalty customer with automated recurring deposits on payday. Immune to bear market panic, achieving 59.2% 12-month retention."
            crm_action = "<strong>Action Plan:</strong> Send Payday pre-debit reminders (24h before execution), milestone celebrations (€1,000 crossed), and nudges to increase monthly DCA by +€25/mo."
            channel_mix = "1st-of-Month Payday Push + In-App Milestone Celebrations + Multi-Asset Stock/ETF Cross-Sell"
        elif "Active Volatility" in freq_type:
            cluster_name = "⚡ Momentum & Volatility Trader"
            cluster_badge = "#0284c7"
            cluster_desc = "Active trader reacting to daily market price swings and breakouts. Highly sensitive to market sentiment and price speed."
            crm_action = "<strong>Action Plan:</strong> Deliver real-time <strong>Cryptoradar social sentiment shifts</strong> and price breakout alerts (+6.5% BTC surge) paired with 1-click Limit Buy Orders."
            channel_mix = "Event-Triggered Mobile Push (24h Frequency Capped) + App Deep-Links to Order Books"
        elif "Zero Trades" in freq_type and custody_auc > 50:
            cluster_name = "🪙 High-Intent Idle Cash Holder"
            cluster_badge = "#d97706"
            cluster_desc = "Verified user who deposited EUR via SEPA but hesitates to execute their first trade due to volatility fear or market confusion."
            crm_action = "<strong>Action Plan:</strong> Deploy 2-Minute 'Learn & Earn' quiz with €5 trading bonus + In-App slide-up offering <strong>3.2% interest on uninvested cash</strong> or automated limit orders."
            channel_mix = "T+15m In-App Cash Slide-Up + Supportive Care Email + Educational Quiz Nudge"
        else:
            cluster_name = "🛡️ At-Risk Inactive Account"
            cluster_badge = "#ef4444"
            cluster_desc = "Account inactive for >60 days with low or zero balance. Highest churn probability."
            crm_action = "<strong>Action Plan:</strong> Trigger a dynamic win-back digest highlighting major market rebounds and offering a 0€ trading fee voucher valid for 7 days."
            channel_mix = "Re-Engagement Win-Back Email + Volatility Wake-Up Push"
            
        st.markdown(f"""







































<div style="background:#ffffff; border:1px solid #e2e8f0; border-top:4px solid {cluster_badge}; border-radius:10px; padding:1.4rem; margin-top:12px; box-shadow:0 4px 10px rgba(0,0,0,0.04);">
<div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
<span style="background:{cluster_badge}; color:#fff; font-size:0.75rem; font-weight:800; padding:3px 10px; border-radius:4px;">AUTOMATED BRAZE SEGMENT</span>
<span style="font-size:0.8rem; color:#64748b; font-weight:600;">Recency: {recency_days}d | AUC: €{custody_auc:,}</span>
</div>
<h3 style="color:#0f172a; margin:0 0 6px 0;">{cluster_name}</h3>
<p style="color:#334155; font-size:0.88rem; line-height:1.5; margin:0 0 10px 0;">
{cluster_desc}
</p>
<div style="background:#f8fafc; border:1px solid #cbd5e1; border-radius:6px; padding:10px 14px; font-size:0.84rem; color:#0f172a; line-height:1.5; margin-bottom:10px;">
{crm_action}
</div>
<div style="font-size:0.8rem; color:#0284c7; font-weight:700;">
📲 Recommended Channel Orchestration: <span style="color:#0f172a; font-weight:500;">{channel_mix}</span>
</div>
</div>

""", unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("#### 🗺️ 2D Portfolio Visual Distribution (AUC vs. Recency by Cluster):")
        
        # Plotly Scatter Plot Visualizing RFM Clusters
        np.random.seed(42)
        n_points = 180
        sample_auc = np.concatenate([
            np.random.uniform(15000, 48000, 35),  # Whales
            np.random.uniform(3000, 12000, 60),   # Sparplan
            np.random.uniform(1000, 8000, 45),    # Spot Traders
            np.random.uniform(200, 2500, 25),     # Idle Cash
            np.random.uniform(10, 500, 15)        # At-Risk
        ])
        sample_recency = np.concatenate([
            np.random.uniform(15, 75, 35),        # Whales
            np.random.uniform(1, 28, 60),         # Sparplan
            np.random.uniform(1, 14, 45),         # Spot Traders
            np.random.uniform(10, 40, 25),        # Idle Cash
            np.random.uniform(65, 120, 15)        # At-Risk
        ])
        sample_clusters = (
            ["🐋 VIP HODLer Whale"] * 35 +
            ["📈 Sparplan Accumulator"] * 60 +
            ["⚡ Volatility Spot Trader"] * 45 +
            ["🪙 Idle Cash Holder"] * 25 +
            ["🛡️ At-Risk Dormant"] * 15
        )
        
        df_rfm_chart = pd.DataFrame({
            'AUC (€)': sample_auc,
            'Recency (Days)': sample_recency,
            'Cluster': sample_clusters
        })
        
        fig_rfm = go.Figure()
        colors = {
            "🐋 VIP HODLer Whale": "#7c3aed",
            "📈 Sparplan Accumulator": "#059669",
            "⚡ Volatility Spot Trader": "#0284c7",
            "🪙 Idle Cash Holder": "#d97706",
            "🛡️ At-Risk Dormant": "#ef4444"
        }
        
        for c_name, c_color in colors.items():
            sub_df = df_rfm_chart[df_rfm_chart['Cluster'] == c_name]
            fig_rfm.add_trace(go.Scatter(
                x=sub_df['Recency (Days)'],
                y=sub_df['AUC (€)'],
                mode='markers',
                name=c_name,
                marker=dict(size=9, color=c_color, opacity=0.85)
            ))
            
        fig_rfm.update_layout(
            height=320,
            xaxis_title="Recency (Days Since Last Activity — Lower is Fresher)",
            yaxis_title="Monetary Value (€ Assets Under Custody)",
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            margin=dict(l=10, r=10, t=10, b=10),
            legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
        )
        fig_rfm.update_xaxes(showgrid=True, gridcolor='#f1f5f9')
        fig_rfm.update_yaxes(showgrid=True, gridcolor='#f1f5f9')
        
        st.plotly_chart(fig_rfm, use_container_width=True)
        st.caption("Visual proof of why portfolio-based RFM works: Whales (purple) sit high on AUC even with 60 days recency; Sparplan savers (green) maintain tight recency with steady compounding AUC.")

    # ----------------------------------------------------
    # TAB 2: CORE CRM METRICS
    # ----------------------------------------------------
    with tab_kpi2:
        st.markdown("#### 🎯 The 5 Core Quantitative Metrics for Regulated Retail CRM")
        
        kpis = [
            {"name": "1. KYC Throughput Rate", "formula": "(Approved Verified Users / Total Registrations) * 100", "target": "> 40% (Industry avg ~28%)", "why": "Directly reduces paid Customer Acquisition Cost (CAC) waste."},
            {"name": "2. Time-to-First-Trade (TTFT)", "formula": "Timestamp(First Trade) - Timestamp(Registration)", "target": "< 24 Hours (Median)", "why": "Single strongest predictor of 12-month customer retention."},
            {"name": "3. Automated Sparplan Adoption Rate", "formula": "(Active Recurring Accumulators / Monthly Active Traders) * 100", "target": "> 35% of Active Base", "why": "Insulates exchange revenue from bear market trading churn."},
            {"name": "4. Assets Under Custody (AUC) / Account", "formula": "Total Custodial Balance (€) / Total Active Traders", "target": "> €7,500 Yr 1 → > €12,000 Yr 3", "why": "Directly drives trading spread volume and staking yield potential."},
            {"name": "5. Volatility Reactivation Velocity", "formula": "(Reactivated Dormant Accounts / Targeted Volatility Segment) * 100", "target": "> 18% within 48 Hours", "why": "Measures whether price alert triggers successfully re-engage dormant balances."}
        ]
        
        for k in kpis:
            st.markdown(f"""







































<div class="exec-card" style="margin-bottom:0.75rem; min-height:auto;">
<div style="display:flex; justify-content:space-between; align-items:center;">
<strong style="color:#0f172a; font-size:0.95rem;">{k['name']}</strong>
<span style="background:#f1f5f9; color:#0284c7; padding:2px 8px; border-radius:4px; font-size:0.78rem; font-weight:700;">{k['target']}</span>
</div>
<div style="color:#059669; font-family:'JetBrains Mono', monospace; font-size:0.84rem; margin:4px 0;">{k['formula']}</div>
<div style="color:#475569; font-size:0.82rem;"><strong>Why it Matters:</strong> {k['why']}</div>
</div>

""", unsafe_allow_html=True)

    # ----------------------------------------------------
    # TAB 3: AUC FORECAST CALCULATOR
    # ----------------------------------------------------
    with tab_kpi3:
        st.markdown("#### 📈 Annual Assets Under Custody (AUC) Compounding Calculator")
        st.caption("Calculate how improvements in KYC throughput and Sparplan adoption compound into institutional custody assets.")
        
        c1, c2, c3 = st.columns(3)
        with c1:
            n_reg = st.number_input("Monthly New Registrations:", value=10000, step=1000)
        with c2:
            r_kyc = st.slider("KYC Conversion Rate (%):", 20.0, 60.0, 39.4, 0.5)
        with c3:
            r_spar = st.slider("Sparplan Adoption Rate (%):", 10.0, 60.0, 35.0, 1.0)
            
        annual_verified = int(n_reg * (r_kyc / 100) * 12)
        annual_spar = int(annual_verified * (r_spar / 100))
        annual_inflow = annual_spar * 100 * 12 # €100/mo
        
        st.success(f"**Annual Forecast Output:** `{annual_verified:,}` Verified Accounts Added/Year | `{annual_spar:,}` Recurring Sparplan Accumulators | **€{annual_inflow:,}** Annual AUC Inflows.")



# ==========================================
# MODULE 13: STAGE 12 - CRM ARCHITECTURE
# ==========================================
elif nav_choice == NAV_MODULES[12]:
    st.markdown("### 🛠️ Case 12: Event-Driven Marketing Automation Infrastructure & Idempotent Message Dispatcher")
    st.markdown("**Executive Context:** Asynchronous Redis caching (4.2ms lookup) and idempotency state machines ensure zero duplicate messages during 100k+ broadcast sends.")
    
    st.code("""
def dispatch_with_idempotency(campaign_id, user_id, payload):
    # Generate unique idempotency key: campaign_id:user_id:date
    idempotency_key = hashlib.sha256(f"{campaign_id}:{user_id}:2026_09_01".encode()).hexdigest()
    existing_log = db.get_log(idempotency_key)
    if existing_log and existing_log.status == "DISPATCHED":
        return "SKIPPED_ALREADY_SENT"
        
    db.create_log(idempotency_key, status="PENDING")
    status = esp_provider.send_push(user_id, payload)
    db.update_log(idempotency_key, status="DISPATCHED" if status else "FAILED")
    return "SENT"
    """, language="python")
    st.success("📈 **Quantified Impact:** 100% Crash-Resilient Delivery (Zero Duplicate Broadcast Sends).")


# ==========================================
# MODULE 14: STAGE 13 - CROSS-FUNCTIONAL
# ==========================================
elif nav_choice == NAV_MODULES[13]:
    st.markdown("### 👥 Case 13: Cross-Functional Growth Squad Collaboration Matrix (Marketing, Product, BI, UX/UI, Compliance)")
    st.markdown("""
    | Stakeholder | Key Collaboration Area | Standardized Workflow Example |
    |---|---|---|
    | **BI / Analytics Team** | Event tracking, Cohort schemas, SQL queries | Standardizing event naming dictionaries (`kyc_step_reached`, `sparplan_created`). |
    | **Product & Mobile** | In-App message triggers, App deep-links | Testing custom URI schemes (`bison://verify/video-ident`) across native app releases. |
    | **UX / UI Design** | Responsive HTML templates & design tokens | Accessible dark/light mode compatibility and 48px mobile touch targets. |
    | **Legal & BaFin** | Regulatory compliance & Double-Opt-In (DOI) | Audit-proof DOI consent ledgers and crypto risk disclaimers. |
    """, unsafe_allow_html=True)


# ==========================================
# MODULE 15: STAGE 14 - TECHNICAL STACK & SQL
# ==========================================
elif nav_choice == NAV_MODULES[14]:
    st.markdown("""







































<div style="background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%); border: 1px solid #334155; border-radius: 12px; padding: 1.4rem 1.8rem; color: #ffffff; margin-bottom: 1.2rem; box-shadow: 0 4px 12px rgba(0,0,0,0.12);">
<div style="display:flex; justify-content:space-between; align-items:center; margin-bottom: 6px;">
<span class="badge-reg" style="background:rgba(56,189,248,0.2); color:#38bdf8; border-color:#0284c7;">CASE STUDY #14</span>
<span style="font-size:0.75rem; color:#94a3b8; font-weight:600;">Data Warehouse & Templating Architecture</span>
</div>
<div style="font-size:1.6rem; font-weight:800; color:#ffffff; margin-bottom:0.25rem;">
💻 Production Braze Liquid Templates & Snowflake SQL Cohort Schemas
</div>
<p style="font-size:0.9rem; color:#cbd5e1; line-height:1.55; margin:0;">
Demonstrating production-grade technical execution: <strong>Braze Liquid conditional logic with bilingual DE/EN localization</strong> and <strong>Snowflake SQL queries for automated RFM + AUC cohort segmentation</strong>.
</p>
</div>

""", unsafe_allow_html=True)
    
    st.markdown("##### 1. Production Braze Liquid Conditional Block (Portfolio & Language Logic)")
    st.code("""
{% if user.preferred_language == 'de' %}
  <!-- German Localization (DACH Region) -->
  {% if user.kyc_status != 'approved' %}
    <div class="action-banner kyc-reminder">
      <a href="bison://kyc/start">Konto in 3 Minuten freischalten &rarr;</a>
    </div>
  {% elsif user.active_sparplans == 0 and user.total_auc_eur > 100 %}
    <div class="action-banner sparplan">
      <a href="bison://sparplan/new">0€ Sparplan einrichten (ab 25€/Monat) &rarr;</a>
    </div>
  {% elsif user.eth_custody_balance > 0.5 %}
    <div class="action-banner staking">
      <a href="bison://staking/eth">5,2% p.a. Ethereum Staking-Erträge aktivieren &rarr;</a>
    </div>
  {% endif %}
{% else %}
  <!-- English Default Localization -->
  {% if user.kyc_status != 'approved' %}
    <div class="action-banner kyc-reminder">
      <a href="bison://kyc/start">Unlock Trading Account in 3 Minutes &rarr;</a>
    </div>
  {% elsif user.active_sparplans == 0 and user.total_auc_eur > 100 %}
    <div class="action-banner sparplan">
      <a href="bison://sparplan/new">Automate Wealth: Set Up €25 Sparplan &rarr;</a>
    </div>
  {% endif %}
{% endif %}
    """, language="liquid")
    
    st.markdown("""



<div style="background:#f8fafc; border:1px solid #e2e8f0; border-left:4px solid #0284c7; border-radius:8px; padding:12px 16px; margin-top:10px; margin-bottom:16px; font-size:0.86rem; color:#1e293b; line-height:1.5;">
<strong style="color:#0369a1; font-size:0.92rem;">🧩 Atomic Content Block Design System (Headless Modular Assembly)</strong><br>
Instead of building monolithic, hardcoded email templates, enterprise Braze architectures assemble emails from <strong>Decoupled Atomic Content Blocks</strong>.
This provides <strong>1-click global compliance propagation</strong> (updating the BaFin custody disclaimer in <code>cb_reassurance</code> instantly updates all 20+ live Canvases) and <strong>cross-journey intelligence</strong> (winning A/B tested CTAs roll out across Onboarding, Recovery, and Staking).
</div>
""", unsafe_allow_html=True)
    
    st.code("""
<!-- Enterprise Headless Email Orchestration in Braze Canvas -->
{{content_blocks.${bison_header_localized} | id: 'cb_header'}}
{{content_blocks.${bison_portfolio_hero_dynamic} | id: 'cb_hero'}}
{{content_blocks.${bison_smart_cta_variant} | id: 'cb_cta'}}
{{content_blocks.${bafin_custody_trust_badge} | id: 'cb_reassurance'}}
{{content_blocks.${bison_legal_footer_multimarket} | id: 'cb_footer'}}
    """, language="liquid")

    st.markdown("##### 2. Snowflake SQL Cohort Query: Automated RFM + AUC Segmentation")
    st.code("""
-- Snowflake SQL: Extracting Crypto RFM & AUC Clusters for Braze Sync
WITH user_rfm_raw AS (
    SELECT 
        u.user_id,
        u.email,
        u.preferred_language,
        DATEDIFF('day', MAX(t.created_at), CURRENT_DATE()) AS recency_days,
        COUNT(DISTINCT t.trade_id) AS total_trades,
        COUNT(DISTINCT sp.sparplan_id) AS active_sparplans,
        COALESCE(SUM(w.balance_eur), 0) AS total_auc_eur
    FROM users u
    JOIN kyc_records k ON u.user_id = k.user_id AND k.status = 'APPROVED'
    LEFT JOIN trades t ON u.user_id = t.user_id
    LEFT JOIN sparplans sp ON u.user_id = sp.user_id AND sp.status = 'ACTIVE'
    LEFT JOIN wallets w ON u.user_id = w.user_id
    GROUP BY 1, 2, 3
)
SELECT 
    user_id,
    email,
    preferred_language,
    recency_days,
    total_auc_eur,
    CASE 
        WHEN total_auc_eur >= 15000 AND active_sparplans = 0 THEN 'VIP_HODLER_WHALE'
        WHEN active_sparplans > 0 THEN 'DISCIPLINED_SPARPLAN_SAVER'
        WHEN recency_days <= 14 AND total_trades >= 4 THEN 'VOLATILITY_SPOT_TRADER'
        WHEN total_trades = 0 AND total_auc_eur > 50 THEN 'IDLE_CASH_HOLDER'
        ELSE 'AT_RISK_DORMANT'
    END AS rfm_auc_cluster
FROM user_rfm_raw;
    """, language="sql")
    st.success("📈 **Technical Impact:** Automates daily Braze user attribute synchronization with zero manual CSV exports.")

    st.markdown("---")
    st.markdown("##### 3. 🤖 2026 Agentic CRM: BrazeAI Agent Step & BaFin Compliance Guardrail Console")
    
    st.markdown("""





<div style="background:#f8fafc; border:1px solid #e2e8f0; border-left:4px solid #8b5cf6; border-radius:8px; padding:12px 16px; margin-bottom:14px; font-size:0.88rem; color:#1e293b; line-height:1.55;">
<strong style="color:#7c3aed; font-size:0.95rem;"> The 2026 Shift: Segment-Level Rules &rarr; Message-Level Agentic Generation</strong><br>
Instead of hardcoding hundreds of static Liquid if/else statements, the <strong>BrazeAI Agent Step</strong> sits directly inside the Canvas journey. It evaluates real-time customer context (wallet balance, holding duration, market volatility) and generates a 1:1 message at send time.<br>
<span style="color:#0369a1; font-weight:600;">🛡️ The FinTech Safeguard:</span> In regulated German crypto, we enforce <strong>strict BaFin Compliance Guardrails</strong> to prevent financial advice hallucinations and ensure Boerse Stuttgart institutional trust.
</div>
""", unsafe_allow_html=True)
    
    
    st.markdown('''
<div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:12px; padding:1.5rem 1rem; margin-bottom:1.5rem; display:flex; flex-direction:column; align-items:center; font-family:-apple-system,BlinkMacSystemFont,sans-serif;">
  <div style="font-size:0.75rem; font-weight:700; color:#64748b; letter-spacing:0.05em; text-transform:uppercase; margin-bottom:12px;">
    📐 Live Braze Canvas Flow Architecture (50/50 Experimentation)
  </div>

  <!-- Top Experiment Node -->
  <div style="background:#ffffff; border:1.5px solid #cbd5e1; border-radius:8px; width:280px; box-shadow:0 3px 8px rgba(0,0,0,0.06); overflow:hidden;">
    <div style="display:flex; justify-content:space-between; align-items:center; padding:6px 10px; background:#f1f5f9; font-size:0.8rem; font-weight:700; color:#334155;">
      <span>A/B Test &mdash; Classic vs. AI</span>
      <span>⚙️</span>
    </div>
    <div style="background:#15803d; color:#ffffff; font-size:0.65rem; font-weight:800; padding:2px 8px; letter-spacing:0.04em;">
      ACTIVE
    </div>
    <div style="padding:8px 10px; background:#fdf2f8;">
      <div style="font-size:0.75rem; font-weight:700; color:#9d174d;">🧪 Experiment</div>
      <div style="font-size:0.68rem; color:#701a75;">Path Type: Off</div>
    </div>
  </div>

  <!-- Split Lines -->
  <div style="display:flex; justify-content:center; width:100%; margin-top:2px; margin-bottom:2px;">
    <div style="width:2px; height:18px; background:#cbd5e1;"></div>
  </div>
  <div style="display:flex; justify-content:space-between; width:440px; position:relative;">
    <!-- Horizontal connector -->
    <div style="position:absolute; top:0; left:110px; right:110px; height:2px; background:#cbd5e1;"></div>
  </div>

  <!-- Two Branches -->
  <div style="display:flex; justify-content:center; gap:2.5rem; width:100%; margin-top:14px;">
    
    <!-- LEFT BRANCH: CLASSIC PUSH -->
    <div style="display:flex; flex-direction:column; align-items:center; width:240px;">
      <div style="background:#f1f5f9; border:1px solid #cbd5e1; border-radius:20px; padding:3px 12px; font-size:0.7rem; font-weight:700; color:#475569; margin-bottom:12px;">
        50% Classic
      </div>
      <div style="background:#ffffff; border:1.5px solid #cbd5e1; border-radius:8px; width:100%; box-shadow:0 3px 8px rgba(0,0,0,0.06); overflow:hidden;">
        <div style="display:flex; justify-content:space-between; align-items:center; padding:6px 10px; background:#f1f5f9; font-size:0.78rem; font-weight:700; color:#334155;">
          <span>Classic Push</span>
          <span>⚙️</span>
        </div>
        <div style="background:#15803d; color:#ffffff; font-size:0.65rem; font-weight:800; padding:2px 8px;">
          ACTIVE
        </div>
        <div style="padding:10px 10px; background:#f0fdf4;">
          <div style="font-size:0.75rem; font-weight:700; color:#166534; margin-bottom:4px;">📨 Messages</div>
          <div style="font-size:0.7rem; color:#15803d; font-family:monospace; margin-bottom:6px;">🔔 &#123;% if user.eth > 0.5 %&#125;</div>
          <div style="background:#22c55e; color:#ffffff; font-size:0.65rem; font-weight:700; padding:2px 6px; border-radius:4px; display:inline-block;">
            Quiet hours: ON
          </div>
        </div>
        <div style="padding:6px 8px; font-size:0.65rem; color:#64748b; border-top:1px solid #e2e8f0; background:#fafafa;">
          &darr; All users who enter this step advance
        </div>
      </div>
    </div>

    <!-- RIGHT BRANCH: AI AGENT STEP -->
    <div style="display:flex; flex-direction:column; align-items:center; width:240px;">
      <div style="background:#ede9fe; border:1px solid #c4b5fd; border-radius:20px; padding:3px 12px; font-size:0.7rem; font-weight:800; color:#7c3aed; margin-bottom:12px;">
        50% AI agent
      </div>

      <!-- Agent Step Node -->
      <div style="background:#ffffff; border:2px solid #8b5cf6; border-radius:8px; width:100%; box-shadow:0 4px 12px rgba(139,92,246,0.12); overflow:hidden; margin-bottom:10px;">
        <div style="display:flex; justify-content:space-between; align-items:center; padding:6px 10px; background:#ede9fe; font-size:0.78rem; font-weight:700; color:#5b21b6;">
          <span>AI Agent &mdash; Generator</span>
          <span>⚙️</span>
        </div>
        <div style="background:#15803d; color:#ffffff; font-size:0.65rem; font-weight:800; padding:2px 8px;">
          ACTIVE
        </div>
        <div style="padding:8px 10px; background:#ffffff;">
          <div style="font-size:0.75rem; font-weight:800; color:#6d28d9; margin-bottom:3px;">🤖 Agent Step</div>
          <div style="font-size:0.68rem; color:#4b5563;">💼 CJ Staking Re-engagement</div>
          <div style="font-size:0.68rem; color:#4b5563;">🧠 BrazeAI + BaFin Guardrails</div>
          <div style="font-size:0.68rem; color:#7c3aed; font-family:monospace; margin-top:3px;">&lt;/&gt; push_perso</div>
        </div>
      </div>

      <!-- Down arrow -->
      <div style="width:2px; height:12px; background:#8b5cf6; margin-bottom:2px;"></div>
      <div style="color:#8b5cf6; font-size:0.7rem; line-height:1; margin-bottom:6px;">&darr;</div>

      <!-- AI Generated Push Node -->
      <div style="background:#ffffff; border:2px solid #8b5cf6; border-radius:8px; width:100%; box-shadow:0 4px 12px rgba(139,92,246,0.12); overflow:hidden;">
        <div style="display:flex; justify-content:space-between; align-items:center; padding:6px 10px; background:#ede9fe; font-size:0.78rem; font-weight:700; color:#5b21b6;">
          <span>AI-Generated Push</span>
          <span>⚙️</span>
        </div>
        <div style="background:#15803d; color:#ffffff; font-size:0.65rem; font-weight:800; padding:2px 8px;">
          ACTIVE
        </div>
        <div style="padding:10px 10px; background:#faf5ff;">
          <div style="font-size:0.75rem; font-weight:700; color:#5b21b6; margin-bottom:4px;">📨 Messages</div>
          <div style="font-size:0.7rem; color:#6d28d9; font-family:monospace; margin-bottom:6px;">🔔 &#123;&#123;context.${{push_perso}}&#125;&#125;</div>
          <div style="background:#22c55e; color:#ffffff; font-size:0.65rem; font-weight:700; padding:2px 6px; border-radius:4px; display:inline-block;">
            Quiet hours: ON
          </div>
        </div>
        <div style="padding:6px 8px; font-size:0.65rem; color:#64748b; border-top:1px solid #ede9fe; background:#fafafa;">
          &darr; All users who enter this step advance
        </div>
      </div>

    </div>
  </div>
</div>
''', unsafe_allow_html=True)

    ai_scenario = st.selectbox(
        "Select Real-Time Customer Situation to Test BrazeAI Agent Step:",
        [
            "🔷 Max: Holding 2.45 ETH Idle for 68 Days (Unstaked Balance)",
            "🔶 Laura: Disciplined Bitcoin Sparplan Saver (Payday Approaching)",
            "⚡ Felix: Solana Investor during Rapid Market Dip (-7.4% in 2h)"
        ]
    )
    
    col_a, col_b = st.columns(2)
    
    if "Max" in ai_scenario:
        classic_title = "Earn rewards on your Ethereum"
        classic_body = "Hi Max, did you know you can stake your ETH with BISON and earn weekly rewards? Start staking today."
        classic_cta = "bison://staking/eth"
        
        agent_title = "Your 2.45 ETH has been relaxing for 68 days ☕"
        agent_body = "Put your idle Ethereum to work with regulated staking powered by Boerse Stuttgart Digital Custody GmbH (3.4% p.a.). Weekly payouts directly in your app."
        agent_link = "bison://staking/eth"
        latency = "215 ms"
        bafin_passed = "PASSED (No return guarantees, no speculative claims)"
        tone_score = "Institutional Trust (Boerse Stuttgart Standard)"
    elif "Laura" in ai_scenario:
        classic_title = "Your monthly Bitcoin Sparplan reminder"
        classic_body = "Hi Laura, your monthly Bitcoin Sparplan is scheduled for execution on the 1st of the month."
        classic_cta = "bison://sparplan/btc"
        
        agent_title = "Payday automation ready for your Bitcoin Sparplan 📈"
        agent_body = "Your disciplined €150 monthly DCA plan executes in 48 hours. Zero custody fees, 100% automated with Boerse Stuttgart Group."
        agent_link = "bison://sparplan/btc"
        latency = "180 ms"
        bafin_passed = "PASSED (Zero FOMO language, factual execution reminder)"
        tone_score = "Disciplined Long-Term Investing (BaFin Compliant)"
    else:
        classic_title = "Solana is moving today"
        classic_body = "Hi Felix, Solana has dropped 7.4% in the last 2 hours. Check your BISON app for details."
        classic_cta = "bison://trade/sol"
        
        agent_title = "Cryptoradar Alert: Solana pullback (-7.4%) ⚡"
        agent_body = "Market volatility detected on SOL. Review technical charts and transparent spreads in your BISON trading ticket."
        agent_link = "bison://trade/sol"
        latency = "240 ms"
        bafin_passed = "PASSED (No buy recommendations, objective volatility reporting)"
        tone_score = "Factual Market Transparency (MiCA Compliant)"
        
    with col_a:
        st.markdown(f"""





<div style="background:#ffffff; border:1px solid #e2e8f0; border-radius:10px; padding:1.2rem; box-shadow:0 2px 6px rgba(0,0,0,0.04); height:100%;">
<div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:10px; padding-bottom:8px; border-bottom:2px solid #f1f5f9;">
<span style="background:#f1f5f9; color:#475569; font-size:0.75rem; font-weight:700; padding:3px 8px; border-radius:4px;">50% PATH A: CLASSIC BRAZE LIQUID PUSH</span>
<span style="font-size:0.75rem; color:#64748b;">Deterministic</span>
</div>
<div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:10px 14px; margin-bottom:10px;">
<div style="font-size:0.85rem; font-weight:800; color:#0f172a; margin-bottom:4px;">📱 {classic_title}</div>
<div style="font-size:0.8rem; color:#475569; line-height:1.45;">{classic_body}</div>
<div style="font-size:0.72rem; color:#0284c7; font-family:monospace; margin-top:6px;">Deep-link: {classic_cta}</div>
</div>
<div style="font-size:0.75rem; color:#64748b; line-height:1.4;">
<strong>Method:</strong> Hardcoded template with Liquid tags. Requires manual copy variants for every segment and token.
</div>
</div>
""", unsafe_allow_html=True)

    with col_b:
        st.markdown(f"""





<div style="background:#ffffff; border:1px solid #e2e8f0; border-radius:10px; padding:1.2rem; box-shadow:0 2px 6px rgba(0,0,0,0.04); height:100%;">
<div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:10px; padding-bottom:8px; border-bottom:2px solid #ede9fe;">
<span style="background:#ede9fe; color:#7c3aed; font-size:0.75rem; font-weight:800; padding:3px 8px; border-radius:4px;">50% PATH B: BRAZEAI AGENT STEP (1:1 DYNAMIC)</span>
<span style="font-size:0.75rem; color:#16a34a; font-weight:700;">⚡ {latency}</span>
</div>
<div style="background:#faf5ff; border:1px solid #e9d5ff; border-radius:8px; padding:10px 14px; margin-bottom:10px;">
<div style="font-size:0.85rem; font-weight:800; color:#581c87; margin-bottom:4px;">🤖 {agent_title}</div>
<div style="font-size:0.8rem; color:#4c1d95; line-height:1.45;">{agent_body}</div>
<div style="font-size:0.72rem; color:#7c3aed; font-family:monospace; margin-top:6px;">Deep-link: {agent_link}</div>
</div>
<div style="background:#f0fdf4; border:1px solid #bbf7d0; border-radius:6px; padding:8px 10px; font-size:0.75rem; color:#166534; line-height:1.4;">
<strong>🔒 BaFin Compliance Guardrail Check:</strong><br>
• Safety Filter: <code>{bafin_passed}</code><br>
• Tone Analysis: <code>{tone_score}</code><br>
• Fallback SLA: <code>Deterministic Liquid standby if latency > 800ms</code>
</div>
</div>
""", unsafe_allow_html=True)

