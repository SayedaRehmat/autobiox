import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from fpdf import FPDF

# ---- App Config ----
st.set_page_config(page_title="AutoBio-X", layout="centered")
st.title("🧬 AutoBio-X: Breast Cancer AI Subtype & Mutation Drug Matcher")

# ---- Train Model Inline ----
train_data = {
    "HER2": [3.2, 3.5, 2.9, 7.1, 6.8, 7.3, 10.9, 11.2, 10.6, 1.9, 2.1, 2.3],
    "TP53": [3.0, 2.8, 3.2, 3.1, 3.0, 3.3, 2.9, 3.2, 3.0, 10.1, 10.3, 9.8],
    "BRCA1": [7.2, 6.8, 7.0, 6.0, 6.1, 5.9, 3.2, 3.1, 2.8, 2.9, 3.0, 2.7],
    "ER": [9.1, 9.0, 8.9, 7.1, 6.9, 7.0, 2.2, 2.0, 1.9, 1.0, 1.2, 0.9],
    "PR": [9.0, 8.8, 9.2, 7.0, 7.1, 6.9, 2.1, 1.8, 2.0, 1.1, 0.9, 1.0],
    "EGFR": [3.2, 3.0, 2.9, 4.2, 3.8, 4.0, 5.1, 5.0, 5.3, 8.2, 8.1, 8.0],
    "Subtype": [
        "Luminal A", "Luminal A", "Luminal A",
        "Luminal B", "Luminal B", "Luminal B",
        "HER2+", "HER2+", "HER2+",
        "Triple-Negative", "Triple-Negative", "Triple-Negative"
    ]
}
df = pd.DataFrame(train_data)
X = df.drop("Subtype", axis=1)
y = df["Subtype"]
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)

# ---- Drug Mapping ----
drug_map = {
    "TP53": ["APR-246", "WEE1 inhibitors"],
    "BRCA1": ["Olaparib", "Talazoparib"],
    "PIK3CA": ["Alpelisib"],
    "PTEN": ["Everolimus"],
    "EGFR": ["Erlotinib", "Gefitinib"],
    "HER2": ["Trastuzumab", "Lapatinib"]
}

# ---- Sidebar ----
st.sidebar.title("🌍 Language / زبان منتخب کریں")
language = st.sidebar.radio("Choose:", ["English", "Urdu"])
st.sidebar.markdown("---")
st.sidebar.markdown("👩‍⚕️ Created by **Syeda Rehmat**, Founder of BioZero")

# ---- Input ----
st.header("📊 Gene Expression Input")
if language == "English":
    st.write("Enter expression values for each gene:")
else:
    st.write("ہر جین کے ایکسپریشن ویلیو درج کریں:")

her2 = st.number_input("HER2", 0.0, 15.0, 5.0)
tp53 = st.number_input("TP53", 0.0, 15.0, 5.0)
brca1 = st.number_input("BRCA1", 0.0, 15.0, 5.0)
er = st.number_input("ER", 0.0, 15.0, 5.0)
pr = st.number_input("PR", 0.0, 15.0, 5.0)
egfr = st.number_input("EGFR", 0.0, 15.0, 5.0)

# ---- Prediction ----
if st.button("🧠 Predict Subtype"):
    input_df = pd.DataFrame([[her2, tp53, brca1, er, pr, egfr]],
                             columns=["HER2", "TP53", "BRCA1", "ER", "PR", "EGFR"])
    subtype = model.predict(input_df)[0]
    st.success(f"🧬 Predicted Subtype: **{subtype}**")

# ---- Mutation File Upload ----
st.header("🧪 Upload Mutation File (.csv)")
mutation_file = st.file_uploader("Upload a CSV with columns: Gene,Mutation,Effect", type="csv")
if mutation_file is not None:
    mut_df = pd.read_csv(mutation_file)
    st.write("🔍 Uploaded Mutations:")
    st.dataframe(mut_df)

    results = []
    for index, row in mut_df.iterrows():
        gene = row["Gene"].strip().upper()
        matched_drugs = drug_map.get(gene, [])
        results.append({
            "Gene": gene,
            "Mutation": row["Mutation"],
            "Effect": row["Effect"],
            "Matched Drugs": ", ".join(matched_drugs) if matched_drugs else "—"
        })

    result_df = pd.DataFrame(results)
    st.subheader("💊 Matched Drugs")
    st.dataframe(result_df)

# ---- Footer ----
st.markdown("---")
st.markdown("© 2025 **Syeda Rehmat** — Founder of 🧬 BioZero")
