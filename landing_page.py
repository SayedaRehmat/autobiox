import streamlit as st

# Page Config
st.set_page_config(
    page_title="AutoBio-X | Let Your Genes Speak",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 🌌 Fullscreen Background
st.markdown("""
<style>
body {
    background-image: linear-gradient(to bottom right, #1b1f2a, #301c3b);
    background-attachment: fixed;
}
button {
    transition: 0.3s ease;
}
button:hover {
    background-color: #b24b8d !important;
}
</style>
""", unsafe_allow_html=True)

# 💖 Logo & Tagline Block
st.markdown("""
<div style="text-align: center; padding-top: 50px;">
    <img src="https://raw.githubusercontent.com/SayedaRehmat/autobiox/main/autobiox_logo.png" width="160" style="margin-bottom: 20px; border-radius: 8px;" />
    <h1 style="font-size: 42px; color: #d16ba5; margin-bottom: 10px;">AutoBio-X</h1>
    <p style="font-size: 20px; color: #eeeeee; margin-top: -5px;">
        From code to cure — Let Your Genes Speak
    </p>
</div>
""", unsafe_allow_html=True)

# 🧬 Description Block
st.markdown("""
<div style="text-align: center; margin-top: 40px; color: #cccccc; font-size: 18px; line-height: 1.7; max-width: 800px; margin-left: auto; margin-right: auto;">
AutoBio-X is a powerful AI-powered platform created to analyze gene expression and mutation patterns in breast cancer patients.<br><br>
Designed by <span style="color: #d16ba5;"><b>Syeda Rehmat</b></span>, this tool blends bioinformatics and artificial intelligence to assist in the discovery of cancer subtypes, targeted drug insights, and research exploration.<br><br>
Built not just as a project — but as a vision.
</div>
""", unsafe_allow_html=True)

# 🚀 CTA Button
st.markdown("""
<div style='text-align: center; margin-top: 60px;'>
    <a href='https://autobiox.streamlit.app/app' target='_blank'>
        <button style='padding: 16px 40px; font-size: 20px; background-color: #d16ba5; color: white; border: none; border-radius: 8px; cursor: pointer;'>🚀 Launch the AutoBio-X Tool</button>
    </a>
</div>
""", unsafe_allow_html=True)

# ✒️ Signature Footer
st.markdown("""
<hr style='margin-top: 80px; border-color: #333;'/>
<div style='text-align: center; color:#777777; font-size: 14px; padding-bottom: 20px;'>
    © 2025 <b>Syeda Rehmat</b> — Founder of <i>BioZero</i><br>
    Powered by curiosity, courage, and code 💫
</div>
""", unsafe_allow_html=True)
