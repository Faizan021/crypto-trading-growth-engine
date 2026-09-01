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

# Professional Institutional Styling
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }
    code, pre {
        font-family: 'JetBrains Mono', monospace !important;
    }
    
    .exec-header {
        background: #0f172a;
        border: 1px solid #1e293b;
        border-radius: 8px;
        padding: 1.5rem 1.8rem;
        margin-bottom: 1.5rem;
    }
    .exec-title {
        font-size: 1.7rem;
        font-weight: 700;
        color: #f8fafc;
        letter-spacing: -0.02em;
        margin-bottom: 0.3rem;
    }
    .exec-sub {
        font-size: 0.92rem;
        color: #94a3b8;
        line-height: 1.5;
        margin: 0;
    }
    .badge-reg {
        display: inline-block;
        background: #064e3b;
        color: #6ee7b7;
        border: 1px solid #047857;
        padding: 2px 10px;
        border-radius: 4px;
        font-size: 0.72rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        margin-right: 6px;
    }
    .badge-crm {
        display: inline-block;
        background: #1e1b4b;
        color: #c7d2fe;
        border: 1px solid #3730a3;
        padding: 2px 10px;
        border-radius: 4px;
        font-size: 0.72rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    .exec-card {
        background: #0f172a;
        border: 1px solid #1e293b;
        border-radius: 8px;
        padding: 1.1rem;
        text-align: left;
    }
    .exec-card-val {
        font-size: 1.6rem;
        font-weight: 700;
        color: #38bdf8;
        margin-bottom: 2px;
    }
    .exec-card-lbl {
        font-size: 0.75rem;
        color: #94a3b8;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    .exec-card-sub {
        font-size: 0.75rem;
        color: #10b981;
        margin-top: 4px;
        font-weight: 500;
    }
    .email-container-a {
        background: #0f172a;
        border: 1px solid #334155;
        border-radius: 8px;
        padding: 1.4rem;
        margin-bottom: 1rem;
    }
    .email-container-b {
        background: #091322;
        border: 1px solid #0284c7;
        border-radius: 8px;
        padding: 1.4rem;
        margin-bottom: 1rem;
    }
    .table-header {
        font-size: 0.8rem;
        font-weight: 600;
        color: #94a3b8;
        text-transform: uppercase;
        border-bottom: 1px solid #1e293b;
        padding-bottom: 6px;
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
            <div class="exec-card-lbl">30-Day Retail Volume</div>
            <div class="exec-card-val">€148.4M</div>
            <div class="exec-card-sub">+12.4% vs. Prior Month</div>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="exec-card">
            <div class="exec-card-lbl">KYC → First-Trade Rate</div>
            <div class="exec-card-val">39.4%</div>
            <div class="exec-card-sub">+11.0% Lift over Baseline (28.4%)</div>
        </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown("""
        <div class="exec-card">
            <div class="exec-card-lbl">12-Month Sparplan Retention</div>
            <div class="exec-card-val">59.2%</div>
            <div class="exec-card-sub">2.6x Higher than Spot (22.8%)</div>
        </div>
        """, unsafe_allow_html=True)
    with col4:
        st.markdown("""
        <div class="exec-card">
            <div class="exec-card-lbl">Avg 2-Year AUC / Account</div>
            <div class="exec-card-val">€9,850</div>
            <div class="exec-card-sub">Steady Recurring Accumulation</div>
        </div>
        """, unsafe_allow_html=True)
        
    st.markdown("<br>", unsafe_allow_html=True)
    
    col_left, col_right = st.columns([1.3, 1])
    with col_left:
        st.markdown("#### Onboarding Throughput Funnel (Per 10,000 Signups)")
        if not df_funnel.empty:
            funnel_display = df_funnel.copy()
            funnel_display['lift_pct'] = ((funnel_display['variant_b_users'] - funnel_display['baseline_users']) / funnel_display['baseline_users'] * 100).round(1)
            funnel_display['lift_str'] = funnel_display['lift_pct'].apply(lambda x: f"+{x}%" if x > 0 else f"{x}%")
            
            st.dataframe(
                funnel_display[['funnel_stage', 'baseline_users', 'variant_b_users', 'lift_str']].rename(columns={
                    'funnel_stage': 'Funnel Stage',
                    'baseline_users': 'Control (Baseline)',
                    'variant_b_users': 'Variant B (Optimized)',
                    'lift_str': 'Throughput Lift'
                }),
                use_container_width=True,
                hide_index=True
            )
            
            fig = go.Figure()
            fig.add_trace(go.Bar(
                y=df_funnel['funnel_stage'],
                x=df_funnel['baseline_users'],
                name='Control (Baseline)',
                orientation='h',
                marker=dict(color='#475569')
            ))
            fig.add_trace(go.Bar(
                y=df_funnel['funnel_stage'],
                x=df_funnel['variant_b_users'],
                name='Variant B (Friction-Breaker)',
                orientation='h',
                marker=dict(color='#0ea5e9')
            ))
            fig.update_layout(
                barmode='group',
                height=300,
                margin=dict(l=10, r=10, t=10, b=10),
                paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(0,0,0,0)',
                font=dict(color='#94a3b8', size=11),
                legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
            )
            st.plotly_chart(fig, use_container_width=True)
            
    with col_right:
        st.markdown("#### Retail Assets Under Custody (AUC) Distribution")
        auc_table = pd.DataFrame({
            "Asset Class": ["Bitcoin (BTC)", "Ethereum (ETH)", "DAX & European ETFs", "Top Altcoins (SOL, ADA)", "Cash / EUR Reserve"],
            "Custody Share": ["42.0%", "24.0%", "18.0%", "11.0%", "5.0%"],
            "Primary CRM Focus": ["DCA Sparplan Accumulation", "Staking Rewards & Yield", "Portfolio Diversification", "Volatility & Limit Alerts", "Instant Dip-Buy Readiness"]
        })
        st.dataframe(auc_table, use_container_width=True, hide_index=True)
        st.caption("ℹ️ **Data Benchmark:** Aggregated from European Securities and Markets Authority (ESMA) retail asset reports and DACH multi-asset exchange portfolio distributions.")

# ==========================================
# MODULE 2: CASE 1
# ==========================================
elif "2. Case 1: Transactional Activation" in nav_choice:
    st.markdown("### Case 1: Transactional Confirmation & Activation Momentum")
    st.markdown("**Executive Context:** Transactional confirmation emails command a **68.2% open rate** (the highest in the customer lifecycle). Treating this email as a plain administrative stop wastes peak customer motivation.")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class="email-container-a">
            <div style="border-bottom: 1px solid #334155; padding-bottom: 8px; margin-bottom: 12px; font-size: 0.85rem; color:#94a3b8;">
                <strong>Subject:</strong> <code>Confirm your email address now!</code><br>
                <strong>Preheader:</strong> <code>Before you can register, please confirm your email...</code>
            </div>
            <div style="color: #cbd5e1; font-size: 0.92rem; line-height: 1.6;">
                Hello friend,<br><br>
                We're delighted that you'd like to become part of our community.<br><br>
                Before you can register, we would like to ask you to confirm your email address by using the following link:<br><br>
                <div style="text-align: center; margin: 14px 0;">
                    <span style="background:#1e293b; color:#f8fafc; border:1px solid #475569; padding:8px 20px; border-radius:4px; font-weight:600; font-size:0.88rem;">Confirm email address</span>
                </div><br>
                Thanks and best regards,<br>
                Your Team
            </div>
            <hr style="border-color: #334155; margin: 14px 0;">
            <div style="font-size:0.82rem; color:#94a3b8;">
                <strong>Baseline Assessment:</strong> 100% deliverability, but plain text creates an administrative dead-end. 58.8% of users delay KYC by >18 hours.
            </div>
        </div>
        """, unsafe_allow_html=True)
        
    with col2:
        st.markdown("""
        <div class="email-container-b">
            <div style="border-bottom: 1px solid #0284c7; padding-bottom: 8px; margin-bottom: 12px; font-size: 0.85rem; color:#94a3b8;">
                <strong>Subject:</strong> <code>⚡ 1 click away from your trading workspace (+ market movers inside)</code><br>
                <strong>Preheader:</strong> <code>Bitcoin +3.8% today • Instant 0€ account setup</code>
            </div>
            <div style="color: #cbd5e1; font-size: 0.92rem; line-height: 1.6;">
                Hi [First Name],<br><br>
                You're seconds away from your digital trading workspace. Confirm your email below to get started:<br><br>
                <div style="text-align: center; margin: 14px 0;">
                    <span style="background:#0284c7; color:#ffffff; padding:9px 22px; border-radius:4px; font-weight:700; font-size:0.9rem;">Confirm Email & Start Exploring &rarr;</span>
                </div><br>
                <div style="background: rgba(15, 23, 42, 0.6); border: 1px solid #1e293b; border-radius: 6px; padding: 10px 12px; font-size: 0.84rem;">
                    <strong style="color:#38bdf8;">🔥 Live Market Context:</strong><br>
                    • <strong>BTC / EUR:</strong> +3.8% (€58,420) • <strong>ETH / EUR:</strong> +5.1% (€2,480)<br>
                    • <strong>Automated Sparplan:</strong> Set and forget from €25/month
                </div>
            </div>
            <hr style="border-color: #0284c7; margin: 14px 0;">
            <div style="font-size:0.82rem; color:#38bdf8;">
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
        <div class="email-container-a">
            <div style="border-bottom: 1px solid #334155; padding-bottom: 8px; margin-bottom: 12px; font-size: 0.85rem; color:#94a3b8;">
                <strong>Subject:</strong> <code>Welcome to Faizex 👋</code><br>
                <strong>Preheader:</strong> <code>When it comes to trading, we are a partner you can rely on...</code>
            </div>
            <div style="color: #cbd5e1; font-size: 0.92rem; line-height: 1.6;">
                Hi,<br><br>
                You've just become part of our community and are now able to use the best crypto app in Germany! When it comes to trading, our exchange-backed platform is a partner you can rely on. Our goal is to make trading as simple as possible for you. There's no need for a wallet, securities account, or even paperwork.<br><br>
                <div style="text-align: center; margin: 10px 0;">
                    <span style="background:#1e293b; color:#fff; border:1px solid #475569; padding:7px 18px; border-radius:4px; font-weight:600; font-size:0.85rem;">Verify now</span>
                </div><br>
                Just take a few minutes to verify your identity through a simple video identification process and you'll be ready to go!<br><br>
                <div style="text-align: center; margin: 10px 0;">
                    <span style="background:#1e293b; color:#fff; border:1px solid #475569; padding:7px 18px; border-radius:4px; font-weight:600; font-size:0.85rem;">Verify now</span>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
    with colB:
        st.markdown("""
        <div class="email-container-b">
            <div style="border-bottom: 1px solid #0284c7; padding-bottom: 8px; margin-bottom: 12px; font-size: 0.85rem; color:#94a3b8;">
                <strong>Subject:</strong> <code>Unlock your trading account in 3 minutes 🛡️ (Step 1 ready)</code><br>
                <strong>Preheader:</strong> <code>ID card ready? 2-min Video-Ident • Insured German custody</code>
            </div>
            <div style="color: #cbd5e1; font-size: 0.92rem; line-height: 1.6;">
                Hi [First Name],<br><br>
                Welcome to your institutional-grade trading account. Your workspace is 1 step away from activation:<br><br>
                <div style="background: rgba(16, 185, 129, 0.08); border: 1px solid #059669; border-radius: 6px; padding: 10px 14px; font-size: 0.86rem;">
                    <strong>Step 1:</strong> Have your ID card or passport ready (1 min)<br>
                    <strong>Step 2:</strong> Quick 2-minute Video-Ident call<br>
                    <strong>Step 3:</strong> Instant account ready for first trade (0€ deposit fee)
                </div><br>
                <div style="text-align: center; margin: 14px 0;">
                    <span style="background:#059669; color:#ffffff; padding:9px 22px; border-radius:4px; font-weight:700; font-size:0.9rem;">Unlock My Account in App (3 Mins) &rarr;</span>
                </div>
                <div style="text-align:center; font-size:0.75rem; color:#94a3b8;">
                    🔒 BaFin Regulated • Insured European Custody • No Wallet Complexity
                </div>
            </div>
            <hr style="border-color: #0284c7; margin: 14px 0;">
            <div style="font-size:0.82rem; color:#38bdf8;">
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
        <div class="email-container-a">
            <p style="color:#94a3b8; font-size:0.85rem; margin-bottom:4px;"><strong>Subject:</strong> Hi, here's your Faizex Market Digest for August 📰</p>
            <p style="color:#cbd5e1; font-size:0.88rem; line-height:1.5;">
                Bitcoin has woken up—and pulled the entire crypto market out of hibernation. The wake-up call came from Washington, where the US debt pile is spiraling out of control...
            </p>
            <div style="text-align: center; margin: 16px 0;">
                <span style="background:#1e293b; color:#fff; border:1px solid #475569; padding:8px 20px; border-radius:4px; font-weight:600; font-size:0.85rem;">Trade Bitcoin</span>
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
        <div class="email-container-b">
            <p style="color:#94a3b8; font-size:0.85rem; margin-bottom:4px;"><strong>Subject:</strong> Market Digest: Institutional flows & Volatility shift [Portfolio Impact] 📈</p>
            <p style="color:#cbd5e1; font-size:0.88rem; line-height:1.5;">
                Bitcoin has woken up—and pulled the entire crypto market out of hibernation. [Macro Report Preserved in Full]...
            </p>
        """, unsafe_allow_html=True)
        
        if "Unverified" in selected_persona:
            st.markdown("""
                <div style="background:rgba(245,158,11,0.1); border:1px solid #d97706; border-radius:6px; padding:10px; text-align:center;">
                    <span style="color:#fbbf24; font-weight:600; font-size:0.88rem;">Complete 3-Min Verification to Catch Market Momentum &rarr;</span>
                </div>
            """, unsafe_allow_html=True)
        elif "Spot Buyer" in selected_persona:
            st.markdown("""
                <div style="background:rgba(16,185,129,0.1); border:1px solid #059669; border-radius:6px; padding:10px; text-align:center;">
                    <span style="color:#34d399; font-weight:600; font-size:0.88rem;">Automate Your Accumulation: Set Up a €25 Sparplan &rarr;</span>
                </div>
            """, unsafe_allow_html=True)
        elif "Sparplan" in selected_persona:
            st.markdown("""
                <div style="background:rgba(56,189,248,0.1); border:1px solid #0284c7; border-radius:6px; padding:10px; text-align:center;">
                    <span style="color:#38bdf8; font-weight:600; font-size:0.88rem;">View August Portfolio Growth & Staking Rewards &rarr;</span>
                </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown("""
                <div style="background:rgba(236,72,153,0.1); border:1px solid #db2777; border-radius:6px; padding:10px; text-align:center;">
                    <span style="color:#f472b6; font-weight:600; font-size:0.88rem;">Activate Real-Time Price Volatility Alerts &rarr;</span>
                </div>
            """, unsafe_allow_html=True)
            
        st.markdown("""
            <hr style="border-color: #0284c7; margin: 12px 0;">
            <div style="font-size:0.82rem; color:#38bdf8;">
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
        <div class="exec-card" style="margin-bottom:0.75rem;">
            <div style="display:flex; justify-content:space-between; align-items:center;">
                <strong style="color:#f8fafc; font-size:0.95rem;">{k['name']}</strong>
                <span style="background:#1e293b; color:#38bdf8; padding:2px 8px; border-radius:4px; font-size:0.78rem; font-weight:600;">{k['target']}</span>
            </div>
            <div style="color:#34d399; font-family:'JetBrains Mono', monospace; font-size:0.84rem; margin:4px 0;">{k['formula']}</div>
            <div style="color:#94a3b8; font-size:0.82rem;"><strong>Why it Matters:</strong> {k['why']}</div>
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
        fig1.add_trace(go.Scatter(x=df_dca_calc['Month'], y=df_dca_calc['Sparplan Retention (%)'], name='Sparplan Accumulator (59.2% at M12)', line=dict(color='#10b981', width=2.5)))
        fig1.add_trace(go.Scatter(x=df_dca_calc['Month'], y=df_dca_calc['Spot Trader Retention (%)'], name='Manual Spot Trader (22.8% at M12)', line=dict(color='#ef4444', width=2, dash='dot')))
        fig1.update_layout(height=300, margin=dict(l=10, r=10, t=10, b=10), paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font=dict(color='#94a3b8', size=11))
        st.plotly_chart(fig1, use_container_width=True)
    with col2:
        st.markdown("##### 2. Assets Under Custody (AUC) Accumulation (€)")
        fig2 = go.Figure()
        fig2.add_trace(go.Scatter(x=df_dca_calc['Month'], y=df_dca_calc['Sparplan AUC (€)'], name='Sparplan Portfolio', line=dict(color='#38bdf8', width=2.5), fill='tozeroy'))
        fig2.add_trace(go.Scatter(x=df_dca_calc['Month'], y=df_dca_calc['Spot Trader AUC (€)'], name='Spot Trader Portfolio', line=dict(color='#64748b', width=1.5)))
        fig2.update_layout(height=300, margin=dict(l=10, r=10, t=10, b=10), paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font=dict(color='#94a3b8', size=11))
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
    <div class="exec-card" style="border-left: 4px solid #0284c7; max-width:650px;">
        <div style="font-size:0.75rem; color:#38bdf8; font-weight:700; margin-bottom:4px;">PUSH NOTIFICATION PAYLOAD • {asset.upper()}</div>
        <strong style="color:#f8fafc; font-size:0.95rem;">{asset} moved ±{vol}% in the last 4 hours ⚡</strong>
        <p style="color:#cbd5e1; font-size:0.86rem; margin:6px 0 0 0; line-height:1.4;">
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
        <div class="exec-card" style="border-left: 4px solid #f59e0b;">
            <div style="font-size:0.75rem; color:#fbbf24; font-weight:700;">TOUCHPOINT 1 • IN-APP SLIDE-UP (T + 15 MIN)</div>
            <strong style="color:#f8fafc; font-size:0.9rem;">Dein 0€ Einzahlungs-Auftrag wartet noch ⏱️</strong>
            <p style="color:#cbd5e1; font-size:0.84rem; margin:4px 0 0 0;">
                Tippe unten, um die IBAN direkt in deine Banking-App zu kopieren. Keine Gebühren, sofort startklar.
            </p>
        </div>
        """, unsafe_allow_html=True)
    with c2:
        st.markdown("""
        <div class="exec-card" style="border-left: 4px solid #10b981;">
            <div style="font-size:0.75rem; color:#34d399; font-weight:700;">TOUCHPOINT 2 • CUSTOMER CARE EMAIL (T + 24H)</div>
            <strong style="color:#f8fafc; font-size:0.9rem;">Brauchst du Unterstützung bei deiner ersten Einzahlung? 🛡️</strong>
            <p style="color:#cbd5e1; font-size:0.84rem; margin:4px 0 0 0;">
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
    <div class="exec-card" style="border-left: 4px solid #38bdf8; max-width:650px;">
        <div style="font-size:0.75rem; color:#38bdf8; font-weight:700; margin-bottom:4px;">IN-APP MILESTONE CELEBRATION (AUC CROSSED €1,000)</div>
        <strong style="color:#f8fafc; font-size:1rem;">🎉 Glückwunsch! Du hast die 1.000€ Spar-Marke erreicht!</strong>
        <p style="color:#cbd5e1; font-size:0.86rem; margin:6px 0 0 0; line-height:1.4;">
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
    <div class="exec-card" style="border-left: 4px solid #10b981; max-width:650px;">
        <div style="font-size:0.75rem; color:#34d399; font-weight:700; margin-bottom:4px;">IN-APP PORTFOLIO REWARD PROJECTION ({tok})</div>
        <div style="display:flex; justify-content:space-between; align-items:center;">
            <div>
                <strong style="color:#f8fafc; font-size:0.95rem;">Lass deine {tok.split()[0]} nicht schlafen 🪙</strong><br>
                <span style="color:#94a3b8; font-size:0.82rem;">100% BaFin-regulierte Verwahrung.</span>
            </div>
            <div style="text-align:right;">
                <span style="color:#34d399; font-size:1.2rem; font-weight:700;">+€{ann} / Jahr</span><br>
                <span style="color:#94a3b8; font-size:0.75rem;">(~€{mo}/Monat)</span>
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
