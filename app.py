import streamlit as st
import pandas as pd
from scraper import get_google_leads
from ai import classify_niche, generate_message

st.set_page_config(page_title="AI Lead Generator", layout="centered")

st.title("🌍 AI-Powered Lead Generation Agent")
st.markdown("Generate qualified leads for any industry + location using AI + Google")

# --- User inputs
industry = st.text_input("🔍 Enter Industry", "Wedding Planners")
location = st.text_input("📍 Enter Location", "Dubai, UAE")

if st.button("🚀 Generate Leads"):
    with st.spinner("Getting real leads and generating messages..."):
        try:
            leads = get_google_leads(industry, location)

            # Run AI classification and messaging
            for lead in leads:
                lead["niche"] = classify_niche(lead["name"], lead.get("description", ""))
                lead["message"] = generate_message(lead["niche"], lead["name"])

            df = pd.DataFrame(leads)
            st.success(f"✅ {len(df)} leads generated!")
            st.dataframe(df)

            # Allow export
            csv = df.to_csv(index=False)
            st.download_button("⬇️ Download Leads CSV", csv, "leads.csv", "text/csv")

        except Exception as e:
            st.error(f"Error: {e}")
