# -*- coding: utf-8 -*-
import streamlit as st
import pandas as pd
import numpy as np
import json
import os
import math
import hashlib
import time
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(
    page_title="FinTech CRM Lifecycle & Architecture OS | Exchange Retention Engine",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom High-End FinTech Terminal Styling
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', sans-serif;
    }
    code, pre {
        font-family: 'JetBrains Mono', monospace !important;
    }
    
    .terminal-hero {
        background: linear-gradient(135deg, #070b14 0%, #0d1829 50%, #0a2540 100%);
        border-radius: 16px;
        padding: 2.2rem 2rem;
        color: white;
        margin-bottom: 1.8rem;
        border: 1px solid rgba(56, 189, 248, 0.2);
        box-shadow: 0 20px 30px -10px rgba(0, 0, 0, 0.5);
    }
    .terminal-title {
        font-size: 2.3rem;
        font-weight: 800;
        letter-spacing: -0.02em;
        background: linear-gradient(to right, #ffffff, #93c5fd, #38bdf8);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.4rem;
    }
    .terminal-sub {
        font-size: 1.05rem;
        color: #94a3b8;
        font-weight: 400;
        line-height: 1.5;
    }
    .badge-bafin {
        display: inline-block;
        background: rgba(16, 185, 129, 0.15);
        color: #34d399;
        border: 1px solid rgba(16, 185, 129, 0.35);
        padding: 4px 12px;
        border-radius: 9999px;
        font-size: 0.75rem;
        font-weight: 700;
        letter-spacing: 0.5px;
        text-transform: uppercase;
        margin-right: 8px;
    }
    .badge-mica {
        display: inline-block;
        background: rgba(56, 189, 248, 0.15);
        color: #38bdf8;
        border: 1px solid rgba(56, 189, 248, 0.35);
        padding: 4px 12px;
        border-radius: 9999px;
        font-size: 0.75rem;
        font-weight: 700;
        letter-spacing: 0.5px;
        text-transform: uppercase;
    }
    .stat-card {
        background: #0f172a;
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 12px;
        padding: 1.2rem;
        text-align: center;
    }
    .stat-val {
        font-size: 1.8rem;
        font-weight: 800;
        color: #38bdf8;
    }
    .stat-lbl {
        font-size: 0.8rem;
        color: #94a3b8;
        text-transform: uppercase;
        letter-spacing: 1px;
        font-weight: 600;
        margin-top: 4px;
    }
    .email-box {
        background: rgba(15, 23, 42, 0.85);
        border: 1px solid rgba(255, 255, 255, 0.12);
        border-radius: 12px;
        padding: 1.5rem;
        margin-bottom: 1.2rem;
    }
    .email-header {
        border-bottom: 1px solid rgba(255, 255, 255, 0.1);
        padding-bottom: 0.8rem;
        margin-bottom: 1rem;
        font-size: 0.9rem;
    }
    .kpi-card {
        background: linear-gradient(145deg, #0f172a 0%, #1e293b 100%);
        border: 1px solid rgba(56, 189, 248, 0.2);
        border-radius: 12px;
        padding: 1.3rem;
        margin-bottom: 1rem;
    }
    .formula-tag {
        background: rgba(56, 189, 248, 0.1);
        color: #38bdf8;
        padding: 3px 8px;
        border-radius: 4px;
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.85rem;
    }
</style>
""", unsafe_allow_html=True)

# Load data assets
base_dir = os.path.dirname(os.path.abspath(__file__))
funnel_path = os.path.join(base_dir, 'data', 'kyc_funnel_dropoffs.csv')
dca_path = os.path.join(base_dir, 'data', 'dca_sparplan_cohorts.csv')
exp_path = os.path.join(base_dir, 'config', 'email_experiments.json')

df_funnel = pd.read_csv(funnel_path) if os.path.exists(funnel_path) else pd.DataFrame()
df_dca = pd.read_csv(dca_path) if os.path.exists(dca_path) else pd.DataFrame()
with open(exp_path, 'r', encoding='utf-8') as f:
    experiments = json.load(f)

# Hero Header

# Disclaimer Banner
st.warning("⚠️ **PORTFOLIO CASE STUDY DISCLAIMER:** **Mison** is a fictional case study name used exclusively for technical CRM demonstration, educational analysis, and open-source system design. It does not represent any real commercial company or trademark. All data and examples are synthetic simulations.")


st.markdown("""
<div class="terminal-hero">
    <div>
        <span class="badge-bafin">🛡️ Regulated European Exchange Framework</span>
        <span class="badge-mica">⚡ Multi-Channel Lifecycle & Open-Source Architecture</span>
    </div>
    <h1 class="terminal-title">FinTech CRM Lifecycle & Architecture OS</h1>
    <p class="terminal-sub">
        Creative CRM Campaigns (Friction Relief & Sparplan Models) + Production Open-Source Engineering (Async Caching, Idempotent Dispatching & Webhook Triggers).
    </p>
</div>
""", unsafe_allow_html=True)

# Sidebar Navigation
st.sidebar.image("https://img.icons8.com/fluency/96/bullish.png", width=54)
st.sidebar.title("CRM Master Navigator")
st.sidebar.markdown("**Dual-Engine Architecture**")

nav_choice = st.sidebar.radio(
    "Select Strategic Module:",
    [
        "📊 1. Executive CRM Dashboard & KPIs",
        "✉️ 2. Case 1: Transactional Confirmation Momentum",
        "🛡️ 3. Case 2: Onboarding & KYC Friction Breaker",
        "📰 4. Case 3: Editorial Newsletter A/B Test (August Edition)",
        "🎯 5. Case 4: Complete Exchange KPI Framework",
        "📈 6. Case 5: 5-Year Sparplan (DCA) LTV & Retention",
        "⚡ 7. Case 6: Volatility Alert Generator & Fatigue Guard",
        "🛠️ 8. Enterprise Architecture & Systems Design Studio",
        "👥 9. Cross-Functional Alignment (Product/BI/Compliance)",
        "💻 10. Technical Stack (Braze, Liquid & SQL Schemas)"
    ]
)

st.sidebar.markdown("---")
st.sidebar.caption("🔒 **Anonymized Portfolio Project**\nDesigned for enterprise digital asset exchanges & regulated European trading ecosystems.")

# ==========================================
# MODULE 1: EXECUTIVE CRM DASHBOARD
# ==========================================
if nav_choice == "📊 1. Executive CRM Dashboard & KPIs":
    st.subheader("🏛️ Executive CRM Dashboard & Exchange Pulse")
    st.markdown("End-to-end view of retail trading velocity, onboarding throughput, automated accumulation (Sparplan) cohorts, and customer lifetime value.")
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown('<div class="stat-card"><div class="stat-val">€148.4M</div><div class="stat-lbl">30D Retail Volume</div></div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="stat-card"><div class="stat-val">39.4%</div><div class="stat-lbl">KYC → 1st Trade Rate (+38.7%)</div></div>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div class="stat-card"><div class="stat-val">59.2%</div><div class="stat-lbl">12M Sparplan Retention</div></div>', unsafe_allow_html=True)
    with col4:
        st.markdown('<div class="stat-card"><div class="stat-val">€9,850</div><div class="stat-lbl">Avg 2-Year AUC / Member</div></div>', unsafe_allow_html=True)
        
    st.markdown("<br>", unsafe_allow_html=True)
    
    col_left, col_right = st.columns([1.2, 1])
    with col_left:
        st.markdown("##### 📉 Onboarding Funnel: Baseline vs. Optimized Lifecycle")
        fig_funnel = go.Figure()
        fig_funnel.add_trace(go.Bar(
            name='Baseline (Control)',
            x=df_funnel['funnel_stage'],
            y=df_funnel['baseline_users'],
            marker_color='#64748b'
        ))
        fig_funnel.add_trace(go.Bar(
            name='Variant B (Friction-Breaker Lifecycle)',
            x=df_funnel['funnel_stage'],
            y=df_funnel['variant_b_users'],
            marker_color='#10b981'
        ))
        fig_funnel.update_layout(
            barmode='group',
            template='plotly_dark',
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            margin=dict(l=20, r=20, t=30, b=80),
            legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
        )
        st.plotly_chart(fig_funnel, use_container_width=True)
        
    with col_right:
        st.markdown("##### 🪙 Retail Asset Allocation (Assets Under Custody)")
        pie_labels = ['Bitcoin (BTC)', 'Ethereum (ETH)', 'DAX & European Equity ETFs', 'Altcoins (SOL, ADA)', 'Cash/Deposit Reserve']
        pie_values = [42, 24, 18, 11, 5]
        fig_pie = px.pie(
            values=pie_values,
            names=pie_labels,
            hole=0.55,
            color_discrete_sequence=['#f59e0b', '#6366f1', '#10b981', '#38bdf8', '#94a3b8']
        )
        fig_pie.update_layout(
            template='plotly_dark',
            paper_bgcolor='rgba(0,0,0,0)',
            margin=dict(l=10, r=10, t=20, b=20)
        )
        st.plotly_chart(fig_pie, use_container_width=True)

# ==========================================
# MODULE 2: CASE 1 - TRANSACTIONAL CONFIRMATION
# ==========================================
elif nav_choice == "✉️ 2. Case 1: Transactional Confirmation Momentum":
    c1 = experiments["case_1_transactional_confirmation"]
    st.subheader("✉️ Case 1: Transactional Email Confirmation & Momentum Builder")
    st.info("**Strategic Context:** Transactional confirmation emails consistently command the highest open rates across the entire lifecycle (65%–75%). Instead of treating this email as a plain administrative stop, our hypothesis tests using the high-intent moment to build momentum directly into app download and verification.")
    
    st.markdown("#### 🔬 Side-by-Side A/B Test Breakdown")
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("##### 🔴 Control (Baseline Email Received)")
        st.markdown(f"""
        <div class="email-box" style="border-left: 4px solid #64748b;">
            <div class="email-header">
                <strong>Subject:</strong> <code>{c1['received_email']['subject']}</code><br>
                <strong>Preheader:</strong> <code>{c1['received_email']['preheader']}</code>
            </div>
            <div style="color: #cbd5e1; font-size: 0.95rem; line-height: 1.6;">
                Hello friend,<br><br>
                We're delighted that you'd like to become part of our community.<br><br>
                Before you can register, we would like to ask you to confirm your email address by using the following link:<br><br>
                <div style="text-align: center; margin: 15px 0;">
                    <span style="background:#0f172a; color:#fff; border:1px solid #38bdf8; padding:9px 22px; border-radius:6px; font-weight:700;">Confirm email address</span>
                </div><br>
                Thanks and best regards,<br>
                Your Team
            </div>
            <hr style="border-color: rgba(255,255,255,0.1);">
            <strong style="color:#38bdf8;">👍 What We Appreciate:</strong> Clean layout, 100% deliverability focus, zero spam triggers.<br><br>
            <strong style="color:#f87171;">💡 Optimization Opportunity:</strong> High open rate (68.2%), but 58.8% of users stop here and take over 18 hours to initiate KYC.
        </div>
        """, unsafe_allow_html=True)
        
    with col2:
        st.markdown("##### 🟢 Variant B (Hypothesis: Momentum Builder)")
        st.markdown(f"""
        <div class="email-box" style="border-left: 4px solid #38bdf8;">
            <div class="email-header">
                <strong>Subject:</strong> <code>{c1['variant_b_hypothesis']['subject']}</code><br>
                <strong>Preheader:</strong> <code>{c1['variant_b_hypothesis']['preheader']}</code>
            </div>
            <div style="color: #cbd5e1; font-size: 0.95rem; line-height: 1.6;">
                Hi [First Name],<br><br>
                You're seconds away from your digital trading workspace. Confirm your email below to get started:<br><br>
                <div style="text-align: center; margin: 15px 0;">
                    <a href="#" style="display:inline-block; background:#38bdf8; color:#0f172a; padding:9px 24px; border-radius:6px; font-weight:800; text-decoration:none;">Confirm Email & Start Exploring &rarr;</a>
                </div><br>
                <div style="background: rgba(0,0,0,0.3); border:1px solid rgba(56,189,248,0.25); border-radius:8px; padding:10px 14px; margin-top:10px;">
                    <strong style="color:#38bdf8; font-size:0.85rem;">🔥 What traders are watching today:</strong><br>
                    <span style="font-size:0.82rem; color:#94a3b8;">• <strong>BTC / EUR:</strong> +3.8% (Consolidating above €58,000)<br>
                    • <strong>ETH / EUR:</strong> +5.1% (Layer-2 volume breakout)<br>
                    • <strong>Automated Sparplan:</strong> Set and forget from €25/month</span>
                </div>
            </div>
            <hr style="border-color: rgba(255,255,255,0.1);">
            <strong style="color:#34d399;">📈 Projected Impact:</strong> <strong>+30.6% Click-Through to App</strong> ($z = 2.89, p = 0.0039$). Reduces time-to-verification from 18.4 hrs to 4.2 hrs.
        </div>
        """, unsafe_allow_html=True)

# ==========================================
# MODULE 3: CASE 2 - ONBOARDING & KYC
# ==========================================
elif nav_choice == "🛡️ 3. Case 2: Onboarding & KYC Friction Breaker":
    c2 = experiments["case_2_welcome_verification"]
    st.subheader("🛡️ Case 2: Onboarding & Video-Ident Friction Breaker")
    st.info("**Strategic Context:** In German & European regulated digital asset exchanges, users sign up eagerly but often hesitate at Video-Ident due to fear of complicated paperwork or long video calls. Our hypothesis replaces dense paragraphs with an empowering 3-step checklist + mobile deep-linking.")
    
    st.markdown("#### 🔬 Side-by-Side A/B Test Breakdown")
    colA, colB = st.columns(2)
    
    with colA:
        st.markdown("##### 🔴 Control (Baseline Email Received)")
        st.markdown(f"""
        <div class="email-box" style="border-left: 4px solid #64748b;">
            <div class="email-header">
                <strong>Subject:</strong> <code>{c2['received_email']['subject']}</code><br>
                <strong>Preheader:</strong> <code>{c2['received_email']['preheader']}</code>
            </div>
            <div style="color: #cbd5e1; font-size: 0.95rem; line-height: 1.6;">
                Hi,<br><br>
                You've just become part of our community and are now able to use the best crypto app in Germany! When it comes to trading, our exchange-backed platform is a partner you can rely on. Our goal is to make trading as simple as possible for you. There's no need for a wallet, securities account, or even paperwork.<br><br>
                <div style="text-align: center; margin: 10px 0;">
                    <span style="background:#0f172a; color:#fff; border:1px solid #38bdf8; padding:8px 20px; border-radius:6px; font-weight:700;">Verify now</span>
                </div><br>
                Are you familiar with the app and ready to start trading? Then jump right in and start trading with real money. Just take a few minutes to verify your identity through a simple video identification process and you'll be ready to go!<br><br>
                <div style="text-align: center; margin: 10px 0;">
                    <span style="background:#0f172a; color:#fff; border:1px solid #38bdf8; padding:8px 20px; border-radius:6px; font-weight:700;">Verify now</span>
                </div>
            </div>
            <hr style="border-color: rgba(255,255,255,0.1);">
            <strong style="color:#38bdf8;">👍 What We Appreciate:</strong> Strong trust anchor (Stock Exchange backing), clear 'no wallet complexity' message.<br><br>
            <strong style="color:#f87171;">💡 Optimization Opportunity:</strong> Two identical buttons and text-heavy blocks create reading fatigue; 42% drop off before starting Video-Ident.
        </div>
        """, unsafe_allow_html=True)
        
    with colB:
        st.markdown("##### 🟢 Variant B (Hypothesis: 3-Step Friction Breaker)")
        st.markdown(f"""
        <div class="email-box" style="border-left: 4px solid #10b981;">
            <div class="email-header">
                <strong>Subject:</strong> <code>{c2['variant_b_hypothesis']['subject']}</code><br>
                <strong>Preheader:</strong> <code>{c2['variant_b_hypothesis']['preheader']}</code>
            </div>
            <div style="color: #cbd5e1; font-size: 0.95rem; line-height: 1.6;">
                Hi [First Name],<br><br>
                Welcome to your institutional-grade trading account. Your workspace is 1 step away from activation:<br><br>
                <div style="background:rgba(16,185,129,0.08); border:1px solid rgba(16,185,129,0.25); border-radius:8px; padding:12px 16px; margin: 10px 0;">
                    <strong>✅ Step 1:</strong> Have your ID card or passport ready (1 min)<br>
                    <strong>✅ Step 2:</strong> Quick 2-minute Video-Ident call<br>
                    <strong>✅ Step 3:</strong> Instant account ready for first trade (0€ deposit fee)
                </div><br>
                <div style="text-align: center; margin: 15px 0;">
                    <a href="#" style="display:inline-block; background:#10b981; color:#0f172a; padding:9px 24px; border-radius:6px; font-weight:800; text-decoration:none;">Unlock My Account in App (3 Mins) &rarr;</a>
                </div><br>
                <div style="text-align:center; font-size:0.8rem; color:#94a3b8;">
                    🔒 BaFin Regulated • Insured European Custody • No Wallet Complexity
                </div>
            </div>
            <hr style="border-color: rgba(255,255,255,0.1);">
            <strong style="color:#34d399;">📈 Projected Impact:</strong> <strong>+38.7% KYC Completion Lift</strong> (28.4% → 39.4%, $z = 3.12, p = 0.0018$).
        </div>
        """, unsafe_allow_html=True)

# ==========================================
# MODULE 4: CASE 3 - MONTHLY NEWSLETTER
# ==========================================
elif nav_choice == "📰 4. Case 3: Editorial Newsletter A/B Test (August Edition)":
    c3 = experiments["case_3_editorial_misonews"]
    st.subheader("📰 Case 3: Monthly Newsletter A/B Test (August Market News)")
    st.info("**Strategic Context:** Monthly market reviews offer great educational value. The August edition clearly breaks down the US debt spiral, Nvidia earnings, and Bitcoin rally. Our hypothesis keeps this high-quality editorial, but tests replacing the single static 'Trade Bitcoin' button with dynamic lifecycle-segmented CTAs.")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("##### 🔴 Control (Actual Newsletter Received)")
        st.markdown("""
        <div class="email-box" style="border-left: 4px solid #64748b;">
            <div class="email-header">
                <strong>Subject:</strong> <code>Hi, here's your Misonews for August 📰</code><br>
                <strong>Preheader:</strong> <code>Bitcoin has woken up and pulled the market out of hibernation</code>
            </div>
            <div style="color: #cbd5e1; font-size: 0.92rem; line-height: 1.5;">
                <p><strong>Hi,</strong></p>
                <p>Bitcoin has woken up—and pulled the entire crypto market out of hibernation. The wake-up call came from Washington, where the US debt pile is spiraling out of control. We break down what's behind it...</p>
                <div style="background:rgba(0,0,0,0.3); border:1px solid rgba(255,255,255,0.1); border-radius:6px; padding:10px; margin: 10px 0;">
                    <strong style="color:#38bdf8;">📊 Market News (August Breakdown):</strong><br>
                    • <strong>Nvidia:</strong> Exceeded expectations, quarterly capex doubled.<br>
                    • <strong>US Debt ($35T):</strong> Interest rate pressures mount.<br>
                    • <strong>Bitcoin & Gold:</strong> Rally as hedge against monetary expansion.
                </div>
                <div style="text-align: center; margin: 15px 0;">
                    <span style="background:#0f172a; color:#fff; border:1px solid #38bdf8; padding:8px 22px; border-radius:6px; font-weight:700;">Trade Bitcoin</span>
                </div>
                <p><strong>🪙 Coin of the Month:</strong> Solana ETF inflows hit 3-month highs...</p>
            </div>
            <hr style="border-color: rgba(255,255,255,0.1);">
            <strong style="color:#38bdf8;">👍 What We Appreciate:</strong> Superb editorial storytelling, digestible macro summaries, attractive 3D visuals.<br><br>
            <strong style="color:#f87171;">💡 Optimization Opportunity:</strong> A single static 'Trade Bitcoin' button ignores user lifecycle state (non-holders hesitate; long-term accumulators prefer DCA).
        </div>
        """, unsafe_allow_html=True)
        
    with col2:
        st.markdown("##### 🟢 Variant B (Hypothesis: Dynamic Lifecycle CTAs)")
        selected_persona = st.selectbox(
            "Select Persona to Preview Dynamic Module:",
            [
                "🌱 Unverified User (0 Trades)",
                "📊 Occasional Spot Buyer (Manual Trader)",
                "📈 Active Sparplan Accumulator (Monthly DCA)",
                "💤 Dormant Account (>60 Days Inactive)"
            ]
        )
        
        st.markdown("""
        <div class="email-box" style="border-left: 4px solid #10b981;">
            <div class="email-header">
                <strong>Subject:</strong> <code>Market Digest: Institutional flows & Volatility shift [Portfolio Impact] 📈</code><br>
                <strong>Preheader:</strong> <code>Bitcoin macro update + personalized accumulation strategy</code>
            </div>
            <div style="color: #cbd5e1; font-size: 0.92rem; line-height: 1.5;">
                <p><strong>Hi [First Name],</strong></p>
                <p>Bitcoin has woken up—and pulled the entire crypto market out of hibernation. [Editorial report preserved in full]...</p>
        """, unsafe_allow_html=True)
        
        if "Unverified" in selected_persona:
            st.markdown("""
                <div style="background:rgba(245,158,11,0.12); border:1px solid #f59e0b; border-radius:8px; padding:12px; margin: 10px 0;">
                    <strong style="color:#f59e0b;">🌱 Tailored Next Step: 3-Minute Verification</strong><br>
                    <span style="font-size:0.85rem;">Ready to participate in market movement? Complete your free 3-minute Video-Ident today.</span><br>
                    <div style="text-align:center; margin-top:8px;">
                        <span style="background:#f59e0b; color:#0f172a; padding:6px 16px; border-radius:4px; font-weight:800; font-size:0.85rem;">Complete Verification in App &rarr;</span>
                    </div>
                </div>
            """, unsafe_allow_html=True)
        elif "Spot Buyer" in selected_persona:
            st.markdown("""
                <div style="background:rgba(16,185,129,0.12); border:1px solid #10b981; border-radius:8px; padding:12px; margin: 10px 0;">
                    <strong style="color:#10b981;">📈 Tailored Next Step: Stress-Free DCA Sparplan</strong><br>
                    <span style="font-size:0.85rem;">Stop timing the market. Automate your Bitcoin accumulation with a monthly Sparplan from €25.</span><br>
                    <div style="text-align:center; margin-top:8px;">
                        <span style="background:#10b981; color:#0f172a; padding:6px 16px; border-radius:4px; font-weight:800; font-size:0.85rem;">Set Up Free Sparplan (0€ Setup) &rarr;</span>
                    </div>
                </div>
            """, unsafe_allow_html=True)
        elif "Sparplan" in selected_persona:
            st.markdown("""
                <div style="background:rgba(56,189,248,0.12); border:1px solid #38bdf8; border-radius:8px; padding:12px; margin: 10px 0;">
                    <strong style="color:#38bdf8;">🚀 Tailored Next Step: Portfolio Milestone & Staking</strong><br>
                    <span style="font-size:0.85rem;">Your Sparplan has steadily accumulated assets. Check your August portfolio performance & staking rewards.</span><br>
                    <div style="text-align:center; margin-top:8px;">
                        <span style="background:#38bdf8; color:#0f172a; padding:6px 16px; border-radius:4px; font-weight:800; font-size:0.85rem;">View My Portfolio & Staking &rarr;</span>
                    </div>
                </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown("""
                <div style="background:rgba(236,72,153,0.12); border:1px solid #ec4899; border-radius:8px; padding:12px; margin: 10px 0;">
                    <strong style="color:#ec4899;">⚡ Tailored Next Step: Custom Volatility Alerts</strong><br>
                    <span style="font-size:0.85rem;">Never miss significant price swings. Turn on real-time price movement push notifications.</span><br>
                    <div style="text-align:center; margin-top:8px;">
                        <span style="background:#ec4899; color:#fff; padding:6px 16px; border-radius:4px; font-weight:800; font-size:0.85rem;">Activate Price Movement Alerts &rarr;</span>
                    </div>
                </div>
            """, unsafe_allow_html=True)
            
        st.markdown("""
            </div>
            <hr style="border-color: rgba(255,255,255,0.1);">
            <strong style="color:#34d399;">📈 Projected Impact:</strong> <strong>+86.3% Click-to-Open (CTOR) Lift</strong> (12.4% → 23.1%, $z = 4.15, p < 0.0001$).
        </div>
        """, unsafe_allow_html=True)

# ==========================================
# MODULE 5: CASE 4 - KEY KPIS
# ==========================================
elif nav_choice == "🎯 5. Case 4: Complete Exchange KPI Framework":
    st.subheader("🎯 Case 4: The 5 Essential KPIs for a Regulated Trading Platform")
    st.markdown("A complete quantitative framework for evaluating customer acquisition, onboarding velocity, retention economics, and lifetime portfolio value.")
    
    kpis = [
        {
            "name": "1. KYC Verification Throughput Rate",
            "formula": "KYC Rate = (Approved Verified Users / Total Registrations) * 100",
            "target": "Target: > 40% (Industry avg is ~28%)",
            "why": "Identifies the drop-off bottleneck between app registration and Video-Ident. In regulated European markets (BaFin/MiCA), drops here directly inflate paid Customer Acquisition Cost (CAC).",
            "how": "Tracked via event timestamps (registration_completed vs. kyc_approved) in amplitude/GA4 & CRM."
        },
        {
            "name": "2. Time-to-First-Trade (TTFT)",
            "formula": "TTFT = Timestamp(First Trade Executed) - Timestamp(Registration Completed)",
            "target": "Target: < 24 Hours (Ideal: < 4 Hours)",
            "why": "The single strongest predictor of 12-month retention. Over 70% of retail churn occurs when TTFT exceeds 7 days due to lost intent.",
            "how": "Measured as median hours across monthly cohorts to filter out inactive outliers."
        },
        {
            "name": "3. Automated Sparplan (DCA) Adoption Rate",
            "formula": "Sparplan Rate = (Active Recurring Accumulators / Monthly Active Traders) * 100",
            "target": "Target: > 35% of Active User Base",
            "why": "Manual spot trading is volatile and drops during bear markets. Recurring Sparplan users accumulate steady Assets Under Custody (AUC) and exhibit 2.6x higher 12-month retention.",
            "how": "Calculated as users with ≥1 active scheduled monthly/weekly recurring order."
        },
        {
            "name": "4. Assets Under Custody (AUC) per Active Trader",
            "formula": "Avg AUC = Total Portfolio Assets in Custody (€) / Total Active Traders",
            "target": "Target: > €7,500 at Year 1 → > €12,000 at Year 3",
            "why": "Measures customer portfolio depth and staking potential. Higher AUC translates directly into spread volume and net interest margin revenue.",
            "how": "Aggregated daily from custodial ledger databases."
        },
        {
            "name": "5. Inactivity Churn Rate & Volatility Reactivation Velocity",
            "formula": "Churn = (Users with 0 Trades in 60 Days / Total Verified Users) * 100",
            "target": "Target Churn: < 4.5% / month | Reactivation: > 18% within 48h of market surge",
            "why": "Measures the effectiveness of volatility-driven trigger alerts in waking up dormant balances before permanent account churn.",
            "how": "Tracked via 30/60/90-day inactivity buckets in CRM (Braze/Klaviyo)."
        }
    ]
    
    for k in kpis:
        st.markdown(f"""
        <div class="kpi-card">
            <div style="display:flex; justify-content:space-between; align-items:center;">
                <h4 style="color:#38bdf8; margin:0;">{k['name']}</h4>
                <span class="formula-tag">{k['target']}</span>
            </div>
            <div style="margin: 8px 0; font-family:'JetBrains Mono', monospace; color:#34d399; font-size:0.9rem;">
                {k['formula']}
            </div>
            <p style="color:#cbd5e1; font-size:0.92rem; margin:6px 0;"><strong>Why it Matters:</strong> {k['why']}</p>
            <p style="color:#94a3b8; font-size:0.85rem; margin:0;"><strong>How to Calculate:</strong> {k['how']}</p>
        </div>
        """, unsafe_allow_html=True)
        
    st.markdown("---")
    st.markdown("#### 🧮 Interactive Revenue & LTV Impact Calculator")
    c_col1, c_col2, c_col3 = st.columns(3)
    with c_col1:
        reg_input = st.number_input("Monthly New Registrations:", value=10000, step=1000)
    with c_col2:
        kyc_input = st.slider("KYC Verification Rate (%):", min_value=20.0, max_value=60.0, value=39.4, step=0.5)
    with c_col3:
        sparplan_input = st.slider("Sparplan Adoption Rate (%):", min_value=10.0, max_value=60.0, value=35.0, step=1.0)
        
    verified_users = int(reg_input * (kyc_input / 100))
    sparplan_users = int(verified_users * (sparplan_input / 100))
    annual_auc_added = sparplan_users * 100 * 12 # €100/mo avg
    
    st.success(f"""
    **Projected Annual Impact for these Parameters:**
    * **Verified Trading Accounts Added/Year:** `{verified_users * 12:,}` active accounts
    * **Recurring Sparplan Accumulators Added/Year:** `{sparplan_users * 12:,}` automated savers
    * **Annual Assets Under Custody (AUC) Inflow:** `€{annual_auc_added:,}` / year
    """)

# ==========================================
# MODULE 6: 5-YEAR SPARPLAN FORECASTER
# ==========================================
elif nav_choice == "📈 6. Case 5: 5-Year Sparplan (DCA) LTV & Retention":
    st.subheader("📈 Case 5: 5-Year Sparplan (DCA) Customer Lifetime Value & Retention Model")
    st.markdown("Comparing long-term retention decay and Assets Under Custody (AUC) between **Manual One-Off Spot Traders** vs. **Automated Recurring Sparplan Accumulators**.")
    
    monthly_deposit = st.slider("Monthly Sparplan Contribution (€/month):", min_value=25, max_value=500, value=100, step=25)
    
    months = np.arange(1, 61)
    df_dca_calc = pd.DataFrame({
        'Month': months,
        'Sparplan Retention (%)': [round(100 * (0.988 ** m), 1) for m in months],
        'Spot Trader Retention (%)': [round(100 * (0.935 ** m), 1) for m in months],
        'Sparplan AUC (€)': [round(monthly_deposit * m * (1.006 ** m), 2) for m in months],
        'Spot Trader AUC (€)': [round(450 * (1 + 0.05 * math.sin(m/3)), 2) for m in months]
    })
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("##### 📊 Cohort Retention Decay Curve")
        fig_ret = go.Figure()
        fig_ret.add_trace(go.Scatter(x=df_dca_calc['Month'], y=df_dca_calc['Sparplan Retention (%)'], name='Sparplan Accumulator', line=dict(color='#10b981', width=3)))
        fig_ret.add_trace(go.Scatter(x=df_dca_calc['Month'], y=df_dca_calc['Spot Trader Retention (%)'], name='Manual Spot Trader', line=dict(color='#f43f5e', width=2, dash='dot')))
        fig_ret.update_layout(template='plotly_dark', paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', margin=dict(l=20, r=20, t=20, b=20))
        st.plotly_chart(fig_ret, use_container_width=True)
        
    with col2:
        st.markdown("##### 💰 Assets Under Custody (AUC) Growth (€)")
        fig_auc = go.Figure()
        fig_auc.add_trace(go.Scatter(x=df_dca_calc['Month'], y=df_dca_calc['Sparplan AUC (€)'], name='Sparplan Portfolio', line=dict(color='#38bdf8', width=3), fill='tozeroy'))
        fig_auc.add_trace(go.Scatter(x=df_dca_calc['Month'], y=df_dca_calc['Spot Trader AUC (€)'], name='Spot Trader Portfolio', line=dict(color='#64748b', width=2)))
        fig_auc.update_layout(template='plotly_dark', paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', margin=dict(l=20, r=20, t=20, b=20))
        st.plotly_chart(fig_auc, use_container_width=True)

# ==========================================
# MODULE 7: VOLATILITY ALERT GENERATOR
# ==========================================
elif nav_choice == "⚡ 7. Case 6: Volatility Alert Generator & Fatigue Guard":
    st.subheader("⚡ Case 6: Market Volatility & Push Trigger Simulator")
    st.markdown("Simulating programmatic trigger alerts dispatched via Braze / Push Notifications when market volatility surges past standard statistical deviations.")
    
    asset = st.selectbox("Select Volatility Instrument:", ["Bitcoin (BTC/EUR)", "Ethereum (ETH/EUR)", "Solana (SOL/EUR)", "DAX 40"])
    vol_threshold = st.slider("Trigger Threshold (24h Price Move %):", min_value=3.0, max_value=15.0, value=5.0, step=0.5)
    
    st.markdown(f"""
    <div class="email-box" style="border-left: 4px solid #10b981;">
        <h4 style="color:#38bdf8;">📲 Simulated Real-Time Push Payload ({asset})</h4>
        <strong>Notification Title:</strong> <code>{asset} moved ±{vol_threshold}% in the last 4 hours ⚡</code><br>
        <strong>Body:</strong> <code>High trading volume detected across European venues. Tap to view live order book depth & update limit orders.</code><br>
        <strong>Deep Link:</strong> <code>exchangeapp://markets/{asset.split()[0].lower()}?tab=chart</code>
    </div>
    """, unsafe_allow_html=True)

# ==========================================
# MODULE 8: OPEN-SOURCE ARCHITECTURE STUDIO
# ==========================================
elif nav_choice == "🛠️ 8. Enterprise Architecture & Systems Design Studio":
    st.subheader("🛠️ Open-Source CRM Architecture & Microservices Studio")
    st.markdown("Demonstrating how open-source CRM architectural patterns (**Mautic**, **EspoCRM**, **Frappe / ERPNext**) solve enterprise-scale FinTech marketing challenges.")
    
    arch_tab1, arch_tab2, arch_tab3 = st.tabs([
        "⚙️ Async In-Memory Segment Cache",
        "🛡️ Idempotent Crash-Resilient Dispatcher",
        "⚡ Real-Time Event-Driven Market Router"
    ])
    
    with arch_tab1:
        st.markdown("#### 1. Mautic-Inspired Async Segment Batching")
        st.markdown("Instead of querying 500,000 rows live during campaign send, an asynchronous background task pre-computes dynamic audience memberships into a fast-lookup Redis cache.")
        
        col_c1, col_c2 = st.columns(2)
        with col_c1:
            st.code("""
# Asynchronous Background Segment Cache Engine
def update_segment_cache(db_conn, segment_id, criteria):
    query = """
        SELECT user_id FROM users 
        WHERE kyc_status = %s 
          AND custody_balance >= %s 
          AND last_trade_days >= %s
    """
    matched_ids = db_conn.execute(query, (criteria['kyc'], criteria['balance'], criteria['days'])).fetchall()
    redis_client.set(f"segment:{segment_id}", json.dumps(matched_ids), ex=900)
    return len(matched_ids)
            """, language="python")
        with col_c2:
            st.markdown("##### 🚀 Test Live Segment Extraction:")
            sim_kyc = st.selectbox("Filter: KYC Status", ["APPROVED", "PENDING_VERIFICATION", "ALL"])
            sim_bal = st.slider("Filter: Min Custody Balance (€)", 0, 5000, 500, 100)
            if st.button("Run Async Batch Cache Simulation"):
                sim_count = int(10000 * (0.4 if sim_kyc=="APPROVED" else 0.28) * (1 - sim_bal/6000))
                st.success(f"✅ Pre-calculated Segment in 4.2ms! Cached {sim_count:,} User IDs to Redis key `segment:active_traders` (TTL: 15m)")
                
    with arch_tab2:
        st.markdown("#### 2. EspoCRM-Inspired Idempotent Dispatcher (Crash Recovery)")
        st.markdown("Uses unique idempotency keys (`campaign:user:date`) to guarantee **zero duplicate messages** even if the broadcast server crashes halfway through a 100k blast.")
        
        st.code("""
# Idempotency Key & State Machine Verification
def dispatch_with_idempotency(campaign_id, user_id, payload):
    idempotency_key = hashlib.sha256(f"{campaign_id}:{user_id}:2026_09_01".encode()).hexdigest()
    
    # Check if already sent or in flight
    existing_log = db.get_log(idempotency_key)
    if existing_log and existing_log.status == "DISPATCHED":
        return "SKIPPED_ALREADY_SENT"
        
    db.create_log(idempotency_key, status="PENDING")
    status = esp_provider.send_push(user_id, payload)
    db.update_log(idempotency_key, status="DISPATCHED" if status else "FAILED")
    return "SENT"
        """, language="python")
        
        if st.button("Simulate Server Crash & Resume Execution"):
            st.warning("⚠️ Worker crashed after sending to 50 / 100 users! Restarting worker...")
            time.sleep(0.5)
            st.success("✅ Worker resumed safely! Skipped 50 already-sent records via Idempotency Log. Dispatched remaining 50 records. Total duplicates: 0.")
            
    with arch_tab3:
        st.markdown("#### 3. Frappe-Inspired Real-Time Webhook Market Event Router")
        st.markdown("Exchange order-book tickers emit a webhook to `/api/v1/market-events`. The engine evaluates volatility anomalies ($Z > 2.5\sigma$), queries pre-computed watcher segments, validates the 24-hour cross-channel fatigue rule, and dispatches targeted push notifications.")
        
        st.code("""
# Real-Time Event-Driven Market Router
@app.post("/api/v1/market-events")
def handle_market_webhook(payload):
    # e.g., payload = {"ticker": "BTC/EUR", "price_change_4h_pct": 5.4}
    if abs(payload['price_change_4h_pct']) >= 5.0:
        target_users = redis_client.get("segment:btc_watchers")
        for user_id in target_users:
            if not fatigue_guard.has_received_push_in_24h(user_id):
                braze_client.send_push(user_id, title=f"Bitcoin moved {payload['price_change_4h_pct']}% ⚡")
        return {"status": "dispatched", "users_targeted": len(target_users)}
        """, language="python")

# ==========================================
# MODULE 9: CROSS-FUNCTIONAL ALIGNMENT
# ==========================================
elif nav_choice == "👥 9. Cross-Functional Alignment (Product/BI/Compliance)":
    st.subheader("👥 Cross-Functional Collaboration & Delivery Framework")
    st.markdown("How the CRM Manager coordinates end-to-end campaign execution across BI, Product, UX/UI, and Compliance.")
    
    st.markdown("""
    | Stakeholder | Key Collaboration Area | Real Workflow Example |
    |---|---|---|
    | **BI / Analytics Team** | Event tracking, Cohort schemas, SQL queries, Amplitude funnels | Defining custom custom event attributes: `sparplan_paused_reason`, `kyc_retry_count`, `last_trade_asset_class`. |
    | **Product & Engineering** | In-App message triggers, App deep-links, API webhooks | Integrating direct URI schemes (`app://verify/video-ident`, `app://sparplan/create`) to ensure seamless in-app navigation. |
    | **UX / UI Design** | In-App Banners, Modal layouts, HTML email templates | Ensuring consistent typography, dark/light mode compatibility, and mobile-first tap targets. |
    | **Legal & Compliance (BaFin/MiCA)** | GDPR consent, Risk disclaimers, Audit trails | Reviewing risk warnings on high-volatility token promotions and ensuring strict double-opt-in (DOI) records. |
    """)

# ==========================================
# MODULE 10: TECHNICAL STACK & LIQUID
# ==========================================
elif nav_choice == "💻 10. Technical Stack (Braze, Liquid & SQL Schemas)":
    st.subheader("💻 Technical Execution: Braze Event Architecture & Liquid Logic")
    st.markdown("Production-ready schemas and dynamic templates demonstrating technical CRM proficiency.")
    
    st.markdown("##### 1. Liquid Dynamic Template for Multichannel Campaign")
    st.code("""
{% assign user_kyc = {{custom_attribute.${kyc_status}}} %}
{% assign last_trade = {{custom_attribute.${last_trade_date}}} %}
{% assign days_dormant = "now" | date: "%s" | minus: last_trade | divided_by: 86400 %}

{% if user_kyc != 'approved' %}
  <!-- Unverified Onboarding Flow -->
  <div class="action-banner kyc-reminder">
    <h3>Complete your 3-minute Video-Ident</h3>
    <a href="exchangeapp://verify/video-ident">Verify Now &rarr;</a>
  </div>
{% elsif days_dormant > 60 %}
  <!-- Re-Engagement Volatility Flow -->
  <div class="action-banner winback">
    <h3>Markets are moving: View {{custom_attribute.${top_watched_coin}}} today</h3>
    <a href="exchangeapp://markets/{{custom_attribute.${top_watched_coin} | downcase}}">Trade {{custom_attribute.${top_watched_coin}}} &rarr;</a>
  </div>
{% else %}
  <!-- Sparplan Accumulation Flow -->
  <div class="action-banner sparplan">
    <h3>Set and forget: Automate your monthly DCA from €25</h3>
    <a href="exchangeapp://sparplan/new">Set Up Sparplan &rarr;</a>
  </div>
{% endif %}
    """, language="liquid")
    
    st.markdown("##### 2. SQL Cohort Extraction Query (Snowflake / PostgreSQL)")
    st.code("""
-- Identify At-Risk Verified Traders for Volatility Re-Engagement
SELECT 
    u.user_id,
    u.email,
    u.preferred_language,
    u.device_os,
    MAX(t.created_at) AS last_trade_timestamp,
    COUNT(DISTINCT sp.sparplan_id) AS active_sparplans,
    SUM(w.balance_eur) AS total_custody_balance_eur
FROM users u
JOIN kyc_records k ON u.user_id = k.user_id AND k.status = 'APPROVED'
LEFT JOIN trades t ON u.user_id = t.user_id
LEFT JOIN sparplans sp ON u.user_id = sp.user_id AND sp.status = 'ACTIVE'
LEFT JOIN wallets w ON u.user_id = w.user_id
GROUP BY 1, 2, 3, 4
HAVING 
    MAX(t.created_at) < CURRENT_DATE - INTERVAL '60 days'
    AND COUNT(DISTINCT sp.sparplan_id) = 0
    AND SUM(w.balance_eur) > 10;
    """, language="sql")
