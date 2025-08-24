# 🤖 HR Chatbot with Gemini + spaCy + Flask + Streamlit

An intelligent HR chatbot that processes job descriptions (JDs), segments user questions into intents (HR, QnA, chitchat), and responds using Google's Gemini API. Includes a Streamlit-based frontend and Flask backend.

---

## 🚀 Features

- Upload a Job Description (`.txt`)
- Ask questions related to roles, experience, qualifications
- Multi-intent segmentation and classification
- Uses Gemini (Google Generative AI) for generation
- Real-time responses via Streamlit UI

---

## 🧭 High-Level Architecture

```
+--------+        +---------------------+        +--------------------+
|  User  | -----> | Streamlit Frontend  | -----> |  Flask Backend API |
+--------+        +---------------------+        +--------------------+
                                                       |         |
                                                       |         |
                                     +-----------------+         +--------------------+
                                     |                                         |
                              +-------------+                        +------------------+
                              |  Gemini API |                        |  spaCy NLP Model |
                              +-------------+                        +------------------+
```

---

## 🛠 Low-Level Design (LLD)

```
                    +------------------------------------------------+
                    |           Streamlit Frontend (UI)             |
                    |----------------------------------------------|
                    | - Upload JD (.txt)                           |
                    | - Text Input for questions                   |
                    | - Display intent-based segmented responses   |
                    | - Chat history                               |
                    +-------------------------+----------------------+
                                              |
                        HTTP POST /upload_jd  |  HTTP POST /chat
                                              ↓
          +-------------------------------------------------------------------+
          |                    Flask Backend (API Server)                    |
          |------------------------------------------------------------------|
          | - /upload_jd: store uploaded JD                                 |
          | - /chat: process user input                                     |
          |   -> split_into_segments()                                      |
          |   -> classify_intents()                                         |
          |   -> generate_hr_response() → Gemini (with JD context)          |
          |   -> generate_gemini_response() → Gemini (general QnA/chitchat) |
          +-----------------------------+------------------------------------+
                                        |
                         +--------------+--------------+
                         |                             |
            +------------------------+     +----------------------------+
            | Gemini API (via SDK)   |     | spaCy (en_core_web_sm)     |
            | for text generation    |     | for segmentation & intents |
            +------------------------+     +----------------------------+
```

---

## 🧪 Requirements

```bash
pip install flask streamlit spacy python-dotenv google-generativeai
python -m spacy download en_core_web_sm
```

---

## 📁 Project Structure

```
├── backend/
    └── main.py   # Flask backend
├── frontend/
│   └── app.py    # Streamlit frontend
├── .env          # contains GOOGLE_API_KEY=your_key
└── README.md
```

---

## 🧑‍💻 How to Run

### 1. Start the backend
```bash
cd backend
python app.py
```

### 2. Start the frontend
```bash
streamlit run frontend/streamlit_app.py
```

---

## 📦 Environment Variables
Create a `.env` file:
```
GOOGLE_API_KEY=your_gemini_key_here
```

---

## 📌 To-Do / Improvements
- Add persistent storage for JD files
- Improve intent classification using ML model
- Stream response chunks from Gemini to frontend

---

## 📄 License
MIT

---

## 🙋‍♀️ Author
Made by @Jyoti · Powered by  Google + Streamlit
