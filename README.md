# 🌿 EcoLab PK — NEQS Compliance & Diagnostic Tool

> **Live Application URL:** [https://ecolab-pk.streamlit.app](https://ecolab-pk.streamlit.app)  
> **Repository Status:** Public

---

## 📋 Overview & Problem Statement
* **App Name:** EcoLab PK
* **Target Audience:** Environmental Science students, laboratory researchers, and environmental auditors in Pakistan.
* **The Real Problem:** During university laboratory practicals and industrial site assessments, students manually evaluate wastewater parameters (pH, BOD, COD, TDS, TSS) against **Pakistan's National Environmental Quality Standards (NEQS)**. Manually looking up standards and compiling diagnostic risk assessments for reports is repetitive and prone to calculation oversight.
* **The Solution:** EcoLab PK provides an instant, AI-driven compliance report that compares raw laboratory readings against NEQS thresholds, identifies exceeded parameters, explains ecological risks, and suggests low-cost local treatment solutions.

---

## ✨ Features List
- [x] **NEQS Parameter Audit:** Evaluates pH, BOD₅, COD, TDS, TSS, and Oil & Grease against Pakistan discharge limits.
- [x] **Automated Compliance Table:** Generates a structured comparison table showing tested values vs. official standards.
- [x] **Ecological Risk Assessment:** Details environmental impacts such as eutrophication and aquatic toxicity.
- [x] **Localized Remediation Guidance:** Recommends practical, low-cost treatment methods (e.g., bio-adsorption using agricultural waste like wheat husk or constructed wetlands).
- [x] **Custom Sample Profiles:** Supports inputs for textile effluents, municipal greywater, lab-scale wetlands, and groundwater.

---

## 🤖 The AI Feature & System Prompt
### AI Implementation
The AI auditing core uses the **Google GenAI SDK** (`gemini-2.5-flash`) to parse laboratory inputs and generate an environmental compliance report.

### System Prompt / System Instructions
\`\`\`text
You are an expert Environmental Engineer and NEQS Auditor specializing in industrial wastewater management in Pakistan.

Evaluate the provided laboratory water parameters strictly against Pakistan's National Environmental Quality Standards (NEQS) for Municipal and Liquid Industrial Effluents.

Format your output in clean Markdown using the following structure:

### 🚦 1. Overall Compliance Status
State clearly whether the sample is COMPLIANT, NON-COMPLIANT, or PARTIALLY COMPLIANT.

### 📊 2. Parameter Comparison Table
Include a clean Markdown table comparing tested values against NEQS limits:
| Parameter | Tested Value | NEQS Limit | Status (Pass / Exceeded) |

### ⚠️ 3. Environmental & Ecological Risk Breakdown
Provide 2 to 3 concise bullet points detailing the ecological impact of exceeded parameters.

### 🛠️ 4. Low-Cost Remediation Strategies
Provide 2 practical, cost-effective remediation strategies suited for local Pakistani conditions (e.g., bio-adsorption using agricultural waste, constructed wetlands, aeration).
\`\`\`

---

## 🛠️ Tools, Services & AI Models Used
* **Framework:** Python + Streamlit
* **AI Provider:** Google Gemini API (`gemini-2.5-flash` via `google-genai` SDK)
* **Hosting Platform:** Streamlit Community Cloud
* **Version Control:** Git & GitHub

---

## 🖼️ Screenshots
![App Form Interface](./screenshots/screenshot1.png)  
*Figure 1: Input form for entering laboratory wastewater readings.*

![AI Processing & Audit Execution](./screenshots/screenshot2.png)  
*Figure 2: Execution of NEQS diagnostic audit.*

![NEQS Compliance Report Output](./screenshots/screenshot3.png)  
*Figure 3: Generated NEQS compliance table, ecological risks, and localized remediation strategies.*

---

## 🚀 How to Run the Project Locally

### Prerequisites
* Python 3.10 or higher
* A free Gemini API key from [Google AI Studio](https://aistudio.google.com/)

### Installation Steps
1. Clone the repository:
   \`\`\`bash
   git clone https://github.com/YOUR_USERNAME/ecolab-pk.git
   cd ecolab-pk
   \`\`\`

2. Install dependencies:
   \`\`\`bash
   pip install -r requirements.txt
   \`\`\`

3. Configure Environment Variables:
   Set your API key in your terminal session:
   \`\`\`bash
   # Windows (CMD)
   set GEMINI_API_KEY="your_api_key_here"

   # macOS / Linux / Bash
   export GEMINI_API_KEY="your_api_key_here"
   \`\`\`

4. Launch the application:
   \`\`\`bash
   streamlit run app.py
   \`\`\`
