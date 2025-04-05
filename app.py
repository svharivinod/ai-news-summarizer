import streamlit as st
import openai
from googletrans import Translator
from gtts import gTTS
import tempfile
from dotenv import load_dotenv
import os

# ----------------------
# Load API Key from .env
# ----------------------
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# ----------------------
# Streamlit App Layout
# ----------------------

st.set_page_config(page_title="AI News Summarizer for Farmers", page_icon="🌾")
st.title("📰 KisanVaani - Local Language News Summarizer for Farmers")

st.markdown("""
This tool summarizes news articles in simple English and translates them to your selected local language with audio playback — ideal for farmers or rural communities.
""")

# 📄 News Input
news_text = st.text_area("Paste the news article here", height=250)

# 🌍 Language Selection
lang = st.selectbox("Choose Output Language", ["Hindi", "Kannada", "Tamil", "Telugu"])
lang_code = {"Hindi": "hi", "Kannada": "kn", "Tamil": "ta", "Telugu": "te"}[lang]

# ----------------------
# Functions
# ----------------------

def get_summary(text):
    prompt = f"Summarize this news article in 5 simple bullet points. Use very simple vocabulary suitable for a rural audience:\n\n{text}"
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response['choices'][0]['message']['content']


def translate_text(text, target_lang="hi"):
    translator = Translator()
    translation = translator.translate(text, dest=target_lang)
    return translation.text


def generate_audio(text, lang_code):
    tts = gTTS(text, lang=lang_code)
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as fp:
        tts.save(fp.name)
        return fp.name

# ----------------------
# Main App Logic
# ----------------------

if st.button("🔍 Summarize and Translate"):
    if not news_text.strip():
        st.error("❌ Please paste some news content to summarize.")
    else:
        with st.spinner("🔄 Generating summary..."):
            try:
                # Step 1: Get English summary
                summary = get_summary(news_text)

                # Step 2: Translate to selected language
                translated = translate_text(summary, lang_code)

                # Step 3: Generate audio
                audio_file = generate_audio(translated, lang_code)

                # Display Results
                st.subheader("📄 Summary in English")
                st.write(summary)

                st.subheader(f"🌐 Translation in {lang}")
                st.write(translated)

                st.subheader("🔊 Listen to Summary")
                st.audio(audio_file, format="audio/mp3")

            except Exception as e:
                st.error(f"Something went wrong: {e}")
