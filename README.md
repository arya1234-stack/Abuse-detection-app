# Social Media Abuse & Toxicity Detection with AI

**Social Media Abuse & Toxicity Detection** is a **real-time toxic content detection platform** that combines **Machine Learning + LLM intelligence + modern analytics UI** to detect abusive language, estimate toxicity, explain predictions, and visualize insights in real time.


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
* ✅ Toxicity confidence bar
* ✅ Pie chart distribution
* ✅ Abuse table with CSV export
* ✅ Word cloud visualization
* ✅ Analysis history tracking



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


## 👨‍💻 Author

**Arya - 2300033603**


## 📜 License

KLU License

---
