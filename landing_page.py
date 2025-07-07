import streamlit as st

# ----- Page Configuration -----
st.set_page_config(
    page_title="AutoBio-X | Let Your Genes Speak",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ----- Custom CSS Styling -----
st.markdown("""
    <style>
    body {
        background-color: #1b1f2a;
    }
    button {
        transition: 0.3s ease;
    }
    button:hover {
        background-color: #b24b8d !important;
    }
    </style>
""", unsafe_allow_html=True)

# ----- Layout: Two Columns -----
col1, col2 = st.columns([1, 2])

# ----- LEFT COLUMN: LOGO -----
with col1:
    st.markdown("""
        <div style="padding-top: 80px; text-align: center;">
            <img src="https://raw.githubusercontent.com/SayedaRehmat/autobiox/main/autobiox_logo.png" width="170" style="border-radius: 12px;" />
        </div>
    """, unsafe_allow_html=True)

# ----- RIGHT COLUMN: TITLE + TEXT + BUTTON -----
with col2:
    st.markdown("""
        <h1 style="color:#d16ba5;">AutoBio-X</h1>
        <p style="color:#eeeeee;">Let Your Genes Speak — Powered by AI</p>
        <div style="margin-top: 30px; color: #cccccc; font-size: 17px; line-height: 1.8;">
            <p><b>AutoBio-X</b> is an AI-powered platform for gene expression and mutation analysis in breast cancer.</p>
            <p>Built by <b>Syeda Rehmat</b>, Founder of <i>BioZero</i>.</p>
        </div>
    """, unsafe_allow_html=True)

    # ✅ Final working launch "button"
    st.markdown("""
        <div style="margin-top: 40px;">
            <a href="https://autobiox.streamlit.app/app" target="_blank" style="
                display: inline-block;
                padding: 14px 32px;
                font-size: 18px;
                background-color: #d16ba5;
                color: white;
                border: none;
                border-radius: 6px;
                text-decoration: none;
                font-weight: bold;
                transition: background 0.3s ease;
            ">
                🚀 Launch the AutoBio-X Tool
            </a>
        </div>
    """, unsafe_allow_html=True)

# ----- FOOTER -----
st.markdown("""
<hr style='margin-top: 60px; border-color: #333;'/>
<div style='text-align: center; color:#777777; font-size: 14px; padding-bottom: 20px;'>
    © 2025 <b>Syeda Rehmat</b> — Founder of <i>BioZero</i><br>
    Powered by curiosity, courage, and code 💫
</div>
""", unsafe_allow_html=True)
