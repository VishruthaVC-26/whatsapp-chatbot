# 🤖 WhatsApp Chatbot

<p align="center">
  <b>Automated WhatsApp Chatbot using Python, Flask & Twilio</b><br>
  Real-time messaging • Webhook-based • Scalable design
</p>

---
## 🚀 Overview
This project is a WhatsApp chatbot built using Python, Flask, and Twilio API. It automatically replies to user messages in real-time.
---

## ✨ Features
- 📱 WhatsApp Integration (Twilio Sandbox)
- ⚡ Real-time Messaging
- 🤖 Automated Replies
- 📋 Menu-based chatbot
- 🌐 Ngrok integration
- 🧩 Flask backend

---
## 🏗️ Architecture
User → Twilio → Ngrok → Flask → Response → WhatsApp
---

## 🛠️ Tech Stack
- Python  
- Flask  
- Twilio API  
- Ngrok  
- dotenv  

---

## ⚙️ Setup Steps

### 1. Clone Repository
git clone https://github.com/VishruthaVC-26/whatsapp-chatbot.git  
cd whatsapp-chatbot  

### 2. Create Virtual Environment
python -m venv venv  
venv\Scripts\activate  

### 3. Install Dependencies
pip install -r requirements.txt  

### 4. Add API Key
Create `.env` file and add:  
OPENAI_API_KEY=your_key  

### 5. Run App
python app.py  

### 6. Start Ngrok
ngrok http 5000  

### 7. Set Webhook in Twilio
https://your-ngrok-url/whatsapp  

---

## 📱 Usage
- Send message to: +1 415 523 8886  
- Join sandbox  
- Send “Hi”  
- Get reply  

---

## ⚠️ Notes
- Uses Twilio sandbox  
- Replace ngrok URL every time  
- Do not upload `.env`  

---

## 🚀 Future Scope
- AI integration  
- Database  
- Deployment  
- Dashboard  

---

## 👨‍💻 Author
Vishrutha VC
