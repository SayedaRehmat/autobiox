import streamlit as st

# Page Config
st.set_page_config(
    page_title="AutoBio-X | Let Your Genes Speak",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom background
st.markdown("""
    <style>
    body {
        background-color: #1b1f2a;
    }
    .css-1aumxhk { padding-top: 1rem; }
    </style>
""", unsafe_allow_html=True)

# Begin 2-column layout
col1, col2 = st.columns([1, 2])

# 🔬 Left: Logo Side Panel
with col1:
    st.markdown("""
        <div style="padding-top: 80px; text-align: center;">
            <img src="https://raw.githubusercontent.com/SayedaRehmat/autobiox/main/autobiox_logo.png" width="160" style="border-radius: 12px;"/>
        </div>
    """, unsafe_allow_html=True)

# 📊 Right: Text + CTA
with col2:
    st.markdown("""
        <div style="padding-top: 60px;">
            <h1 style="color:#d16ba5; font-size: 42px; margin-bottom: 5px;">AutoBio-X</h1>
            <p style="color:#eeeeee; font-size: 20px; margin-top: 0;">From code to cure — Let Your Genes Speak</p>

            <div style="margin-top: 40px; color: #cccccc; font-size: 17px; line-height: 1.7;">
                AutoBio-X is an AI-powered platform built to explore gene expression and mutation patterns in breast cancer.<br><br>
                Designed by <b>Syeda Rehmat</b> — blending bioinformatics and artificial intelligence for real clinical impact.
            </div>

            <div style="margin-top: 40px;">
                <a href='https://autobiox.streamlit.app/app' target='_blank'>
                    <button style='padding: 14px 32px; font-size: 18px; background-color: #d16ba5; color: white; border: none; border-radius: 6px; cursor: pointer;'>🚀 Launch the AutoBio-X Tool</button>
                </a>
            </div>
        </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("""
<hr style='margin-top: 60px; border-color: #333;'/>
<div style='text-align: center; color:#777777; font-size: 14px; padding-bottom: 20px;'>
    © 2025 <b>Syeda Rehmat</b> — Founder of <i>BioZero</i><br>
    Built with passion, purpose, and code 💫
</div>
""", unsafe_allow_html=True)
