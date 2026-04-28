import streamlit as st
import pandas as pd
import plotly.express as px
from sklearn.ensemble import RandomForestClassifier
import base64
st.markdown("""
<style>

/* 🌄 BACKGROUND IMAGE */
.stApp {
    background: url("https://images.unsplash.com/photo-1504674900247-0877df9cc836") no-repeat center center fixed;
    background-size: cover;
}

/* 🌑 DARK + BLUR OVERLAY */
.stApp::before {
    content: "";
    position: fixed;
    inset: 0;
    backdrop-filter: blur(6px);
    background: rgba(0, 0, 0, 0.75);
    z-index: -1;
}

/* 📦 MAIN CONTAINER */
.block-container {
    padding-top: 1.5rem;
}

/* 🎓 SIDEBAR (RED GRADIENT LIKE ZOMATO) */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #fecaca, #f87171);
    width: 260px !important;
}

/* Sidebar text */
section[data-testid="stSidebar"] * {
    color: #111827 !important;
}

/* 📊 METRIC CARDS (GLASS) */
[data-testid="stMetric"] {
    background: rgba(255, 255, 255, 0.10);
    backdrop-filter: blur(10px);
    padding: 18px;
    border-radius: 15px;
    border: 1px solid rgba(255,255,255,0.2);
    text-align: center;
    color: white;
}

/* 🔥 GLASS TITLES */
h1, h2, h3 {
    background: rgba(255, 255, 255, 0.12);
    backdrop-filter: blur(12px);
    padding: 10px 20px;
    border-radius: 12px;
    display: inline-block;
    color: white !important;
}

/* TEXT */
p, span, label {
    color: #e5e7eb !important;
}

/* 📋 TABLE */
[data-testid="stDataFrame"] {
    background-color: rgba(255,255,255,0.08);
    border-radius: 10px;
}

/* 🔘 BUTTON */
.stButton>button {
    background: linear-gradient(90deg, #ef4444, #dc2626);
    color: white;
    border-radius: 10px;
    border: none;
}

/* ➖ DIVIDER */
hr {
    border: 1px solid rgba(255,255,255,0.2);
}

</style>
""", unsafe_allow_html=True)