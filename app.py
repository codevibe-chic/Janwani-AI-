import streamlit as st
import time

# --- PAGE SETUP (Mobile/iPad Optimized) ---
st.set_page_config(page_title="Janwani AI", page_icon="🎙️", layout="centered")

# Custom Dark Theme Styling
st.markdown("""
    <style>
        body { background-color: #050811; }
        .stApp { background-color: #050811; color: #FFFFFF; }
        .title { font-size: 36px; font-weight: 800; color: #2DD4BF; text-align: center; }
        .subtitle { font-size: 16px; color: #94A3B8; text-align: center; margin-bottom: 20px; }
        .card { background: rgba(255,255,255,0.05); padding: 20px; border-radius: 15px; border: 1px solid rgba(45,212,191,0.3); margin-top: 15px; }
        .status-tag { background-color: #10B981; color: black; font-weight: bold; padding: 4px 10px; border-radius: 8px; font-size: 12px; }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="title">JANWANI AI</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Voice-First Gateway to India\'s Welfare Stack</div>', unsafe_allow_html=True)

# --- 1. LANGUAGE SELECTOR ---
lang = st.selectbox(
    "Select Your Language / भाषा चुनें / భాష / भाषा निवडा",
    ["Hindi (हिन्दी)", "Marathi (मराठी)", "Telugu (తెలుగు)", "English"]
)

# Simulated Knowledge Base of Schemes
scheme_database = {
    "Hindi (हिन्दी)": {
        "pension": "नमस्ते। वृद्धावस्था पेंशन योजना के तहत आपको हर महीने ₹1,000 की वित्तीय सहायता सीधे बैंक खाते में मिलेगी।",
        "farmer": "प्रधानमंत्री किसान सम्मान निधि योजना के तहत किसानों को हर साल ₹6,000 की आर्थिक मदद 3 किश्तों में दी जाती है।",
        "general": "नमस्ते! मैं जनवाणी एआई हूँ। आप बोलकर अपनी पेंशन, किसान सहायता या राशन कार्ड की जानकारी प्राप्त कर सकते हैं।"
    },
    "Marathi (मराठी)": {
        "pension": "नमस्कार. संजय गांधी निराधार योजनेअंतर्गत ज्येष्ठ नागरिकांना दरमहा ₹1,500 आर्थिक सहाय्य थेट बँक खात्यात दिले जाते.",
        "farmer": "नमो शेतकरी महासन्मान निधी योजनेअंतर्गत शेतकऱ्यांना वर्षाला ₹6,000 अतिरिक्त मदत मिळते.",
        "general": "नमस्कार! मी जनवाणी एआय. तुम्ही बोलून पेन्शन, शेतकरी योजना किंवा रेशन कार्डची माहिती मिळवू शकता."
    },
    "Telugu (తెలుగు)": {
        "pension": "నమస్కారం. వైఎస్సార్ పెన్షన్ కానుక కింద అర్హులైన వృద్ధులకు ప్రతి నెలా ₹3,000 ఆర్థిక సహాయం అందుతుంది.",
        "farmer": "రైతు భరోసా పథకం ద్వారా రైతులకు పెట్టుబడి సహాయంగా ప్రతి సంవత్సరం నిధులు విడుదల చేయబడతాయి.",
        "general": "నమస్కారం! నేను జన్వాణి AI. మీరు మాట్లాడి మీ పెన్షన్ లేదా రైతు పథకాల వివరాలు తెలుసుకోవచ్చు."
    },
    "English": {
        "pension": "Hello. Under the National Social Assistance Programme, senior citizens receive direct monthly pension credits into their bank accounts.",
        "farmer": "Under PM-KISAN, small and marginal farmers receive ₹6,000 annually in three direct installments.",
        "general": "Hello! I am Janwani AI. Speak to ask about pensions, farmer subsidies, or welfare schemes."
    }
}

# --- 2. VOICE INPUT SIMULATION & TESTING ---
st.write("---")
st.write("### 🎙️ Step 1: Speak to Janwani AI")

# Standard audio recorder widget in Streamlit
audio_file = st.audio_input("Tap the mic to ask a question (e.g., say 'Pension' or 'Kisan')")

# Quick simulation buttons for live jury presentations
st.caption("Or simulate common voice queries:")
col1, col2 = st.columns(2)
query_type = None

if col1.button("👴 'Ask about Pension'"):
    query_type = "pension"
if col2.button("🌾 'Ask about Farmer Subsidy'"):
    query_type = "farmer"

if audio_file is not None or query_type is not None:
    with st.spinner("Processing speech via Bhashini Dialect Engine..."):
        time.sleep(1) # Simulating fast AI processing
        
    selected_query = query_type if query_type else "pension"
    response_text = scheme_database[lang].get(selected_query, scheme_database[lang]["general"])
    
    st.success("✅ Voice query recognized and processed!")
    
    # Display Result Card
    st.markdown(f"""
        <div class="card">
            <span class="status-tag">ACTIVE AI RESPONSE</span>
            <h4 style="margin-top: 10px; color: #2DD4BF;">Welfare Match Found</h4>
            <p style="font-size: 18px; color: #FFFFFF;">{response_text}</p>
        </div>
    """, unsafe_allow_html=True)

# --- 3. DOORSTEP IDENTITY & SCAN SIMULATION ---
st.write("---")
st.write("### 📷 Step 2: Doorstep Liveness & Card Scan")

camera_img = st.camera_input("Take a photo to test on-device verification")

if camera_img:
    st.info("Analyzing facial presence and document boundaries locally...")
    time.sleep(1)
    st.success("✅ Liveness Confirmed: Remote Digital Life Certificate Issued (Zero Travel).")
