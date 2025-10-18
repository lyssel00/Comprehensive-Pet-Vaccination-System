import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# --- PAGE CONFIG ---
st.set_page_config(page_title="TAM & UAT Graphical Results", layout="centered")

st.title("📊 Technology Acceptance Model (TAM) and User Acceptance Testing (UAT) Results")

# --- FILE UPLOAD ---
uploaded_file = st.file_uploader("Upload your dataset (Excel file)", type=["xlsx"])

if uploaded_file:
    df = pd.read_excel(uploaded_file)
    st.success("✅ Dataset successfully uploaded!")

    st.subheader("Preview of Data")
    st.dataframe(df.head())

    # --- SECTION SELECTION ---
    section = st.sidebar.radio(
        "Select Section:",
        ["📘 TAM Charts", "🧪 UAT Charts"]
    )

    # =========================
    # 📘 TECHNOLOGY ACCEPTANCE MODEL (TAM)
    # =========================
    if section == "📘 TAM Charts":
        st.header("📘 Technology Acceptance Model (TAM)")

        tam_chart = st.selectbox(
            "Select a TAM construct:",
            [
                "Perceived Usefulness (PU)",
                "Perceived Ease of Use (PEOU)",
                "Attitude Toward Using (ATU)",
                "Behavioral Intention (BI)"
            ]
        )

        # PIE CHART FOR TAM
        if tam_chart:
            try:
                selected_data = df[df["Category"] == tam_chart].iloc[0, 1:]
                labels = selected_data.index.tolist()
                values = selected_data.values.tolist()

                fig, ax = plt.subplots(figsize=(6, 5))
                ax.pie(values, labels=labels, autopct="%1.1f%%", startangle=90)
                ax.set_title(tam_chart)
                st.pyplot(fig)

            except Exception as e:
                st.error(f"Error loading chart for {tam_chart}: {e}")

    # =========================
    # 🧪 USER ACCEPTANCE TESTING (UAT)
    # =========================
    elif section == "🧪 UAT Charts":
        st.header("🧪 User Acceptance Testing (UAT)")

        uat_chart = st.selectbox(
            "Select a UAT construct:",
            [
                "UAT Functionality",
                "UAT Usability",
                "UAT Performance",
                "UAT Satisfaction & Acceptance"
            ]
        )

        # PIE CHART FOR UAT
        if uat_chart:
            try:
                selected_data = df[df["Category"] == uat_chart].iloc[0, 1:]
                labels = selected_data.index.tolist()
                values = selected_data.values.tolist()

                fig, ax = plt.subplots(figsize=(6, 5))
                ax.pie(values, labels=labels, autopct="%1.1f%%", startangle=90)
                ax.set_title(uat_chart)
                st.pyplot(fig)

            except Exception as e:
                st.error(f"Error loading chart for {uat_chart}: {e}")

else:
    st.info("📂 Please upload your Excel file to start.")

