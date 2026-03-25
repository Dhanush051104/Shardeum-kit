# ॐ VedicBot — Ancient Wisdom, Modern Interface

A multilingual AI chatbot powered by LLaMA 3.3 that answers questions about Vedic knowledge, Sanskrit texts, and ancient Indian philosophy. Built on the Shardeum blockchain ecosystem.

## 🌐 Live Demo
- **Frontend:** Open `frontend/index.html` in your browser
- **Backend API:** https://shardeum-kit.onrender.com

## ✨ Features
- 💬 Chat with an AI Vedic scholar
- 🌍 Multilingual support — English, हिन्दी, தமிழ், తెలుగు, संस्कृत, ಕನ್ನಡ
- 📜 Sanskrit shlokas with translations in every response
- 🔗 Shardeum wallet connect (MetaMask)
- 📱 Beautiful parchment-themed UI

## 🛠️ Tech Stack
| Layer | Technology |
|-------|-----------|
| Frontend | HTML, CSS, JavaScript |
| Backend | Python, FastAPI |
| AI Model | LLaMA 3.3-70b via Groq API |
| Hosting | Render.com |
| Blockchain | Shardeum Testnet |

## 🚀 How to Run Locally

### Backend
```bash
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
```

### Frontend
Just open `frontend/index.html` in your browser.

### Environment Variables
Create a `backend/.env` file:
```
GROQ_API_KEY=your_groq_api_key_here
```

## 🏗️ Architecture
User → index.html → FastAPI (Render) → Groq API (LLaMA 3.3) → Response

## 📜 Vedic Knowledge Covered
- The four Vedas (Rigveda, Samaveda, Yajurveda, Atharvaveda)
- Upanishads and Bhagavad Gita
- Sanskrit language and shlokas
- Dharma, Karma, Moksha
- Ayurveda, Yoga, Jyotisha
```

Save with **Ctrl+S** then push:
```
git add .
git commit -m "update README"
git push