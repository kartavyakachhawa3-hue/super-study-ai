import streamlit as st
import asyncio
import edge_tts
from PIL import Image
import pytesseract
import os

# 1. पेज की पूरी सेटिंग
st.set_page_config(page_title="Super Study AI", page_icon="📚", layout="centered")

# 2. ज़बरदस्त 3D और क्लासरूम स्टाइल (CSS)
st.markdown("""
    <style>
    .stApp {
        background: #fdf6e3;
        font-family: 'Georgia', serif;
    }
    .master-card {
        background: white;
        padding: 30px;
        border-radius: 20px;
        border: 4px solid #8b4513;
        box-shadow: 0 15px 35px rgba(0,0,0,0.2);
        text-align: center;
    }
    h1 {
        color: #8b4513;
        text-shadow: 1px 1px 2px #d2b48c;
    }
    .status-text {
        color: #5d2e0d;
        font-style: italic;
        font-size: 18px;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. बैकग्राउंड संगीत (BGM) - एकदम हल्का
st.markdown("""
    <audio id="bgm" loop autoplay>
        <source src="https://www.soundhelix.com/examples/mp3/SoundHelix-Song-17.mp3" type="audio/mpeg">
    </audio>
    <script>
        var audio = document.getElementById("bgm");
        audio.volume = 0.02;
    </script>
    """, unsafe_allow_html=True)

# 4. मुख्य इंटरफेस
st.markdown("<div class='master-card'>", unsafe_allow_html=True)
st.markdown("<h1>📚 SUPER STUDY AI</h1>", unsafe_allow_html=True)
st.markdown("<p class='status-text'>मास्टर जी क्लासरूम में आपका स्वागत है, बेटा।</p>", unsafe_allow_html=True)

# मास्टर जी की इमेज (किताब वाली)
st.image("https://img.icons8.com/illustrations/printable/200/teacher.png", width=250)
st.markdown("</div>", unsafe_allow_html=True)

# 5. आवाज़ का फंक्शन
async def generate_voice(text):
    # -15% Speed और -2Hz Pitch बुजुर्ग मास्टर जी की आवाज़ के लिए
    communicate = edge_tts.Communicate(text, "hi-IN-MadhurNeural", rate="-15%", pitch="-2Hz")
    await communicate.save("voice.mp3")

# 6. फाइल अपलोडर
st.write("---")
uploaded_file = st.file_uploader("अपनी किताब का फोटो यहाँ डालें...", type=['jpg', 'png', 'jpeg'])

if uploaded_file:
    img = Image.open(uploaded_file)
    st.image(img, caption='आपकी किताब', width=300)
    
    with st.spinner('मास्टर जी पढ़ रहे हैं...'):
text = pytesseract.image_to_string(lang='hin+eng')
        if text.strip():
            asyncio.run(generate_voice(text))
            st.audio("voice.mp3", format="audio/mp3")
            st.balloons()
            st.success("मास्टर जी ने पढ़ लिया! अब ऊपर प्ले बटन दबाकर सुनें।")
        else:
            st.error("मास्टर जी को कुछ दिख नहीं रहा, फोटो साफ खींचें।")
