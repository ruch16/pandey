import streamlit as st
import streamlit.components.v1 as components

# Page configuration
st.set_page_config(
    page_title="💌 A Special Question",
    page_icon="💕",
    layout="centered"
)

# ============================================
# CUSTOMIZE THESE!
# ============================================
SECRET_PASSWORD = "MeNu1316"  # Change this!

LETTER_GREETING = "My Duduuuuuuuuuuuuuuuuuuuuuuuuuuuuuu 💕"

LETTER_MESSAGE = """ Ever since, i met you, i seem to have fallen
    deeply in love with you. So much so that i cant even breathe
    but you r not with me. I never thought my lil crush on you will
    grow so much, though we r in a relationship i seem to fall in love with u 
    daily. not just ur face, but ur sweetness, ur cuteness, ur kindness,
    the way your eyes sparkle in the sun, the way u look mrng mrng, or the way u act only around me.
    i cant wait to be with you my lovee
    
    So, on this special day, I have one very important question to ask you...
    
    Will you be my Valentine? 💖
"""

LETTER_SIGNATURE = "With all my heart and pussy, your bubu💖"
SUCCESS_TITLE = "YES! 🎉💕"

SUCCESS_MESSAGE = """You just made me even more happy! i m the happiest person in this worldddddd 
    
    I promise to make this Valentine's Day (and every day after) 
    absolutely special for you. 
    
    Get ready for an amazing time together! 💖
    
    I can't wait to celebrate with you! 🌹
"""

# ============================================
# Initialize session state
# ============================================
if 'stage' not in st.session_state:
    st.session_state.stage = 'password'  # password, envelope, success
if 'no_clicks' not in st.session_state:
    st.session_state.no_clicks = 0

# ============================================
# CSS Styling
# ============================================
st.markdown("""
<style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    .stApp {
        background: linear-gradient(135deg, #ffeef8 0%, #ffe0f0 100%);
    }
    
    .big-title {
        text-align: center;
        color: #ff1493;
        font-size: 3em;
        margin-top: 100px;
        font-family: 'Georgia', serif;
    }
    
    .subtitle {
        text-align: center;
        color: #666;
        font-size: 1.3em;
        margin-bottom: 30px;
    }
    
    .letter {
        max-width: 600px;
        margin: 30px auto;
        padding: 40px;
        background: white;
        border: 2px solid #ff69b4;
        border-radius: 15px;
        box-shadow: 0 15px 50px rgba(255, 105, 180, 0.3);
        font-family: 'Georgia', serif;
        line-height: 1.8;
    }
    
    .letter h2 {
        color: #ff1493;
        text-align: center;
        margin-bottom: 30px;
        font-size: 2em;
    }
    
    .letter p {
        color: #333;
        font-size: 1.1em;
        white-space: pre-line;
    }
    
    .success-box {
        text-align: center;
        padding: 50px 20px;
    }
    
    .success-box h1 {
        font-size: 3em;
        color: #ff1493;
        margin-bottom: 30px;
        font-family: 'Georgia', serif;
    }
    
    .success-box p {
        font-size: 1.3em;
        color: #333;
        line-height: 1.8;
        white-space: pre-line;
    }
</style>
""", unsafe_allow_html=True)

# ============================================
# STAGE 1: PASSWORD
# ============================================
if st.session_state.stage == 'password':
    st.markdown("<h1 class='big-title'>💕 Enter Secret Code 💕</h1>", unsafe_allow_html=True)
    st.markdown("<p class='subtitle'>This is a private invitation just for you!</p>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        password_input = st.text_input("Secret Code:", type="password", key="pwd")
        
        if st.button("✨ Enter ✨", type="primary", use_container_width=True):
            if password_input == SECRET_PASSWORD:
                st.session_state.stage = 'envelope'
                st.rerun()
            else:
                st.error("❌ Wrong code! Try again 💔")

# ============================================
# STAGE 2: ENVELOPE OPENS TO LETTER
# ============================================
elif st.session_state.stage == 'envelope':
    components.html(f"""
    <!DOCTYPE html>
    <html>
    <head>
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{
            font-family: 'Georgia', serif;
            display: flex;
            justify-content: center;
            align-items: flex-start;
            min-height: 800px;
            padding: 50px 20px;
            background: transparent;
        }}
        
        .container {{
            text-align: center;
            position: relative;
            width: 100%;
            max-width: 700px;
        }}
        
        .envelope-wrapper {{
            position: relative;
            width: 280px;
            height: 180px;
            margin: 0 auto;
            cursor: pointer;
            transition: transform 0.3s;
        }}
        
        .envelope-wrapper:hover {{
            transform: scale(1.05);
        }}
        
        .envelope {{
            width: 100%;
            height: 100%;
            background: #fff5f5;
            border: 3px solid #ff69b4;
            border-radius: 10px;
            box-shadow: 0 10px 30px rgba(255, 105, 180, 0.4);
            position: relative;
            overflow: visible;
        }}
        
        .flap {{
            position: absolute;
            top: 0;
            left: 0;
            border-left: 137px solid transparent;
            border-right: 137px solid transparent;
            border-top: 90px solid #ff69b4;
            transform-origin: top center;
            transition: transform 0.6s ease;
            z-index: 10;
        }}
        
        .envelope-wrapper.opened .flap {{
            transform: rotateX(180deg);
        }}
        
        .heart {{
            position: absolute;
            top: 70px;
            left: 50%;
            transform: translateX(-50%);
            font-size: 3em;
            z-index: 11;
            animation: beat 1.5s infinite;
        }}
        
        @keyframes beat {{
            0%, 100% {{ transform: translateX(-50%) scale(1); }}
            50% {{ transform: translateX(-50%) scale(1.1); }}
        }}
        
        .instruction {{
            margin-top: 20px;
            font-size: 1.8em;
            color: #ff1493;
            font-weight: bold;
        }}
        
        .letter {{
            position: absolute;
            top: -20px;
            left: 50%;
            transform: translateX(-50%) translateY(0);
            width: 90%;
            max-width: 600px;
            padding: 40px;
            background: white;
            border: 2px solid #ff69b4;
            border-radius: 15px;
            box-shadow: 0 15px 50px rgba(255, 105, 180, 0.3);
            opacity: 0;
            transition: all 0.8s ease;
            pointer-events: none;
            z-index: 5;
        }}
        
        .letter.visible {{
            opacity: 1;
            transform: translateX(-50%) translateY(220px);
            pointer-events: all;
        }}
        
        .letter h2 {{
            color: #ff1493;
            text-align: center;
            margin-bottom: 25px;
            font-size: 1.8em;
        }}
        
        .letter p {{
            color: #333;
            font-size: 1.05em;
            line-height: 1.8;
            white-space: pre-line;
            margin-bottom: 15px;
        }}
        
        .signature {{
            text-align: right;
            font-style: italic;
            margin-top: 30px;
        }}
        
        .buttons {{
            margin-top: 30px;
            text-align: center;
            opacity: 0;
            transition: opacity 0.5s ease 0.5s;
        }}
        
        .letter.visible .buttons {{
            opacity: 1;
        }}
    </style>
    </head>
    <body>
        <div class="container">
            <div class="envelope-wrapper" id="envWrap" onclick="openEnvelope()">
                <div class="envelope">
                    <div class="flap"></div>
                    <div class="heart">❤️</div>
                </div>
                <div class="instruction" id="instruction">Click to Open 💌</div>
            </div>
            
            <div class="letter" id="letter">
                <h2>{LETTER_GREETING}</h2>
                <p>{LETTER_MESSAGE}</p>
                <p class="signature">{LETTER_SIGNATURE}</p>
                <div class="buttons" id="buttons">
                    <!-- Buttons will be added by Streamlit -->
                </div>
            </div>
        </div>
        
        <script>
            let opened = false;
            function openEnvelope() {{
                if (!opened) {{
                    opened = true;
                    document.getElementById('envWrap').classList.add('opened');
                    document.getElementById('instruction').style.opacity = '0';
                    setTimeout(() => {{
                        document.getElementById('letter').classList.add('visible');
                    }}, 400);
                }}
            }}
        </script>
    </body>
    </html>
    """, height=900)
    
    # Add spacing to position buttons below the letter
    st.markdown("<br>" * 35, unsafe_allow_html=True)
    
    # Button sizing
    yes_scale = 1.0 + (st.session_state.no_clicks * 0.3)
    no_scale = max(0.3, 1.0 - (st.session_state.no_clicks * 0.15))
    
    st.markdown(f"""
    <style>
        .stButton > button {{
            width: 100%;
        }}
        .yes-btn button {{
            background: linear-gradient(135deg, #ff69b4, #ff1493) !important;
            color: white !important;
            font-size: {yes_scale}em !important;
            font-weight: bold !important;
            border-radius: 50px !important;
            padding: 20px 40px !important;
            border: none !important;
            box-shadow: 0 5px 15px rgba(255, 105, 180, 0.4) !important;
        }}
        .yes-btn button:hover {{
            transform: scale(1.05);
            box-shadow: 0 8px 25px rgba(255, 105, 180, 0.6) !important;
        }}
        .no-btn button {{
            background: #ddd !important;
            color: #666 !important;
            font-size: {no_scale}em !important;
            border-radius: 50px !important;
            padding: 15px 30px !important;
            border: none !important;
        }}
    </style>
    """, unsafe_allow_html=True)
    
    col1, col2, col3, col4, col5 = st.columns([1, 2, 1, 2, 1])
    
    with col2:
        st.markdown('<div class="yes-btn">', unsafe_allow_html=True)
        if st.button("💖 YES! 💖", key="yes_btn", use_container_width=True):
            st.session_state.stage = 'success'
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col4:
        st.markdown('<div class="no-btn">', unsafe_allow_html=True)
        if st.button("No", key="no_btn", use_container_width=True):
            st.session_state.no_clicks += 1
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)
    
    if st.session_state.no_clicks > 0:
        hints = [
            "Are you sure? 🥺",
            "The Yes button is growing! 💕",
            "Come on... you know you want to say yes! 😊",
            "The No is shrinking... 👀",
            "Just say Yes! 💝",
            "I'm not giving up! 💪💕"
        ]
        hint = hints[min(st.session_state.no_clicks - 1, len(hints) - 1)]
        st.markdown(f"<p style='text-align:center;color:#ff69b4;font-size:1.3em;margin-top:20px;font-weight:bold;'>{hint}</p>", unsafe_allow_html=True)

# ============================================
# STAGE 3: SUCCESS WITH CONFETTI
# ============================================
else:
    components.html("""
    <style>
        body { margin: 0; padding: 0; height: 500px; overflow: hidden; }
        .confetti {
            position: fixed;
            width: 10px;
            height: 10px;
        }
        @keyframes fall {
            to { transform: translateY(120vh) rotate(360deg); opacity: 0; }
        }
    </style>
    <script>
        const colors = ['#ff69b4', '#ff1493', '#ffc0cb', '#ff85a1', '#db7093'];
        for (let i = 0; i < 150; i++) {
            const c = document.createElement('div');
            c.className = 'confetti';
            c.style.left = Math.random() * 100 + 'vw';
            c.style.background = colors[Math.floor(Math.random() * colors.length)];
            c.style.width = c.style.height = (Math.random() * 10 + 5) + 'px';
            c.style.animation = `fall ${Math.random() * 3 + 2}s linear infinite`;
            c.style.animationDelay = Math.random() * 3 + 's';
            document.body.appendChild(c);
        }
    </script>
    """, height=500)
    
    st.markdown(f"""
    <div class="success-box">
        <h1>{SUCCESS_TITLE}</h1>
        <p>{SUCCESS_MESSAGE}</p>
    </div>
    """, unsafe_allow_html=True)
