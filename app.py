import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ---- PAGE CONFIG ----
st.set_page_config(page_title="CPVS Data Visualization", layout="wide")
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

# ---- SHOW NOTHING UNTIL UPLOAD ----
if uploaded_file is None:
    st.info("👋 Please upload an Excel dataset (.xlsx) to view the charts.")
    st.stop()

# ---- LOAD DATA ----
try:
    df = pd.read_excel(uploaded_file)
    st.success("✅ Dataset successfully loaded!")
except Exception as e:
    st.error(f"❌ Error loading file: {e}")
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
            "Perceived Usefulness (PU) - Pie Chart",
            "Perceived Ease of Use (PEOU) - Bar Chart",
            "Attitude Toward Using (ATU) - Line Chart",
            "Behavioral Intention (BI) - Stacked Bar Chart"
        ]
    )

    if "Category" not in df.columns:
        st.error("❌ The dataset must contain a 'Category' column.")
        st.stop()

    # ---- PIE CHART ----
    if tam_chart == "Perceived Usefulness (PU) - Pie Chart":
        data = df[df["Category"] == "Perceived Usefulness (PU)"]
        if data.empty:
            st.warning("⚠️ No data found for 'Perceived Usefulness (PU)'.")
        else:
            selected_data = data.iloc[0, 1:]
            fig, ax = plt.subplots(figsize=(6, 5))
            ax.pie(selected_data, labels=selected_data.index, autopct="%1.1f%%", startangle=90)
            ax.set_title("Perceived Usefulness (PU)")
            st.pyplot(fig)

    # ---- BAR CHART ----
    elif tam_chart == "Perceived Ease of Use (PEOU) - Bar Chart":
        data = df[df["Category"] == "Perceived Ease of Use (PEOU)"]
        if data.empty:
            st.warning("⚠️ No data found for 'Perceived Ease of Use (PEOU)'.")
        else:
            selected_data = data.iloc[0, 1:]
            fig, ax = plt.subplots(figsize=(7, 5))
            ax.bar(selected_data.index, selected_data.values, color="royalblue", edgecolor="black")
            ax.set_title("Perceived Ease of Use (PEOU)")
            st.pyplot(fig)

    # ---- LINE CHART ----
    elif tam_chart == "Attitude Toward Using (ATU) - Line Chart":
        data = df[df["Category"] == "Attitude Toward Using (ATU)"]
        if data.empty:
            st.warning("⚠️ No data found for 'Attitude Toward Using (ATU)'.")
        else:
            selected_data = data.iloc[0, 1:]
            fig, ax = plt.subplots(figsize=(8, 5))
            ax.plot(selected_data.index, selected_data.values, marker="o", color="mediumseagreen", linewidth=2)
            ax.set_title("Attitude Toward Using (ATU)")
            st.pyplot(fig)

    # ---- STACKED BAR ----
    elif tam_chart == "Behavioral Intention (BI) - Stacked Bar Chart":
        data = df[df["Category"] == "Behavioral Intention (BI)"]
        if data.empty:
            st.warning("⚠️ No data found for 'Behavioral Intention (BI)'.")
        else:
            scales = ["3-Neutral", "4-Agree", "5-Strongly Agree"]
            colors = ["moccasin", "lightskyblue", "royalblue"]
            fig, ax = plt.subplots(figsize=(8, 5))
            bottom = [0]
            for i, scale in enumerate(scales):
                ax.bar(
                    ["Behavioral Intention (BI)"],
                    data[scale],
                    bottom=bottom,
                    label=scale,
                    color=colors[i]
                )
                bottom = [a + b for a, b in zip(bottom, data[scale])]
            ax.legend(title="Scale", bbox_to_anchor=(1.05, 1), loc="upper left")
            ax.set_title("Behavioral Intention (BI)")
            st.pyplot(fig)

# =============================
# 🧪 USER ACCEPTANCE TESTING (UAT)
# =============================
elif section == "🧪 UAT Charts":
    st.header("🧪 User Acceptance Testing (UAT)")

    uat_chart = st.selectbox(
        "Select a UAT construct:",
        [
            "Functionality (Pie Chart)",
            "Usability (Bar Chart)",
            "Performance (Line Chart)",
            "Satisfaction & Acceptance (Stacked Bar Chart)"
        ]
    )

    # ---- PIE CHART ----
    if uat_chart == "Functionality (Pie Chart)":
        data = df[df["Category"] == "UAT Functionality"]
        if data.empty:
            st.warning("⚠️ No data found for 'UAT Functionality'.")
        else:
            selected_data = data.iloc[0, 1:]
            fig, ax = plt.subplots(figsize=(6, 5))
            ax.pie(selected_data, labels=selected_data.index, autopct="%1.1f%%", startangle=90)
            ax.set_title("UAT Functionality")
            st.pyplot(fig)

    elif uat_chart == "Usability (Bar Chart)":
        data = df[df["Category"] == "UAT Usability"]
        if data.empty:
            st.warning("⚠️ No data found for 'UAT Usability'.")
        else:
            selected_data = data.iloc[0, 1:]
            fig, ax = plt.subplots(figsize=(7, 5))
            ax.bar(selected_data.index, selected_data.values, color="lightcoral", edgecolor="black")
            ax.set_title("UAT Usability")
            st.pyplot(fig)

    elif uat_chart == "Performance (Line Chart)":
        data = df[df["Category"] == "UAT Performance"]
        if data.empty:
            st.warning("⚠️ No data found for 'UAT Performance'.")
        else:
            selected_data = data.iloc[0, 1:]
            fig, ax = plt.subplots(figsize=(8, 5))
            ax.plot(selected_data.index, selected_data.values, marker="o", color="darkorange", linewidth=2)
            ax.set_title("UAT Performance")
            st.pyplot(fig)

    elif uat_chart == "Satisfaction & Acceptance (Stacked Bar Chart)":
        uat_subset = df[df["Category"].str.contains("UAT", case=False, na=False)]
        if uat_subset.empty:
            st.warning("⚠️ No data found for UAT categories.")
        else:
            categories = uat_subset["Category"]
            scales = ["3-Neutral", "4-Agree", "5-Strongly Agree"]
            colors = ["moccasin", "lightskyblue", "royalblue"]
            fig, ax = plt.subplots(figsize=(9, 6))
            bottom = [0] * len(categories)
            for i, scale in enumerate(scales):
                ax.bar(categories, uat_subset[scale], bottom=bottom, label=scale, color=colors[i])
                bottom = [a + b for a, b in zip(bottom, uat_subset[scale])]
            ax.legend(title="Scale", bbox_to_anchor=(1.05, 1), loc="upper left")
            ax.set_title("UAT Satisfaction & Acceptance")
            st.pyplot(fig)

# =============================
# 📘 ABOUT SECTION
# =============================
elif section == "📘 About":
    st.header("📘 About This Dashboard")
    st.markdown("""
    This interactive dashboard visualizes the **Technology Acceptance Model (TAM)** and **User Acceptance Testing (UAT)**
    results for the *Community Pet Vaccination System (CPVS)* study.
    
    **Developed by:** Research Team  
    **Purpose:** To present survey results in visual form for academic reporting and analysis.  
    **Built with:** Streamlit, Pandas, and Matplotlib.
    """)
