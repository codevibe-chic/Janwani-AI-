import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Janwani AI - Smart Prototype",
    page_icon="🎙️",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Hide Streamlit Chrome for Native App Feel
st.markdown("""
<style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .block-container {
        padding: 0 !important;
        max-width: 450px !important;
        margin: auto;
    }
</style>
""", unsafe_allow_html=True)

# Upgraded Interactive Native App Component
smart_app_html = """
<!DOCTYPE html>
<html lang="hi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>Janwani AI Native Experience</title>
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;700;800&family=Noto+Sans+Devanagari:wght@400;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
    <style>
        * { box-sizing: border-box; margin: 0; padding: 0; -webkit-tap-highlight-color: transparent; }
        body {
            background-color: #030712;
            color: #f9fafb;
            font-family: 'Plus Jakarta Sans', 'Noto Sans Devanagari', sans-serif;
            overflow: hidden;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            user-select: none;
        }

        .phone-shell {
            width: 100%;
            max-width: 410px;
            height: 92vh;
            max-height: 840px;
            background: #090d16;
            border-radius: 40px;
            border: 1.5px solid rgba(0, 240, 255, 0.25);
            box-shadow: 0 30px 80px rgba(0, 0, 0, 0.95), 0 0 50px rgba(0, 240, 255, 0.12);
            display: flex;
            flex-direction: column;
            position: relative;
            overflow: hidden;
        }

        /* Top Bar */
        .status-bar {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 14px 24px 8px;
            font-size: 13px;
            color: #64748b;
            font-weight: 600;
        }
        .notch {
            width: 85px;
            height: 16px;
            background: #030712;
            border-radius: 20px;
        }

        /* Live Govt Push SMS Banner */
        .sms-banner {
            position: absolute;
            top: -140px;
            left: 14px;
            right: 14px;
            background: rgba(15, 23, 42, 0.96);
            border: 1px solid #10b981;
            backdrop-filter: blur(20px);
            border-radius: 20px;
            padding: 14px 16px;
            box-shadow: 0 15px 35px rgba(0,0,0,0.85), 0 0 25px rgba(16, 185, 129, 0.35);
            z-index: 2000;
            transition: transform 0.6s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            display: flex;
            gap: 12px;
            align-items: center;
        }
        .sms-banner.show { transform: translateY(155px); }
        .sms-icon {
            width: 40px;
            height: 40px;
            background: #10b981;
            color: #030712;
            border-radius: 12px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 20px;
            flex-shrink: 0;
        }
        .sms-text h5 { font-size: 13px; color: #10b981; font-weight: 800; margin-bottom: 2px; }
        .sms-text p { font-size: 12px; color: #e2e8f0; line-height: 1.3; }

        /* Main Screen Container */
        .screen-content {
            flex: 1;
            padding: 16px 20px;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            position: relative;
            overflow-y: auto;
        }

        /* Pulsating Voice Orb Logo */
        .logo-hub {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            margin: 10px 0;
            text-align: center;
        }
        .orb-ring {
            width: 125px;
            height: 125px;
            border-radius: 50%;
            background: radial-gradient(circle, rgba(0, 240, 255, 0.25) 0%, rgba(14, 165, 233, 0.05) 70%);
            border: 2px solid rgba(0, 240, 255, 0.5);
            display: flex;
            align-items: center;
            justify-content: center;
            position: relative;
            box-shadow: 0 0 35px rgba(0, 240, 255, 0.25);
            transition: all 0.4s ease;
            cursor: pointer;
        }
        .orb-ring.speaking {
            animation: orbPulse 1.2s infinite alternate ease-in-out;
            border-color: #00F0FF;
            box-shadow: 0 0 60px rgba(0, 240, 255, 0.7);
        }
        .orb-icon {
            font-size: 46px;
            color: #00F0FF;
            filter: drop-shadow(0 0 15px rgba(0, 240, 255, 0.9));
        }

        @keyframes orbPulse {
            0% { transform: scale(0.96); box-shadow: 0 0 25px rgba(0, 240, 255, 0.3); }
            100% { transform: scale(1.12); box-shadow: 0 0 65px rgba(0, 240, 255, 0.85); }
        }

        /* Soundwave frequency bars */
        .wave-bars {
            display: flex;
            gap: 5px;
            height: 28px;
            align-items: center;
            margin-top: 14px;
        }
        .bar {
            width: 3.5px;
            background: #00F0FF;
            border-radius: 4px;
            height: 5px;
            transition: height 0.2s ease;
        }
        .speaking .bar {
            animation: bounceBar 0.7s infinite ease-in-out alternate;
        }
        .speaking .bar:nth-child(2) { animation-delay: 0.1s; }
        .speaking .bar:nth-child(3) { animation-delay: 0.25s; }
        .speaking .bar:nth-child(4) { animation-delay: 0.4s; }
        .speaking .bar:nth-child(5) { animation-delay: 0.18s; }
        .speaking .bar:nth-child(6) { animation-delay: 0.32s; }

        @keyframes bounceBar {
            0% { height: 5px; }
            100% { height: 28px; background: #38bdf8; }
        }

        .ai-dialogue {
            margin-top: 14px;
            font-size: 17px;
            font-weight: 700;
            color: #ffffff;
            line-height: 1.4;
            text-align: center;
            padding: 0 8px;
        }
        .ai-badge {
            display: inline-flex;
            align-items: center;
            gap: 6px;
            background: rgba(0, 240, 255, 0.1);
            border: 1px solid rgba(0, 240, 255, 0.3);
            padding: 4px 12px;
            border-radius: 20px;
            font-size: 11px;
            color: #00F0FF;
            margin-top: 8px;
            font-weight: 700;
            letter-spacing: 0.5px;
        }

        /* Keyword Filter Pills Grid */
        .keyword-scroll {
            display: flex;
            gap: 8px;
            overflow-x: auto;
            padding: 8px 0;
            margin-bottom: 10px;
            scrollbar-width: none;
        }
        .keyword-scroll::-webkit-scrollbar { display: none; }
        .pill {
            background: rgba(255, 255, 255, 0.05);
            border: 1px solid rgba(255, 255, 255, 0.12);
            color: #e2e8f0;
            padding: 8px 14px;
            border-radius: 20px;
            font-size: 13px;
            font-weight: 600;
            white-space: nowrap;
            cursor: pointer;
            transition: all 0.2s;
        }
        .pill.active, .pill:hover {
            background: #00F0FF;
            color: #030712;
            border-color: #00F0FF;
            font-weight: 800;
        }

        /* Scheme Cards */
        .scheme-card {
            background: rgba(255, 255, 255, 0.03);
            border: 1px solid rgba(0, 240, 255, 0.25);
            border-radius: 16px;
            padding: 14px;
            margin-bottom: 10px;
            transition: all 0.3s;
            cursor: pointer;
        }
        .scheme-card:hover, .scheme-card.selected {
            border-color: #00F0FF;
            background: rgba(0, 240, 255, 0.08);
            box-shadow: 0 0 20px rgba(0, 240, 255, 0.2);
        }
        .scheme-card h4 { font-size: 15px; color: #00F0FF; margin-bottom: 4px; font-weight: 700; }
        .scheme-card p { font-size: 12px; color: #cbd5e1; line-height: 1.3; }

        /* Form Mockup Box */
        .form-box {
            background: rgba(255, 255, 255, 0.02);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 18px;
            padding: 14px;
        }
        .form-row { margin-bottom: 10px; }
        .form-row label { display: block; font-size: 11px; color: #94a3b8; margin-bottom: 3px; font-weight: 700; }
        .form-input {
            width: 100%;
            background: rgba(0, 0, 0, 0.6);
            border: 1px solid rgba(0, 240, 255, 0.3);
            padding: 8px 12px;
            border-radius: 8px;
            color: #fff;
            font-size: 13px;
            font-weight: 600;
        }

        /* Action Buttons */
        .primary-btn {
            background: #00F0FF;
            color: #030712;
            border: none;
            padding: 14px;
            border-radius: 14px;
            font-size: 15px;
            font-weight: 800;
            cursor: pointer;
            width: 100%;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            box-shadow: 0 0 25px rgba(0, 240, 255, 0.35);
            margin-top: 8px;
        }

        .tap-prompt {
            position: absolute;
            top: 0; left: 0; width: 100%; height: 100%;
            background: rgba(3, 7, 18, 0.85);
            backdrop-filter: blur(8px);
            z-index: 3000;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            text-align: center;
            padding: 30px;
            cursor: pointer;
        }
        .tap-prompt i { font-size: 54px; color: #00F0FF; margin-bottom: 16px; animation: pulseWave 1s infinite alternate; }
        .tap-prompt h3 { font-size: 20px; color: #fff; margin-bottom: 6px; }
        .tap-prompt p { font-size: 13px; color: #94a3b8; }
    </style>
</head>
<body>

<div class="phone-shell" id="phoneContainer">
    
    <!-- Tap Anywhere Start Mask (Browser Autoplay Unlock) -->
    <div class="tap-prompt" id="startMask" onclick="unlockAudioAndStart()">
        <i class="fa-solid fa-fingerprint"></i>
        <h3>स्क्रीन पर कहीं भी टच करें</h3>
        <p>जनवाणी AI वॉइस असिस्टेंट शुरू करने के लिए</p>
    </div>

    <!-- Official Govt Push Notification Banner -->
    <div class="sms-banner" id="govtSms">
        <div class="sms-icon"><i class="fa-solid fa-building-columns"></i></div>
        <div class="sms-text">
            <h5>भारत सरकार / DBT कल्याण पोर्टल</h5>
            <p>आपकी योजना का आवेदन #IN-984210 सफलतापूर्वक दर्ज हो गया है। डायरेक्ट बेनिफिट ट्रांसफर (DBT) स्वीकृत है।</p>
        </div>
    </div>

    <!-- Status Bar -->
    <div class="status-bar">
        <span>09:41</span>
        <div class="notch"></div>
        <span><i class="fa-solid fa-wifi"></i> <i class="fa-solid fa-bolt" style="color:#00F0FF;"></i> 5G</span>
    </div>

    <!-- Screen Viewport -->
    <div class="screen-content" id="screenView">
        
        <!-- Center Logo & Sound Wave Hub -->
        <div class="logo-hub">
            <div class="orb-ring" id="orbVisual" onclick="reSpeakCurrent()">
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

            <div class="ai-dialogue" id="aiDialogue">
                नमस्ते! मैं जनवाणी एआई हूँ।
            </div>
            <div class="ai-badge" id="aiBadge"><i class="fa-solid fa-language"></i> भाषिणी AI वॉइस इंजन सक्रिय</div>
        </div>

        <!-- Dynamic Content Body -->
        <div id="actionArea">
            <!-- Will be dynamically populated via JS -->
        </div>

    </div>

</div>

<script>
    // Clean String Audio Synthesizer (Fixes exclamation & punctuation reading bugs)
    let currentSpeechText = "";

    function cleanTextForSpeech(rawText) {
        return rawText
            .replace(/[#!*\_~`><]/g, '')
            .replace(/[-]/g, ' ')
            .replace(/\s+/g, ' ')
            .trim();
    }

    function speakText(rawText, langCode = 'hi-IN', callback = null) {
        currentSpeechText = rawText;
        if ('speechSynthesis' in window) {
            window.speechSynthesis.cancel();
            const cleanText = cleanTextForSpeech(rawText);
            const utterance = new SpeechSynthesisUtterance(cleanText);
            utterance.lang = langCode;
            utterance.rate = 0.92;
            utterance.pitch = 1.0;
            
            const orb = document.getElementById('orbVisual');
            utterance.onstart = () => { orb.classList.add('speaking'); };
            utterance.onend = () => { 
                orb.classList.remove('speaking');
                if (callback) callback();
            };
            utterance.onerror = () => { orb.classList.remove('speaking'); };

            window.speechSynthesis.speak(utterance);
        }
    }

    function reSpeakCurrent() {
        if(currentSpeechText) speakText(currentSpeechText);
    }

    // Comprehensive Scheme Database for Keyword Matching
    const schemeDatabase = [
        {
            category: "pension",
            name: "👴 इंदिरा गांधी राष्ट्रीय वृद्धावस्था पेंशन",
            desc: "60+ वर्ष के बुजुर्गों को हर महीने सीधे बैंक खाते में ₹1,000 से ₹1,500 की पेंशन सहायता।"
        },
        {
            category: "kisan",
            name: "🌾 पीएम किसान सम्मान निधि योजना",
            desc: "छोटे व सीमांत किसानों को हर साल ₹6,000 की आर्थिक मदद (₹2,000 की 3 किश्तें)।"
        },
        {
            category: "health",
            name: "🏥 आयुष्मान भारत योजना (PM-JAY)",
            desc: "हर परिवार को ₹5 लाख तक का सालाना मुफ्त इलाज और कैशलेस अस्पताल सुविधा।"
        },
        {
            category: "makan",
            name: "🏠 प्रधानमंत्री आवास योजना (ग्रामीण)",
            desc: "पक्का मकान बनाने के लिए ₹1.20 लाख की सीधी सरकारी सब्सिडी राशि।"
        },
        {
            category: "ration",
            name: "🌾 पीएम गरीब कल्याण अन्न योजना",
            desc: "राशन कार्ड धारकों को हर महीने प्रति व्यक्ति 5 किलो मुफ्त अनाज।"
        },
        {
            category: "artisan",
            name: "🔨 पीएम विश्वकर्मा योजना",
            desc: "कारीगरों व शिल्पकारों को ₹3 लाख तक का बिना गारंटी सस्ता कर्ज व आधुनिक टूलकिट।"
        }
    ];

    // Tap Anywhere Unlocks Audio Policy
    function unlockAudioAndStart() {
        document.getElementById('startMask').style.display = 'none';
        goToScreen1();
    }

    // SCREEN 1: First Hindi Voice Prompt
    function goToScreen1() {
        const dialogue = "नमस्ते! मैं जनवाणी एआई हूँ। आपको किस समस्या या मुद्दे पर सरकारी योजना चाहिए?";
        document.getElementById('aiDialogue').innerText = dialogue;
        
        speakText(dialogue);

        document.getElementById('actionArea').innerHTML = `
            <div style="text-align:center; margin-bottom:8px;">
                <p style="font-size:12px; color:#94a3b8;">नीचे अपनी समस्या या मुद्दा चुनें या बोलें:</p>
            </div>
            <div class="keyword-scroll">
                <div class="pill active" onclick="filterSchemes('all')">🌟 सभी योजनाएं</div>
                <div class="pill" onclick="filterSchemes('pension')">👴 बुजुर्ग पेंशन</div>
                <div class="pill" onclick="filterSchemes('kisan')">🌾 किसान सहायता</div>
                <div class="pill" onclick="filterSchemes('health')">🏥 अस्पताल व इलाज</div>
                <div class="pill" onclick="filterSchemes('makan')">🏠 पक्का मकान</div>
                <div class="pill" onclick="filterSchemes('ration')">🌾 मुफ्त राशन</div>
                <div class="pill" onclick="filterSchemes('artisan')">🔨 कारीगर / कर्ज</div>
            </div>
            <div id="schemesList" style="max-height:220px; overflow-y:auto;">
                <!-- Populated dynamically -->
            </div>
        `;

        filterSchemes('all');
    }

    // SCREEN 2: Keyword Filtered Schemes
    function filterSchemes(cat) {
        const container = document.getElementById('schemesList');
        let filtered = schemeDatabase;
        if(cat !== 'all') {
            filtered = schemeDatabase.filter(s => s.category === cat);
        }

        container.innerHTML = filtered.map((s, idx) => `
            <div class="scheme-card" onclick="selectScheme('${s.name}', '${s.desc}')">
                <h4>${s.name}</h4>
                <p>${s.desc}</p>
            </div>
        `).join('');

        if(cat !== 'all') {
            const dialogue = "आपके चुने हुए मुद्दे से जुड़ी सरकारी योजनाएं स्क्रीन पर आ गई हैं। जिस योजना में आवेदन करना है उस पर टैप करें।";
            document.getElementById('aiDialogue').innerText = dialogue;
            speakText(dialogue);
        }
    }

    // SCREEN 3: Scheme Explanation & Voice Registration Prompt
    function selectScheme(name, desc) {
        const dialogue = name + "। " + desc + "। क्या आप इस योजना के लिए फॉर्म भरना चाहते हैं?";
        document.getElementById('aiDialogue').innerText = dialogue;
        
        speakText(dialogue);

        document.getElementById('actionArea').innerHTML = `
            <div class="scheme-card selected">
                <h4>${name}</h4>
                <p>${desc}</p>
                <div style="margin-top:8px; font-size:11px; color:#00F0FF; font-weight:700;">
                    <i class="fa-solid fa-shield-halved"></i> डिजीलॉकर द्वारा तुरंत ऑनलाइन सत्यापन
                </div>
            </div>
            <button class="primary-btn" onclick="goToFormFill()">
                <i class="fa-solid fa-microphone"></i> हाँ, फॉर्म भरें (Voice Form Fill)
            </button>
        `;
    }

    // SCREEN 4: Auto Data Mapping & Live OTP Simulation
    function goToFormFill() {
        const dialogue = "आपका आधार और डिजीलॉकर डेटा जोड़ लिया गया है। फोन पर आया ओटीपी अपने आप भरा जा रहा है।";
        document.getElementById('aiDialogue').innerText = dialogue;
        
        speakText(dialogue);

        document.getElementById('actionArea').innerHTML = `
            <div class="form-box">
                <div class="form-row">
                    <label>लाभार्थी का नाम (DigiLocker)</label>
                    <input class="form-input" value="रामेश्वर ज्ञानोबा पाटिल" readonly>
                </div>
                <div class="form-row">
                    <label>मोबाइल नंबर (Aadhaar Linked)</label>
                    <input class="form-input" value="+91 98450 •••••" readonly>
                </div>
                <div class="form-row">
                    <label>सरकारी OTP (Auto Filling...)</label>
                    <input class="form-input" id="otpField" value="• • • • • •" style="border-color:#00F0FF; color:#00F0FF; font-size:16px; letter-spacing:6px;" readonly>
                </div>
            </div>
        `;

        // OTP Auto fill after 2.2 seconds
        setTimeout(() => {
            document.getElementById('otpField').value = "9 4 1 8 0 2";
            speakText("ओटीपी सत्यापन पूरा हुआ। फॉर्म सरकार को भेजा जा रहा है।");
        }, 2200);

        // Submit & Trigger Govt Push SMS after 4.8 seconds
        setTimeout(() => {
            triggerGovtSubmissionSuccess();
        }, 4800);
    }

    // SCREEN 5: Govt Push Notification + Audio Confirmation
    function triggerGovtSubmissionSuccess() {
        document.getElementById('govtSms').classList.add('show');

        const dialogue = "बधाई हो! आपका आवेदन सफलतापूर्वक जमा हो गया है। सरकार का मैसेज भी आ गया है, जल्द ही पैसे सीधे आपके बैंक खाते में आ जाएंगे।";
        document.getElementById('aiDialogue').innerText = dialogue;
        
        speakText(dialogue);

        document.getElementById('actionArea').innerHTML = `
            <div class="form-box" style="text-align:center; border-color:#10b981; background:rgba(16, 185, 129, 0.05); padding:20px;">
                <i class="fa-solid fa-circle-check" style="font-size:42px; color:#10b981; margin-bottom:8px;"></i>
                <h3 style="color:#10b981; font-size:18px; font-weight:800;">आवेदन स्वीकृत हुआ (DBT Direct)</h3>
                <p style="font-size:12px; color:#cbd5e1; margin-top:4px;">जीरो ट्रैवल • जीरो दलाल • 100% सीधा बैंक ट्रांसफर</p>
            </div>
            <button class="primary-btn" style="background:rgba(255,255,255,0.1); color:#fff; box-shadow:none; margin-top:10px;" onclick="goToScreen1()">
                <i class="fa-solid fa-rotate-right"></i> नया आवेदन करें (Start Again)
            </button>
        `;
    }
</script>

</body>
</html>
"""

components.html(smart_app_html, height=850, scrolling=False)
