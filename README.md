# 🌾 KisanVaani: AI-Powered News Summarizer for Farmers

**KisanVaani** is an AI-powered web app that helps farmers and rural communities access important news and government updates in **simplified language** and their **local languages**, with **audio narration** for easy listening.

Built using [Streamlit](https://streamlit.io/), the app makes complex news articles easy to understand by summarizing them into 5 simple bullet points using **OpenAI's GPT-3.5**, and then translating them into **Hindi, Kannada, Tamil, or Telugu** — with optional **Text-to-Speech (TTS)** for accessibility.

---

## 📌 Summary

Farmers often miss out on critical information due to:
- Complex news language
- Language barriers
- Low literacy levels
- Lack of digital accessibility

**KisanVaani** bridges this gap using AI, by:
- Simplifying news articles
- Translating them to regional languages
- Adding audio output for those who prefer listening

---

## 🚀 Features

- 🧠 **AI Summarization** using GPT-3.5 (OpenAI)
- 🌐 **Translation** to:
  - Hindi 🇮🇳
  - Kannada 🇰🇳
  - Tamil 🇮🇳
  - Telugu 🇮🇳
- 🔊 **Text-to-Speech** audio playback for translated text
- 🎯 Built for **rural readability** (10th-grade level or lower)
- ⚡ Simple and fast interface using Streamlit

---

## 🛠 Technical Stack

| Component         | Technology                 |
|------------------|----------------------------|
| UI Framework      | [Streamlit](https://streamlit.io/) |
| AI Model          | [OpenAI GPT-3.5 Turbo](https://platform.openai.com/) |
| Translation       | [Googletrans](https://pypi.org/project/googletrans/) (Google Translate unofficial API) |
| Text-to-Speech    | [gTTS (Google Text-to-Speech)](https://pypi.org/project/gTTS/) |
| Environment Mgmt  | Python `.env` + `python-dotenv` |
| Python Version    | ✅ Must use Python **3.10 or 3.11** (not 3.12+ due to `cgi` deprecation)

---

## 📦 Setup Instructions

### 1. Clone the repository

## Create and activate virtual environment
git clone https://github.com/your-username/kisan-vaani.git
cd kisan-vaani

# Windows
python -m venv venv310
venv310\Scripts\activate

# Mac/Linux
python3 -m venv venv310
source venv310/bin/activate

 ## Install dependencies
 pip install -r requirements.txt

 ## Add your OpenAI API key
 OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxx

 ## ▶️ Run the App
 streamlit run app.py

 ## 📂 Repository Structure
 kisan-vaani/
│
├── app.py               # Main Streamlit app
├── .env                 # Stores OpenAI API Key (not committed)
├── .gitignore           # Excludes .env and venv from repo
├── requirements.txt     # Python dependencies
├── venv310/             # Virtual environment (ignored)
└── README.md            # Project overview

## 📸 Screenshots



## 💡 Future Scope
🌐 Accept news URLs instead of pasted text
📰 Add multiple article summarization (daily digest)
☁️ Deploy as a mobile-friendly web app
📞 Add WhatsApp bot integration
🗣️ Add voice input (speech-to-text) for users who can’t type

## 🤝 Contributing
Got ideas to improve KisanVaani?
Feel free to fork the repo and raise a PR!

## 📜 License
This project is licensed under the MIT License.

## 🙏 Acknowledgements
OpenAI for GPT-3.5 Turbo
Google Translate & googletrans
gTTS for Text-to-Speech
Streamlit for an amazing rapid app framework

## 🔗 Project Link
🔗 GitHub: https://github.com/svharivinod/kisan-vaani

## 💬 Let's Connect
If you found this project helpful or inspiring, feel free to connect on LinkedIn or drop a ⭐️ on GitHub!

## 📝 Final To-Dos for You:
1. Replace:
   - `your-username` with your actual GitHub username
   - `your-link` with your LinkedIn profile URL
2. Add screenshots if you'd like
3. Commit this file:

```bash
git add README.md
git commit -m "Add full project README for KisanVaani"
git push

