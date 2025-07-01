import streamlit as st
import pandas as pd
from scraper import get_google_leads
from ai import classify_niche, generate_message
import time

st.set_page_config(page_title="AI Lead Agent", layout="centered")

st.title("🌍 AI Lead Generation Agent")
st.markdown("Get real-time leads + smart outreach messages using AI.")

# --- Input fields
industry = st.text_input("🔍 Enter Industry (e.g. Wedding Planners)", "")
location = st.text_input("📍 Enter Location (e.g. Dubai)", "")

if st.button("🚀 Generate Leads"):
    if not industry or not location:
        st.warning("Please fill both industry and location.")
    else:
        with st.spinner("Fetching leads & generating messages..."):
            try:
                leads = get_google_leads(industry, location)

                # Process each lead
                for lead in leads:
                    desc = lead.get("description", lead.get("website", ""))
                    lead["niche"] = classify_niche(lead["name"], desc)
                    lead["message"] = generate_message(lead["niche"], lead["name"])

                if leads:
                    df = pd.DataFrame(leads)
                    st.success(f"✅ {len(df)} leads generated!")
                    st.dataframe(df)

                    # Download CSV
                    csv = df.to_csv(index=False)
                    st.download_button("⬇️ Download CSV", csv, "leads.csv", "text/csv")
                else:
                    st.info("No leads found for this location and industry.")
            except Exception as e:
                st.error(f"❌ Error: {e}")

# 🔁 Keep app alive on Render
while True:
    time.sleep(1)
