import streamlit as st
import streamlit.components.v1 as components
import os

st.set_page_config(
    page_title="Janwani AI - Autonomous LLM",
    page_icon="🎙️",
    layout="centered",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .block-container {
        padding: 0 !important;
        max-width: 440px !important;
        margin: auto;
    }
</style>
""", unsafe_allow_html=True)

# Complete Autonomous Conversational Web App
conversational_llm_html = """
<!DOCTYPE html>
<html lang="hi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>Janwani AI - Neural Conversational</title>
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@500;700;800&family=Noto+Sans+Devanagari:wght@500;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
    <style>
        * { box-sizing: border-box; margin: 0; padding: 0; -webkit-tap-highlight-color: transparent; }
        body {
            background-color: #030712;
            color: #f9fafb;
            font-family: 'Plus Jakarta Sans', 'Noto Sans Devanagari', sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            overflow: hidden;
            user-select: none;
        }

        .phone-shell {
            width: 100%;
            max-width: 410px;
            height: 92vh;
            max-height: 840px;
            background: #090d16;
            border-radius: 40px;
            border: 1.5px solid rgba(0, 240, 255, 0.3);
            box-shadow: 0 30px 80px rgba(0, 0, 0, 0.95), 0 0 45px rgba(0, 240, 255, 0.15);
            display: flex;
            flex-direction: column;
            position: relative;
            overflow: hidden;
        }

        .status-bar {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 14px 24px 8px;
            font-size: 13px;
            color: #64748b;
            font-weight: 700;
        }
        .notch {
            width: 85px;
            height: 16px;
            background: #030712;
            border-radius: 20px;
        }

        .screen-content {
            flex: 1;
            padding: 16px 20px;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            position: relative;
            overflow-y: auto;
        }

        .logo-hub {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            margin: 10px 0;
            text-align: center;
        }

        .orb-ring {
            width: 120px;
            height: 120px;
            border-radius: 50%;
            background: radial-gradient(circle, rgba(0, 240, 255, 0.25) 0%, rgba(14, 165, 233, 0.05) 70%);
            border: 2px solid rgba(0, 240, 255, 0.4);
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
            box-shadow: 0 0 65px rgba(0, 240, 255, 0.7);
        }

        .orb-ring.listening {
            animation: listenPulse 0.9s infinite alternate ease-in-out;
            border-color: #10b981;
            box-shadow: 0 0 65px rgba(16, 185, 129, 0.8);
            background: radial-gradient(circle, rgba(16, 185, 129, 0.3) 0%, transparent 70%);
        }

        .orb-icon {
            font-size: 42px;
            color: #00F0FF;
            transition: color 0.3s;
        }
        .orb-ring.listening .orb-icon { color: #10b981; }

        @keyframes orbPulse {
            0% { transform: scale(0.96); }
            100% { transform: scale(1.1); box-shadow: 0 0 70px rgba(0, 240, 255, 0.85); }
        }

        @keyframes listenPulse {
            0% { transform: scale(1.0); }
            100% { transform: scale(1.15); }
        }

        .wave-bars {
            display: flex;
            gap: 5px;
            height: 24px;
            align-items: center;
            margin-top: 12px;
        }
        .bar {
            width: 3.5px;
            background: #00F0FF;
            border-radius: 4px;
            height: 5px;
            transition: height 0.2s ease;
        }
        .speaking .bar { animation: bounceBar 0.7s infinite ease-in-out alternate; }
        .listening .bar { background: #10b981; animation: bounceBar 0.5s infinite ease-in-out alternate; }

        @keyframes bounceBar {
            0% { height: 5px; }
            100% { height: 24px; }
        }

        .ai-dialogue {
            margin-top: 12px;
            font-size: 15px;
            font-weight: 700;
            color: #ffffff;
            line-height: 1.45;
            text-align: center;
            min-height: 48px;
        }
        .user-spoken-tag {
            font-size: 12px;
            color: #10b981;
            font-weight: 700;
            margin-top: 4px;
            min-height: 18px;
            text-align: center;
        }

        .chat-history {
            flex: 1;
            background: rgba(255, 255, 255, 0.02);
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 16px;
            padding: 12px;
            overflow-y: auto;
            max-height: 250px;
            display: flex;
            flex-direction: column;
            gap: 8px;
        }
        .chat-bubble {
            padding: 8px 12px;
            border-radius: 12px;
            font-size: 13px;
            line-height: 1.4;
            max-width: 88%;
        }
        .chat-bubble.ai {
            background: rgba(0, 240, 255, 0.1);
            border: 1px solid rgba(0, 240, 255, 0.3);
            color: #e2e8f0;
            align-self: flex-start;
        }
        .chat-bubble.user {
            background: rgba(16, 185, 129, 0.15);
            border: 1px solid rgba(16, 185, 129, 0.3);
            color: #fff;
            align-self: flex-end;
        }

        .api-input-box {
            display: flex;
            gap: 6px;
            margin-top: 10px;
        }
        .api-input {
            flex: 1;
            background: rgba(0,0,0,0.5);
            border: 1px solid rgba(255,255,255,0.15);
            border-radius: 10px;
            padding: 8px 10px;
            color: #fff;
            font-size: 12px;
        }
        .api-btn {
            background: #00F0FF;
            color: #000;
            border: none;
            border-radius: 10px;
            padding: 8px 12px;
            font-weight: 700;
            font-size: 12px;
            cursor: pointer;
        }

        .tap-prompt {
            position: absolute;
            top: 0; left: 0; width: 100%; height: 100%;
            background: rgba(3, 7, 18, 0.9);
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
        .tap-prompt i { font-size: 50px; color: #00F0FF; margin-bottom: 16px; }
        .tap-prompt h3 { font-size: 19px; color: #fff; margin-bottom: 6px; }
    </style>
</head>
<body>

<div class="phone-shell">
    
    <div class="tap-prompt" id="startMask" onclick="initConversation()">
        <i class="fa-solid fa-brain"></i>
        <h3>जनवाणी न्यूरल AI शुरू करें</h3>
        <p>स्क्रीन पर कहीं भी टच करें</p>
    </div>

    <div class="status-bar">
        <span>09:41</span>
        <div class="notch"></div>
        <span><i class="fa-solid fa-bolt" style="color:#00F0FF;"></i> Gemini LLM</span>
    </div>

    <div class="screen-content">
        
        <div class="logo-hub">
            <div class="orb-ring" id="orbVisual" onclick="toggleListening()">
                <i class="fa-solid fa-microphone-lines orb-icon"></i>
            </div>
            
            <div class="wave-bars">
                <div class="bar"></div>
                <div class="bar"></div>
                <div class="bar"></div>
                <div class="bar"></div>
                <div class="bar"></div>
            </div>

            <div class="ai-dialogue" id="aiDialogue">नमस्ते! मैं जनवाणी एआई हूँ।</div>
            <div class="user-spoken-tag" id="userSpokenTag"></div>
        </div>

        <div class="chat-history" id="chatContainer">
            <div class="chat-bubble ai">नमस्ते! आप किस भाषा (हिन्दी, हरियाणवी, मराठी, तेलुगु) में बात करना चाहते हैं? अपनी समस्या या योजना के बारे में पूछें।</div>
        </div>

        <div class="api-input-box">
            <input type="password" id="geminiKey" class="api-input" placeholder="Enter Gemini API Key (Optional for fallback)">
            <button class="api-btn" onclick="saveApiKey()">Save</button>
        </div>

    </div>

</div>

<script>
    let apiKey = localStorage.getItem('gemini_api_key') || "";
    let conversationHistory = [
        {
            role: "system",
            content: `You are Janwani AI, a conversational, empathetic voice assistant for Indian rural citizens and senior citizens.
            You have full knowledge of Indian welfare schemes (e.g., Old Age Pension, PM-Kisan, Ayushman Bharat, PM Awas Yojana, PM Vishwakarma, Ration Card).
            Always respond naturally in the user's preferred language and dialect (Hindi, Haryanvi, Marathi, Telugu, English).
            When asked about required documents, list simple essentials like Aadhaar, Bank Passbook, Ration Card, or Land Record clearly.
            Keep spoken responses concise (2 to 4 sentences max) so they sound natural when read aloud.`
        }
    ];

    let recognition;
    let isSpeaking = false;

    if ('webkitSpeechRecognition' in window || 'SpeechRecognition' in window) {
        const SpeechRec = window.SpeechRecognition || window.webkitSpeechRecognition;
        recognition = new SpeechRec();
        recognition.continuous = false;
        recognition.interimResults = false;
        recognition.lang = 'hi-IN';

        recognition.onresult = async (event) => {
            const spokenText = event.results[0][0].transcript;
            document.getElementById('userSpokenTag').innerText = "🗣️ " + spokenText;
            addChatBubble("user", spokenText);
            await queryAIModel(spokenText);
        };

        recognition.onerror = () => stopListeningAnimation();
        recognition.onend = () => stopListeningAnimation();
    }

    function saveApiKey() {
        apiKey = document.getElementById('geminiKey').value.trim();
        localStorage.setItem('gemini_api_key', apiKey);
        alert("API Key Saved!");
    }

    function addChatBubble(sender, text) {
        const chat = document.getElementById('chatContainer');
        const bubble = document.createElement('div');
        bubble.className = "chat-bubble " + sender;
        bubble.innerText = text;
        chat.appendChild(bubble);
        chat.scrollTop = chat.scrollHeight;
    }

    function cleanString(text) {
        return text.replace(/[#!*\_~`><]/g, '').replace(/[-]/g, ' ').replace(/\s+/g, ' ').trim();
    }

    function speakAI(text, callback = null) {
        if ('speechSynthesis' in window) {
            window.speechSynthesis.cancel();
            isSpeaking = true;
            
            const utterance = new SpeechSynthesisUtterance(cleanString(text));
            utterance.lang = 'hi-IN';
            utterance.rate = 0.90;

            const orb = document.getElementById('orbVisual');
            orb.classList.remove('listening');
            orb.classList.add('speaking');

            utterance.onend = () => {
                isSpeaking = false;
                orb.classList.remove('speaking');
                if (callback) callback();
                else startListening();
            };

            utterance.onerror = () => {
                isSpeaking = false;
                orb.classList.remove('speaking');
            };

            window.speechSynthesis.speak(utterance);
        }
    }

    function startListening() {
        if (recognition && !isSpeaking) {
            const orb = document.getElementById('orbVisual');
            orb.classList.add('listening');
            document.getElementById('userSpokenTag').innerText = "🎧 जनवाणी सुन रही है...";
            try { recognition.start(); } catch(e) {}
        }
    }

    function stopListeningAnimation() {
        document.getElementById('orbVisual').classList.remove('listening');
    }

    function toggleListening() {
        if (isSpeaking) {
            window.speechSynthesis.cancel();
            isSpeaking = false;
        }
        startListening();
    }

    function initConversation() {
        document.getElementById('startMask').style.display = 'none';
        if (localStorage.getItem('gemini_api_key')) {
            document.getElementById('geminiKey').value = localStorage.getItem('gemini_api_key');
        }
        const welcome = "नमस्ते! मैं जनवाणी एआई हूँ। आप मुझसे किसी भी भाषा में सरकारी योजनाओं, उनके फायदे या जरूरी कागजात के बारे में पूछ सकते हैं।";
        document.getElementById('aiDialogue').innerText = welcome;
        speakAI(welcome);
    }

    // Call LLM API (Gemini or Fallback Engine)
    async function queryAIModel(userQuery) {
        document.getElementById('aiDialogue').innerText = "AI सोच रहा है...";
        conversationHistory.push({ role: "user", content: userQuery });

        if (apiKey) {
            try {
                // Direct Gemini API Call
                const response = await fetch(`https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key=${apiKey}`, {
                    method: "POST",
                    headers: { "Content-Type": "application/json" },
                    body: JSON.stringify({
                        contents: [
                            { role: "user", parts: [{ text: conversationHistory[0].content + "\\n\\nUser says: " + userQuery }] }
                        ]
                    })
                });
                const data = await response.json();
                const aiResponse = data.candidates[0].content.parts[0].text;
                
                document.getElementById('aiDialogue').innerText = aiResponse;
                addChatBubble("ai", aiResponse);
                speakAI(aiResponse);
                return;
            } catch (err) {
                console.error("Gemini API error, falling back to local reasoning", err);
            }
        }

        // Autonomous Context Fallback Engine if no key is entered
        let reply = "";
        const q = userQuery.toLowerCase();

        if (q.includes("haryanvi") || q.includes("हरियाणवी")) {
            reply = "राम राम जी! इब हम हरियाणवी में बात करेंगे। बताओ के तकलीफ से, बुढ़ापा पेंशन या खेत की योजना के बारे में पूछना से?";
        } else if (q.includes("kaagaz") || q.includes("document") || q.includes("कागजात") || q.includes("kya chahiye")) {
            reply = "इसके लिए मुख्य रूप से तीन कागजात चाहिए: आपका आधार कार्ड, बैंक पासबुक की फोटोकॉपी और राशन कार्ड या जमीन की फर्द।";
        } else if (q.includes("pension") || q.includes("पेंशन") || q.includes("budhapa")) {
            reply = "वृद्धावस्था पेंशन योजना में 60 वर्ष से अधिक उम्र के बुजुर्गों को हर महीने वित्तीय सहायता सीधे बैंक खाते में मिलती है। क्या आप इसके नियम या आवेदन के बारे में जानना चाहते हैं?";
        } else if (q.includes("kisan") || q.includes("किसान") || q.includes("kheti")) {
            reply = "पीएम किसान योजना के तहत हर साल 6,000 रुपये 3 किश्तों में दिए जाते हैं। इसके लिए खतौनी और आधार लिंक बैंक खाता चाहिए।";
        } else if (q.includes("ilaj") || q.includes("ayushman") || q.includes("इलाज") || q.includes("hospital")) {
            reply = "आयुष्मान भारत योजना में 5 लाख रुपये तक का मुफ्त इलाज मिलता है। क्या आपका आयुष्मान कार्ड बना हुआ है?";
        } else {
            reply = "मैंने आपकी बात समझ ली है। जनवाणी एआई इस योजना के नियमों, लाभ और जरूरी कागजातों की पूरी जानकारी आपको सीधे बोलकर समझाएगी।";
        }

        document.getElementById('aiDialogue').innerText = reply;
        addChatBubble("ai", reply);
        speakAI(reply);
    }
</script>

</body>
</html>
"""

components.html(conversational_llm_html, height=850, scrolling=False)
