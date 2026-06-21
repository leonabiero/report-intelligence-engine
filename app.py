import streamlit as st
import time

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="Report Intelligence Engine", page_icon="🧠", layout="centered")

# --- CUSTOM STYLING ---
st.markdown("""
    <style>
    .main-title { font-size: 32px; font-weight: bold; color: #1E3A8A; text-align: center; margin-bottom: 5px; }
    .subtitle { font-size: 16px; color: #4B5563; text-align: center; margin-bottom: 25px; }
    .section-header { font-size: 20px; font-weight: bold; color: #1F2937; margin-top: 20px; margin-bottom: 10px; }
    </style>
""", unsafe_allow_html=True)

# --- HEADER SECTION ---
st.markdown('<div class="main-title">The Report Intelligence Engine</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">EDE Fundazioa — AI-Based Social Support Model Prototype</div>', unsafe_allow_html=True)

st.info("💡 **Pitch Mode Active:** This interactive interface simulates the live retrieval of relevant historical records from a database of 50,000 reports to generate intelligent, context-aware interventions.")

# --- INPUT SECTION ---
st.markdown('<div class="section-header">New Client Intake Details</div>', unsafe_allow_html=True)
client_case = st.text_area(
    label="Describe the current client profile and challenges faced:",
    height=150,
    placeholder="Example: Mary, age 22, completed vocational training, currently unemployed, facing significant transport challenges impeding job hunting...",
    value="Mary, age 22, completed vocational training, currently unemployed, facing severe transport challenges which are holding back her job search."
)

# --- ANALYZE BUTTON ---
if st.button("🚀 Analyze & Retrieve Insights", type="primary", use_container_width=True):
    
    # 1. Simulate the Data Retrieval Layer (Searching Qdrant Database)
    with st.status("🔍 Scanning 50,000 historical reports in Qdrant Vector DB...", expanded=True) as status:
        time.sleep(1.5)
        st.write("✅ Mathematical semantic match completed.")
        st.write("📥 Retrieving top 3 most similar historical interventions...")
        time.sleep(1.0)
        status.update(label="Retrieval Complete!", state="complete", expanded=False)
    
    # --- DISPLAY RETRIEVED MATCHES ---
    st.markdown("---")
    st.markdown('<div class="section-header">📂 Historical Matches Found (Qdrant Database)</div>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        **Case Study A** (Match: 94%)
        * **Profile:** Vocational grad, transport barrier.
        * **Action:** Provided short-term transport subsidy.
        * **Outcome:** Secured employment within 2 months.
        """)
        
    with col2:
        st.markdown("""
        **Case Study B** (Match: 89%)
        * **Profile:** Vocational grad, no transit support.
        * **Action:** Traditional job-coaching only.
        * **Outcome:** Remained unemployed after 6 months.
        """)
        
    with col3:
        st.markdown("""
        **Case Study C** (Match: 85%)
        * **Profile:** Vocational grad, entry barrier.
        * **Action:** Direct internship match + transit stipend.
        * **Outcome:** Full-time employment in 3 months.
        """)

    # 2. Simulate the Reasoning Layer (Claude AI Response Generation)
    st.markdown("---")
    st.markdown('<div class="section-header">🤖 Claude AI Generated Recommendation Plan</div>', unsafe_allow_html=True)
    
    with st.spinner("Claude is synthesizing historical context into an optimized intervention strategy..."):
        time.sleep(2.5)  # Simulate Claude thinking
        
        st.success("### 📋 Recommended Strategic Action Plan for Mary")
        st.write("""
        Based on a deep historical analysis of **50,000 archival records**, structural training completion paired with unresolved logistics risks an extended unemployment cycle (as demonstrated in **Case B**). Conversely, direct logistical mitigation has a **94% historical correlation** with rapid employment success.

        #### 🌟 Primary Recommendations:
        1. **Deploy Immediate Transport Support:** Allocate a targeted transport subsidy for the next 60 days specifically to facilitate interview attendance and early commuting, replicating the successful framework of **Case A**.
        2. **Targeted Internship Placement:** Cross-reference current openings with active internship partners to bridge the immediate employment gap, matching the acceleration mechanics seen in **Case C**.
        3. **Administrative Savings:** By identifying these matches instantly through the Engine, the manual case-review workload for this intake was reduced by approximately **30 minutes**.
        """)

# --- FOOTER ---
st.markdown("---")
st.caption("Developed for EDE Fundazioa — Empowering Social Workers through Retrieval-Augmented Generation (RAG).")