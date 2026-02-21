# 🛡️ ToxiGuard AI

**ToxiGuard AI** is a **real-time toxic content detection platform** that combines **Machine Learning + LLM intelligence + modern analytics UI** to detect abusive language, estimate toxicity, explain predictions, and visualize insights in real time.


## 🌐 Live Demo

**Frontend (Vercel)**
👉 [https://toxiguard-ai.vercel.app](https://toxiguard-ai.vercel.app)

**Backend API (Render)**
👉 [https://toxiguard-ai-backend.onrender.com](https://toxiguard-ai-backend.onrender.com)

**GitHub Repository**
👉 [https://github.com/arya1234-stack/Abuse-detection-app.git](https://github.com/arya1234-stack/Abuse-detection-app.git)


## 🧠 Tech Stack

* ⚛️ **React (Vite)** — Premium glassmorphism UI
* 🚀 **FastAPI** — High-performance backend API
* 🧠 **Machine Learning** — TF-IDF + Logistic Regression
* 🤖 **LLM (OpenRouter)** — Context-aware moderation fallback
* 📊 **Analytics** — KPI dashboard, charts, word clouds


## ✨ Key Features

* ✅ Real-time toxic word detection
* ✅ ML-based classification (97%+ accuracy)
* ✅ LLM fallback for ambiguous content
* ✅ Highlight abusive words
* ✅ KPI dashboard (word count, abusive count, toxicity)
* ✅ Toxicity confidence bar
* ✅ Pie chart distribution
* ✅ Abuse table with CSV export
* ✅ Word cloud visualization
* ✅ Analysis history tracking
* ✅ Premium glassmorphism UI


## 📁 Project Structure

```
ToxiGuard-AI/
│
├── backend/
│   ├── app.py
│   ├── train_model.py
│   ├── requirements.txt
│   ├── abuse_model.joblib
│   ├── label_encoder.joblib
│   └── utils/
│       ├── abuse_words.py
│       ├── preprocessing.py
│       ├── sentiment.py
│       └── llm_guard.py
│
├── frontend/
│   ├── package.json
│   ├── vite.config.js
│   ├── index.html
│   └── src/
│       ├── main.jsx
│       ├── App.jsx
│       ├── api.js
│       ├── styles.css
│       └── components/
│           ├── Header.jsx
│           ├── TextInput.jsx
│           ├── LiveResult.jsx
│           ├── KPI.jsx
│           ├── Charts.jsx
│           ├── AbuseTable.jsx
│           ├── History.jsx
│           └── WordClouds.jsx
│
└── README.md
```


## 🧩 Backend Setup (Local)

### 1️⃣ Create virtual environment

```bash
cd backend
python -m venv venv
venv\Scripts\activate
```


### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```



### 3️⃣ Environment variables

Create file:

```
backend/.env
```

Add:

```env
OPENROUTER_API_KEY=your_api_key_here
OPENROUTER_MODEL=xiaomi/mimo-v2-flash:free
```


### 4️⃣ Train ML model (run once)

```bash
python train_model.py
```

This generates:

```
abuse_model.joblib
label_encoder.joblib
```


### 5️⃣ Run backend

```bash
uvicorn app:app --host 0.0.0.0 --port 8090 --reload
```

Backend URL:

```
http://127.0.0.1:8090
```

Swagger Docs:

```
http://127.0.0.1:8090/docs
```

## ⚛️ Frontend Setup (Local)

### 1️⃣ Install dependencies

```bash
cd frontend
npm install
```


### 2️⃣ Environment variable

Create file:

```
frontend/.env
```

Add:

```env
VITE_BACKEND_URL=http://127.0.0.1:8090
```


### 3️⃣ Run frontend

```bash
npm run dev
```

Open browser:

```
http://localhost:5173
```


## 🔗 API Usage

### Endpoint

```
POST /predict
```



### Request

```json
{
  "text": "you are stupid"
}
```


### Response

```json
{
  "toxic": true,
  "confidence": 0.95,
  "severity": "high",
  "reason": "Matched abusive keywords",
  "abusive_words": ["stupid"],
  "sentiment": {
    "label": "negative",
    "polarity": -0.6,
    "confidence": 0.6
  },
  "source": "rules"
}
```


## ⚠️ Common Issues & Fixes

### ❌ Backend not opening

```bash
uvicorn app:app --host 0.0.0.0 --port 8090 --reload
```

Verify:

```
http://127.0.0.1:8090/docs
```


### ❌ Node dependency conflicts

```bash
npm cache clean --force
npm install
npm run dev
```

Recommended Node version:

```
Node 18 LTS
```


### ❌ ML model not loading

```bash
python train_model.py
```


### ❌ CORS or API not responding

Ensure backend is running before frontend and correct backend URL is configured.


## 📦 Production Build

```bash
npm run build
```

Output folder:

```
frontend/dist
```


## 👨‍💻 Author

**Arya**


## 📜 License

KLU License

---
