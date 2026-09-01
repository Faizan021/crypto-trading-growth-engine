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
    page_title="Faizex Digital | CRM Lifecycle Marketing & Retention OS",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# High-End FinTech Terminal & Glassmorphism Styling
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
        background: linear-gradient(135deg, #070b14 0%, #0d1829 45%, #0f2e4a 100%);
        border-radius: 16px;
        padding: 2.2rem 2.2rem;
        color: white;
        margin-bottom: 1.5rem;
        border: 1px solid rgba(56, 189, 248, 0.25);
        box-shadow: 0 20px 35px -10px rgba(0, 0, 0, 0.6);
    }
    .terminal-title {
        font-size: 2.4rem;
        font-weight: 800;
        letter-spacing: -0.03em;
        background: linear-gradient(to right, #ffffff, #93c5fd, #38bdf8);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.4rem;
    }
    .terminal-sub {
        font-size: 1.05rem;
        color: #94a3b8;
        font-weight: 400;
        line-height: 1.6;
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
    .badge-braze {
        display: inline-block;
        background: rgba(168, 85, 247, 0.15);
        color: #c084fc;
        border: 1px solid rgba(168, 85, 247, 0.35);
        padding: 4px 12px;
        border-radius: 9999px;
        font-size: 0.75rem;
        font-weight: 700;
        letter-spacing: 0.5px;
        text-transform: uppercase;
    }
    .phone-mockup {
        background: #090d16;
        border: 3px solid #1e293b;
        border-radius: 28px;
        padding: 1.5rem 1.2rem;
        max-width: 420px;
        margin: 0 auto;
        box-shadow: 0 25px 40px -15px rgba(0,0,0,0.8);
    }
    .phone-notch {
        width: 120px;
        height: 18px;
        background: #1e293b;
        border-radius: 0 0 10px 10px;
        margin: -1.5rem auto 1rem auto;
    }
    .stat-card {
        background: linear-gradient(145deg, #0b1120 0%, #0f172a 100%);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 14px;
        padding: 1.2rem;
        text-align: center;
        transition: transform 0.2s ease;
    }
    .stat-card:hover {
        border-color: rgba(56, 189, 248, 0.4);
    }
    .stat-val {
        font-size: 1.85rem;
        font-weight: 800;
        color: #38bdf8;
    }
    .stat-lbl {
        font-size: 0.78rem;
        color: #94a3b8;
        text-transform: uppercase;
        letter-spacing: 1px;
        font-weight: 600;
        margin-top: 4px;
    }
    .email-container-control {
        background: #0f172a;
        border: 1px solid rgba(100, 116, 139, 0.3);
        border-radius: 12px;
        padding: 1.5rem;
        margin-bottom: 1.2rem;
    }
    .email-container-variant {
        background: linear-gradient(165deg, #0b1528 0%, #071322 100%);
        border: 1px solid rgba(56, 189, 248, 0.4);
        border-radius: 12px;
        padding: 1.5rem;
        margin-bottom: 1.2rem;
        box-shadow: 0 10px 25px -5px rgba(56, 189, 248, 0.1);
    }
    .kpi-row-card {
        background: #0b1120;
        border: 1px solid rgba(56, 189, 248, 0.2);
        border-radius: 12px;
        padding: 1.2rem 1.4rem;
        margin-bottom: 0.9rem;
    }
</style>
""", unsafe_allow_html=True)

# Top Disclaimer Notice
st.warning("⚠️ **PORTFOLIO CASE STUDY NOTICE:** **Faizex** is a custom portfolio case study platform created by **Faizan Ahmed** to demonstrate multi-channel CRM lifecycle design, behavioral segmentation, and data-driven A/B testing in a regulated European trading environment. All company names and metrics are synthetic simulations.")

# Hero Header
st.markdown("""
<div class="terminal-hero">
    <div>
        <span class="badge-bafin">🛡️ BaFin & MiCA Regulated Architecture</span>
        <span class="badge-braze">⚡ Braze Multi-Channel Lifecycle OS</span>
    </div>
    <h1 class="terminal-title">Faizex Digital | CRM Growth & Retention Engine</h1>
    <p class="terminal-sub">
        Data-Driven Customer Journeys (Email, Push, In-App, Banners), Behavioral Friction-Breakers, Sparplan DCA Models, and Real-Time Volatility Triggers.
    </p>
</div>
""", unsafe_allow_html=True)

# Load data assets safely
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
st.sidebar.image("https://img.icons8.com/fluency/96/bullish.png", width=54)
st.sidebar.title("Faizex CRM Navigator")
st.sidebar.markdown("**Lifecycle Pillars (Job Specs)**")

nav_choice = st.sidebar.radio(
    "Select Lifecycle Pillar:",
    [
        "📊 1. Executive CRM Dashboard & KPIs",
        "✉️ 2. Case 1: Activation (Transactional Confirmation Momentum)",
        "🛡️ 3. Case 2: Onboarding (KYC Friction-Breaker Journey)",
        "📰 4. Case 3: Engagement (Newsletter A/B Test & Liquid CTAs)",
        "🎯 5. Case 4: Exchange CRM & Retention KPIs",
        "📈 6. Case 5: Retention & Loyalty (5-Year Sparplan Model)",
        "⚡ 7. Case 6: Push & In-App Triggers (Market Volatility Engine)",
        "🏦 8. Case 7: Stalled-Deposit Recovery Flow",
        "🏆 9. Case 8: Milestone Habit Gamification (Goal Gradient DCA)",
        "🪙 10. Case 9: Idle Capital Staking & Yield Nudge",
        "🛠️ 11. Case 10: CRM Automation Architecture & Crash Recovery",
        "👥 12. Case 11: Cross-Functional Alignment (Product/BI/Compliance)",
        "💻 13. Case 12: Technical CRM Stack (Braze, Liquid & SQL Schemas)"
    ]
)

st.sidebar.markdown("---")
st.sidebar.caption("👨‍💻 **Portfolio Project by Faizan Ahmed**\nDesigned for enterprise digital asset exchanges & regulated European trading platforms.")

# ==========================================
# MODULE 1: EXECUTIVE CRM DASHBOARD
# ==========================================
if "1. Executive CRM Dashboard" in nav_choice:
    st.subheader("🏛️ Executive CRM Dashboard & Retail Trading Pulse")
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
        st.markdown("##### 📉 Onboarding Funnel: Baseline vs. Optimized Friction-Breaker")
        if not df_funnel.empty:
            fig_funnel = go.Figure()
            fig_funnel.add_trace(go.Bar(
                name='Control (Baseline)',
                x=df_funnel['funnel_stage'],
                y=df_funnel['baseline_users'],
                marker_color='#64748b'
            ))
            fig_funnel.add_trace(go.Bar(
                name='Variant B (Friction-Breaker)',
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
        st.markdown("##### 🪙 Retail Assets Under Custody (AUC) Allocation")
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
elif "2. Case 1: Activation" in nav_choice:
    st.subheader("✉️ Case 1: Transactional Confirmation & Momentum Builder")
    st.info("**Strategic Context:** Transactional confirmation emails consistently command the highest open rates across the entire lifecycle (68.2%). Instead of treating this email as a plain administrative stop, our hypothesis tests using the high-intent moment to build momentum directly into app download and verification.")
    
    st.markdown("#### 🔬 Interactive Side-by-Side Email Client Preview")
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("##### 🔴 Control (Current Baseline Email)")
        st.markdown("""
        <div class="email-container-control">
            <div style="border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 8px; margin-bottom: 12px; font-size: 0.88rem;">
                <strong>Subject:</strong> <code>Confirm your email address now!</code><br>
                <strong>Preheader:</strong> <code>Before you can register, please confirm your email...</code>
            </div>
            <div style="color: #cbd5e1; font-size: 0.95rem; line-height: 1.6;">
                Hello friend,<br><br>
                We're delighted that you'd like to become part of our community.<br><br>
                Before you can register, we would like to ask you to confirm your email address by using the following link:<br><br>
                <div style="text-align: center; margin: 16px 0;">
                    <span style="background:#0f172a; color:#fff; border:1px solid #38bdf8; padding:9px 22px; border-radius:6px; font-weight:700;">Confirm email address</span>
                </div><br>
                Thanks and best regards,<br>
                Your Team
            </div>
            <hr style="border-color: rgba(255,255,255,0.1);">
            <strong style="color:#38bdf8;">👍 What We Appreciate:</strong> 100% deliverability focus, zero spam triggers.<br><br>
            <strong style="color:#f87171;">💡 Optimization Opportunity:</strong> High open rate (68.2%), but 58.8% of users drop off and take >18h to start KYC.
        </div>
        """, unsafe_allow_html=True)
        
    with col2:
        st.markdown("##### 🟢 Variant B (Hypothesis: Momentum Activation Hook)")
        st.markdown("""
        <div class="email-container-variant">
            <div style="border-bottom: 1px solid rgba(56,189,248,0.2); padding-bottom: 8px; margin-bottom: 12px; font-size: 0.88rem;">
                <strong>Subject:</strong> <code>⚡ 1 click away from your trading workspace (+ market movers inside)</code><br>
                <strong>Preheader:</strong> <code>Bitcoin +3.8% today • Instant 0€ account setup</code>
            </div>
            <div style="color: #cbd5e1; font-size: 0.95rem; line-height: 1.6;">
                Hi [First Name],<br><br>
                You're seconds away from your digital trading workspace. Confirm your email below to get started:<br><br>
                <div style="text-align: center; margin: 16px 0;">
                    <span style="display:inline-block; background:#38bdf8; color:#0f172a; padding:10px 24px; border-radius:6px; font-weight:800;">Confirm Email & Start Exploring &rarr;</span>
                </div><br>
                <div style="background: rgba(0,0,0,0.35); border:1px solid rgba(56,189,248,0.25); border-radius:8px; padding:12px 14px;">
                    <strong style="color:#38bdf8; font-size:0.85rem;">🔥 What traders are watching today:</strong><br>
                    <span style="font-size:0.82rem; color:#94a3b8;">• <strong>BTC / EUR:</strong> +3.8% (Consolidating above €58,000)<br>
                    • <strong>ETH / EUR:</strong> +5.1% (Layer-2 volume breakout)<br>
                    • <strong>Automated Sparplan:</strong> Set and forget from €25/month</span>
                </div>
            </div>
            <hr style="border-color: rgba(255,255,255,0.1);">
            <strong style="color:#34d399;">📈 Quantified Impact:</strong> <strong>+30.6% Click-through Velocity</strong> ($z = 2.89, p = 0.0039$). Reduces median KYC lag from 18.4h to 4.2h.
        </div>
        """, unsafe_allow_html=True)

# ==========================================
# MODULE 3: CASE 2 - ONBOARDING & KYC
# ==========================================
elif "3. Case 2: Onboarding" in nav_choice:
    st.subheader("🛡️ Case 2: Onboarding & Video-Ident Friction Breaker")
    st.info("**Strategic Context:** In German & European regulated digital asset exchanges, users sign up eagerly but often hesitate at Video-Ident due to fear of complicated paperwork or long video calls. Our hypothesis replaces dense paragraphs with an empowering 3-step checklist + mobile deep-linking.")
    
    colA, colB = st.columns(2)
    with colA:
        st.markdown("##### 🔴 Control (Current Baseline Email)")
        st.markdown("""
        <div class="email-container-control">
            <div style="border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 8px; margin-bottom: 12px; font-size: 0.88rem;">
                <strong>Subject:</strong> <code>Welcome to Faizex 👋</code><br>
                <strong>Preheader:</strong> <code>When it comes to trading, we are a partner you can rely on...</code>
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
            <strong style="color:#f87171;">💡 Optimization Opportunity:</strong> Two identical buttons and text-heavy blocks create cognitive fatigue; 42% drop off before Video-Ident.
        </div>
        """, unsafe_allow_html=True)
        
    with colB:
        st.markdown("##### 🟢 Variant B (Hypothesis: 3-Step Friction Breaker)")
        st.markdown("""
        <div class="email-container-variant">
            <div style="border-bottom: 1px solid rgba(56,189,248,0.2); padding-bottom: 8px; margin-bottom: 12px; font-size: 0.88rem;">
                <strong>Subject:</strong> <code>Unlock your trading account in 3 minutes 🛡️ (Step 1 ready)</code><br>
                <strong>Preheader:</strong> <code>ID card ready? 2-min Video-Ident • Insured German custody</code>
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
                    <span style="display:inline-block; background:#10b981; color:#0f172a; padding:10px 24px; border-radius:6px; font-weight:800;">Unlock My Account in App (3 Mins) &rarr;</span>
                </div><br>
                <div style="text-align:center; font-size:0.8rem; color:#94a3b8;">
                    🔒 BaFin Regulated • Insured European Custody • No Wallet Complexity
                </div>
            </div>
            <hr style="border-color: rgba(255,255,255,0.1);">
            <strong style="color:#34d399;">📈 Quantified Impact:</strong> <strong>+38.7% KYC Completion Lift</strong> (28.4% → 39.4%, $z = 3.12, p = 0.0018$).
        </div>
        """, unsafe_allow_html=True)

# ==========================================
# MODULE 4: CASE 3 - MONTHLY NEWSLETTER
# ==========================================
elif "4. Case 3: Engagement" in nav_choice:
    st.subheader("📰 Case 3: Monthly Newsletter Personalization (August Edition)")
    st.info("**Strategic Context:** Monthly market reviews offer great educational storytelling. The August edition clearly breaks down the US debt spiral, Nvidia capex, and Bitcoin rally. Our hypothesis preserves 100% of this high-quality editorial, but tests replacing the single static 'Trade Bitcoin' button with dynamic lifecycle-segmented CTAs.")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("##### 🔴 Control (Actual Newsletter Received)")
        st.markdown("""
        <div class="email-container-control">
            <div style="border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 8px; margin-bottom: 12px; font-size: 0.88rem;">
                <strong>Subject:</strong> <code>Hi, here's your Faizex Market Digest for August 📰</code><br>
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
            <strong style="color:#f87171;">💡 Optimization Opportunity:</strong> A single static 'Trade Bitcoin' button ignores user lifecycle state (non-holders hesitate; long-term accumulators prefer DCA).
        </div>
        """, unsafe_allow_html=True)
        
    with col2:
        st.markdown("##### 🟢 Variant B (Hypothesis: Dynamic Liquid CTAs)")
        selected_persona = st.selectbox(
            "Select Persona to Preview Dynamic Liquid Module:",
            [
                "🌱 Unverified User (0 Trades)",
                "📊 Occasional Spot Buyer (Manual Trader)",
                "📈 Active Sparplan Accumulator (Monthly DCA)",
                "💤 Dormant Account (>60 Days Inactive)"
            ]
        )
        
        st.markdown("""
        <div class="email-container-variant">
            <div style="border-bottom: 1px solid rgba(56,189,248,0.2); padding-bottom: 8px; margin-bottom: 12px; font-size: 0.88rem;">
                <strong>Subject:</strong> <code>Market Digest: Institutional flows & Volatility shift [Portfolio Impact] 📈</code><br>
                <strong>Preheader:</strong> <code>August macro update + customized accumulation strategy</code>
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
            <strong style="color:#34d399;">📈 Quantified Impact:</strong> <strong>+86.3% Click-to-Open (CTOR) Lift</strong> (12.4% → 23.1%, $z = 4.15, p < 0.0001$).
        </div>
        """, unsafe_allow_html=True)

# ==========================================
# MODULE 5: CASE 4 - KEY KPIS
# ==========================================
elif "5. Case 4: Exchange CRM" in nav_choice:
    st.subheader("🎯 Case 4: Complete Exchange CRM & Retention KPI Framework")
    st.markdown("A complete quantitative framework for evaluating customer acquisition, onboarding velocity, retention economics, and lifetime portfolio value.")
    
    kpis = [
        {
            "name": "1. KYC Verification Throughput Rate",
            "formula": "KYC Rate = (Approved Verified Users / Total Registrations) * 100",
            "target": "Target: > 40% (Industry avg is ~28%)",
            "why": "Identifies drop-off bottlenecks in the onboarding funnel. Drops here directly inflate Customer Acquisition Cost (CAC).",
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
        <div class="kpi-row-card">
            <div style="display:flex; justify-content:space-between; align-items:center;">
                <h4 style="color:#38bdf8; margin:0;">{k['name']}</h4>
                <span class="formula-tag">{k['target']}</span>
            </div>
            <div style="margin: 6px 0; font-family:'JetBrains Mono', monospace; color:#34d399; font-size:0.9rem;">
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
# MODULE 6: CASE 5 - 5-YEAR SPARPLAN LTV
# ==========================================
elif "6. Case 5: Retention" in nav_choice:
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
# MODULE 7: CASE 6 - VOLATILITY ALERT GENERATOR
# ==========================================
elif "7. Case 6: Push & In-App" in nav_choice:
    st.subheader("⚡ Case 6: Market Volatility & Push Trigger Simulator")
    st.markdown("Simulating programmatic trigger alerts dispatched via Braze / Push Notifications when market volatility surges past standard statistical deviations.")
    
    asset = st.selectbox("Select Volatility Instrument:", ["Bitcoin (BTC/EUR)", "Ethereum (ETH/EUR)", "Solana (SOL/EUR)", "DAX 40"])
    vol_threshold = st.slider("Trigger Threshold (24h Price Move %):", min_value=3.0, max_value=15.0, value=5.0, step=0.5)
    
    st.markdown(f"""
    <div class="phone-mockup">
        <div class="phone-notch"></div>
        <div style="background:rgba(255,255,255,0.08); border-radius:14px; padding:12px 14px; border:1px solid rgba(255,255,255,0.12);">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:4px;">
                <span style="font-size:0.75rem; font-weight:700; color:#38bdf8;">FAIZEX TRADING • NOW</span>
                <span style="font-size:0.75rem; color:#94a3b8;">Just now</span>
            </div>
            <strong style="color:#fff; font-size:0.92rem;">{asset} moved ±{vol_threshold}% in 4h ⚡</strong><br>
            <p style="color:#cbd5e1; font-size:0.84rem; margin:4px 0 0 0; line-height:1.4;">
                High European volume detected. Tap to view live order book depth & set limit orders.
            </p>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ==========================================
# MODULE 8: CASE 7 - STALLED DEPOSIT RECOVERY
# ==========================================
elif "8. Case 7: Stalled-Deposit Recovery" in nav_choice:
    st.subheader("🏦 Case 7: Stalled-Deposit Recovery Flow (High-Intent Capital Rescue)")
    st.info("**Strategic Context:** The highest drop-off in trading apps occurs after KYC approval but before the first bank deposit. This omnichannel journey rescues stalled deposits within 24 hours using supportive, low-friction messaging.")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class="email-container-variant">
            <h4 style="color:#f59e0b;">📲 Step 1: In-App Slide-Up (Triggered T + 15 min)</h4>
            <strong>Trigger:</strong> <code>deposit_initiated</code> without confirmation in 15 mins.<br><br>
            <div style="background:rgba(245,158,11,0.1); border:1px solid #f59e0b; border-radius:8px; padding:12px;">
                <strong>Dein 0€ Einzahlungs-Auftrag wartet noch ⏱️</strong><br>
                <span style="font-size:0.88rem; color:#cbd5e1;">Tippe unten, um die IBAN direkt in deine Banking-App zu kopieren. Keine Gebühren, sofort startklar.</span>
                <div style="margin-top:8px; text-align:center;">
                    <span style="background:#f59e0b; color:#0f172a; padding:6px 16px; border-radius:4px; font-weight:800; font-size:0.85rem;">IBAN kopieren & Überweisung abschließen &rarr;</span>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="email-container-variant">
            <h4 style="color:#10b981;">✉️ Step 2: Customer Care Email (Triggered T + 24 hours)</h4>
            <strong>Subject:</strong> <code>Brauchst du Unterstützung bei deiner ersten Einzahlung? 🛡️</code><br>
            <strong>Angle:</strong> Replaces pushy sales pressure with reassuring customer care.<br><br>
            <div style="font-size:0.9rem; color:#cbd5e1; line-height:1.5;">
                Hallo [Vorname],<br><br>
                wir haben gesehen, dass deine Verifizierung erfolgreich war, deine Einzahlung aber noch aussteht.<br><br>
                Gibt es Fragen zu SEPA-Echtzeitüberweisungen oder Banklaufzeiten? Unser deutscher Kundenservice unterstützt dich gerne jederzeit.<br><br>
                <div style="text-align:center;">
                    <span style="background:#10b981; color:#0f172a; padding:6px 16px; border-radius:4px; font-weight:800; font-size:0.85rem;">1-Klick Anleitung zur Einzahlung ansehen &rarr;</span>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
    st.success("📈 **Quantified Impact:** +20.3% First-Deposit Conversion Rate / +64% Email CTR.")

# ==========================================
# MODULE 9: CASE 8 - MILESTONE GAMIFICATION
# ==========================================
elif "9. Case 8: Milestone Habit Gamification" in nav_choice:
    st.subheader("🏆 Case 8: Milestone Habit Gamification (Goal Gradient DCA)")
    st.info("**Strategic Context:** Based on the psychological Goal Gradient Effect: retail investors accelerate their saving behavior when approaching meaningful milestones (€500, €1,000, €5,000 AUC).")
    
    st.markdown("""
    <div class="email-container-variant" style="text-align:center; padding:2rem;">
        <div style="font-size:3rem; margin-bottom:0.5rem;">🎉 🪙 📈</div>
        <h3 style="color:#38bdf8; margin:0 0 0.5rem 0;">Glückwunsch! Du hast die 1.000€ Spar-Marke erreicht!</h3>
        <p style="color:#94a3b8; font-size:0.95rem; max-width:600px; margin:0 auto 1.2rem auto;">
            Damit gehörst du zu den Top 25% der disziplinierten Langzeit-Investoren auf Faizex. Dein automatischer Sparplan arbeitet kontinuierlich für deine finanzielle Zukunft.
        </p>
        <div style="background:rgba(56,189,248,0.08); border:1px solid rgba(56,189,248,0.2); border-radius:8px; padding:12px 20px; display:inline-block; margin-bottom:1.2rem;">
            <strong style="color:#38bdf8;">📊 Nächster Meilenstein: 2.500€ Vermögen</strong><br>
            <span style="font-size:0.85rem; color:#cbd5e1;">Erhöhe deinen Sparplan um 25€/Monat, um dein Ziel 4 Monate schneller zu erreichen.</span>
        </div><br>
        <span style="display:inline-block; background:#38bdf8; color:#0f172a; padding:9px 24px; border-radius:6px; font-weight:800;">Sparplan anpassen (+25€/Mo) &rarr;</span>
    </div>
    """, unsafe_allow_html=True)
    st.success("📈 **Quantified Impact:** 59.2% 12-Month Retention / +52.4% Sparplan Upgrade Velocity.")

# ==========================================
# MODULE 10: CASE 9 - IDLE STAKING ACTIVATION
# ==========================================
elif "10. Case 9: Idle Capital Staking" in nav_choice:
    st.subheader("🪙 Case 9: Idle Capital Staking & Yield Activation Nudge")
    st.info("**Strategic Context:** Users holding un-staked tokens (ETH, SOL) or cash for >30 days suffer from opportunity cost. We show a personalized, dynamic in-app reward projection to activate dormant assets.")
    
    token_hold = st.selectbox("Select Token in User Portfolio:", ["Ethereum (ETH)", "Solana (SOL)", "Cardano (ADA)"])
    token_amount = st.slider("User Token Balance (€ equivalent):", 200, 10000, 1500, 100)
    
    annual_yield = round(token_amount * 0.048, 2) # 4.8% p.a.
    monthly_yield = round(annual_yield / 12, 2)
    
    st.markdown(f"""
    <div class="email-container-variant">
        <h4 style="color:#10b981;">📲 Dynamic Portfolio In-App Widget ({token_hold})</h4>
        <div style="display:flex; justify-content:space-between; align-items:center;">
            <div>
                <strong style="font-size:1.1rem; color:#fff;">Lass deine {token_hold.split()[0]} nicht schlafen 🪙</strong><br>
                <span style="color:#94a3b8; font-size:0.9rem;">Aktiviere 1-Klick Staking mit 100% deutscher BaFin-Verwahrung.</span>
            </div>
            <div style="background:rgba(16,185,129,0.15); border:1px solid #10b981; border-radius:8px; padding:10px 18px; text-align:right;">
                <span style="font-size:1.2rem; font-weight:800; color:#34d399;">+€{annual_yield} / Jahr</span><br>
                <span style="font-size:0.75rem; color:#94a3b8;">(~€{monthly_yield}/Monat Rewards)</span>
            </div>
        </div>
        <div style="margin-top:1rem; text-align:right;">
            <span style="background:#10b981; color:#0f172a; padding:8px 20px; border-radius:4px; font-weight:800; font-size:0.85rem;">Staking mit 1 Klick aktivieren &rarr;</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.success("📈 **Quantified Impact:** +3.4x Staking Product Adoption Rate (27.8% Conversion).")

# ==========================================
# MODULE 11: CASE 10 - CRM ARCHITECTURE
# ==========================================
elif "11. Case 10: CRM Automation Architecture" in nav_choice:
    st.subheader("🛠️ Case 10: CRM Automation Architecture & Microservices Studio")
    st.markdown("Demonstrating how asynchronous in-memory caching and idempotency state machines guarantee **zero duplicate messages** and sub-second execution.")
    
    arch_tab1, arch_tab2 = st.tabs([
        "⚙️ Async Segment Batcher (In-Memory Cache)",
        "🛡️ Idempotent Dispatcher (Crash Recovery)"
    ])
    
    with arch_tab1:
        st.markdown("#### 1. Asynchronous Dynamic Segment Batching")
        st.markdown("Instead of querying 500,000 rows live during campaign send, an asynchronous background task pre-computes dynamic audience memberships into a fast-lookup Redis cache.")
        
        col_c1, col_c2 = st.columns(2)
        with col_c1:
            st.code("""
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
        st.markdown("#### 2. Idempotent Dispatcher (Crash Recovery)")
        st.markdown("Uses unique idempotency keys (`campaign:user:date`) to guarantee **zero duplicate messages** even if the broadcast server crashes halfway through a 100k blast.")
        
        st.code("""
def dispatch_with_idempotency(campaign_id, user_id, payload):
    idempotency_key = hashlib.sha256(f"{campaign_id}:{user_id}:2026_09_01".encode()).hexdigest()
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

# ==========================================
# MODULE 12: CASE 11 - CROSS-FUNCTIONAL
# ==========================================
elif "12. Case 11: Cross-Functional" in nav_choice:
    st.subheader("👥 Case 11: Cross-Functional Collaboration & Delivery Framework")
    st.markdown("How the CRM Manager coordinates end-to-end campaign execution across BI, Product, UX/UI, and Compliance.")
    
    st.markdown("""
    | Stakeholder | Key Collaboration Area | Real Workflow Example |
    |---|---|---|
    | **BI / Analytics Team** | Event tracking, Cohort schemas, SQL queries, Amplitude funnels | Defining custom event attributes: `sparplan_paused_reason`, `kyc_retry_count`, `last_trade_asset_class`. |
    | **Product & Engineering** | In-App message triggers, App deep-links, API webhooks | Integrating direct URI schemes (`faizex://verify/video-ident`, `faizex://sparplan/create`) to ensure seamless in-app navigation. |
    | **UX / UI Design** | In-App Banners, Modal layouts, HTML email templates | Ensuring consistent typography, dark/light mode compatibility, and mobile-first tap targets. |
    | **Legal & Compliance (BaFin/MiCA)** | GDPR consent, Risk disclaimers, Audit trails | Reviewing risk warnings on high-volatility token promotions and ensuring strict double-opt-in (DOI) records. |
    """)

# ==========================================
# MODULE 13: CASE 12 - TECHNICAL STACK
# ==========================================
elif "13. Case 12: Technical CRM Stack" in nav_choice:
    st.subheader("💻 Case 12: Technical Execution (Braze Event Architecture & Liquid Logic)")
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
    <a href="faizex://verify/video-ident">Verify Now &rarr;</a>
  </div>
{% elsif days_dormant > 60 %}
  <!-- Re-Engagement Volatility Flow -->
  <div class="action-banner winback">
    <h3>Markets are moving: View {{custom_attribute.${top_watched_coin}}} today</h3>
    <a href="faizex://markets/{{custom_attribute.${top_watched_coin} | downcase}}">Trade {{custom_attribute.${top_watched_coin}}} &rarr;</a>
  </div>
{% else %}
  <!-- Sparplan Accumulation Flow -->
  <div class="action-banner sparplan">
    <h3>Set and forget: Automate your monthly DCA from €25</h3>
    <a href="faizex://sparplan/new">Set Up Sparplan &rarr;</a>
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
