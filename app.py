# app.py

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ---- PAGE CONFIG ----
st.set_page_config(page_title="CPVS Data Visualization", layout="wide")

# ---- CUSTOM CSS ----
st.markdown(
    """
    <style>
    body {
        background-color: #f9fafc;
        color: #1f2937;
        font-family: 'Segoe UI', sans-serif;
    }
    h1, h2, h3 {
        color: #0f172a;
    }
    .title {
        font-size: 2.2rem;
        font-weight: bold;
        color: #1e40af;
        text-align: center;
        margin-bottom: 0.3rem;
    }
    .subtitle {
        text-align: center;
        color: #475569;
        font-size: 1.1rem;
        margin-bottom: 1.5rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ---- HEADER ----
st.markdown('<div class="title">📊 CPVS TAM & UAT Visualization Dashboard</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Technology Transfer and Project Implementation of Pet Vaccination Software System for Municipality of Bunawan, Agusan del Sur: Enhancing Efficiency in Vaccination Management</div>', unsafe_allow_html=True)
st.markdown("---")

# ---- SIDEBAR ----
st.sidebar.header("📂 Upload Dataset")
uploaded_file = st.sidebar.file_uploader("Upload Excel Dataset (.xlsx)", type=["xlsx"])

# ---- WAIT FOR FILE ----
if uploaded_file is None:
    st.info("👋 Please upload an Excel dataset (.xlsx) to view the charts.")
    st.stop()

# ---- LOAD DATA ----
try:
    df = pd.read_excel(uploaded_file)
    if "Category" not in df.columns:
        st.error("❌ The uploaded Excel file must contain a 'Category' column.")
        st.stop()
    st.success("✅ Dataset successfully loaded!")
except Exception as e:
    st.error(f"❌ Error reading file: {e}")
    st.stop()

# ---- SIDEBAR MENU ----
section = st.sidebar.radio(
    "Select Section:",
    ("🏫 TAM Pie Charts", "🧪 UAT Pie Charts", "📘 About")
)

# =============================
# 🏫 TECHNOLOGY ACCEPTANCE MODEL (TAM)
# =============================
if section == "🏫 TAM Pie Charts":
    st.header("🏫 Technology Acceptance Model (TAM) - Pie Charts Only")

    tam_chart = st.selectbox(
        "Select a TAM construct:",
        [
            "Perceived Usefulness (PU)",
            "Perceived Ease of Use (PEOU)",
            "Attitude Towards Using (ATU)",
            "Behavioral Intention (BI)"
        ]
    )

    def get_data(category):
        if category not in df["Category"].values:
            st.warning(f"⚠️ No data found for '{category}'")
            return None
        return df[df["Category"] == category].iloc[0, 1:]

    selected_data = get_data(tam_chart)
    if selected_data is not None:
        labels = selected_data.index.tolist()[::-1]
        values = selected_data.values.tolist()[::-1]
        fig, ax = plt.subplots()
        wedges, texts, autotexts = ax.pie(
            values,
            labels=None,
            autopct="%1.1f%%",
            startangle=90
        )
        ax.set_title(tam_chart)
        # Add legend beside chart
        ax.legend(
            wedges,
            labels,
            title="Response Scale",
            loc="center left",
            bbox_to_anchor=(1, 0.5),
            frameon=False
        )
        st.pyplot(fig)

# =============================
# 🧪 USER ACCEPTANCE TESTING (UAT)
# =============================
elif section == "🧪 UAT Pie Charts":
    st.header("🧪 User Acceptance Testing (UAT) - Pie Charts Only")

    uat_chart = st.selectbox(
        "Select a UAT construct:",
        [
            "UAT Functionality",
            "UAT Usability",
            "UAT Performance",
            "UAT Satisfaction and Acceptance"
        ]
    )

    def get_uat_data(cat):
        if cat not in df["Category"].values:
            st.warning(f"⚠️ No data found for '{cat}'")
            return None
        return df[df["Category"] == cat].iloc[0, 1:]

    selected_data = get_uat_data(uat_chart)
    if selected_data is not None:
        labels = selected_data.index.tolist()[::-1]
        values = selected_data.values.tolist()[::-1]
        fig, ax = plt.subplots()
        wedges, texts, autotexts = ax.pie(
            values,
            labels=None,
            autopct="%1.1f%%",
            startangle=90
        )
        ax.set_title(uat_chart)
        # Add legend beside chart
        ax.legend(
            wedges,
            labels,
            title="Response Scale",
            loc="center left",
            bbox_to_anchor=(1, 0.5),
            frameon=False
        )
        st.pyplot(fig)

# =============================
# 📘 ABOUT SECTION
# =============================
elif section == "📘 About":
    st.header("📘 About This Dashboard")
    st.markdown("""
    This interactive dashboard visualizes **TAM (Technology Acceptance Model)** and **UAT (User Acceptance Testing)** data 
    from the **Computerized Pet Vaccination System (CPVS)**.
    
    ✅ Upload an Excel file with a 'Category' column and numerical values.  
    📊 Each selected construct will be shown as a **pie chart** with a legend for clear interpretation.
    """)
