import streamlit as st

st.set_page_config(page_title="AutoBio-X | AI Breast Cancer Platform", layout="centered")

st.markdown("""
# 🧬 AutoBio-X
### AI-Powered Breast Cancer Subtype Prediction Tool  
---

AutoBio-X is an intelligent web platform that analyzes **gene expression** and **mutations**  
to predict **breast cancer subtypes** — helping researchers and doctors make informed decisions.

🎯 Built with AI, genetics, and bilingual accessibility (Urdu & English).  
💡 Created by **Syeda Rehmat — Founder, BioZero**

---

### 🔗 Try the Tool
if st.button("🔗 Launch the AutoBio-X Tool"):
    st.markdown("[Click here to open AutoBio-X](https://autobiox.streamlit.app)", unsafe_allow_html=True)

---

### 🧕 About Me
I’m Syeda Rehmat, a passionate bioinformatics student and founder of BioZero.  
My goal is to make genomic tools accessible for all — with love, science, and AI 💛

---

### 📫 Contact
- GitHub: [github.com/SayedaRehmat](https://github.com/SayedaRehmat)
- Email: your@email.com

---

<sub>© 2025 BioZero — Empowering Genes, Empowering Women</sub>
""", unsafe_allow_html=True)
