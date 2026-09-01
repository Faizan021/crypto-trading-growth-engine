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
    page_title="Faizex Digital | Regulated Exchange CRM & Retention Engine",
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
        gap: 6px !important;
    }
    section[data-testid="stSidebar"] .stRadio label {
        font-size: 0.92rem !important;
        font-weight: 500 !important;
        padding: 6px 10px !important;
        margin-bottom: 3px !important;
        line-height: 1.4 !important;
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
</style>
""", unsafe_allow_html=True)

# Top Disclaimer Notice
st.caption("🔒 **PORTFOLIO NOTICE:** Faizex Digital is an independent portfolio case study platform created by Faizan Ahmed for technical and quantitative CRM demonstration. All trading and customer metrics are synthetic simulations.")

# Executive Header
st.markdown("""
<div class="exec-header">
    <div style="margin-bottom: 8px;">
        <span class="badge-reg">BaFin & MiCA Framework</span>
        <span class="badge-crm">Braze Lifecycle Architecture</span>
    </div>
    <div class="exec-title">Faizex Digital — Retail CRM & Retention Engine</div>
    <p class="exec-sub">
        Quantitative Customer Journeys, Multi-Channel Onboarding Funnels, Sparplan DCA Models, and A/B Testing Infrastructure.
    </p>
</div>
""", unsafe_allow_html=True)

# Data assets
base_dir = os.path.dirname(os.path.abspath(__file__))
funnel_path = os.path.join(base_dir, 'data', 'kyc_funnel_dropoffs.csv')
dca_path = os.path.join(base_dir, 'data', 'dca_sparplan_cohorts.csv')
exp_path = os.path.join(base_dir, 'config', 'email_experiments.json')

df_funnel = pd.read_csv(funnel_path) if os.path.exists(funnel_path) else pd.DataFrame()
df_dca = pd.read_csv(dca_path) if os.path.exists(dca_path) else pd.DataFrame()
experiments = {}
if os.path.exists(exp_path):
    with open(exp_path, 'r', encoding='utf-8') as f:
        experiments = json.load(f)

# Sidebar Navigation
st.sidebar.title("Faizex CRM Platform")
st.sidebar.markdown("**Operational Modules**")

nav_choice = st.sidebar.radio(
    "Select Strategic Module:",
    [
        "📊 1. Executive Performance Dashboard",
        "✉️ 2. Case 1: Transactional Activation Momentum",
        "🛡️ 3. Case 2: Onboarding & KYC Friction Breaker",
        "📰 4. Case 3: Editorial Newsletter Personalization",
        "🎯 5. Case 4: Exchange CRM & Retention KPIs",
        "📈 6. Case 5: 5-Year Sparplan (DCA) Cohort Model",
        "⚡ 7. Case 6: Market Volatility Push Engine",
        "🏦 8. Case 7: Stalled-Deposit Recovery Flow",
        "🏆 9. Case 8: Milestone Habit Gamification",
        "🪙 10. Case 9: Idle Asset Staking Yield Nudge",
        "🛠️ 11. Case 10: CRM Automation Architecture",
        "👥 12. Case 11: Cross-Functional Alignment Framework",
        "💻 13. Case 12: Production Liquid & SQL Schemas"
    ]
)

st.sidebar.markdown("---")
st.sidebar.caption("Portfolio Project | Faizan Ahmed")

# ==========================================
# MODULE 1: EXECUTIVE DASHBOARD
# ==========================================
if "1. Executive Performance Dashboard" in nav_choice:
    st.markdown("### Executive Summary — Monthly Retail Throughput & Custody Metrics")
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown("""
        <div class="exec-card">
            <div class="exec-card-lbl" style="min-height:34px;">30-Day Retail<br>Trading Volume</div>
            <div class="exec-card-val">€148.4M</div>
            <div class="exec-card-sub" style="min-height:32px;">+12.4% vs. Prior Month<br>&nbsp;</div>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="exec-card">
            <div class="exec-card-lbl" style="min-height:34px;">KYC → First-Trade<br>Throughput Rate</div>
            <div class="exec-card-val">39.4%</div>
            <div class="exec-card-sub" style="min-height:32px;">+11.0% Lift vs. Baseline<br>(28.4% Control)</div>
        </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown("""
        <div class="exec-card">
            <div class="exec-card-lbl" style="min-height:34px;">12-Month Sparplan<br>Customer Retention</div>
            <div class="exec-card-val">59.2%</div>
            <div class="exec-card-sub" style="min-height:32px;">2.6x Higher Retention<br>(vs. 22.8% Spot)</div>
        </div>
        """, unsafe_allow_html=True)
    with col4:
        st.markdown("""
        <div class="exec-card">
            <div class="exec-card-lbl" style="min-height:34px;">Avg 2-Year AUC<br>per Active Account</div>
            <div class="exec-card-val">€9,850</div>
            <div class="exec-card-sub" style="min-height:32px;">Steady Compound<br>Recurring Inflows</div>
        </div>
        """, unsafe_allow_html=True)
        
    st.markdown("<br>", unsafe_allow_html=True)
    
    col_left, col_right = st.columns([1.25, 1])
    with col_left:
        st.markdown("#### ⚡ Onboarding Conversion Funnel (Per 10,000 Signups)")
        st.markdown("""
        <div class="expl-box-blue">
            <strong style="color:#0284c7; font-size:0.92rem;">💡 Why this Funnel matters for CRM:</strong><br>
            Over 60% of paid ad traffic drops off before completing KYC. This live model shows how our multi-channel lifecycle journeys (Cases 1, 2, and 7) eliminate drop-offs at each critical gate—lifting final first-trade activation from <strong>22.3% to 39.4% (+76.7% through-funnel lift)</strong>.
        </div>
        """, unsafe_allow_html=True)
        
        stages = [
            {"step": "01", "name": "App Download & Registration", "control": "10,000", "variant": "10,000", "pct": 100, "lift": "Baseline", "color": "#0284c7"},
            {"step": "02", "name": "Email Address Confirmed (Case 1)", "control": "8,420", "variant": "8,940", "pct": 89.4, "lift": "+6.2% Lift", "color": "#0284c7"},
            {"step": "03", "name": "Video-Ident Call Initiated (Case 2)", "control": "4,820", "variant": "6,780", "pct": 67.8, "lift": "+40.7% Lift", "color": "#059669"},
            {"step": "04", "name": "KYC Verification Approved", "control": "3,920", "variant": "5,910", "pct": 59.1, "lift": "+50.8% Lift", "color": "#059669"},
            {"step": "05", "name": "First Bank / SEPA Deposit (Case 7)", "control": "2,850", "variant": "4,790", "pct": 47.9, "lift": "+68.1% Lift", "color": "#d97706"},
            {"step": "06", "name": "First Trade Executed (Activated)", "control": "2,230", "variant": "3,940", "pct": 39.4, "lift": "+76.7% Lift", "color": "#7c3aed"}
        ]
        
        for s in stages:
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
            </div>
            """, unsafe_allow_html=True)
            
    with col_right:
        st.markdown("#### 🪙 Assets Under Custody (AUC) Segmentation")
        st.markdown("""
        <div class="expl-box-green">
            <strong style="color:#059669; font-size:0.92rem;">💡 How Custody Distribution Drives CRM Personalization:</strong><br>
            Retention is maximized when CRM messaging matches what the user holds. We use automated Braze segments to trigger tailored next steps: <strong>DCA Sparpläne for BTC</strong>, <strong>Staking Rewards for ETH</strong>, and <strong>Limit Alerts for Cash</strong>.
        </div>
        """, unsafe_allow_html=True)
        
        assets = [
            {"name": "Bitcoin (BTC)", "share": "42%", "pct": 42, "color": "#d97706", "action": "Automated DCA Sparplan Focus"},
            {"name": "Ethereum (ETH)", "share": "24%", "pct": 24, "color": "#4f46e5", "action": "Staking Rewards & Yield Activation"},
            {"name": "DAX 40 & European Equity ETFs", "share": "18%", "pct": 18, "color": "#059669", "action": "Multi-Asset Long-Term Wealth"},
            {"name": "Top Altcoins (SOL, ADA)", "share": "11%", "pct": 11, "color": "#0284c7", "action": "Volatility & Limit Order Alerts"},
            {"name": "Cash / EUR Reserve", "share": "5%", "pct": 5, "color": "#64748b", "action": "Instant Dip-Buy Readiness"}
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
            
        st.caption("ℹ️ **Data Benchmark Source:** Aggregated from European Securities and Markets Authority (ESMA) retail asset reports and DACH multi-asset exchange distributions.")

# ==========================================
# MODULE 2: CASE 1
# ==========================================
elif "2. Case 1: Transactional Activation" in nav_choice:
    st.markdown("### Case 1: Transactional Confirmation & Activation Momentum")
    st.markdown("**Executive Context:** Transactional confirmation emails command a **68.2% open rate** (the highest in the customer lifecycle). Treating this email as a plain administrative stop wastes peak customer motivation.")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div style="background:#ffffff; border:1px solid #e2e8f0; border-radius:8px; padding:1.2rem;">
            <div style="border-bottom: 1px solid #e2e8f0; padding-bottom: 8px; margin-bottom: 12px; font-size: 0.85rem; color:#64748b;">
                <strong>Subject:</strong> <code>Confirm your email address now!</code><br>
                <strong>Preheader:</strong> <code>Before you can register, please confirm your email...</code>
            </div>
            <div style="color: #1e293b; font-size: 0.92rem; line-height: 1.6;">
                Hello friend,<br><br>
                We're delighted that you'd like to become part of our community.<br><br>
                Before you can register, we would like to ask you to confirm your email address by using the following link:<br><br>
                <div style="text-align: center; margin: 14px 0;">
                    <span style="background:#f1f5f9; color:#0f172a; border:1px solid #cbd5e1; padding:8px 20px; border-radius:4px; font-weight:600; font-size:0.88rem;">Confirm email address</span>
                </div><br>
                Thanks and best regards,<br>
                Your Team
            </div>
            <hr style="border-color: #e2e8f0; margin: 14px 0;">
            <div style="font-size:0.82rem; color:#64748b;">
                <strong>Baseline Assessment:</strong> 100% deliverability, but plain text creates an administrative dead-end. 58.8% of users delay KYC by >18 hours.
            </div>
        </div>
        """, unsafe_allow_html=True)
        
    with col2:
        st.markdown("""
        <div style="background:#f0f9ff; border:1px solid #bae6fd; border-radius:8px; padding:1.2rem;">
            <div style="border-bottom: 1px solid #bae6fd; padding-bottom: 8px; margin-bottom: 12px; font-size: 0.85rem; color:#0284c7;">
                <strong>Subject:</strong> <code>⚡ 1 click away from your trading workspace (+ market movers inside)</code><br>
                <strong>Preheader:</strong> <code>Bitcoin +3.8% today • Instant 0€ account setup</code>
            </div>
            <div style="color: #0f172a; font-size: 0.92rem; line-height: 1.6;">
                Hi [First Name],<br><br>
                You're seconds away from your digital trading workspace. Confirm your email below to get started:<br><br>
                <div style="text-align: center; margin: 14px 0;">
                    <span style="background:#0284c7; color:#ffffff; padding:9px 22px; border-radius:4px; font-weight:700; font-size:0.9rem;">Confirm Email & Start Exploring &rarr;</span>
                </div><br>
                <div style="background: #ffffff; border: 1px solid #bae6fd; border-radius: 6px; padding: 10px 12px; font-size: 0.84rem;">
                    <strong style="color:#0284c7;">🔥 Live Market Context:</strong><br>
                    • <strong>BTC / EUR:</strong> +3.8% (€58,420) • <strong>ETH / EUR:</strong> +5.1% (€2,480)<br>
                    • <strong>Automated Sparplan:</strong> Set and forget from €25/month
                </div>
            </div>
            <hr style="border-color: #bae6fd; margin: 14px 0;">
            <div style="font-size:0.82rem; color:#0284c7;">
                <strong>Performance Impact:</strong> <strong>+30.6% Click-through Velocity</strong> ($z = 2.89, p = 0.0039$). Reduces median time-to-verification from 18.4h to 4.2h.
            </div>
        </div>
        """, unsafe_allow_html=True)

# ==========================================
# MODULE 3: CASE 2
# ==========================================
elif "3. Case 2: Onboarding" in nav_choice:
    st.markdown("### Case 2: Onboarding & Video-Ident Friction Breaker")
    st.markdown("**Executive Context:** In regulated European markets (BaFin & MiCA), identity verification creates a major cognitive barrier. Our hypothesis replaces dense paragraphs with a 3-step time-stamped checklist and mobile deep-linking.")
    
    colA, colB = st.columns(2)
    with colA:
        st.markdown("""
        <div style="background:#ffffff; border:1px solid #e2e8f0; border-radius:8px; padding:1.2rem;">
            <div style="border-bottom: 1px solid #e2e8f0; padding-bottom: 8px; margin-bottom: 12px; font-size: 0.85rem; color:#64748b;">
                <strong>Subject:</strong> <code>Welcome to Faizex 👋</code><br>
                <strong>Preheader:</strong> <code>When it comes to trading, we are a partner you can rely on...</code>
            </div>
            <div style="color: #1e293b; font-size: 0.92rem; line-height: 1.6;">
                Hi,<br><br>
                You've just become part of our community and are now able to use the best crypto app in Germany! When it comes to trading, our exchange-backed platform is a partner you can rely on. Our goal is to make trading as simple as possible for you. There's no need for a wallet, securities account, or even paperwork.<br><br>
                <div style="text-align: center; margin: 10px 0;">
                    <span style="background:#f1f5f9; color:#0f172a; border:1px solid #cbd5e1; padding:7px 18px; border-radius:4px; font-weight:600; font-size:0.85rem;">Verify now</span>
                </div><br>
                Just take a few minutes to verify your identity through a simple video identification process and you'll be ready to go!<br><br>
                <div style="text-align: center; margin: 10px 0;">
                    <span style="background:#f1f5f9; color:#0f172a; border:1px solid #cbd5e1; padding:7px 18px; border-radius:4px; font-weight:600; font-size:0.85rem;">Verify now</span>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
    with colB:
        st.markdown("""
        <div style="background:#ecfdf5; border:1px solid #a7f3d0; border-radius:8px; padding:1.2rem;">
            <div style="border-bottom: 1px solid #a7f3d0; padding-bottom: 8px; margin-bottom: 12px; font-size: 0.85rem; color:#059669;">
                <strong>Subject:</strong> <code>Unlock your trading account in 3 minutes 🛡️ (Step 1 ready)</code><br>
                <strong>Preheader:</strong> <code>ID card ready? 2-min Video-Ident • Insured German custody</code>
            </div>
            <div style="color: #0f172a; font-size: 0.92rem; line-height: 1.6;">
                Hi [First Name],<br><br>
                Welcome to your institutional-grade trading account. Your workspace is 1 step away from activation:<br><br>
                <div style="background: #ffffff; border: 1px solid #a7f3d0; border-radius: 6px; padding: 10px 14px; font-size: 0.86rem;">
                    <strong>Step 1:</strong> Have your ID card or passport ready (1 min)<br>
                    <strong>Step 2:</strong> Quick 2-minute Video-Ident call<br>
                    <strong>Step 3:</strong> Instant account ready for first trade (0€ deposit fee)
                </div><br>
                <div style="text-align: center; margin: 14px 0;">
                    <span style="background:#059669; color:#ffffff; padding:9px 22px; border-radius:4px; font-weight:700; font-size:0.9rem;">Unlock My Account in App (3 Mins) &rarr;</span>
                </div>
                <div style="text-align:center; font-size:0.75rem; color:#64748b;">
                    🔒 BaFin Regulated • Insured European Custody • No Wallet Complexity
                </div>
            </div>
            <hr style="border-color: #a7f3d0; margin: 14px 0;">
            <div style="font-size:0.82rem; color:#059669;">
                <strong>Performance Impact:</strong> <strong>+38.7% Relative Lift in KYC</strong> (28.4% → 39.4%, $z = 3.12, p = 0.0018$).
            </div>
        </div>
        """, unsafe_allow_html=True)

# ==========================================
# MODULE 4: CASE 3
# ==========================================
elif "4. Case 3: Engagement" in nav_choice:
    st.markdown("### Case 3: Monthly Market Newsletter Personalization")
    st.markdown("**Executive Context:** Preserves 100% of high-quality macro storytelling, but uses **Liquid logic** to dynamically adapt the Call-to-Action module based on real-time subscriber lifecycle state.")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("##### 🔴 Control (Single Static CTA)")
        st.markdown("""
        <div style="background:#ffffff; border:1px solid #e2e8f0; border-radius:8px; padding:1.2rem;">
            <p style="color:#64748b; font-size:0.85rem; margin-bottom:4px;"><strong>Subject:</strong> Hi, here's your Faizex Market Digest for August 📰</p>
            <p style="color:#1e293b; font-size:0.88rem; line-height:1.5;">
                Bitcoin has woken up—and pulled the entire crypto market out of hibernation. The wake-up call came from Washington, where the US debt pile is spiraling out of control...
            </p>
            <div style="text-align: center; margin: 16px 0;">
                <span style="background:#f1f5f9; color:#0f172a; border:1px solid #cbd5e1; padding:8px 20px; border-radius:4px; font-weight:600; font-size:0.85rem;">Trade Bitcoin</span>
            </div>
            <p style="color:#64748b; font-size:0.78rem;">Static button underperforms across unverified users and long-term savers.</p>
        </div>
        """, unsafe_allow_html=True)
        
    with col2:
        st.markdown("##### 🟢 Variant B (Dynamic Liquid CTAs)")
        selected_persona = st.selectbox(
            "Select Subscriber Lifecycle Persona:",
            [
                "Unverified Lead (KYC Pending)",
                "Manual Spot Buyer (0 Active Sparplans)",
                "Active Sparplan Accumulator (Monthly DCA)",
                "Dormant Account (>60 Days Inactive)"
            ]
        )
        
        st.markdown("""
        <div style="background:#f0f9ff; border:1px solid #bae6fd; border-radius:8px; padding:1.2rem;">
            <p style="color:#0284c7; font-size:0.85rem; margin-bottom:4px;"><strong>Subject:</strong> Market Digest: Institutional flows & Volatility shift [Portfolio Impact] 📈</p>
            <p style="color:#0f172a; font-size:0.88rem; line-height:1.5;">
                Bitcoin has woken up—and pulled the entire crypto market out of hibernation. [Macro Report Preserved in Full]...
            </p>
        """, unsafe_allow_html=True)
        
        if "Unverified" in selected_persona:
            st.markdown("""
                <div style="background:#ffffff; border:1px solid #f59e0b; border-radius:6px; padding:10px; text-align:center;">
                    <span style="color:#d97706; font-weight:700; font-size:0.88rem;">Complete 3-Min Verification to Catch Market Momentum &rarr;</span>
                </div>
            """, unsafe_allow_html=True)
        elif "Spot Buyer" in selected_persona:
            st.markdown("""
                <div style="background:#ffffff; border:1px solid #059669; border-radius:6px; padding:10px; text-align:center;">
                    <span style="color:#059669; font-weight:700; font-size:0.88rem;">Automate Your Accumulation: Set Up a €25 Sparplan &rarr;</span>
                </div>
            """, unsafe_allow_html=True)
        elif "Sparplan" in selected_persona:
            st.markdown("""
                <div style="background:#ffffff; border:1px solid #0284c7; border-radius:6px; padding:10px; text-align:center;">
                    <span style="color:#0284c7; font-weight:700; font-size:0.88rem;">View August Portfolio Growth & Staking Rewards &rarr;</span>
                </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown("""
                <div style="background:#ffffff; border:1px solid #db2777; border-radius:6px; padding:10px; text-align:center;">
                    <span style="color:#db2777; font-weight:700; font-size:0.88rem;">Activate Real-Time Price Volatility Alerts &rarr;</span>
                </div>
            """, unsafe_allow_html=True)
            
        st.markdown("""
            <hr style="border-color: #bae6fd; margin: 12px 0;">
            <div style="font-size:0.82rem; color:#0284c7;">
                <strong>Performance Impact:</strong> <strong>+86.3% Click-to-Open (CTOR) Lift</strong> (12.4% → 23.1%, $z = 4.15, p < 0.0001$).
            </div>
        </div>
        """, unsafe_allow_html=True)

# ==========================================
# MODULE 5: CASE 4 - KPIS
# ==========================================
elif "5. Case 4: Exchange CRM" in nav_choice:
    st.markdown("### Case 4: Exchange CRM & Retention KPI Framework")
    
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
        
    st.markdown("---")
    st.markdown("#### Annual Assets Under Custody (AUC) Forecast Calculator")
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
# MODULE 6: CASE 5 - SPARPLAN LTV
# ==========================================
elif "6. Case 5: Retention" in nav_choice:
    st.markdown("### Case 5: 5-Year Sparplan (DCA) Cohort Retention Model")
    st.markdown("Comparing long-term retention decay and Assets Under Custody (AUC) between **Manual Spot Traders** vs. **Automated Recurring Sparplan Accumulators**.")
    
    m_dep = st.slider("Monthly Sparplan Contribution (€/month):", 25, 500, 100, 25)
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
        st.markdown("##### 1. Cohort Retention Decay Curve")
        fig1 = go.Figure()
        fig1.add_trace(go.Scatter(x=df_dca_calc['Month'], y=df_dca_calc['Sparplan Retention (%)'], name='Sparplan Accumulator (59.2% at M12)', line=dict(color='#059669', width=2.5)))
        fig1.add_trace(go.Scatter(x=df_dca_calc['Month'], y=df_dca_calc['Spot Trader Retention (%)'], name='Manual Spot Trader (22.8% at M12)', line=dict(color='#ef4444', width=2, dash='dot')))
        fig1.update_layout(height=300, margin=dict(l=10, r=10, t=10, b=10), paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font=dict(color='#475569', size=11))
        st.plotly_chart(fig1, use_container_width=True)
    with col2:
        st.markdown("##### 2. Assets Under Custody (AUC) Accumulation (€)")
        fig2 = go.Figure()
        fig2.add_trace(go.Scatter(x=df_dca_calc['Month'], y=df_dca_calc['Sparplan AUC (€)'], name='Sparplan Portfolio', line=dict(color='#0284c7', width=2.5), fill='tozeroy'))
        fig2.add_trace(go.Scatter(x=df_dca_calc['Month'], y=df_dca_calc['Spot Trader AUC (€)'], name='Spot Trader Portfolio', line=dict(color='#64748b', width=1.5)))
        fig2.update_layout(height=300, margin=dict(l=10, r=10, t=10, b=10), paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font=dict(color='#475569', size=11))
        st.plotly_chart(fig2, use_container_width=True)

# ==========================================
# MODULE 7: CASE 6 - VOLATILITY PUSH
# ==========================================
elif "7. Case 6: Push & In-App" in nav_choice:
    st.markdown("### Case 6: Real-Time Market Volatility Push Engine")
    st.markdown("**Executive Context:** High market volatility generates trading volume, but spammy messaging leads to push opt-outs. We enforce an objective, factual notification structure with a **strict 24h frequency cap**.")
    
    asset = st.selectbox("Select Trading Instrument:", ["Bitcoin (BTC/EUR)", "Ethereum (ETH/EUR)", "Solana (SOL/EUR)", "DAX 40 ETF"])
    vol = st.slider("Trigger Anomaly Threshold (24h Move %):", 3.0, 15.0, 5.4, 0.5)
    
    st.markdown(f"""
    <div class="exec-card" style="border-left: 4px solid #0284c7; max-width:650px; min-height:auto;">
        <div style="font-size:0.75rem; color:#0284c7; font-weight:700; margin-bottom:4px;">PUSH NOTIFICATION PAYLOAD • {asset.upper()}</div>
        <strong style="color:#0f172a; font-size:0.95rem;">{asset} moved ±{vol}% in the last 4 hours ⚡</strong>
        <p style="color:#334155; font-size:0.86rem; margin:6px 0 0 0; line-height:1.4;">
            High European volume detected. Tap to view order book depth and set limit orders stress-free.
        </p>
        <div style="margin-top:8px; font-size:0.75rem; color:#64748b;">Deep-link: <code>faizex://markets/{asset.split()[0].lower()}?tab=chart</code> • 24h Frequency Cap Enforced</div>
    </div>
    """, unsafe_allow_html=True)
    st.success("📈 **Quantified Impact:** +44.1% 24h Trade Volume Lift / -62.3% Reduction in Push Opt-Outs.")

# ==========================================
# MODULE 8: CASE 7 - STALLED DEPOSIT
# ==========================================
elif "8. Case 7: Stalled-Deposit Recovery" in nav_choice:
    st.markdown("### Case 7: Stalled-Deposit Recovery Flow")
    st.markdown("**Executive Context:** Recovers verified users who stalled before initiating their first bank transfer using a 15-minute in-app slide-up and a 24-hour supportive care email.")
    
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("""
        <div class="exec-card" style="border-left: 4px solid #d97706; min-height:auto;">
            <div style="font-size:0.75rem; color:#d97706; font-weight:700;">TOUCHPOINT 1 • IN-APP SLIDE-UP (T + 15 MIN)</div>
            <strong style="color:#0f172a; font-size:0.9rem;">Dein 0€ Einzahlungs-Auftrag wartet noch ⏱️</strong>
            <p style="color:#334155; font-size:0.84rem; margin:4px 0 0 0;">
                Tippe unten, um die IBAN direkt in deine Banking-App zu kopieren. Keine Gebühren, sofort startklar.
            </p>
        </div>
        """, unsafe_allow_html=True)
    with c2:
        st.markdown("""
        <div class="exec-card" style="border-left: 4px solid #059669; min-height:auto;">
            <div style="font-size:0.75rem; color:#059669; font-weight:700;">TOUCHPOINT 2 • CUSTOMER CARE EMAIL (T + 24H)</div>
            <strong style="color:#0f172a; font-size:0.9rem;">Brauchst du Unterstützung bei deiner ersten Einzahlung? 🛡️</strong>
            <p style="color:#334155; font-size:0.84rem; margin:4px 0 0 0;">
                Reassuring guidance explaining SEPA instant settlement, zero deposit fees, and German custody security.
            </p>
        </div>
        """, unsafe_allow_html=True)
    st.success("📈 **Quantified Impact:** +20.3% First-Deposit Recovery Rate (+64% Email CTR).")

# ==========================================
# MODULE 9: CASE 8 - MILESTONE GAMIFICATION
# ==========================================
elif "9. Case 8: Milestone Habit Gamification" in nav_choice:
    st.markdown("### Case 8: Milestone Habit Gamification (Goal Gradient DCA)")
    st.markdown("**Executive Context:** Based on the Goal Gradient Effect: celebrates users reaching €500, €1,000, or €5,000 AUC milestones to drive Sparplan retention.")
    
    st.markdown("""
    <div class="exec-card" style="border-left: 4px solid #0284c7; max-width:650px; min-height:auto;">
        <div style="font-size:0.75rem; color:#0284c7; font-weight:700; margin-bottom:4px;">IN-APP MILESTONE CELEBRATION (AUC CROSSED €1,000)</div>
        <strong style="color:#0f172a; font-size:1rem;">🎉 Glückwunsch! Du hast die 1.000€ Spar-Marke erreicht!</strong>
        <p style="color:#334155; font-size:0.86rem; margin:6px 0 0 0; line-height:1.4;">
            Damit gehörst du zu den Top 25% der disziplinierten Langzeit-Investoren auf Faizex. Erhöhe deinen Sparplan um +25€/Monat, um deinen nächsten Meilenstein (2.500€) 4 Monate schneller zu erreichen.
        </p>
    </div>
    """, unsafe_allow_html=True)
    st.success("📈 **Quantified Impact:** 59.2% 12-Month Retention / +52.4% Sparplan Upgrade Velocity.")

# ==========================================
# MODULE 10: CASE 9 - STAKING
# ==========================================
elif "10. Case 9: Idle Asset Staking" in nav_choice:
    st.markdown("### Case 9: Idle Asset Staking Yield Nudge")
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
                <strong style="color:#0f172a; font-size:0.95rem;">Lass deine {tok.split()[0]} nicht schlafen 🪙</strong><br>
                <span style="color:#64748b; font-size:0.82rem;">100% BaFin-regulierte Verwahrung.</span>
            </div>
            <div style="text-align:right;">
                <span style="color:#059669; font-size:1.2rem; font-weight:700;">+€{ann} / Jahr</span><br>
                <span style="color:#64748b; font-size:0.75rem;">(~€{mo}/Monat)</span>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.success("📈 **Quantified Impact:** +3.4x Staking Product Adoption Rate (27.8% Conversion).")

# ==========================================
# MODULE 11: CASE 10 - CRM ARCHITECTURE
# ==========================================
elif "11. Case 10: CRM Automation Architecture" in nav_choice:
    st.markdown("### Case 10: CRM Automation Architecture & State Machine")
    st.markdown("**Executive Context:** Asynchronous Redis caching (4.2ms lookup) and idempotency state machines ensure zero duplicate messages during 100k+ broadcast sends.")
    
    st.code('''
def dispatch_with_idempotency(campaign_id, user_id, payload):
    idempotency_key = hashlib.sha256(f"{campaign_id}:{user_id}:2026_09_01".encode()).hexdigest()
    existing_log = db.get_log(idempotency_key)
    if existing_log and existing_log.status == "DISPATCHED":
        return "SKIPPED_ALREADY_SENT"
        
    db.create_log(idempotency_key, status="PENDING")
    status = esp_provider.send_push(user_id, payload)
    db.update_log(idempotency_key, status="DISPATCHED" if status else "FAILED")
    return "SENT"
    ''', language="python")
    st.success("📈 **Quantified Impact:** 100% Crash-Resilient Delivery (Zero Duplicate Broadcast Sends).")

# ==========================================
# MODULE 12: CASE 11 - CROSS FUNCTIONAL
# ==========================================
elif "12. Case 11: Cross-Functional" in nav_choice:
    st.markdown("### Case 11: Cross-Functional Collaboration & Delivery Framework")
    st.markdown("""
    | Stakeholder | Key Collaboration Area | Standardized Workflow Example |
    |---|---|---|
    | **BI / Analytics Team** | Event tracking, Cohort schemas, SQL queries | Standardizing event naming dictionaries (`kyc_step_reached`, `sparplan_created`). |
    | **Product & Mobile** | In-App message triggers, App deep-links | Testing custom URI schemes (`faizex://verify/video-ident`) across native app releases. |
    | **UX / UI Design** | Responsive HTML templates & design tokens | Accessible dark/light mode compatibility and 48px mobile touch targets. |
    | **Legal & BaFin** | Regulatory compliance & Double-Opt-In (DOI) | Audit-proof DOI consent ledgers and crypto risk disclaimers. |
    """)

# ==========================================
# MODULE 13: CASE 12 - TECHNICAL STACK
# ==========================================
elif "13. Case 12: Technical CRM Stack" in nav_choice:
    st.markdown("### Case 12: Production Liquid & SQL Schemas")
    st.markdown("##### 1. Braze Liquid Conditional Block")
    st.code("""
{% if user.kyc_status != 'approved' %}
  <!-- Unverified Onboarding Flow -->
  <div class="action-banner kyc-reminder">
    <a href="faizex://verify/video-ident">Complete 3-Min Verification &rarr;</a>
  </div>
{% elsif user.active_sparplans == 0 %}
  <!-- Sparplan Accumulation Flow -->
  <div class="action-banner sparplan">
    <a href="faizex://sparplan/new">Set Up €25 Sparplan &rarr;</a>
  </div>
{% endif %}
    """, language="liquid")
    
    st.markdown("##### 2. Snowflake SQL Cohort Extraction Query")
    st.code("""
SELECT 
    u.user_id,
    u.email,
    u.preferred_language,
    MAX(t.created_at) AS last_trade_timestamp,
    COUNT(DISTINCT sp.sparplan_id) AS active_sparplans,
    SUM(w.balance_eur) AS total_custody_balance_eur
FROM users u
JOIN kyc_records k ON u.user_id = k.user_id AND k.status = 'APPROVED'
LEFT JOIN trades t ON u.user_id = t.user_id
LEFT JOIN sparplans sp ON u.user_id = sp.user_id AND sp.status = 'ACTIVE'
LEFT JOIN wallets w ON u.user_id = w.user_id
GROUP BY 1, 2, 3
HAVING 
    MAX(t.created_at) < CURRENT_DATE - INTERVAL '60 days'
    AND COUNT(DISTINCT sp.sparplan_id) = 0
    AND SUM(w.balance_eur) > 10;
    """, language="sql")
