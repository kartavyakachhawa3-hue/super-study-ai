import google.generativeai as genai

# अपनी API Key यहाँ डालें
genai.configure(api_key="YOUR_GEMINI_API_KEY")

def get_text_from_image(image):
    model = genai.GenerativeModel('gemini-1.5-flash')
    # AI को निर्देश दें
    prompt = "इस फोटो में जो भी हिंदी और इंग्लिश टेक्स्ट लिखा है, उसे साफ़-साफ़ लिखो।"
    response = model.generate_content([prompt, image])
    return response.text

# Streamlit के अंदर का हिस्सा
if uploaded_file is not None:
    img = Image.open(uploaded_file)
    with st.spinner('AI पढ़ रहा है...'):
        result_text = get_text_from_image(img)
        st.write(result_text)
