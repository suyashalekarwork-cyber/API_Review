import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="TDU API Review Dashboard",
    page_icon="🐢",
    layout="wide"
)

# Header
st.markdown("""
<div style="
    background: #1a3c5e;
    padding: 20px 30px;
    border-radius: 10px;
    margin-bottom: 24px;
">
    <h1 style="color:white;margin:0;font-size:26px;">
        🐢 TDU Unified Product API
    </h1>
    <p style="color:#a0c4d8;margin:4px 0 0 0;
              font-size:14px;">
        AI Extraction Review Dashboard —
        Rezdy + Fareharbor
    </p>
</div>
""", unsafe_allow_html=True)

# KPI row
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Rezdy Products", "50",
              "ChatGPT extracted")
with col2:
    st.metric("Fareharbor Products", "10",
              "Ollama extracted")
with col3:
    st.metric("Avg Accuracy", "97%",
              "words grounded in source")
with col4:
    st.metric("Sources Combined", "2",
              "Rezdy + Fareharbor")

st.markdown("---")

# Tabs
tab1, tab2 = st.tabs([
    "📦 Rezdy — ChatGPT Results (50 products)",
    "🚀 Fareharbor — Ollama Results (10 products)"
])

with tab1:
    st.markdown("""
    ### Rezdy ChatGPT Extraction Results
    50 products extracted using ChatGPT v2 prompt.
    Shows extracted fields vs original description.
    """)

    try:
        with open(
            "rezdy_50_results_chatgpt.html",
            "r", encoding="utf-8"
        ) as f:
            html_content = f.read()
        components.html(
            html_content,
            height=1200,
            scrolling=True
        )
    except FileNotFoundError:
        st.error(
            "File not found: "
            "rezdy_50_results_chatgpt.html")

with tab2:
    st.markdown("""
    ### Fareharbor Ollama Extraction Results
    10 products extracted using local
    Ollama qwen2.5:7b model.
    Shows extracted fields vs original text.
    """)

    try:
        with open(
            "fareharbor_ollama_10_review.html",
            "r", encoding="utf-8"
        ) as f:
            html_content = f.read()
        components.html(
            html_content,
            height=1200,
            scrolling=True
        )
    except FileNotFoundError:
        st.error(
            "File not found: "
            "fareharbor_ollama_10_review.html")

st.markdown("---")
st.markdown("""
<p style="text-align:center;color:#888;
           font-size:12px;">
    TDU Unified Product API —
    Data Engineering Review | July 2026
</p>
""", unsafe_allow_html=True)
