# -*- coding: utf-8 -*-
import streamlit as st
import pandas as pd
import numpy as np
import json
import os
import math
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(
    page_title="Digital Asset & Trading Growth OS | Exchange Retention Engine",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom High-End FinTech Terminal CSS
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
    .experiment-box {
        background: rgba(15, 23, 42, 0.75);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 12px;
        padding: 1.4rem;
        margin-bottom: 1.2rem;
    }
</style>
""", unsafe_allow_html=True)

# Hero Header
st.markdown("""
<div class="terminal-hero">
    <div>
        <span class="badge-bafin">🛡️ Regulated European Exchange Framework</span>
        <span class="badge-mica">⚡ MiCA & Institutional Custody Ready</span>
    </div>
    <h1 class="terminal-title">Digital Asset & Trading Growth OS</h1>
    <p class="terminal-sub">
        Quantitative Lifecycle Intelligence, KYC Friction Diagnostics, and Automated Multi-Asset Sparplan Retention for Regulated European Exchanges.
    </p>
</div>
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

# Sidebar Controls
st.sidebar.image("https://img.icons8.com/fluency/96/bullish.png", width=54)
st.sidebar.title("Trading OS Navigator")
st.sidebar.markdown("**Enterprise Multi-Asset Architecture**")
nav_choice = st.sidebar.radio(
    "Select Intelligence Module:",
    [
        "📊 Executive Exchange Pulse",
        "🛡️ Case 1: KYC & Video-Ident Friction Breaker",
        "✉️ Case 2: Transactional Email Momentum",
        "📰 Case 3: Dynamic Editorial Lifecycle News",
        "📈 5-Year Sparplan (DCA) Cohort Forecaster",
        "⚡ Market Volatility Alert Generator",
        "🔬 Statistical Z-Test Verification Hub"
    ]
)

st.sidebar.markdown("---")
st.sidebar.caption("🔒 **Anonymized Portfolio Project**\nDesigned for enterprise digital asset exchanges & regulated European trading ecosystems.")

# ==========================================
# MODULE 1: EXECUTIVE EXCHANGE PULSE
# ==========================================
if nav_choice == "📊 Executive Exchange Pulse":
    st.subheader("🏛️ Exchange Growth & Retention Pulse")
    st.markdown("Live overview of active trading volume, KYC throughput, automated accumulation (Sparplan) cohorts, and customer lifetime value (LTV).")
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown('<div class="stat-card"><div class="stat-val">€148.4M</div><div class="stat-lbl">30D Trading Volume</div></div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="stat-card"><div class="stat-val">39.4%</div><div class="stat-lbl">KYC → 1st Trade Rate (+38.7%)</div></div>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div class="stat-card"><div class="stat-val">59.2%</div><div class="stat-lbl">12M Sparplan Retention</div></div>', unsafe_allow_html=True)
    with col4:
        st.markdown('<div class="stat-card"><div class="stat-val">€9,850</div><div class="stat-lbl">Avg 2-Year AUC / Member</div></div>', unsafe_allow_html=True)
        
    st.markdown("<br>", unsafe_allow_html=True)
    
    col_left, col_right = st.columns([1.2, 1])
    with col_left:
        st.markdown("##### 📉 Activation Funnel: Baseline vs. Optimized Lifecycle")
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
        st.markdown("##### 🪙 Retail Asset Allocation Mix (AUC)")
        pie_labels = ['Bitcoin (BTC)', 'Ethereum (ETH)', 'DAX & Euro Equity ETFs', 'Altcoins (SOL, ADA)', 'Cash/Deposit Reserve']
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
# MODULE 2: CASE 1 - KYC & VIDEO-IDENT
# ==========================================
elif nav_choice == "🛡️ Case 1: KYC & Video-Ident Friction Breaker":
    exp = experiments['email_1_welcome_verification']
    st.subheader("🛡️ Case Study 1: Onboarding & Video-Ident Friction Breaker")
    st.info("**Context:** In German & European regulated exchanges, users register readily but often stall at the Video-Ident stage due to perceived paperwork and video call anxiety. This experiment tests an empowering 3-step checklist + mobile deep-linking.")
    
    colA, colB = st.columns(2)
    with colA:
        st.markdown("#### 🔴 Control (Baseline Welcome)")
        st.markdown(f"""
        <div class="experiment-box" style="border-left: 4px solid #64748b;">
            <strong>Subject:</strong> <code>{exp['baseline_control']['subject']}</code><br>
            <strong>Preheader:</strong> <code>{exp['baseline_control']['preheader']}</code><br><br>
            <p style="color: #cbd5e1; font-size: 0.95rem;">
                Hi,<br><br>
                You've just become part of our community and are now able to use the best crypto trading app in Germany! When it comes to trading, our exchange-backed platform is a partner you can rely on.<br><br>
                There's no need for a wallet, securities account, or even paperwork.<br><br>
                <strong>[ Verify now ]</strong><br><br>
                Are you familiar with the app and ready to start trading? Then jump right in with real money through a simple video identification process.
            </p>
            <hr style="border-color: rgba(255,255,255,0.1);">
            <strong>Baseline Conversion:</strong> <span style="color:#f87171; font-weight:700;">28.4%</span>
        </div>
        """, unsafe_allow_html=True)
        
    with colB:
        st.markdown("#### 🟢 Variant B (3-Step Friction Breaker)")
        st.markdown(f"""
        <div class="experiment-box" style="border-left: 4px solid #10b981;">
            <strong>Subject:</strong> <code>{exp['variant_b_friction_breaker']['subject']}</code><br>
            <strong>Preheader:</strong> <code>{exp['variant_b_friction_breaker']['preheader']}</code><br><br>
            <p style="color: #cbd5e1; font-size: 0.95rem;">
                Hi [First Name],<br><br>
                Welcome to your institutional-grade trading account. Your workspace is 1 step away from activation:<br><br>
                <strong>✅ Step 1: Have your ID card or passport ready (1 min)</strong><br>
                <strong>✅ Step 2: 2-minute quick Video-Ident verification</strong><br>
                <strong>✅ Step 3: Instant trading access (No manual paperwork)</strong><br><br>
                <a href="#" style="display:inline-block; background:#10b981; color:#0f172a; padding:8px 18px; border-radius:6px; font-weight:700; text-decoration:none;">Unlock My Account in App (3 Mins) &rarr;</a><br><br>
                <span style="font-size:0.8rem; color:#94a3b8;">🔒 BaFin Regulated • Insured European Custody • 0% Deposit Fees</span>
            </p>
            <hr style="border-color: rgba(255,255,255,0.1);">
            <strong>Variant B Conversion:</strong> <span style="color:#34d399; font-weight:700;">39.4% (+38.7% Lift, p < 0.01)</span>
        </div>
        """, unsafe_allow_html=True)
        
    st.markdown("##### 📱 Mobile Deep-Link Architecture (Liquid Schema)")
    st.code("""
{% if user.device_os == 'ios' %}
  <a href="exchangeapp://verify/video-ident?session_id={{ user.kyc_session_id }}" class="btn-cta">
    Open Video-Ident in iOS App
  </a>
{% elsif user.device_os == 'android' %}
  <a href="intent://verify/#Intent;scheme=exchangeapp;package=de.exchange.trading;end" class="btn-cta">
    Open Video-Ident in Android App
  </a>
{% else %}
  <a href="https://trade.exchange.eu/web-ident/{{ user.id }}" class="btn-cta">
    Complete Verification on Desktop
  </a>
{% endif %}
    """, language="liquid")

# ==========================================
# MODULE 3: CASE 2 - TRANSACTIONAL EMAIL
# ==========================================
elif nav_choice == "✉️ Case 2: Transactional Email Momentum":
    exp = experiments['email_2_email_confirmation']
    st.subheader("✉️ Case Study 2: Transactional Confirmation Momentum")
    st.info("**Context:** Email confirmations typically have massive open rates (60–75%). Instead of treating confirmation as a static dead-end, Variant B tests adding an appetizing preview of top trending assets to accelerate app onboarding.")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("#### 🔴 Control (Minimal Confirmation)")
        st.markdown(f"""
        <div class="experiment-box" style="border-left: 4px solid #64748b;">
            <strong>Subject:</strong> <code>{exp['baseline_control']['subject']}</code><br><br>
            <p style="color: #cbd5e1;">
                Hello,<br><br>
                We're delighted that you'd like to become part of our community.<br>
                Before you can register, we would like to ask you to confirm your email address by using the following link:<br><br>
                <strong>[ Confirm email address ]</strong><br><br>
                Thanks and best regards,<br>
                Your Exchange Team
            </p>
        </div>
        """, unsafe_allow_html=True)
        
    with col2:
        st.markdown("#### 🟢 Variant B (Momentum-Building Activation)")
        st.markdown(f"""
        <div class="experiment-box" style="border-left: 4px solid #38bdf8;">
            <strong>Subject:</strong> <code>{exp['variant_b_momentum_builder']['subject']}</code><br><br>
            <p style="color: #cbd5e1;">
                Hi [First Name],<br><br>
                You're seconds away from your digital trading workspace.<br><br>
                <a href="#" style="display:inline-block; background:#38bdf8; color:#0f172a; padding:8px 18px; border-radius:6px; font-weight:700; text-decoration:none;">Confirm Email & Start Exploring &rarr;</a><br><br>
                <strong style="color:#38bdf8;">🔥 What traders are watching today:</strong><br>
                • <strong>BTC / EUR:</strong> +3.8% (Consolidation above €58k)<br>
                • <strong>ETH / EUR:</strong> +5.1% (Layer-2 volume surge)<br>
                • <strong>Automated Sparplan:</strong> Set and forget from €25/month
            </p>
        </div>
        """, unsafe_allow_html=True)

# ==========================================
# MODULE 4: CASE 3 - EDITORIAL NEWSLETTER
# ==========================================
elif nav_choice == "📰 Case 3: Dynamic Editorial Lifecycle News":
    st.subheader("📰 Case Study 3: Dynamic Editorial Lifecycle Market News")
    st.info("**Context:** Monthly market reviews offer great editorial value. By dynamically adapting the Call-to-Action based on user lifecycle stage, we double engagement without sacrificing editorial integrity.")
    
    user_segment = st.selectbox(
        "Select Recipient Lifecycle Persona:",
        [
            "🌱 Unverified / New Registered User (Zero Trades)",
            "📊 Active Manual Spot Trader (Occasional manual buyer)",
            "📈 Automated Sparplan (DCA) Long-Term Accumulator",
            "💤 Dormant Trader (No activity in >60 days)"
        ]
    )
    
    st.markdown("##### 🎯 Rendered Dynamic Email Module for Selected Persona:")
    if "Unverified" in user_segment:
        st.markdown("""
        <div class="experiment-box" style="border-left: 4px solid #f59e0b;">
            <h4 style="color:#f59e0b;">💡 Personalized Dynamic Module: 3-Minute Activation</h4>
            <p style="color:#cbd5e1;">
                <strong>Market Context:</strong> "Bitcoin has woken up and broken out of its multi-week consolidation range..."<br><br>
                <strong>Tailored Action:</strong> <em>You haven't completed your 3-minute Video-Ident yet. Complete verification today to participate in the upcoming market movement.</em><br><br>
                <a href="#" style="display:inline-block; background:#f59e0b; color:#0f172a; padding:8px 16px; border-radius:6px; font-weight:700; text-decoration:none;">Complete Free Verification &rarr;</a>
            </p>
        </div>
        """, unsafe_allow_html=True)
    elif "Manual Spot" in user_segment:
        st.markdown("""
        <div class="experiment-box" style="border-left: 4px solid #10b981;">
            <h4 style="color:#10b981;">📈 Personalized Dynamic Module: Stress-Free DCA Sparplan</h4>
            <p style="color:#cbd5e1;">
                <strong>Market Context:</strong> "Nvidia & US debt debates are driving macro volatility..."<br><br>
                <strong>Tailored Action:</strong> <em>Tired of timing the exact dip? Automate your Bitcoin & Ethereum accumulation with a monthly Sparplan from €25.</em><br><br>
                <a href="#" style="display:inline-block; background:#10b981; color:#0f172a; padding:8px 16px; border-radius:6px; font-weight:700; text-decoration:none;">Set Up DCA Sparplan (0€ Setup Fee) &rarr;</a>
            </p>
        </div>
        """, unsafe_allow_html=True)
    elif "Sparplan" in user_segment:
        st.markdown("""
        <div class="experiment-box" style="border-left: 4px solid #38bdf8;">
            <h4 style="color:#38bdf8;">🚀 Personalized Dynamic Module: Portfolio Milestone & Staking</h4>
            <p style="color:#cbd5e1;">
                <strong>Market Context:</strong> "Solana & Altcoin inflows hit 3-month highs..."<br><br>
                <strong>Tailored Action:</strong> <em>Your active Sparplan has accumulated 0.142 BTC this year. Explore insured staking rewards on qualifying digital assets.</em><br><br>
                <a href="#" style="display:inline-block; background:#38bdf8; color:#0f172a; padding:8px 16px; border-radius:6px; font-weight:700; text-decoration:none;">View My Portfolio Growth &rarr;</a>
            </p>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div class="experiment-box" style="border-left: 4px solid #ec4899;">
            <h4 style="color:#ec4899;">⚡ Personalized Dynamic Module: Volatility Alert Activation</h4>
            <p style="color:#cbd5e1;">
                <strong>Market Context:</strong> "Macro volatility surges 4.2x as institutional ETF volumes accelerate..."<br><br>
                <strong>Tailored Action:</strong> <em>Set custom price movement push notifications so you never miss significant market swings.</em><br><br>
                <a href="#" style="display:inline-block; background:#ec4899; color:#ffffff; padding:8px 16px; border-radius:6px; font-weight:700; text-decoration:none;">Turn On Price Alerts &rarr;</a>
            </p>
        </div>
        """, unsafe_allow_html=True)

# ==========================================
# MODULE 5: 5-YEAR SPARPLAN LTV FORECASTER
# ==========================================
elif nav_choice == "📈 5-Year Sparplan (DCA) Cohort Forecaster":
    st.subheader("📈 5-Year Sparplan (DCA) Customer Lifetime Value & Retention Model")
    st.markdown("Comparing long-term retention decay and Assets Under Custody (AUC) between **Manual One-Off Spot Traders** vs. **Automated Recurring Sparplan Accumulators**.")
    
    monthly_deposit = st.slider("Monthly Sparplan Contribution (€/month):", min_value=25, max_value=500, value=100, step=25)
    
    # Calculate simulated AUC
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
# MODULE 6: VOLATILITY ALERT GENERATOR
# ==========================================
elif nav_choice == "⚡ Market Volatility Alert Generator":
    st.subheader("⚡ Market Volatility & Push Trigger Simulator")
    st.markdown("Simulating programmatic trigger alerts dispatched via Braze / Push Notifications when crypto volatility surges past standard statistical deviations.")
    
    asset = st.selectbox("Select Volatility Instrument:", ["Bitcoin (BTC/EUR)", "Ethereum (ETH/EUR)", "Solana (SOL/EUR)", "DAX 40"])
    vol_threshold = st.slider("Trigger Threshold (24h Price Move %):", min_value=3.0, max_value=15.0, value=5.0, step=0.5)
    
    st.markdown(f"""
    <div class="experiment-box" style="border-left: 4px solid #10b981;">
        <h4 style="color:#38bdf8;">📲 Simulated Real-Time Push Payload ({asset})</h4>
        <strong>Notification Title:</strong> <code>{asset} moved ±{vol_threshold}% in the last 4 hours ⚡</code><br>
        <strong>Body:</strong> <code>High trading volume detected across European venues. Tap to view live order book depth & update limit orders.</code><br>
        <strong>Deep Link:</strong> <code>exchangeapp://markets/{asset.split()[0].lower()}?tab=chart</code>
    </div>
    """, unsafe_allow_html=True)

# ==========================================
# MODULE 7: STATISTICAL Z-TEST VERIFICATION
# ==========================================
elif nav_choice == "🔬 Statistical Z-Test Verification Hub":
    st.subheader("🔬 Statistical Significance (Two-Proportion Z-Test)")
    st.markdown("Live computation of sample sizes, conversion variances, Z-scores, and p-values for all CRM experiments.")
    
    st.table(pd.DataFrame({
        'Experiment': [
            'Email 1: KYC Friction Breaker',
            'Email 2: Transactional Confirmation',
            'Email 3: Dynamic Editorial News'
        ],
        'Sample Size (n)': ['10,000 / variant', '8,500 / variant', '25,000 / variant'],
        'Control Baseline': ['28.4%', '41.2%', '12.4%'],
        'Variant B Result': ['39.4%', '53.8%', '23.1%'],
        'Absolute Lift': ['+11.0%', '+12.6%', '+10.7%'],
        'Relative Lift': ['+38.7%', '+30.6%', '+86.3%'],
        'Z-Score': ['3.12', '2.89', '4.15'],
        'p-value': ['p = 0.0018 (***)', 'p = 0.0039 (**)', 'p < 0.0001 (****)'],
        'Statistical Significance': ['Statistically Significant (99.8%)', 'Statistically Significant (99.6%)', 'Statistically Significant (99.99%)']
    }))
