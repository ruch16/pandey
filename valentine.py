import streamlit as st
import streamlit.components.v1 as components

# Page configuration
st.set_page_config(
    page_title="💌 A Special Question",
    page_icon="💕",
    layout="centered"
)

# ============================================
# CUSTOMIZABLE CONTENT - EDIT THESE!
# ============================================

# Change this password!
SECRET_PASSWORD = "MeNu1316"

LETTER_CONTENT = {
    "greeting": "My Duduuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu 💕",
    "message": """
    Ever since, i met you, i seem to have fallen
    deeply in love with you. So much so that i cant even breathe
    but you r not with me. I never thought my lil crush on you will
    grow so much, though we r in a relationship i seem to fall in love with u 
    daily. not just ur face, but ur sweetness, ur cuteness, ur kindness,
    the way your eyes sparkle in the sun, the way u look mrng mrng, or the way u act only around me.
    i cant wait to be with you my lovee
    
    So, on this special day, I have one very important question to ask you...
    
    Will you be my Valentine? 💖
    """,
    "signature": "With all my heart and pussy, your bubu💖"
}

SUCCESS_MESSAGE = {
    "title": "YES! 🎉💕",
    "message": """
   You just made me even more happy! i m the happiest person in this worldddddd 
    
    I promise to make this Valentine's Day (and every day after) 
    absolutely special for you. 
    
    Get ready for an amazing time together! 💖
    
    I can't wait to celebrate with you! 🌹
    """
}

# ============================================
# DO NOT EDIT BELOW THIS LINE
# ============================================

# Custom CSS
st.markdown("""
<style>
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Background */
    .stApp {
        background: linear-gradient(135deg, #ffeef8 0%, #ffe0f0 100%);
    }
    
    /* Letter */
    .letter {
        max-width: 600px;
        margin: 50px auto;
        padding: 40px;
        background: white;
        border: 2px solid #ff69b4;
        border-radius: 15px;
        box-shadow: 0 15px 50px rgba(255, 105, 180, 0.3);
        font-family: 'Georgia', serif;
        line-height: 1.8;
        animation: fadeIn 1s ease-in;
    }
    
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    .letter h2 {
        color: #ff1493;
        text-align: center;
        margin-bottom: 30px;
        font-size: 2.2em;
    }
    
    .letter p {
        color: #333;
        font-size: 1.2em;
        margin-bottom: 20px;
        white-space: pre-line;
    }
    
    /* Success message */
    .success-message {
        text-align: center;
        padding: 50px 20px;
        animation: fadeIn 1s ease-in;
    }
    
    .success-message h1 {
        font-size: 3em;
        color: #ff1493;
        margin-bottom: 30px;
        font-family: 'Georgia', serif;
    }
    
    .success-message p {
        font-size: 1.5em;
        color: #333;
        line-height: 1.8;
        font-family: 'Georgia', serif;
        white-space: pre-line;
    }
    
    /* Floating hearts */
    @keyframes float {
        0%, 100% { transform: translateY(0px) rotate(0deg); }
        50% { transform: translateY(-20px) rotate(10deg); }
    }
    .floating-heart {
        position: fixed;
        font-size: 2em;
        animation: float 3s ease-in-out infinite;
        opacity: 0.6;
        z-index: -1;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False
if 'curtains_open' not in st.session_state:
    st.session_state.curtains_open = False
if 'envelope_opened' not in st.session_state:
    st.session_state.envelope_opened = False
if 'answer' not in st.session_state:
    st.session_state.answer = None
if 'no_clicks' not in st.session_state:
    st.session_state.no_clicks = 0

# ============================================
# PASSWORD SCREEN
# ============================================
if not st.session_state.authenticated:
    st.markdown("<br><br><br>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; color: #ff1493;'>💕 Enter Secret Code 💕</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #666; font-size: 1.2em;'>This is a private invitation just for you!</p>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        password = st.text_input("Secret Code:", type="password", key="auth_password")
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("✨ Enter ✨", type="primary", use_container_width=True, key="enter_btn"):
            if password == SECRET_PASSWORD:
                st.session_state.authenticated = True
                st.rerun()
            else:
                st.error("❌ Wrong code! Try again 💔")
    
    # Add floating hearts
    st.markdown("""
    <div class="floating-heart" style="top: 10%; left: 10%; animation-delay: 0s;">💕</div>
    <div class="floating-heart" style="top: 20%; right: 15%; animation-delay: 1s;">💖</div>
    <div class="floating-heart" style="bottom: 15%; left: 20%; animation-delay: 2s;">💗</div>
    <div class="floating-heart" style="bottom: 25%; right: 10%; animation-delay: 1.5s;">💝</div>
    """, unsafe_allow_html=True)

# ============================================
# CURTAINS SCREEN
# ============================================
elif not st.session_state.curtains_open:
    components.html("""
    <!DOCTYPE html>
    <html>
    <head>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        body {
            overflow: hidden;
            height: 100vh;
            font-family: 'Georgia', serif;
        }
        .curtain-container {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100vh;
            cursor: pointer;
        }
        
        .curtain {
            position: absolute;
            top: 0;
            width: 50%;
            height: 100%;
            background: linear-gradient(90deg, #ff69b4 0%, #ff1493 100%);
            transition: transform 1.5s ease-in-out;
            box-shadow: inset 0 0 50px rgba(0,0,0,0.3);
        }
        
        .curtain-left {
            left: 0;
            border-right: 3px solid #c71585;
        }
        
        .curtain-right {
            right: 0;
            border-left: 3px solid #c71585;
        }
        
        .curtain.open.curtain-left {
            transform: translateX(-100%);
        }
        
        .curtain.open.curtain-right {
            transform: translateX(100%);
        }
        
        .curtain-text {
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            color: white;
            font-size: 2.5em;
            font-weight: bold;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
            pointer-events: none;
            text-align: center;
            width: 80%;
        }
    </style>
    </head>
    <body>
        <div class="curtain-container" onclick="openCurtains()">
            <div class="curtain curtain-left" id="leftCurtain">
                <div class="curtain-text">Click Anywhere to Open</div>
            </div>
            <div class="curtain curtain-right" id="rightCurtain"></div>
        </div>
        
        <script>
            let clicked = false;
            
            function openCurtains() {
                if (!clicked) {
                    clicked = true;
                    document.getElementById('leftCurtain').classList.add('open');
                    document.getElementById('rightCurtain').classList.add('open');
                }
            }
        </script>
    </body>
    </html>
    """, height=700)
    
    st.markdown("<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        if st.button("Continue After Curtains Open", type="primary", use_container_width=True, key="curtain_btn"):
            st.session_state.curtains_open = True
            st.rerun()

# ============================================
# ENVELOPE SCREEN
# ============================================
elif not st.session_state.envelope_opened:
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    components.html("""
    <!DOCTYPE html>
    <html>
    <head>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        body {
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 400px;
            background: transparent;
            font-family: 'Georgia', serif;
        }
        
        .envelope-container {
            text-align: center;
            cursor: pointer;
            transition: transform 0.3s ease;
            padding: 40px;
        }
        
        .envelope-container:hover {
            transform: scale(1.05);
        }
        
        .envelope {
            display: inline-block;
            position: relative;
            width: 250px;
            height: 160px;
            background: #fff5f5;
            border: 3px solid #ff69b4;
            border-radius: 10px;
            box-shadow: 0 10px 30px rgba(255, 105, 180, 0.4);
        }
        
        .envelope-flap {
            position: absolute;
            top: 0;
            left: 0;
            width: 0;
            height: 0;
            border-left: 125px solid transparent;
            border-right: 125px solid transparent;
            border-top: 80px solid #ff69b4;
        }
        
        .heart-seal {
            position: absolute;
            top: 60px;
            left: 50%;
            transform: translateX(-50%);
            font-size: 3em;
            animation: heartbeat 1.5s infinite;
        }
        
        @keyframes heartbeat {
            0%, 100% { transform: translateX(-50%) scale(1); }
            50% { transform: translateX(-50%) scale(1.1); }
        }
        
        .open-me-text {
            margin-top: 20px;
            font-size: 1.8em;
            color: #ff1493;
            font-weight: bold;
            text-shadow: 1px 1px 2px rgba(0,0,0,0.1);
        }
    </style>
    </head>
    <body>
        <div class="envelope-container" onclick="pulseEnvelope()">
            <div class="envelope" id="envelope">
                <div class="envelope-flap"></div>
                <div class="heart-seal">❤️</div>
            </div>
            <div class="open-me-text">Click the Envelope 💌</div>
        </div>
        
        <script>
            function pulseEnvelope() {
                const env = document.getElementById('envelope');
                env.style.transform = 'scale(0.95)';
                setTimeout(() => {
                    env.style.transform = 'scale(1)';
                }, 100);
            }
        </script>
    </body>
    </html>
    """, height=400)
    
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        if st.button("📬 Open Envelope", type="primary", use_container_width=True, key="env_btn"):
            st.session_state.envelope_opened = True
            st.rerun()

# ============================================
# LETTER AND YES/NO BUTTONS
# ============================================
elif st.session_state.answer is None:
    st.markdown(f"""
    <div class="letter">
        <h2>{LETTER_CONTENT['greeting']}</h2>
        <p>{LETTER_CONTENT['message']}</p>
        <p style="text-align: right; font-style: italic; margin-top: 40px;">
            {LETTER_CONTENT['signature']}
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Calculate button sizes
    yes_size = 1.5 + (st.session_state.no_clicks * 0.3)
    no_size = max(0.5, 1.5 - (st.session_state.no_clicks * 0.2))
    
    col1, col2, col3 = st.columns([1, 1, 1])
    
    with col1:
        st.markdown(f"""
        <style>
            div[data-testid="column"]:nth-child(1) button {{
                transform: scale({yes_size}) !important;
                background: linear-gradient(135deg, #ff69b4 0%, #ff1493 100%) !important;
                color: white !important;
                font-size: 1.2em !important;
                font-weight: bold !important;
                padding: 15px 30px !important;
                border-radius: 50px !important;
                border: none !important;
                box-shadow: 0 5px 15px rgba(255, 105, 180, 0.4) !important;
            }}
        </style>
        """, unsafe_allow_html=True)
        if st.button("💖 YES! 💖", key="yes_button"):
            st.session_state.answer = "yes"
            st.rerun()
    
    with col3:
        st.markdown(f"""
        <style>
            div[data-testid="column"]:nth-child(3) button {{
                transform: scale({no_size}) !important;
                background: linear-gradient(135deg, #ddd 0%, #bbb 100%) !important;
                color: #666 !important;
                font-size: 1.2em !important;
                font-weight: bold !important;
                padding: 15px 30px !important;
                border-radius: 50px !important;
                border: none !important;
            }}
        </style>
        """, unsafe_allow_html=True)
        if st.button("No", key="no_button"):
            st.session_state.no_clicks += 1
            st.rerun()
    
    if st.session_state.no_clicks > 0:
        hints = [
            "Are you sure? 🥺",
            "The Yes button is getting bigger for a reason! 💕",
            "Come on... you know you want to say yes! 😊",
            "The No button is disappearing... 👀",
            "Just click Yes already! 💝",
            "I'm not giving up! 💪💕"
        ]
        hint_index = min(st.session_state.no_clicks - 1, len(hints) - 1)
        st.markdown(f"<p style='text-align: center; color: #ff69b4; font-style: italic; font-size: 1.2em; margin-top: 30px;'>{hints[hint_index]}</p>", unsafe_allow_html=True)

# ============================================
# SUCCESS PAGE WITH CONFETTI
# ============================================
else:
    # Confetti
    components.html("""
    <!DOCTYPE html>
    <html>
    <head>
    <style>
        body {
            margin: 0;
            padding: 0;
            overflow: hidden;
            height: 600px;
        }
        .confetti {
            position: fixed;
            width: 10px;
            height: 10px;
            z-index: 9999;
        }
        @keyframes confetti-fall {
            0% {
                transform: translateY(-10vh) rotate(0deg);
                opacity: 1;
            }
            100% {
                transform: translateY(110vh) rotate(720deg);
                opacity: 0;
            }
        }
    </style>
    </head>
    <body>
    <script>
        const colors = ['#ff69b4', '#ff1493', '#ff6b9d', '#ffc0cb', '#ff85a1', '#ffb6c1', '#db7093', '#c71585', '#ff007f'];
        
        function createConfetti() {
            for (let i = 0; i < 200; i++) {
                const confetti = document.createElement('div');
                confetti.className = 'confetti';
                confetti.style.left = Math.random() * 100 + 'vw';
                confetti.style.top = '-10px';
                confetti.style.animationDelay = Math.random() * 3 + 's';
                confetti.style.animationDuration = (Math.random() * 3 + 2) + 's';
                confetti.style.background = colors[Math.floor(Math.random() * colors.length)];
                confetti.style.width = (Math.random() * 15 + 5) + 'px';
                confetti.style.height = confetti.style.width;
                confetti.style.borderRadius = Math.random() > 0.5 ? '50%' : '0%';
                confetti.style.animation = 'confetti-fall ' + confetti.style.animationDuration + ' linear infinite';
                confetti.style.animationDelay = confetti.style.animationDelay;
                document.body.appendChild(confetti);
            }
        }
        
        createConfetti();
        setInterval(createConfetti, 3000);
    </script>
    </body>
    </html>
    """, height=600)
    
    st.markdown(f"""
    <div class="success-message">
        <h1>{SUCCESS_MESSAGE['title']}</h1>
        <p>{SUCCESS_MESSAGE['message']}</p>
    </div>
    """, unsafe_allow_html=True)

# Floating hearts on all pages
st.markdown("""
<div class="floating-heart" style="top: 10%; left: 10%; animation-delay: 0s;">💕</div>
<div class="floating-heart" style="top: 20%; right: 15%; animation-delay: 1s;">💖</div>
<div class="floating-heart" style="bottom: 15%; left: 20%; animation-delay: 2s;">💗</div>
<div class="floating-heart" style="bottom: 25%; right: 10%; animation-delay: 1.5s;">💝</div>
<div class="floating-heart" style="top: 50%; left: 5%; animation-delay: 0.5s;">💞</div>
<div class="floating-heart" style="top: 60%; right: 5%; animation-delay: 2.5s;">💓</div>
""", unsafe_allow_html=True)
