import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ---- PAGE CONFIG ----
st.set_page_config(page_title="CPVS Data Visualization", layout="wide")

# ---- STYLING ----
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
    unsafe_allow_html=True
)

# ---- HEADER ----
st.markdown('<div class="title">📊 CPVS TAM & UAT Visualization Dashboard</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Technology Transfer and Project Implementation of Pet Vaccination Software System for Municipality of Bunawan, Agusan del Sur</div>', unsafe_allow_html=True)
st.markdown("---")

# ---- SIDEBAR ----
st.sidebar.header("📂 Upload Dataset")
uploaded_file = st.sidebar.file_uploader("Upload Excel Dataset (.xlsx)", type=["xlsx"])

# ---- CHECK UPLOAD ----
if uploaded_file is None:
    st.info("👋 Please upload an Excel dataset (.xlsx) to view the charts.")
    st.stop()

# ---- LOAD DATA ----
try:
    df = pd.read_excel(uploaded_file, engine="openpyxl")
    st.success("✅ Dataset successfully loaded!")
except Exception as e:
    st.error(f"❌ Error loading dataset: {e}")
    st.stop()

# ---- SIDEBAR MENU ----
section = st.sidebar.radio(
    "Select Section:",
    ("🏫 TAM Charts", "🧪 UAT Charts", "📘 About")
)

# =============================
# 🏫 TECHNOLOGY ACCEPTANCE MODEL (TAM)
# =============================
if section == "🏫 TAM Charts":
    st.header("🏫 Technology Acceptance Model (TAM)")

    tam_chart = st.selectbox(
        "Select a TAM construct:",
        [
            "Perceived Usefulness (PU)",
            "Perceived Ease of Use (PEOU)",
            "Attitude Toward Using (ATU)",
            "Behavioral Intention (BI)"
        ]
    )

    if "Category" not in df.columns:
        st.error("❌ The dataset must contain a 'Category' column.")
        st.stop()

    data = df[df["Category"].str.contains(tam_chart.split()[0], case=False, na=False)]

    if data.empty:
        st.warning(f"⚠️ No data found for {tam_chart}.")
    else:
        selected_data = data.iloc[0, 1:]
        chart_type = st.radio("Select Chart Type:", ["Pie", "Bar", "Line"])
        fig, ax = plt.subplots(figsize=(7, 5))

        if chart_type == "Pie":
            ax.pie(selected_data, labels=selected_data.index, autopct="%1.1f%%", startangle=90)
        elif chart_type == "Bar":
            ax.bar(selected_data.index, selected_data.values, color="royalblue", edgecolor="black")
        else:
            ax.plot(selected_data.index, selected_data.values, marker="o", color="seagreen", linewidth=2)

        ax.set_title(tam_chart)
        st.pyplot(fig)

# =============================
# 🧪 USER ACCEPTANCE TESTING (UAT)
# =============================
elif section == "🧪 UAT Charts":
    st.header("🧪 User Acceptance Testing (UAT)")

    uat_chart = st.selectbox(
        "Select a UAT construct:",
        [
            "Functionality",
            "Usability",
            "Performance",
            "Satisfaction & Acceptance"
        ]
    )

    data = df[df["Category"].str.contains(uat_chart, case=False, na=False)]

    if data.empty:
        st.warning(f"⚠️ No data found for {uat_chart}.")
    else:
        selected_data = data.iloc[0, 1:]
        chart_type = st.radio("Select Chart Type:", ["Pie", "Bar", "Line"])
        fig, ax = plt.subplots(figsize=(7, 5))

        if chart_type == "Pie":
            ax.pie(selected_data, labels=selected_data.index, autopct="%1.1f%%", startangle=90)
        elif chart_type == "Bar":
            ax.bar(selected_data.index, selected_data.values, color="salmon", edgecolor="black")
        else:
            ax.plot(selected_data.index, selected_data.values, marker="o", color="darkorange", linewidth=2)

        ax.set_title(f"UAT {uat_chart}")
        st.pyplot(fig)

# =============================
# 📘 ABOUT
# =============================
elif section == "📘 About":
    st.header("📘 About This Dashboard")
    st.markdown("""
    This dashboard visualizes the **Technology Acceptance Model (TAM)** and **User Acceptance Testing (UAT)** data
    for the *Community Pet Vaccination System (CPVS)* research project.

    **Developed by:** Research Team  
    **Purpose:** To interpret and visualize respondent feedback effectively.  
    **Tools Used:** Streamlit, Pandas, Matplotlib
    """)
