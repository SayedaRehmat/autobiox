import streamlit as st

# Page Config
st.set_page_config(
    page_title="AutoBio-X | Let Your Genes Speak",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 🌌 Custom Background
st.markdown("""
    <style>
    body {
        background-color: #1b1f2a;
    }
    .css-1aumxhk { padding-top: 1rem; }
    button {
        transition: 0.3s ease;
    }
    button:hover {
        background-color: #b24b8d !important;
    }
    </style>
""", unsafe_allow_html=True)

# 💻 Layout: 2 columns (Logo | Text + Button)
col1, col2 = st.columns([1, 2])

# 🔬 Left Column: Logo
with col1:
    st.markdown("""
        <div style="padding-top: 80px; text-align: center;">
            <img src="https://raw.githubusercontent.com/SayedaRehmat/autobiox/main/autobiox_logo.png" width="160" style="border-radius: 12px;"/>
        </div>
    """, unsafe_allow_html=True)

# ✨ Right Column: Project Info + Button
with col2:
    st.markdown("""
    <h1 style="color:#d16ba5; font-size: 42px; margin-bottom: 5px;">AutoBio-X</h1>
    <p style="color:#eeeeee; font-size: 20px; margin-top: 0;">From code to cure — Let Your Genes Speak</p>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div style="margin-top: 30px; color: #cccccc; font-size: 17px; line-height: 1.8;">
        <p><b>AutoBio-X</b> is an AI-powered platform designed to analyze gene expression and mutation patterns in breast cancer — empowering early diagnosis, subtype classification, and potential therapy guidance.</p>
        <p>Created by <b>Syeda Rehmat</b>, founder of <i>BioZero</i>, this tool combines bioinformatics and artificial intelligence with a human purpose: to let your genes speak — and to let them be heard.</p>
    </div>
    """, unsafe_allow_html=True)

     # 🚀 Streamlit-safe Button Redirect
    st.markdown("###")  # spacing

     if st.button("🚀 Launch the AutoBio-X Tool"):
    st.markdown("""
        <meta http-equiv="refresh" content="0;url=https://autobiox.streamlit.app/app">
    """, unsafe_allow_html=True)


# 🖋️ Footer
st.markdown("""
<hr style='margin-top: 60px; border-color: #333;'/>
<div style='text-align: center; color:#777777; font-size: 14px; padding-bottom: 20px;'>
    © 2025 <b>Syeda Rehmat</b> — Founder of <i>BioZero</i><br>
    Powered by curiosity, courage, and code 💫
</div>
""", unsafe_allow_html=True)
