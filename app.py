import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Janwani AI - Interactive Demo",
    page_icon="🎙️",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Hide Streamlit default headers for a pure native mobile app feel
st.markdown("""
<style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .block-container {
        padding: 0 !important;
        max-width: 480px !important;
        margin: auto;
    }
</style>
""", unsafe_allow_html=True)

# Complete Cinematic Web-App Simulation with Voice, Animations, Soundwaves, Auto-OTP, and Govt SMS
interactive_app_html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>Janwani AI Native App</title>
    <link href="https://fonts.googleapis.com/css2?family=Urbanist:wght@400;600;700;800&family=Noto+Sans+Devanagari:wght@400;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
    <style>
        * { box-sizing: border-box; margin: 0; padding: 0; -webkit-tap-highlight-color: transparent; }
        body {
            background-color: #030712;
            color: #f9fafb;
            font-family: 'Urbanist', 'Noto Sans Devanagari', sans-serif;
            overflow-x: hidden;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
        }

        .phone-shell {
            width: 100%;
            max-width: 420px;
            height: 90vh;
            max-height: 840px;
            background: #090d16;
            border-radius: 36px;
            border: 2px solid rgba(45, 212, 191, 0.3);
            box-shadow: 0 25px 60px rgba(0, 0, 0, 0.9), 0 0 40px rgba(45, 212, 191, 0.15);
            display: flex;
            flex-direction: column;
            position: relative;
            overflow: hidden;
        }

        /* Top Notch & Status */
        .status-bar {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 12px 24px 8px;
            font-size: 13px;
            color: #94a3b8;
            font-weight: 600;
        }
        .notch {
            width: 90px;
            height: 18px;
            background: #030712;
            border-radius: 20px;
        }

        /* Government Notification Banner */
        .sms-banner {
            position: absolute;
            top: -120px;
            left: 16px;
            right: 16px;
            background: rgba(15, 23, 42, 0.95);
            border: 1px solid #10b981;
            backdrop-filter: blur(15px);
            border-radius: 18px;
            padding: 14px 16px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.8), 0 0 20px rgba(16, 185, 129, 0.3);
            z-index: 1000;
            transition: transform 0.6s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            display: flex;
            gap: 12px;
            align-items: center;
        }
        .sms-banner.show {
            transform: translateY(135px);
        }
        .sms-icon {
            width: 38px;
            height: 38px;
            background: #10b981;
            color: #000;
            border-radius: 10px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 20px;
            flex-shrink: 0;
        }
        .sms-text h5 { font-size: 14px; color: #10b981; font-weight: 700; margin-bottom: 2px; }
        .sms-text p { font-size: 12px; color: #e2e8f0; line-height: 1.3; }

        /* Main Screen Container */
        .screen-content {
            flex: 1;
            padding: 20px 24px;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            position: relative;
        }

        /* Animated Mic / Sound Logo */
        .logo-hub {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            margin: auto 0;
            text-align: center;
        }
        .orb-ring {
            width: 140px;
            height: 140px;
            border-radius: 50%;
            background: radial-gradient(circle, rgba(45, 212, 191, 0.2) 0%, rgba(14, 165, 233, 0.05) 70%);
            border: 2px solid rgba(45, 212, 191, 0.4);
            display: flex;
            align-items: center;
            justify-content: center;
            position: relative;
            box-shadow: 0 0 35px rgba(45, 212, 191, 0.3);
            transition: all 0.4s ease;
        }
        .orb-ring.speaking {
            animation: pulseWave 1.4s infinite alternate;
            border-color: #2dd4bf;
            box-shadow: 0 0 50px rgba(45, 212, 191, 0.6);
        }
        .orb-icon {
            font-size: 52px;
            color: #2dd4bf;
            filter: drop-shadow(0 0 15px rgba(45, 212, 191, 0.8));
        }

        @keyframes pulseWave {
            0% { transform: scale(0.95); box-shadow: 0 0 20px rgba(45, 212, 191, 0.2); }
            100% { transform: scale(1.1); box-shadow: 0 0 55px rgba(45, 212, 191, 0.7); }
        }

        /* Sound Wave Visualizer Bars */
        .wave-bars {
            display: flex;
            gap: 6px;
            height: 35px;
            align-items: center;
            margin-top: 20px;
        }
        .bar {
            width: 4px;
            background: #2dd4bf;
            border-radius: 4px;
            height: 6px;
            transition: height 0.2s ease;
        }
        .speaking .bar {
            animation: bounceBar 0.8s infinite ease-in-out alternate;
        }
        .speaking .bar:nth-child(2) { animation-delay: 0.15s; }
        .speaking .bar:nth-child(3) { animation-delay: 0.3s; }
        .speaking .bar:nth-child(4) { animation-delay: 0.45s; }
        .speaking .bar:nth-child(5) { animation-delay: 0.2s; }
        .speaking .bar:nth-child(6) { animation-delay: 0.35s; }

        @keyframes bounceBar {
            0% { height: 6px; }
            100% { height: 32px; background: #38bdf8; }
        }

        .ai-subtitle {
            margin-top: 20px;
            font-size: 19px;
            font-weight: 600;
            color: #ffffff;
            min-height: 55px;
            line-height: 1.4;
            text-align: center;
            padding: 0 10px;
        }
        .ai-sub-caption {
            font-size: 13px;
            color: #64748b;
            margin-top: 4px;
        }

        /* Buttons & Options Grid */
        .options-grid {
            display: flex;
            flex-direction: column;
            gap: 12px;
            width: 100%;
            margin-top: 10px;
        }
        .opt-btn {
            background: rgba(255, 255, 255, 0.04);
            border: 1px solid rgba(255, 255, 255, 0.12);
            color: #ffffff;
            padding: 16px 18px;
            border-radius: 16px;
            font-size: 16px;
            font-weight: 700;
            display: flex;
            align-items: center;
            justify-content: space-between;
            cursor: pointer;
            transition: all 0.3s;
        }
        .opt-btn:hover, .opt-btn:active {
            background: rgba(45, 212, 191, 0.15);
            border-color: #2dd4bf;
            transform: scale(1.02);
        }
        .opt-btn i { color: #2dd4bf; font-size: 18px; }

        /* Scheme Cards Layout */
        .scheme-card {
            background: rgba(255, 255, 255, 0.03);
            border: 1px solid rgba(45, 212, 191, 0.2);
            border-radius: 18px;
            padding: 15px;
            margin-bottom: 12px;
            transition: all 0.3s;
            cursor: pointer;
        }
        .scheme-card.active-scheme {
            border-color: #2dd4bf;
            background: rgba(45, 212, 191, 0.08);
            box-shadow: 0 0 20px rgba(45, 212, 191, 0.2);
        }
        .scheme-card h4 { font-size: 16px; color: #2dd4bf; margin-bottom: 4px; }
        .scheme-card p { font-size: 13px; color: #cbd5e1; line-height: 1.3; }

        /* Form Fill Mockup */
        .form-box {
            background: rgba(255, 255, 255, 0.03);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 18px;
            padding: 18px;
        }
        .form-row {
            margin-bottom: 12px;
        }
        .form-row label {
            display: block;
            font-size: 12px;
            color: #94a3b8;
            margin-bottom: 4px;
            text-transform: uppercase;
            letter-spacing: 1px;
        }
        .form-input {
            width: 100%;
            background: rgba(0, 0, 0, 0.5);
            border: 1px solid rgba(45, 212, 191, 0.3);
            padding: 10px 14px;
            border-radius: 10px;
            color: #fff;
            font-size: 14px;
            font-weight: 600;
        }

        .digilocker-badge {
            display: inline-flex;
            align-items: center;
            gap: 6px;
            background: rgba(56, 189, 248, 0.15);
            border: 1px solid #38bdf8;
            padding: 4px 10px;
            border-radius: 20px;
            font-size: 11px;
            color: #38bdf8;
            margin-top: 8px;
            font-weight: 700;
        }

        .pulse-btn {
            background: #2dd4bf;
            color: #030712;
            border: none;
            padding: 16px;
            border-radius: 16px;
            font-size: 16px;
            font-weight: 800;
            cursor: pointer;
            width: 100%;
            text-transform: uppercase;
            letter-spacing: 1px;
            box-shadow: 0 0 25px rgba(45, 212, 191, 0.4);
            margin-top: 10px;
        }
    </style>
</head>
<body>

<div class="phone-shell" id="phoneContainer">
    
    <!-- Top Government Notification Bar (Simulated) -->
    <div class="sms-banner" id="govtSms">
        <div class="sms-icon"><i class="fa-solid fa-building-columns"></i></div>
        <div class="sms-text">
            <h5>GOVT OF MAHARASHTRA / DBT</h5>
            <p>संजय गांधी निराधार योजना अर्ज क्र. #MH-9842 यशस्वीरीत्या नोंदवला गेला आहे. बँक खात्याची पडताळणी पूर्ण झाली आहे.</p>
        </div>
    </div>

    <!-- Status Bar -->
    <div class="status-bar">
        <span>09:41</span>
        <div class="notch"></div>
        <span><i class="fa-solid fa-wifi"></i> <i class="fa-solid fa-bolt" style="color:#2dd4bf;"></i> 5G</span>
    </div>

    <!-- Interactive Screen Viewport -->
    <div class="screen-content" id="screenView">
        
        <!-- Center Logo & Sound Wave Hub -->
        <div class="logo-hub">
            <div class="orb-ring" id="orbVisual">
                <i class="fa-solid fa-microphone-lines orb-icon"></i>
            </div>
            
            <div class="wave-bars">
                <div class="bar"></div>
                <div class="bar"></div>
                <div class="bar"></div>
                <div class="bar"></div>
                <div class="bar"></div>
                <div class="bar"></div>
            </div>

            <div class="ai-subtitle" id="aiDialogue">
                नमस्ते! मी जनवाणी एआय आहे.<br>तुम्ही माझ्याशी कोणत्या भाषेत बोलू इच्छिता?
            </div>
            <div class="ai-sub-caption" id="aiSub">Bhashini Multilingual Speech Core Active</div>
        </div>

        <!-- Dynamic Controls Viewport -->
        <div id="actionArea">
            <div class="options-grid" id="langOptions">
                <button class="opt-btn" onclick="startAppSequence('mr')">
                    <span><i class="fa-solid fa-volume-high" style="margin-right:10px;"></i> मराठी (Marathi)</span>
                    <i class="fa-solid fa-chevron-right"></i>
                </button>
                <button class="opt-btn" onclick="startAppSequence('hi')">
                    <span><i class="fa-solid fa-volume-high" style="margin-right:10px;"></i> हिन्दी (Hindi)</span>
                    <i class="fa-solid fa-chevron-right"></i>
                </button>
                <button class="opt-btn" onclick="startAppSequence('en')">
                    <span><i class="fa-solid fa-volume-high" style="margin-right:10px;"></i> English</span>
                    <i class="fa-solid fa-chevron-right"></i>
                </button>
            </div>
        </div>

    </div>

</div>

<script>
    // Audio Synthetic Engine (Speaks in Marathi/Hindi/English)
    function speakText(text, langCode = 'mr-IN') {
        if ('speechSynthesis' in window) {
            window.speechSynthesis.cancel();
            const utterance = new SpeechSynthesisUtterance(text);
            utterance.lang = langCode;
            utterance.rate = 0.95;
            
            const orb = document.getElementById('orbVisual');
            utterance.onstart = () => { orb.classList.add('speaking'); };
            utterance.onend = () => { orb.classList.remove('speaking'); };
            utterance.onerror = () => { orb.classList.remove('speaking'); };

            window.speechSynthesis.speak(utterance);
        }
    }

    // Trigger Initial Welcome Greeting on Load/First Tap
    window.addEventListener('load', () => {
        setTimeout(() => {
            speakText("नमस्ते! आप किस भाषा में मुझसे बात करना चाहेंगे?", "hi-IN");
        }, 600);
    });

    // STEP 1: User Chooses Marathi / Regional Language
    function startAppSequence(lang) {
        const aiDialogue = document.getElementById('aiDialogue');
        const actionArea = document.getElementById('actionArea');
        
        aiDialogue.innerHTML = "नमस्कार! मी जनवाणी एआय.<br>तुम्हाला कोणत्या योजनेबद्दल माहिती हवी आहे?";
        speakText("नमस्कार! मी जनवाणी एआय. तुम्हाला कोणत्या योजनेबद्दल माहिती हवी आहे? जसे की पेन्शन किंवा शेतकरी योजना.", "mr-IN");

        actionArea.innerHTML = `
            <div class="options-grid">
                <button class="opt-btn" onclick="openSchemesView('pension')">
                    <span><i class="fa-solid fa-hands-holding-child" style="margin-right:8px;"></i> मला पेन्शन हवी आहे (Senior Pension)</span>
                    <i class="fa-solid fa-chevron-right"></i>
                </button>
                <button class="opt-btn" onclick="openSchemesView('farmer')">
                    <span><i class="fa-solid fa-wheat-awn" style="margin-right:8px;"></i> शेतकरी योजना (Farmer Subsidy)</span>
                    <i class="fa-solid fa-chevron-right"></i>
                </button>
            </div>
        `;
    }

    // STEP 2: Show Schemes & Explain Benefits Verbally
    function openSchemesView(type) {
        const aiDialogue = document.getElementById('aiDialogue');
        const actionArea = document.getElementById('actionArea');

        aiDialogue.innerHTML = "ज्येष्ठ नागरिकांसाठी संजय गांधी निराधार योजना उपलब्ध आहे. दरमहा ₹१,५०० थेट खात्यात मिळतील.";
        speakText("ज्येष्ठ नागरिकांसाठी संजय गांधी निराधार योजना उपलब्ध आहे. या योजनेत दरमहा १५०० रुपये थेट बँक खात्यात मिळतील. तुम्हाला या योजनेसाठी अर्ज करायचा आहे का?", "mr-IN");

        actionArea.innerHTML = `
            <div class="scheme-card active-scheme">
                <h4>📜 संजय गांधी निराधार पेन्शन योजना</h4>
                <p><strong>फायदा:</strong> दरमहा ₹1,500 थेट DBT द्वारे खात्यात जमा. वयोमर्यादा: 65+ वर्षे.</p>
                <div class="digilocker-badge"><i class="fa-solid fa-shield-halved"></i> DigiLocker द्वारे थेट पडताळणी</div>
            </div>
            <button class="pulse-btn" onclick="startVoiceFormFill()">
                <i class="fa-solid fa-microphone"></i> होय, अर्ज भरा (Voice Enroll)
            </button>
        `;
    }

    // STEP 3: Automated Voice Form Filling & Auto OTP Simulation
    function startVoiceFormFill() {
        const aiDialogue = document.getElementById('aiDialogue');
        const actionArea = document.getElementById('actionArea');

        aiDialogue.innerHTML = "तुमचा आधार आणि डिजीलॉकर जोडले आहे. फोनवर आलेला OTP आपोआप भरला जात आहे...";
        speakText("तुमचा आधार आणि डिजीलॉकर जोडले आहे. फोनवर आलेला ओटीपी आपोआप भरला जात आहे. कृपया थांबा.", "mr-IN");

        actionArea.innerHTML = `
            <div class="form-box">
                <div class="form-row">
                    <label>लाभार्थ्याचे नाव (Name)</label>
                    <input class="form-input" value="आनंदीबाई ज्ञानोबा कांबळे" readonly>
                </div>
                <div class="form-row">
                    <label>मोबाईल क्रमांक (Mobile)</label>
                    <input class="form-input" value="+91 98450 •••••" readonly>
                </div>
                <div class="form-row">
                    <label>शासकीय OTP (Auto-Filling)</label>
                    <input class="form-input" id="otpField" value="•• •• ••" style="border-color:#2dd4bf; color:#2dd4bf; letter-spacing:4px;" readonly>
                </div>
                <div class="digilocker-badge"><i class="fa-solid fa-circle-check"></i> डिजिटल लाइफ सर्टिफिकेट जोडले गेले</div>
            </div>
        `;

        // Simulate Live OTP Arrival after 2.5 seconds
        setTimeout(() => {
            document.getElementById('otpField').value = "8 4 9 2 0 1";
            speakText("ओटीपी पडताळणी पूर्ण झाली. अर्ज सरकारकडे सादर केला जात आहे.", "mr-IN");
        }, 2200);

        // Submit & Trigger Government Notification after 5 seconds
        setTimeout(() => {
            triggerGovtSubmissionSuccess();
        }, 4800);
    }

    // STEP 4: Govt SMS Pop-up + Voice Confirmation of Direct Benefit Transfer
    function triggerGovtSubmissionSuccess() {
        const govtSms = document.getElementById('govtSms');
        const aiDialogue = document.getElementById('aiDialogue');
        const actionArea = document.getElementById('actionArea');

        // Show Slide-down Official Govt SMS
        govtSms.classList.add('show');

        aiDialogue.innerHTML = "अभिनंदन! तुमचा अर्ज जमा झाला आहे. शासनाचा संदेश आला आहे, लवकरच पैसे खात्यात येतील.";
        speakText("अभिनंदन! तुमचा अर्ज यशस्वीरीत्या जमा झाला आहे. सरकारकडून मेसेज आला आहे, लवकरच पैसे थेट तुमच्या बँक खात्यात जमा होतील. तुम्हाला कोणाकडेही जाण्याची गरज नाही.", "mr-IN");

        actionArea.innerHTML = `
            <div class="form-box" style="text-align:center; border-color:#10b981; background:rgba(16, 185, 129, 0.05);">
                <i class="fa-solid fa-circle-check" style="font-size:48px; color:#10b981; margin-bottom:10px;"></i>
                <h3 style="color:#10b981; font-size:20px; font-weight:800;">अर्ज मंजूर झाला (DBT Active)</h3>
                <p style="font-size:13px; color:#cbd5e1; margin-top:8px;">Zero Travel • Zero Middlemen • 100% Direct Transfer</p>
            </div>
            <button class="opt-btn" style="justify-content:center; margin-top:12px;" onclick="location.reload()">
                <i class="fa-solid fa-rotate-right" style="margin-right:8px;"></i> पुन्हा नवीन अर्ज करा (Restart)
            </button>
        `;
    }
</script>

</body>
</html>
"""

components.html(interactive_app_html, height=860, scrolling=False)
