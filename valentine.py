import streamlit as st
import streamlit.components.v1 as components

# Page configuration
st.set_page_config(
    page_title="💌 A Special Question",
    page_icon="💕",
    layout="centered"
)

# ============================================
# PASSWORD PROTECTION - ENABLED BY DEFAULT
# ============================================

if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False
    st.session_state.curtains_open = False

if not st.session_state.authenticated:
    # Add pink gradient background for password page
    st.markdown("""
    <style>
        .stApp {{
        background: linear-gradient(135 deg, #ffeef8 0%, #ffe0f0 100%);"
        {}
    </style>
    """, unsafe_allow_html=True)
    
    st.markdown("<h1 style='text-align: center; color: #ff1493; margin-top: 100px;'>💕 Enter Secret Code 💕</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #666; font-size: 1.2em;'>This is a private invitation just for you!</p>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        password = st.text_input("Secret Code:", type="password", key="auth_password")
        if st.button("✨ Enter ✨", type="primary", use_container_width=True):
            # CHANGE THIS PASSWORD TO YOUR OWN SECRET CODE!
            if password == "MeNu1316":
                st.session_state.authenticated = True
                st.session_state.curtains_open = False  # Start with curtains closed
                st.rerun()
            else:
                st.error("❌ Wrong code! Try again 💔")
    st.stop()

# ============================================
# CUSTOMIZABLE CONTENT - EDIT THESE!
# ============================================

LETTER_CONTENT = {
    "greeting": "My Dudu 💕",
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

}

# ============================================
# DO NOT EDIT BELOW THIS LINE
# ============================================

# Custom CSS for animations and styling
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
    
    /* Hide default button */
    .element-container:has(#hidden-button) {
        display: none;
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
if 'curtains_open' not in st.session_state:
    st.session_state.curtains_open = False
if 'envelope_opened' not in st.session_state:
    st.session_state.envelope_opened = False
if 'answer' not in st.session_state:
    st.session_state.answer = None
if 'no_clicks' not in st.session_state:
    st.session_state.no_clicks = 0

# Curtains
if not st.session_state.curtains_open:
    components.html("""
    <!DOCTYPE html>
    <html>
    <head>
    <style>
        body {
            margin: 0;
            padding: 0;
            overflow: hidden;
            height: 100vh;
        }
        .curtain-container {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            cursor: pointer;
            z-index: 9999;
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
            font-family: 'Georgia', serif;
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
                    
                    // After curtains open animation, trigger page reload to show envelope
                    setTimeout(function() {
                        // Use Streamlit's query params to trigger state change
                        const url = new URL(window.parent.location.href);
                        url.searchParams.set('curtains', 'open');
                        window.parent.history.pushState({}, '', url);
                        window.parent.location.reload();
                    }, 1600);
                }
            }
        </script>
    </body>
    </html>
    """, height=600)
    
    # Check URL params to see if curtains were opened
    try:
        if st.query_params.get("curtains") == "open":
            st.session_state.curtains_open = True
            st.query_params.clear()
            st.rerun()
    except:
        pass

# Envelope
elif not st.session_state.envelope_opened:
    components.html("""
    <!DOCTYPE html>
    <html>
    <head>
    <style>
        body {
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 500px;
            background: transparent;
        }
        
        .envelope-container {
            text-align: center;
            cursor: pointer;
            transition: transform 0.3s ease;
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
            transform-origin: top;
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
            font-family: 'Georgia', serif;
            text-shadow: 1px 1px 2px rgba(0,0,0,0.1);
        }
    </style>
    </head>
    <body>
        <div class="envelope-container" onclick="openEnvelope()">
            <div class="envelope">
                <div class="envelope-flap"></div>
                <div class="heart-seal">❤️</div>
            </div>
            <div class="open-me-text">Click the Envelope 💌</div>
        </div>
        
        <script>
            let clicked = false;
            
            function openEnvelope() {
                if (!clicked) {
                    clicked = true;
                    // Trigger page reload to show letter
                    const url = new URL(window.parent.location.href);
                    url.searchParams.set('envelope', 'open');
                    window.parent.history.pushState({}, '', url);
                    window.parent.location.reload();
                }
            }
        </script>
    </body>
    </html>
    """, height=400)
    
    # Check URL params to see if envelope was opened
    try:
        if st.query_params.get("envelope") == "open":
            st.session_state.envelope_opened = True
            st.query_params.clear()
            st.rerun()
    except:
        pass

# Letter and Yes/No buttons
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
    
    # Calculate button sizes based on no_clicks
    yes_size = 1.5 + (st.session_state.no_clicks * 0.3)
    no_size = max(0.5, 1.5 - (st.session_state.no_clicks * 0.2))
    
    st.markdown('<div class="button-container">', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 1, 1])
    
    with col1:
        st.markdown(f"""
        <style>
            div[data-testid="column"]:nth-child(1) button {{
                transform: scale({yes_size}) !important;
                background: linear-gradient(135deg, #ff69b4 0%, #ff1493 100%);
                color: white;
                font-size: 1.2em;
                font-weight: bold;
                padding: 15px 30px;
                border-radius: 50px;
                border: none;
                box-shadow: 0 5px 15px rgba(255, 105, 180, 0.4);
            }}
            div[data-testid="column"]:nth-child(1) button:hover {{
                box-shadow: 0 8px 25px rgba(255, 105, 180, 0.6);
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
                background: linear-gradient(135deg, #ddd 0%, #bbb 100%);
                color: #666;
                font-size: 1.2em;
                font-weight: bold;
                padding: 15px 30px;
                border-radius: 50px;
                border: none;
            }}
        </style>
        """, unsafe_allow_html=True)
        if st.button("No", key="no_button"):
            st.session_state.no_clicks += 1
            st.rerun()
    
    st.markdown('</div>', unsafe_allow_html=True)
    
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
        st.markdown(f"<p style='text-align: center; color: #ff69b4; font-style: italic; font-size: 1.2em;'>{hints[hint_index]}</p>", unsafe_allow_html=True)

# Success page with confetti
else:
    # Confetti animation
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
        
        // Create confetti immediately
        createConfetti();
        
        // Add more confetti every 3 seconds
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

# Add some floating hearts
st.markdown("""
<div class="floating-heart" style="top: 10%; left: 10%; animation-delay: 0s;">💕</div>
<div class="floating-heart" style="top: 20%; right: 15%; animation-delay: 1s;">💖</div>
<div class="floating-heart" style="bottom: 15%; left: 20%; animation-delay: 2s;">💗</div>
<div class="floating-heart" style="bottom: 25%; right: 10%; animation-delay: 1.5s;">💝</div>
<div class="floating-heart" style="top: 50%; left: 5%; animation-delay: 0.5s;">💞</div>
<div class="floating-heart" style="top: 60%; right: 5%; animation-delay: 2.5s;">💓</div>
""", unsafe_allow_html=True)
