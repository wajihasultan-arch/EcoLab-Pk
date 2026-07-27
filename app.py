import os
import streamlit as st
from google import genai

# Page Configuration
st.set_page_config(
    page_title="EcoLab PK - NEQS Wastewater Diagnostic Tool",
    page_icon="🌿",
    layout="wide"
)

st.title("🌿 EcoLab PK: NEQS Compliance & Diagnostic Tool")
st.markdown("""
**Automated Environmental Diagnostic & Compliance Reporter**  
Analyze laboratory water parameters directly against **Pakistan's National Environmental Quality Standards (NEQS)** for municipal and liquid industrial effluents.
""")

st.sidebar.header("ℹ️ Project Info & API Setup")
st.sidebar.write("Built for Environmental Science laboratory practicals and industrial compliance evaluation in Pakistan.")

# Fetch API Key from environment or Streamlit Secrets
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    # Sidebar fallback for local testing
    api_key = st.sidebar.text_input("Enter Gemini API Key (Local Testing)", type="password")
    if not api_key:
        st.warning("👈 API Key not detected. Please add `GEMINI_API_KEY` to Streamlit Secrets or enter it in the sidebar.")
        st.stop()

# Initialize Google GenAI Client
client = genai.Client(api_key=api_key)

# Input Form
st.subheader("🧪 Input Laboratory Wastewater Parameters")

col1, col2 = st.columns(2)

with col1:
    sample_source = st.selectbox(
        "Sample Source / Industry",
        ["Textile Effluent", "Municipal Greywater", "Lab-Scale Artificial Wetland", "Sugar Mill Effluent", "Groundwater / Well Sample"]
    )
    ph_val = st.number_input("pH Level (NEQS Limit: 6 - 9)", min_value=0.0, max_value=14.0, value=9.5, step=0.1)
    bod_val = st.number_input("BOD₅ - Biological Oxygen Demand (mg/L) [NEQS: 80 mg/L]", min_value=0.0, value=140.0, step=5.0)
    cod_val = st.number_input("COD - Chemical Oxygen Demand (mg/L) [NEQS: 150 mg/L]", min_value=0.0, value=320.0, step=10.0)

with col2:
    tds_val = st.number_input("TDS - Total Dissolved Solids (mg/L) [NEQS: 3500 mg/L]", min_value=0.0, value=2200.0, step=50.0)
    tss_val = st.number_input("TSS - Total Suspended Solids (mg/L) [NEQS: 200 mg/L]", min_value=0.0, value=280.0, step=10.0)
    oil_grease = st.number_input("Oil & Grease (mg/L) [NEQS: 10 mg/L]", min_value=0.0, value=15.0, step=1.0)
    additional_notes = st.text_area("Observations / Treatment Method Used (Optional)", placeholder="e.g., Treated using wheat husk bio-adsorption column...")

submit_button = st.button("🚀 Run NEQS Compliance Analysis", type="primary", use_container_width=True)

# System Prompt
SYSTEM_PROMPT = """
You are an expert Environmental Engineer and NEQS Auditor specializing in industrial wastewater management in Pakistan.

Evaluate the provided laboratory water parameters strictly against Pakistan's National Environmental Quality Standards (NEQS) for Municipal and Liquid Industrial Effluents.

Format your output in clean Markdown using the following structure:

### 🚦 1. Overall Compliance Status
State clearly whether the sample is **COMPLIANT**, **NON-COMPLIANT**, or **PARTIALLY COMPLIANT**.

### 📊 2. Parameter Comparison Table
Include a clean Markdown table comparing tested values against NEQS limits:
| Parameter | Tested Value | NEQS Limit | Status (Pass / Exceeded) |

### ⚠️ 3. Environmental & Ecological Risk Breakdown
Provide 2 to 3 concise bullet points detailing the ecological impact of exceeded parameters (e.g., aquatic toxicity, eutrophication, dissolved oxygen depletion, soil degradation).

### 🛠️ 4. Low-Cost Remediation Strategies
Provide 2 practical, cost-effective remediation strategies suited for local Pakistani conditions (e.g., bio-adsorption using agricultural waste like wheat husk/sugarcane bagasse, constructed wetlands, simple aeration, or alum coagulation).
"""

if submit_button:
    user_payload = f"""
    Sample Source: {sample_source}
    pH: {ph_val}
    BOD5: {bod_val} mg/L
    COD: {cod_val} mg/L
    TDS: {tds_val} mg/L
    TSS: {tss_val} mg/L
    Oil & Grease: {oil_grease} mg/L
    Additional Notes: {additional_notes}
    """
    
    with st.spinner("Auditing laboratory parameters against Pakistan NEQS..."):
        try:
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=f"{SYSTEM_PROMPT}\n\nUSER LAB DATA FOR AUDIT:\n{user_payload}"
            )
            
            st.divider()
            st.subheader("📋 Official NEQS Audit Report")
            st.markdown(response.text)
            
        except Exception as e:
            st.error(f"Error connecting to AI service: {e}")
