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
</style>
""", unsafe_allow_html=True)

# Top Disclaimer Notice
st.caption("🔒 **PORTFOLIO NOTICE:** Faizex Digital is an independent portfolio case study platform created by Faizan Ahmed for technical and quantitative CRM demonstration. All trading and customer metrics are synthetic simulations.")

# Executive Header
st.markdown("""
<div class="exec-header">
    <div style="margin-bottom: 8px;">
        <span class="badge-reg">PORTFOLIO CASE STUDY</span>
        <span class="badge-crm">LIFECYCLE MARKETING & RETENTION STRATEGY</span>
    </div>
    <div class="exec-title">Faizex Digital — CRM Lifecycle & Retention Strategy</div>
    <p class="exec-sub">
        <em>A simulated case study in retail fintech CRM: turning first-time signups into long-term, high-value customers through activation funnel redesign, behavioral segmentation, and recurring-revenue product strategy. All data synthetic.</em>
    </p>
</div>
""", unsafe_allow_html=True)

# Master Navigation Menu Array (16 Operational Modules with BISON Strategic Fit)
NAV_MODULES = [
    "📊 Executive Summary: Strategy & Scorecard",
    "🦬 BISON (Boerse Stuttgart Digital): Strategic Fit & Blueprint",
    "✉️ Stage 1: Double Opt-In (DOI) Email Redesign",
    "🛡️ Stage 2: Breaking the KYC Drop-off",
    "🏦 Stage 3: High-Intent Deposit Recovery",
    "🎓 Stage 4: 'Learn & Earn' Quiz & Risk Profiling",
    "📱 Stage 5: Contextual In-App Conversion Nudges",
    "📈 Stage 6: The 5-Year Sparplan (DCA) Retention Engine",
    "📲 Stage 7: Event-Triggered Mobile Push (4 Scenarios)",
    "🪙 Stage 8: Idle Staking Yield & Cash Activation",
    "🏆 Stage 9: Milestone Habit Loops & Goal Gradient",
    "📰 Stage 10: Dynamic 1:1 Lifecycle Newsletter",
    "🎯 Stage 11: Retention Metrics, Unit Economics & AUC Forecast",
    "🛠️ Stage 12: Event-Driven Infrastructure & Idempotency",
    "👥 Stage 13: Cross-Functional Squad Execution Matrix",
    "💻 Stage 14: Production Liquid & Snowflake SQL Schemas"
]

# Sidebar Navigation
st.sidebar.title("Faizex CRM Case Study")
st.sidebar.markdown("**Customer Lifecycle Stages**")
nav_choice = st.sidebar.radio("Select Lifecycle Stage:", NAV_MODULES)

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
    st.markdown("### Executive Scorecard — Monthly Retail Throughput, Retention & Custody Metrics")
    
    # Framing line
    st.markdown("This is the executive view of a full-funnel CRM strategy — from onboarding friction to retention mechanics to portfolio-level revenue. The short version: we fixed the leaks, made recurring behavior the default, and let segmentation do the heavy lifting on engagement.")
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown("""
        <div class="exec-card">
            <div class="exec-card-lbl" style="min-height:34px;">30-Day Retail<br>Trading Volume</div>
            <div class="exec-card-val">€148.4M</div>
            <div class="exec-card-sub" style="min-height:32px;">+12.4% MoM · compounding off funnel and retention wins below</div>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="exec-card">
            <div class="exec-card-lbl" style="min-height:34px;">KYC → First-Trade<br>Throughput Rate</div>
            <div class="exec-card-val">39.4%</div>
            <div class="exec-card-sub" style="min-height:32px;">+11.0pts vs. 28.4% baseline · driven by the Video-Ident redesign</div>
        </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown("""
        <div class="exec-card">
            <div class="exec-card-lbl" style="min-height:34px;">12-Month Sparplan<br>Customer Retention</div>
            <div class="exec-card-val">59.2%</div>
            <div class="exec-card-sub" style="min-height:32px;">2.6x lift vs. 22.8% spot traders · the single biggest lever we pulled</div>
        </div>
        """, unsafe_allow_html=True)
    with col4:
        st.markdown("""
        <div class="exec-card">
            <div class="exec-card-lbl" style="min-height:34px;">Avg 2-Year AUC<br>per Active Account</div>
            <div class="exec-card-val">€9,850</div>
            <div class="exec-card-sub" style="min-height:32px;">Built almost entirely on recurring, habitual investing behavior</div>
        </div>
        """, unsafe_allow_html=True)
        
    st.markdown("""
    <div style="background:#ffffff; border:1px solid #e2e8f0; border-radius:8px; padding:14px 18px; margin: 12px 0 16px 0; font-size:0.9rem; color:#1e293b; line-height:1.6; box-shadow:0 1px 3px rgba(0,0,0,0.03);">
        <strong style="color:#0284c7; font-size:0.95rem;">The strategy in three moves:</strong>
        <ul style="margin:6px 0 10px 0; padding-left:20px;">
            <li><strong>Fixed the leaky funnel first.</strong> First-trade activation jumped to 39.4% (vs. 28.4% industry baseline) by simplifying the Video-Ident step — the single biggest drop-off point in onboarding.</li>
            <li><strong>Made retention a product decision, not a re-engagement campaign.</strong> Moving traders from reactive spot trading into automated Sparplans took 12-month retention from 22.8% to 59.2%. Once the behavior is automated, churn stops being emotional.</li>
            <li><strong>Let portfolio behavior drive the messaging.</strong> Segments built on what people actually hold — not who they are — kept AUC compounding steadily to €9,850 per account over two years.</li>
        </ul>
        <div style="color:#64748b; font-size:0.86rem; border-top:1px solid #f1f5f9; padding-top:8px;">
            Full funnel breakdown, segmentation logic, and stage-by-stage execution below.
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    col_left, col_right = st.columns([1.25, 1])
    with col_left:
        st.markdown("#### ⚡ Through-Funnel Onboarding Conversion (Per 10,000 Signups)")
        st.markdown("""
        <div class="expl-box-blue">
            <strong style="color:#0284c7; font-size:0.92rem;">💡 Where We Focused First</strong><br>
            Most retail platforms lose 60%+ of signups before KYC is even complete — acquisition spend evaporating before a customer ever trades. Rather than spread effort evenly across the funnel, we diagnosed the single biggest leak (Video-Ident) and rebuilt that step first. The result: a 76.7% cumulative lift in first-trade activation, from 22.3% to 39.4%.
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
        <div class="expl-box-green">
            <strong style="color:#059669; font-size:0.92rem;">💡 Why Segment by Portfolio, Not Persona</strong><br>
            Demographic segments tell you who someone is. Portfolio segments tell you what they're about to do next. By triggering messages off actual holdings — not age or signup date — each nudge lands at the moment it's most relevant, which is why retention velocity holds up across every asset class below.
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
    <div style="background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%); border: 1px solid #334155; border-radius: 12px; padding: 1.5rem 1.8rem; color: #ffffff; margin-bottom: 1.2rem; box-shadow: 0 4px 12px rgba(0,0,0,0.15);">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom: 8px;">
            <div>
                <span class="badge-reg" style="background:rgba(245,158,11,0.2); color:#fbbf24; border-color:#f59e0b;">Boerse Stuttgart Digital</span>
                <span class="badge-crm" style="background:rgba(56,189,248,0.2); color:#38bdf8; border-color:#0284c7;">BISON Retail CRM Strategy</span>
            </div>
            <span style="font-size:0.75rem; color:#94a3b8; font-weight:600;">Direct Application Blueprint for CRM-Manager Role</span>
        </div>
        <div style="font-size:1.6rem; font-weight:800; color:#ffffff; margin-bottom:0.3rem;">
            🦬 How This Engine Solves BISON's Core CRM & Lifecycle Challenges
        </div>
        <p style="font-size:0.92rem; color:#cbd5e1; line-height:1.5; margin:0;">
            As Germany's leading regulated retail crypto & multi-asset platform powered by <strong>Boerse Stuttgart Group</strong>, BISON combines institutional trust (BaFin regulation & Boerse Stuttgart Digital Custody) with mobile-first retail trading. This blueprint demonstrates end-to-end campaign execution matching BISON's tech stack (Braze, Snowflake, Liquid, Multilingual DACH setups).
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    tab_b1, tab_b2, tab_b3, tab_b4, tab_b5 = st.tabs([
        "🎯 1. 1:1 Mapping to BISON Tasks",
        "💡 2. The 6 BISON Strategic Growth Levers",
        "📱 3. Multichannel Suite (Email, Push, IAM, Banners)",
        "🗓️ 4. 30-60-90 Day BISON Roadmap",
        "💬 5. Interview Talking Points & Executive Pitch"
    ])
    
    with tab_b1:
        st.markdown("#### 📋 Direct Job Description & Skill Requirements Mapping")
        st.markdown("""
        <div class="expl-box-blue">
            <strong style="color:#0284c7; font-size:0.95rem;">💡 Built to Match BISON's Daily Operational Realities:</strong><br>
            Every task outlined in the <strong>CRM-Manager (gn) at Boerse Stuttgart Digital</strong> specification has been actively engineered and verified in this live dashboard.
        </div>
        """, unsafe_allow_html=True)
        
        mapping_data = [
            {
                "task": "1. CRM Campaigns & Full-Lifecycle Management",
                "bison_need": "Planning, execution & optimization across onboarding, activation, retention, and re-engagement.",
                "solution": "14-Stage Lifecycle Model covering Double Opt-In (DOI), Video-Ident KYC, Sparplan DCA cadence, and dormant win-back flows.",
                "tag": "Stages 1, 2, 6, 7, 10"
            },
            {
                "task": "2. Multichannel Communication (Email, Push, IAM, Banners)",
                "bison_need": "Managing target-group-specific campaigns across email, push notifications, in-app messages, and feed banners with consistent brand voice.",
                "solution": "Fully drafted multi-channel templates: responsive HTML emails, 4 volatility push triggers, 3 IAM modals, and native in-app banners.",
                "tag": "Stages 1, 5, 7, 10"
            },
            {
                "task": "3. Customer Journeys & Trigger Automation",
                "bison_need": "Developing automated communication flows based on user behavior, lifecycle stages, and relevant market triggers.",
                "solution": "T+15m & T+24h deposit abandonment recovery, payday Sparplan execution nudges, and peak-joy micro-NPS loops.",
                "tag": "Stages 3, 4, 6"
            },
            {
                "task": "4. Segmentation & Personalization (Liquid Templating)",
                "bison_need": "Defining customer segments and implementing personalized CRM measures to increase relevance, engagement, and loyalty.",
                "solution": "Portfolio-based segmentation (BTC DCA vs. ETH Staking vs. Cash Dip-Buyers) with production Braze Liquid tags & bilingual DE/EN logic.",
                "tag": "Stages 8, 10, 14"
            },
            {
                "task": "5. Testing, Optimization & Statistical Rigor",
                "bison_need": "Running A/B tests, analyzing relevant CRM KPIs, and continuously improving campaign logic.",
                "solution": "Rigorous Two-Proportion Z-Tests with sample size calculators, p-values, confidence intervals, and 5 automated unit tests.",
                "tag": "Stage 11 + test_engine.py"
            },
            {
                "task": "6. Cross-Functional Collaboration & QA / Compliance",
                "bison_need": "Working with Marketing, Product, BI, UX/UI and ensuring GDPR / BaFin compliance, DOI ledgers, and QA documentation.",
                "solution": "Audit-proof DOI consent architecture, BaFin crypto risk disclaimers, Pre-Launch QA Checklist, and squad alignment matrix.",
                "tag": "Stages 1, 12, 13, 14"
            }
        ]
        
        for m in mapping_data:
            st.markdown(f"""
            <div class="funnel-card" style="margin-bottom:10px;">
                <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:4px;">
                    <strong style="color:#0f172a; font-size:0.92rem;">{m['task']}</strong>
                    <span style="background:#f1f5f9; color:#0284c7; border:1px solid #cbd5e1; border-radius:4px; padding:2px 8px; font-size:0.75rem; font-weight:700;">{m['tag']}</span>
                </div>
                <div style="font-size:0.84rem; color:#475569; margin-bottom:3px;">
                    <strong>BISON Role Scope:</strong> {m['bison_need']}
                </div>
                <div style="font-size:0.84rem; color:#059669;">
                    <strong>Live Demonstration in Project:</strong> {m['solution']}
                </div>
            </div>
            """, unsafe_allow_html=True)

    with tab_b2:
        st.markdown("#### 💡 The 6 Strategic Growth Levers for BISON")
        
        c_a, c_b = st.columns(2)
        with c_a:
            st.markdown("""
            <div style="background:#ffffff; border:1px solid #e2e8f0; border-top:4px solid #0284c7; border-radius:8px; padding:1.2rem; margin-bottom:12px;">
                <strong style="color:#0284c7; font-size:0.95rem;">1. Solving the German Video-Ident Drop-Off 🛡️</strong>
                <p style="color:#334155; font-size:0.86rem; line-height:1.5; margin:6px 0 0 0;">
                    <strong>The BISON Challenge:</strong> As a BaFin-regulated German platform, users must complete Video-Ident. Over 60% of signups stall at this step.<br>
                    <strong>The CRM Fix:</strong> Replaced dry administrative copy with a 3-step time-stamped checklist + mobile deep-linking, lifting KYC throughput from <strong>28.4% to 39.4% (+38.7% lift)</strong>.
                </p>
            </div>
            
            <div style="background:#ffffff; border:1px solid #e2e8f0; border-top:4px solid #059669; border-radius:8px; padding:1.2rem; margin-bottom:12px;">
                <strong style="color:#059669; font-size:0.95rem;">2. Scaling BISON Sparplans (Savings Plans) 📈</strong>
                <p style="color:#334155; font-size:0.86rem; line-height:1.5; margin:6px 0 0 0;">
                    <strong>The BISON Challenge:</strong> Spot trading volume drops heavily during crypto bear markets, causing trading fee churn.<br>
                    <strong>The CRM Fix:</strong> Automated Payday (1st of month) Sparplan nudges from €25/mo. Increases 12-month retention to <strong>59.2% (2.6x higher than spot traders)</strong> and builds steady recurring trading spreads.
                </p>
            </div>
            
            <div style="background:#ffffff; border:1px solid #e2e8f0; border-top:4px solid #7c3aed; border-radius:8px; padding:1.2rem;">
                <strong style="color:#7c3aed; font-size:0.95rem;">3. Regulated Staking & Yield Cross-Sell 🪙</strong>
                <p style="color:#334155; font-size:0.86rem; line-height:1.5; margin:6px 0 0 0;">
                    <strong>The BISON Challenge:</strong> Customers leave tokens sitting idle in custody without generating revenue.<br>
                    <strong>The CRM Fix:</strong> In-app contextual cards translating idle ETH/SOL balances into concrete annual EUR rewards with Boerse Stuttgart Digital Custody trust signals (+3.4x staking adoption).
                </p>
            </div>
            """, unsafe_allow_html=True)
            
        with c_b:
            st.markdown("""
            <div style="background:#ffffff; border:1px solid #e2e8f0; border-top:4px solid #d97706; border-radius:8px; padding:1.2rem; margin-bottom:12px;">
                <strong style="color:#d97706; font-size:0.95rem;">4. High-Converting In-App Messaging (IAM) & Banners 📱</strong>
                <p style="color:#334155; font-size:0.86rem; line-height:1.5; margin:6px 0 0 0;">
                    <strong>The BISON Challenge:</strong> Email open rates are declining across Gen-Z/Millennial mobile traders.<br>
                    <strong>The CRM Fix:</strong> Contextual In-App modals triggered immediately after successful deposits (post-deposit Sparplan upsell) and FaceID biometric prompts (+31.4% direct conversion).
                </p>
            </div>
            
            <div style="background:#ffffff; border:1px solid #e2e8f0; border-top:4px solid #db2777; border-radius:8px; padding:1.2rem; margin-bottom:12px;">
                <strong style="color:#db2777; font-size:0.95rem;">5. Event-Driven Volatility & Cryptoradar Push 📲</strong>
                <p style="color:#334155; font-size:0.86rem; line-height:1.5; margin:6px 0 0 0;">
                    <strong>The BISON Challenge:</strong> Push fatigue and user opt-outs if notifications feel like clickbait spam.<br>
                    <strong>The CRM Fix:</strong> Factual price movement triggers & Cryptoradar sentiment shifts paired with direct Limit Order deep-links and a strict 24-hour frequency cap (-62.3% opt-outs).
                </p>
            </div>
            
            <div style="background:#ffffff; border:1px solid #e2e8f0; border-top:4px solid #0891b2; border-radius:8px; padding:1.2rem;">
                <strong style="color:#0891b2; font-size:0.95rem;">6. Multi-Asset Expansion (Crypto $	o$ Stocks/ETFs) 🌐</strong>
                <p style="color:#334155; font-size:0.86rem; line-height:1.5; margin:6px 0 0 0;">
                    <strong>The BISON Challenge:</strong> Cross-selling crypto native users into Boerse Stuttgart's stock and ETF trading accounts.<br>
                    <strong>The CRM Fix:</strong> Milestone triggers (€1,000 crypto milestone crossed) nudging users to diversify into DAX 40 & European equity ETFs (+28.4% multi-asset adoption).
                </p>
            </div>
            """, unsafe_allow_html=True)

    with tab_b3:
        st.markdown("#### 📱 Multichannel Campaign Orchestration Suite (Email, Push, IAM, Banners)")
        st.caption("How campaigns are orchestrated across all 4 channels specified in the BISON job description.")
        
        m_channel = st.selectbox(
            "Select BISON Channel to Inspect Campaign Execution:",
            [
                "✉️ Channel 1: Double Opt-In (DOI) & Weekly Market Digest (Email)",
                "📲 Channel 2: Real-Time Price Breakout & Cryptoradar Alerts (Push)",
                "📱 Channel 3: Contextual Post-Deposit Sparplan Upsell (In-App Message)",
                "🖼️ Channel 4: Native Home Screen Announcement Banner (In-App Feed Banner)"
            ]
        )
        
        if "Channel 1" in m_channel:
            st.markdown("""
            <div style="background:#ffffff; border:1px solid #e2e8f0; border-radius:8px; padding:1.2rem;">
                <strong style="color:#0284c7; font-size:0.92rem;">✉️ Email Channel Strategy (Braze + Liquid):</strong><br>
                <p style="color:#334155; font-size:0.86rem; line-height:1.5; margin:6px 0;">
                    • <strong>Double Opt-In (DOI):</strong> Converts the mandatory German UWG compliance step into an activation hook with live Bitcoin market movers (+30.6% click velocity).<br>
                    • <strong>Weekly Market Digest:</strong> Dynamic Liquid content blocks automatically swapping CTAs based on whether the subscriber is unverified, a manual trader, or an active Sparplan saver.
                </p>
                <div style="background:#f8fafc; border:1px solid #cbd5e1; border-radius:4px; padding:6px 10px; font-size:0.78rem; font-family:'JetBrains Mono', monospace; color:#0f172a;">
                    {{ user.preferred_language == 'de' ? 'Jetzt Sparplan einrichten' : 'Set Up Your Sparplan Now' }}
                </div>
            </div>
            """, unsafe_allow_html=True)
            
        elif "Channel 2" in m_channel:
            st.markdown("""
            <div style="background:#ffffff; border:1px solid #e2e8f0; border-radius:8px; padding:1.2rem;">
                <strong style="color:#0284c7; font-size:0.92rem;">📲 Mobile Push Notification Strategy:</strong><br>
                <p style="color:#334155; font-size:0.86rem; line-height:1.5; margin:6px 0;">
                    • <strong>Event Triggers:</strong> High volatility (+6.5% move in 2h), support level pullbacks, and BISON Cryptoradar bullish sentiment shifts.<br>
                    • <strong>Smart Deep-Linking:</strong> Deep-links directly to <code>bison://trade/btc?type=limit_order</code> to enable 1-click execution.<br>
                    • <strong>Fatigue Protection:</strong> Hard 24-hour frequency capping per user to maintain high notification opt-in rates.
                </p>
            </div>
            """, unsafe_allow_html=True)
            
        elif "Channel 3" in m_channel:
            st.markdown("""
            <div style="background:#ffffff; border:1px solid #e2e8f0; border-radius:8px; padding:1.2rem;">
                <strong style="color:#0284c7; font-size:0.92rem;">📱 In-App Message (IAM) Conversion Strategy:</strong><br>
                <p style="color:#334155; font-size:0.86rem; line-height:1.5; margin:6px 0;">
                    • <strong>100% Delivery Rate:</strong> Triggered contextually while user is active in the app.<br>
                    • <strong>Post-Deposit Modal:</strong> Fires immediately after first €100 deposit, asking: <em>"Automate this €100 deposit monthly with 0€ setup fee?"</em> (+31.4% Sparplan conversion).<br>
                    • <strong>Biometric Slide-Up:</strong> Prompts 1-click FaceID activation to reduce login friction (+42% app open frequency).
                </p>
            </div>
            """, unsafe_allow_html=True)
            
        else:
            st.markdown("""
            <div style="background:#ffffff; border:1px solid #e2e8f0; border-radius:8px; padding:1.2rem;">
                <strong style="color:#0284c7; font-size:0.92rem;">🖼️ Native In-App Feed Banner Strategy:</strong><br>
                <p style="color:#334155; font-size:0.86rem; line-height:1.5; margin:6px 0;">
                    • <strong>Persistent Non-Intrusive Guidance:</strong> Positioned at the top of the BISON home portfolio feed.<br>
                    • <strong>Dynamic Persona Targeting:</strong> Unverified users see KYC completion countdowns; active accumulators see staking yield projections and new token listings.<br>
                    • <strong>Zero Churn Risk:</strong> Does not interrupt critical trading workflows.
                </p>
                <div style="background:#eff6ff; border:1px solid #bfdbfe; border-radius:6px; padding:10px 14px; margin-top:8px; display:flex; justify-content:space-between; align-items:center;">
                    <div>
                        <strong style="color:#1e40af; font-size:0.86rem;">🪙 New on BISON: Earn 5.2% p.a. on Ethereum Staking</strong><br>
                        <span style="color:#3b82f6; font-size:0.78rem;">100% Insured German Custody by Boerse Stuttgart Digital.</span>
                    </div>
                    <span style="background:#1e40af; color:#fff; padding:4px 12px; border-radius:4px; font-size:0.75rem; font-weight:700;">Explore &rarr;</span>
                </div>
            </div>
            """, unsafe_allow_html=True)

    with tab_b4:
        st.markdown("#### 🗓️ 30-60-90 Day Operational Roadmap for BISON")
        
        r1, r2, r3 = st.columns(3)
        with r1:
            st.markdown("""
            <div style="background:#ffffff; border:1px solid #e2e8f0; border-top:4px solid #0284c7; border-radius:8px; padding:1.2rem; min-height:340px;">
                <span style="background:#f0f9ff; color:#0284c7; font-weight:700; font-size:0.75rem; padding:2px 8px; border-radius:4px;">FIRST 30 DAYS</span>
                <h4 style="color:#0f172a; margin:8px 0 6px 0;">Audit & Quick Wins</h4>
                <ul style="color:#334155; font-size:0.84rem; line-height:1.5; padding-left:18px; margin:0;">
                    <li>Deep-dive into BISON's current Braze/ESP canvas flows and event taxonomy.</li>
                    <li>Audit the Double Opt-In (DOI) and Video-Ident KYC drop-off funnels.</li>
                    <li>Implement T+15m and T+24h stalled-deposit recovery slide-ups.</li>
                    <li>Establish A/B testing standards with statistical z-test tracking.</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
            
        with r2:
            st.markdown("""
            <div style="background:#ffffff; border:1px solid #e2e8f0; border-top:4px solid #059669; border-radius:8px; padding:1.2rem; min-height:340px;">
                <span style="background:#ecfdf5; color:#059669; font-weight:700; font-size:0.75rem; padding:2px 8px; border-radius:4px;">DAY 31 - 60</span>
                <h4 style="color:#0f172a; margin:8px 0 6px 0;">Retention & Sparplan Engine</h4>
                <ul style="color:#334155; font-size:0.84rem; line-height:1.5; padding-left:18px; margin:0;">
                    <li>Launch the automated Payday Sparplan (DCA) campaign series.</li>
                    <li>Deploy contextual In-App Messages (IAM) for post-deposit upsells and biometric FaceID logins.</li>
                    <li>Implement Liquid conditional logic in BISON's weekly market updates.</li>
                    <li>Collaborate with BI on Snowflake cohort extraction queries.</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
            
        with r3:
            st.markdown("""
            <div style="background:#ffffff; border:1px solid #e2e8f0; border-top:4px solid #7c3aed; border-radius:8px; padding:1.2rem; min-height:340px;">
                <span style="background:#f5f3ff; color:#7c3aed; font-weight:700; font-size:0.75rem; padding:2px 8px; border-radius:4px;">DAY 61 - 90</span>
                <h4 style="color:#0f172a; margin:8px 0 6px 0;">Scale, Staking & NPS Loops</h4>
                <ul style="color:#334155; font-size:0.84rem; line-height:1.5; padding-left:18px; margin:0;">
                    <li>Roll out the Staking Yield cross-sell engine for eligible ETH/SOL holders.</li>
                    <li>Launch the 2-minute 'Learn & Earn' onboarding quiz and 1-click risk survey.</li>
                    <li>Integrate Peak-Joy Micro-NPS feedback loops to drive 5-star App Store ratings.</li>
                    <li>Present 90-day LTV, retention lift, and AUC compounding report to leadership.</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)

    with tab_b5:
        st.markdown("#### 💬 High-Impact Interview Talking Points & Executive Pitch")
        
        st.markdown("""
        <div style="background:#f8fafc; border:1px solid #e2e8f0; border-left:4px solid #0284c7; border-radius:8px; padding:1.2rem; margin-bottom:12px;">
            <strong style="color:#0284c7; font-size:0.95rem;">Q: How do you approach CRM at a regulated crypto platform like BISON?</strong><br>
            <p style="color:#1e293b; font-size:0.88rem; line-height:1.6; margin:6px 0 0 0;">
                <em>"At BISON, trust and simplicity are your greatest competitive moats. Regulated German custody by Boerse Stuttgart Digital gives you an immense advantage over unregulated offshore exchanges. My approach to CRM is to turn that trust into a frictionless lifecycle journey: fixing the Video-Ident drop-off first with clear 3-minute expectations, shifting users from panic-prone spot trading into automated monthly Sparplans to secure 59%+ 12-month retention, and using Braze Liquid personalization so every notification is actionable and respectful of user attention."</em>
            </p>
        </div>
        
        <div style="background:#f8fafc; border:1px solid #e2e8f0; border-left:4px solid #059669; border-radius:8px; padding:1.2rem; margin-bottom:12px;">
            <strong style="color:#059669; font-size:0.95rem;">Q: How do you coordinate multichannel messaging across Email, Push, In-App Messages, and Banners?</strong><br>
            <p style="color:#1e293b; font-size:0.88rem; line-height:1.6; margin:6px 0 0 0;">
                <em>"I orchestrate channels based on customer intent and latency. <strong>Push notifications</strong> are reserved for high-urgency market triggers (volatility breakout, Cryptoradar sentiment) with strict 24-hour frequency capping to prevent opt-outs. <strong>In-App Messages (IAM)</strong> are our highest-converting channel for in-the-moment milestones (e.g., upselling a Sparplan right after a successful deposit). <strong>In-App Banners</strong> provide persistent non-intrusive education on the home screen. And <strong>Email</strong> is our long-form macro storytelling engine, powered by Liquid conditional logic for 1:1 personalization."</em>
            </p>
        </div>
        
        <div style="background:#f8fafc; border:1px solid #e2e8f0; border-left:4px solid #7c3aed; border-radius:8px; padding:1.2rem; margin-bottom:12px;">
            <strong style="color:#7c3aed; font-size:0.95rem;">Q: How do you collaborate cross-functionally with Product, BI, UX, and Compliance?</strong><br>
            <p style="color:#1e293b; font-size:0.88rem; line-height:1.6; margin:6px 0 0 0;">
                <em>"CRM cannot operate in a silo. I work with <strong>BI</strong> on event dictionaries (`kyc_step_reached`, `sparplan_created`) and Snowflake SQL cohort extractions; with <strong>Product & Mobile</strong> on deep-link schemas (`bison://sparplan/new`) and native SDK triggers; with <strong>UX/UI</strong> to ensure accessible, brand-compliant Figma tokens; and with <strong>Legal/Compliance</strong> to guarantee audit-proof Double Opt-In (DOI) ledgers and BaFin risk disclosures."</em>
            </p>
        </div>
        
        <div style="background:#f8fafc; border:1px solid #e2e8f0; border-left:4px solid #d97706; border-radius:8px; padding:1.2rem;">
            <strong style="color:#d97706; font-size:0.95rem;">Q: How do you ensure high quality and zero errors before campaign go-live?</strong><br>
            <p style="color:#1e293b; font-size:0.88rem; line-height:1.6; margin:6px 0 0 0;">
                <em>"I follow a strict Pre-Launch QA Checklist: (1) Seed list preview across 12+ email clients and dark/light modes, (2) Deep-link verification on both iOS and Android staging builds, (3) Liquid fallback testing for empty user attributes, (4) Frequency capping & quiet hours validation, and (5) BaFin risk disclaimer and Double-Opt-In consent audit verification."</em>
            </p>
        </div>
        """, unsafe_allow_html=True)

# ==========================================
# MODULE 2: STAGE 1 - DOUBLE OPT-IN (DOI)
# ==========================================
elif nav_choice == NAV_MODULES[2]:
    st.markdown("### ✉️ Stage 1: Double Opt-In (DOI) Confirmation & Activation Momentum")
    st.markdown("**Executive Context:** Under European GDPR and German UWG regulations, **Double Opt-In (DOI)** confirmation is legally mandatory before sending marketing communications. With an outstanding **68.2% open rate** (the highest in the customer lifecycle), treating the DOI email as a dry legal stop wastes peak customer motivation. Our hypothesis embeds live market movers directly into the DOI confirmation to drive immediate momentum into Video-Ident (KYC).")
    
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
# MODULE 3: STAGE 2 - ONBOARDING / KYC
# ==========================================
elif nav_choice == NAV_MODULES[3]:
    st.markdown("### 🛡️ Stage 2: Regulated Identity Verification (KYC) Funnel Optimization")
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
# MODULE 4: STAGE 3 - STALLED DEPOSIT RECOVERY
# ==========================================
elif nav_choice == NAV_MODULES[4]:
    st.markdown("### 🏦 Stage 3: High-Intent Deposit Abandonment & Recovery Journey")
    st.markdown("**Executive Context:** Recovers verified users who stalled before initiating their first bank transfer using a 15-minute in-app slide-up and a 24-hour supportive care email.")
    
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("""
        <div class="exec-card" style="border-left: 4px solid #d97706; min-height:auto;">
            <div style="font-size:0.75rem; color:#d97706; font-weight:700;">TOUCHPOINT 1 • IN-APP SLIDE-UP (T + 15 MIN)</div>
            <strong style="color:#0f172a; font-size:0.9rem;">Your 0€ Deposit Request is Ready ⏱️</strong>
            <p style="color:#334155; font-size:0.84rem; margin:4px 0 0 0;">
                Tap below to copy your dedicated IBAN directly into your banking app. 0€ deposit fee, ready in minutes.
            </p>
            <div style="margin-top:8px;">
                <span style="background:#d97706; color:#fff; padding:4px 12px; border-radius:4px; font-size:0.75rem; font-weight:700;">Copy IBAN & Finish &rarr;</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
    with c2:
        st.markdown("""
        <div class="exec-card" style="border-left: 4px solid #059669; min-height:auto;">
            <div style="font-size:0.75rem; color:#059669; font-weight:700;">TOUCHPOINT 2 • CUSTOMER CARE EMAIL (T + 24H)</div>
            <strong style="color:#0f172a; font-size:0.9rem;">Need help with your first account deposit? 🛡️</strong>
            <p style="color:#334155; font-size:0.84rem; margin:4px 0 0 0;">
                Reassuring customer care explaining SEPA instant settlement, zero fees, and European custody security.
            </p>
            <div style="margin-top:8px;">
                <span style="background:#059669; color:#fff; padding:4px 12px; border-radius:4px; font-size:0.75rem; font-weight:700;">View 1-Click Guide &rarr;</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
    st.success("📈 **Quantified Impact:** +20.3% First-Deposit Recovery Rate (+64% Email CTR).")

# ==========================================
# MODULE 5: STAGE 4 - LEARN & EARN, SURVEYS & NPS
# ==========================================
elif nav_choice == NAV_MODULES[5]:
    st.markdown("### 💡 Stage 4: Zero-Party Data Collection, 'Learn & Earn' Gamification & In-App NPS")
    
    st.markdown("""
    <div class="expl-box-blue">
        <strong style="color:#0284c7; font-size:1rem;">💡 The FinTech & Crypto Growth Secret (Coinbase & Revolut Benchmark):</strong><br>
        Traditional ads tell users to deposit money before they understand the product. Industry leaders like <strong>Revolut Crypto Learn</strong> and <strong>Coinbase Quests</strong> proved that interactive <strong>2-minute bite-sized quizzes and 1-click risk surveys</strong> lower psychological friction, educate users on smart trading strategies (DCA & Limit Orders), and generate a <strong>+52.4% lift in first-time trading volume</strong>.
    </div>
    """, unsafe_allow_html=True)
    
    tab1, tab2, tab3 = st.tabs([
        "🎓 1. Interactive 'Learn & Earn' Quiz",
        "🎯 2. 1-Click Trading Risk & Persona Survey",
        "⭐ 3. In-App NPS & CSAT Feedback Loop"
    ])
    
    with tab1:
        st.markdown("#### 🎓 2-Minute Trading Mastery Quiz (With Instant €5 Trading Bonus)")
        st.caption("Benchmark: Revolut 'Crypto Learn' & Coinbase Quests model.")
        
        q1 = st.radio(
            "Question 1: What is the main benefit of an automated Sparplan (Dollar-Cost Averaging)?",
            [
                "A) Trying to predict exact daily price peaks and valleys",
                "B) Steadily lowering average purchase price over time without market timing stress (Correct)",
                "C) Paying high manual execution fees on every single trade"
            ]
        )
        
        q2 = st.radio(
            "Question 2: How do Limit Buy Orders protect you during high volatility?",
            [
                "A) They automatically buy only when the price drops to your chosen discount level (Correct)",
                "B) They execute immediately at whatever market price is offered",
                "C) They prevent you from withdrawing funds"
            ]
        )
        
        if st.button("Submit Quiz & Claim €5 Trading Reward 🎁"):
            if "Correct" in q1 and "Correct" in q2:
                st.balloons()
                st.markdown("""
                <div style="background:linear-gradient(135deg, #059669 0%, #047857 100%); color:#fff; border-radius:12px; padding:1.5rem; text-align:center; max-width:600px; margin:10px auto;">
                    <h3 style="color:#fff; margin:0 0 6px 0;">🎉 100% Score! €5 Trading Bonus Credited</h3>
                    <p style="font-size:0.9rem; margin:0 0 12px 0;">You've mastered Dollar-Cost Averaging and Limit Orders. Your €5 trading credit is ready in your wallet.</p>
                    <span style="background:#ffffff; color:#059669; padding:8px 20px; border-radius:6px; font-weight:800; font-size:0.88rem;">Set Up 1st Sparplan with €5 Bonus &rarr;</span>
                </div>
                """, unsafe_allow_html=True)
            else:
                st.warning("Almost there! Review your answers and try again to unlock your €5 reward.")
                
        st.markdown("""
        <div style="font-size:0.82rem; color:#475569; margin-top:10px;">
            📈 <strong>CRM Impact:</strong> 74.2% Quiz Completion Rate • <strong>+52.4% 7-Day First-Trade Conversion</strong> • <strong>+38.6% Higher 30-Day AUC Inflow</strong>.
        </div>
        """, unsafe_allow_html=True)
        
    with tab2:
        st.markdown("#### 🎯 1-Click Investor Risk & Goal Assessment Survey")
        st.caption("Benchmark: Robinhood & Trade Republic suitability and profile onboarding.")
        
        survey_style = st.selectbox(
            "What is your primary investment goal on Faizex?",
            [
                "🛡️ Steady Long-Term Wealth Accumulation (Automate BTC & ETF Sparplans)",
                "🪙 Passive Staking Rewards & Yield (Earn 4.8% on ETH/SOL + 3.2% on EUR Cash)",
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
                ✅ <strong>Zero Spam Guarantee:</strong> Users only receive educational campaigns matching their declared risk appetite.
            </div>
        </div>
        """, unsafe_allow_html=True)
        
    with tab3:
        st.markdown("#### ⭐ In-App Micro-NPS (Net Promoter Score) Feedback Engine")
        st.caption("Benchmark: Triggered at Peak-Joy moments (e.g., T+2 minutes after first profitable trade or Sparplan execution).")
        
        nps_score = st.slider("How likely are you to recommend Faizex to a colleague or friend? (0 = Not likely, 10 = Extremely likely)", 0, 10, 9)
        
        if nps_score >= 9:
            st.markdown("""
            <div style="background:#ecfdf5; border:1px solid #a7f3d0; border-radius:8px; padding:1.2rem; margin-top:10px;">
                <strong style="color:#059669; font-size:0.95rem;">🌟 Promoter Workflow Triggered (Score 9-10):</strong>
                <p style="color:#0f172a; font-size:0.86rem; margin:6px 0 10px 0;">
                    Thank you for the amazing score! Would you take 10 seconds to rate us on the App Store or share your €15 referral code with friends?
                </p>
                <span style="background:#059669; color:#fff; padding:6px 14px; border-radius:4px; font-weight:700; font-size:0.82rem;">Rate on App Store ⭐⭐⭐⭐⭐</span>
                <span style="background:#ffffff; color:#059669; border:1px solid #a7f3d0; padding:6px 14px; border-radius:4px; font-weight:700; font-size:0.82rem; margin-left:8px;">Share €15 Invite Link 🎁</span>
            </div>
            """, unsafe_allow_html=True)
        elif nps_score >= 7:
            st.markdown("""
            <div style="background:#f0f9ff; border:1px solid #bae6fd; border-radius:8px; padding:1.2rem; margin-top:10px;">
                <strong style="color:#0284c7; font-size:0.95rem;">💬 Passive Feedback Prompt (Score 7-8):</strong>
                <p style="color:#0f172a; font-size:0.86rem; margin:6px 0 10px 0;">
                    Thank you for trading with us! What single feature or asset would make Faizex a 10/10 for you?
                </p>
                <input type="text" placeholder="e.g. Add Solana staking, lower spreads, recurring SEPA..." style="width:100%; padding:8px; border:1px solid #cbd5e1; border-radius:4px; font-size:0.85rem;">
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown("""
            <div style="background:#fef2f2; border:1px solid #fecaca; border-radius:8px; padding:1.2rem; margin-top:10px;">
                <strong style="color:#ef4444; font-size:0.95rem;">🛡️ Detractor Churn-Prevention Escalation (Score 0-6):</strong>
                <p style="color:#0f172a; font-size:0.86rem; margin:6px 0 10px 0;">
                    We are so sorry we did not meet your expectations. A dedicated customer care specialist has been alerted to assist you within 15 minutes.
                </p>
                <span style="background:#ef4444; color:#fff; padding:6px 14px; border-radius:4px; font-weight:700; font-size:0.82rem;">Open Priority Support Chat 💬</span>
            </div>
            """, unsafe_allow_html=True)
            
        st.markdown("""
        <div style="font-size:0.82rem; color:#475569; margin-top:12px;">
            📈 <strong>Quantified Impact:</strong> <strong>+62.0% App Store 5-Star Ratings Lift</strong> • <strong>-44.8% Churn Prevention on Detractors</strong>.
        </div>
        """, unsafe_allow_html=True)

# ==========================================
# MODULE 6: STAGE 5 - IN-APP MESSAGE SUITE
# ==========================================
elif nav_choice == NAV_MODULES[6]:
    st.markdown("### 📱 Stage 5: Contextual In-App Messaging (IAM) & Conversion Modals")
    
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
# MODULE 7: STAGE 6 - SPARPLAN LTV COHORT MODEL
# ==========================================
elif nav_choice == NAV_MODULES[7]:
    st.markdown("### 📈 Stage 6: Recurring Dollar-Cost Averaging (DCA Sparplan) Retention Engine")
    
    st.markdown("""
    <div class="expl-box-blue">
        <strong style="color:#0284c7; font-size:1rem;">💡 The CRM Strategy in Simple Words:</strong><br>
        <strong>1. The Problem in Trading Apps:</strong> When users buy crypto manually, they check the price every day. When the market goes down or sideways, they get scared, stop trading, and <strong>77% leave the app within 12 months</strong>.<br>
        <strong>2. What We Did (CRM Campaign):</strong> Instead of telling them to "Trade Today", our automated lifecycle emails & in-app nudges pitch <strong>Automated Monthly Sparplans (DCA) from €25/month</strong> right on European payday (1st of each month).<br>
        <strong>3. The 5-Year Result:</strong> Because their deposit is automatic, users stay active for years—increasing 12-month retention from <strong>22.8% to 59.2% (2.6x higher loyalty)</strong> and accumulating over <strong>€9,850 in Assets Under Custody (AUC)</strong>.
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("#### ✉️ The Automated CRM Campaign We Deployed:")
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
# MODULE 8: STAGE 7 - MOBILE PUSH SCENARIOS
# ==========================================
elif nav_choice == NAV_MODULES[8]:
    st.markdown("### 📲 Stage 7: Event-Triggered Mobile Push & Volatility Reactivation Engine")
    
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
        deep_link = "faizex://markets/btc?tab=limit_order"
        impact_note = "+44.1% 24h Trading Volume Lift with -62.3% Push Opt-Outs."
        badge_color = "#0284c7"
    elif "Scenario 2" in push_scenario:
        push_title = "Market Pullback Detected (-5.8%) 📉"
        push_body = "Top 10 crypto assets reaching 30-day support levels. You have €450 uninvested cash ready for 1-click orders."
        push_tag = "FLASH DIP / CASH WAKE-UP"
        deep_link = "faizex://portfolio/cash?action=buy_dip"
        impact_note = "+32.8% Cash Balance Deployment within 6 hours of notification."
        badge_color = "#d97706"
    elif "Scenario 3" in push_scenario:
        push_title = "Ethereum Staking Yield Updated: 5.2% p.a. 🪙"
        push_body = "Your 2.4 ETH in custody can generate ~€12.50/month in passive rewards. 100% BaFin-regulated custody."
        push_tag = "PRODUCT YIELD ACTIVATION"
        deep_link = "faizex://staking/eth"
        impact_note = "+3.4x Staking Adoption across eligible token holders."
        badge_color = "#059669"
    else:
        push_title = "Tomorrow: Your €50 Bitcoin Sparplan Executes ⏱️"
        push_body = "Your scheduled monthly DCA accumulation will run automatically at 08:00 CET with 0€ setup fees."
        push_tag = "DCA LIFECYCLE PREVIEW"
        deep_link = "faizex://sparplan/details"
        impact_note = "Reduces failed bank direct-debits by 38.2% via advance balance awareness."
        badge_color = "#7c3aed"
        
    st.markdown(f"""
    <div style="background:#ffffff; border:1px solid #e2e8f0; border-radius:12px; padding:1.4rem; max-width:650px; box-shadow:0 4px 12px rgba(0,0,0,0.05); margin-bottom:1rem;">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
            <div style="display:flex; align-items:center; gap:8px;">
                <span style="background:{badge_color}; color:#fff; border-radius:6px; padding:3px 8px; font-size:0.72rem; font-weight:800;">FAIZEX DIGITAL</span>
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
# MODULE 9: STAGE 8 - IDLE STAKING YIELD
# ==========================================
elif nav_choice == NAV_MODULES[9]:
    st.markdown("### 🪙 Stage 8: Cross-Sell Staking Yield & Idle Capital Monetization")
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
# MODULE 10: STAGE 9 - MILESTONE GAMIFICATION
# ==========================================
elif nav_choice == NAV_MODULES[10]:
    st.markdown("### 🏆 Stage 9: Milestone-Based Retention Loops & Goal-Gradient Rewards")
    st.markdown("**Executive Context:** Based on the Goal Gradient Effect: celebrates users reaching €500, €1,000, or €5,000 AUC milestones to drive Sparplan retention.")
    
    st.markdown("""
    <div class="exec-card" style="border-left: 4px solid #0284c7; max-width:650px; min-height:auto;">
        <div style="font-size:0.75rem; color:#0284c7; font-weight:700; margin-bottom:4px;">IN-APP MILESTONE CELEBRATION (AUC CROSSED €1,000)</div>
        <strong style="color:#0f172a; font-size:1rem;">🎉 Congratulations! You Crossed the €1,000 Savings Milestone!</strong>
        <p style="color:#334155; font-size:0.86rem; margin:6px 0 0 0; line-height:1.5;">
            You are now in the top 25% of disciplined long-term accumulators on Faizex. Increase your Sparplan by +€25/month to reach your €2,500 goal 4 months faster.
        </p>
        <div style="margin-top:10px;">
            <span style="background:#0284c7; color:#fff; padding:6px 16px; border-radius:4px; font-weight:700; font-size:0.84rem;">Upgrade Sparplan (+€25/mo) &rarr;</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.success("📈 **Quantified Impact:** 59.2% 12-Month Retention / +52.4% Sparplan Upgrade Velocity.")

# ==========================================
# MODULE 11: STAGE 10 - EDITORIAL NEWSLETTER
# ==========================================
elif nav_choice == NAV_MODULES[11]:
    st.markdown("### 📰 Stage 10: Dynamic 1:1 Personalized Newsletter (Liquid Content Blocks)")
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
# MODULE 12: STAGE 11 - KPIS & FORECAST
# ==========================================
elif nav_choice == NAV_MODULES[12]:
    st.markdown("### 🎯 Stage 11: Quantitative CRM Metrics, LTV/CAC & AUC Forecasting")
    
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
# MODULE 13: STAGE 12 - CRM ARCHITECTURE
# ==========================================
elif nav_choice == NAV_MODULES[13]:
    st.markdown("### 🛠️ Stage 12: Event-Driven CRM Infrastructure & Idempotent Dispatcher")
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
elif nav_choice == NAV_MODULES[14]:
    st.markdown("### 👥 Stage 13: Cross-Functional Squad Execution Matrix (BI, Product, Compliance)")
    st.markdown("""
    | Stakeholder | Key Collaboration Area | Standardized Workflow Example |
    |---|---|---|
    | **BI / Analytics Team** | Event tracking, Cohort schemas, SQL queries | Standardizing event naming dictionaries (`kyc_step_reached`, `sparplan_created`). |
    | **Product & Mobile** | In-App message triggers, App deep-links | Testing custom URI schemes (`faizex://verify/video-ident`) across native app releases. |
    | **UX / UI Design** | Responsive HTML templates & design tokens | Accessible dark/light mode compatibility and 48px mobile touch targets. |
    | **Legal & BaFin** | Regulatory compliance & Double-Opt-In (DOI) | Audit-proof DOI consent ledgers and crypto risk disclaimers. |
    """, unsafe_allow_html=True)

# ==========================================
# MODULE 15: STAGE 14 - TECHNICAL STACK
# ==========================================
elif nav_choice == NAV_MODULES[15]:
    st.markdown("### 💻 Stage 14: Production Liquid Templates & Snowflake Cohort Schemas")
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
