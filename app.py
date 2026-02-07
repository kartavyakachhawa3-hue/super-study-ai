import streamlit as st
import asyncio
import edge_tts
from PIL import Image
import pytesseract
import os

# पेज की सेटिंग (Browser tab पर क्या दिखेगा)
st.set_page_config(page_title="Super Study AI", page_icon="📚")

# CSS: मास्टर जी का क्लासरूम लुक
st.markdown("""
    <style>
    .stApp { background-color: #fdf6e3; }
    .title { color: #8b4513; text-align: center; font-family: 'Georgia', serif; text-shadow: 2px 2px #d2b48c; }
    .status { color: #5d2e0d; font-style: italic; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 class='title'>📚 Super Study: मास्टर जी क्लासरूम</h1>", unsafe_allow_html=True)

# बैकग्राउंड धुन (BGM) - बहुत हल्का वॉल्यूम (3%)
st.markdown("""
    <audio id="bgm" loop autoplay>
        <source src="https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3" type="audio/mpeg">
    </audio>
    <script>
        var audio = document.getElementById("bgm");
        audio.volume = 0.03;
    </script>
    """, unsafe_allow_html=True)

# आवाज़ का फंक्शन (बुजुर्गवार और गहरी आवाज़)
async def generate_voice(text):
    # rate="-15%" (धीमी), pitch="-2Hz" (गहरी/Bass)
    communicate = edge_tts.Communicate(text, "hi-IN-MadhurNeural", rate="-15%", pitch="-2Hz")
    await communicate.save("voice.mp3")

# मास्टर जी की फोटो और स्टेटस
col1, col2, col3 = st.columns([1,2,1])
with col2:
    st.image("https://img.icons8.com/illustrations/printable/200/teacher.png", width=200)
    st.markdown("<p class='status'>\"बेटा, अपनी किताब की फोटो दिखाओ, मैं पढ़ता हूँ...\"</p>", unsafe_allow_html=True)

# फोटो अपलोडर बटन
uploaded_file = st.file_uploader("यहाँ क्लिक करके फोटो चुनें", type=['jpg', 'png', 'jpeg'])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='आपकी किताब का पन्ना', width=300)
    
    with st.spinner('मास्टर जी चश्मा लगा रहे हैं और पढ़ रहे हैं...'):
        # OCR प्रोसेसिंग
        text = pytesseract.image_to_string(image)
        
        if text.strip():
            asyncio.run(generate_voice(text))
            st.audio("voice.mp3", format="audio/mp3", start_time=0)
            st.success("शाबाश! मास्टर जी ने पढ़ लिया है, अब आप सुनिए।")
        else:
            st.error("मास्टर जी को अक्षर साफ़ नहीं दिख रहे, कृपया साफ़ फोटो अपलोड करें।")
