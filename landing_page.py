import streamlit as st

# ---- Page Config ----
st.set_page_config(
    page_title="Welcome | AutoBio-X",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ---- Main Logo Section ----
st.markdown("""
    <div style='text-align: center; padding-top: 30px;'>
        <img src="https://raw.githubusercontent.com/SayedaRehmat/autobiox/main/autobiox_logo.png" width="170" style="border-radius: 10px; margin-bottom: 20px;">
        <h1 style='color:#d16ba5; font-size: 40px; margin-bottom: 0;'>AutoBio-X</h1>
        <p style='color:#f5f5f5; font-size: 20px; margin-top: 5px;'>Let Your Genes Speak — Powered by AI & Bioinformatics</p>
    </div>
""", unsafe_allow_html=True)

# ---- Description ----
st.markdown("""
<div style='text-align: center; margin-top: 40px; color:#dddddd; font-size: 18px; line-height: 1.6;'>
AutoBio-X is a next-generation platform designed to explore gene expression<br>
and mutation data in breast cancer using AI. Built for researchers, clinicians,<br>
and dreamers — by <b>Syeda Rehmat</b>, founder of <i>BioZero</i>.
</div>
""", unsafe_allow_html=True)

# ---- Launch Button ----
st.markdown("""
<div style='text-align: center; margin-top: 50px;'>
    <a href='https://autobiox.streamlit.app/app' target='_blank'>
        <button style='padding: 14px 32px; font-size: 18px; background-color: #d16ba5; color: white; border: none; border-radius: 6px; cursor: pointer;'>🚀 Launch AutoBio-X Tool</button>
    </a>
</div>
""", unsafe_allow_html=True)

# ---- Footer ----
st.markdown("""
<hr style='margin-top: 60px; border-color: #333;'/>
<div style='text-align: center; color:#888888; font-size: 14px;'>
    © 2025 Syeda Rehmat — Founder of BioZero
</div>
""", unsafe_allow_html=True)
