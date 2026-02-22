import os
import joblib
import numpy as np
from collections import Counter

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

# ------------------- Local Imports -------------------
from utils.preprocessing import preprocess
from utils.abuse_words import detect_abusive_tokens
from utils.sentiment import analyze_sentiment
from utils.llm_guard import analyze_toxicity_llm

# =====================================================
# APP INITIALIZATION
# =====================================================

app = FastAPI(
    title="ToxiGuard AI",
    description="Hybrid AI Toxic Content Detection API",
    version="4.0.0"
)

# =====================================================
# CORS CONFIG
# =====================================================

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# =====================================================
# LOAD ML MODELS
# =====================================================

BASE_DIR = os.path.dirname(__file__)
MODEL_PATH = os.path.join(BASE_DIR, "abuse_model.joblib")
ENCODER_PATH = os.path.join(BASE_DIR, "label_encoder.joblib")

model = None
label_encoder = None

try:
    model = joblib.load(MODEL_PATH)
    label_encoder = joblib.load(ENCODER_PATH)
    print("✅ ML model loaded successfully")
except Exception as e:
    print("⚠️ ML model load failed:", e)

# =====================================================
# REQUEST SCHEMA
# =====================================================

class TextRequest(BaseModel):
    text: str

# =====================================================
# HEALTH CHECK
# =====================================================

@app.get("/")
def health():
    return {"status": "ToxiGuard API running"}

# =====================================================
# SAFE NUMPY CONVERTER
# =====================================================

def convert_numpy(obj):
    if isinstance(obj, dict):
        return {k: convert_numpy(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [convert_numpy(i) for i in obj]
    elif isinstance(obj, np.ndarray):
        return obj.tolist()
    elif isinstance(obj, (np.integer,)):
        return int(obj)
    elif isinstance(obj, (np.floating,)):
        return float(obj)
    return obj

# =====================================================
# RESPONSE BUILDER
# =====================================================

def build_response(payload: dict):
    abusive_words = payload.get("abusive_words", [])
    payload["word_frequency"] = dict(Counter(abusive_words))
    return convert_numpy(payload)

# =====================================================
# MAIN ENDPOINT
# =====================================================

@app.post("/predict")
def predict(req: TextRequest):

    text = req.text.strip()

    if not text:
        return build_response({
            "toxic": False,
            "confidence": 0.0,
            "severity": "low",
            "reason": "Empty input",
            "abusive_words": [],
            "sentiment": None,
            "source": "none",
            "rules": None,
            "ml": None,
            "llm": None
        })

    # ---------------- PREPROCESS ----------------
    processed = preprocess(text)
    clean_text = processed["clean_text"]

    sentiment = analyze_sentiment(clean_text)

    # ---------------- RULE ENGINE ----------------
    abusive_hits = detect_abusive_tokens(clean_text)

    rules_confidence = 0.95 if abusive_hits else 0.0

    rules_result = {
        "triggered": len(abusive_hits) > 0,
        "abusive_words": abusive_hits,
        "confidence": rules_confidence
    }

    # ---------------- ML ENGINE ----------------
    toxic_probability = 0.0
    ml_result = None

    if model and label_encoder:
        try:
            probs = model.predict_proba([clean_text])[0]
            labels = list(label_encoder.classes_)

            # Assume binary 0=not toxic, 1=toxic
            if 1 in labels:
                toxic_index = labels.index(1)
            else:
                toxic_index = np.argmax(probs)

            toxic_probability = float(probs[toxic_index])

            pred_index = int(np.argmax(probs))
            pred_label = labels[pred_index]

            ml_result = {
                "label": str(pred_label),
                "toxicity_probability": round(toxic_probability, 3),
                "all_probabilities": {
                    str(labels[i]): round(float(probs[i]), 3)
                    for i in range(len(labels))
                }
            }

        except Exception as e:
            print("⚠️ ML prediction error:", e)

    # ---------------- LLM ENGINE ----------------
    llm_result = analyze_toxicity_llm(text)

    llm_toxic = llm_result.get("toxic", False)

    # ---------------- FINAL DECISION ----------------
    toxic = (
        toxic_probability >= 0.6
        or rules_confidence > 0
        or llm_toxic is True
    )

    # Confidence now reflects toxic confidence ONLY
    confidence = round(
        max(toxic_probability, rules_confidence),
        3
    )

    if toxic:
        if confidence > 0.85:
            severity = "high"
        elif confidence > 0.6:
            severity = "medium"
        else:
            severity = "low"
    else:
        severity = "low"

    abusive_words = list(set(
        abusive_hits +
        llm_result.get("detected_phrases", [])
    ))

    reason = (
        f"Rules: {rules_result['triggered']} | "
        f"ML toxic prob: {round(toxic_probability,2)} | "
        f"LLM toxic: {llm_toxic}"
    )

    payload = {
        "toxic": toxic,
        "confidence": confidence,
        "severity": severity,
        "reason": reason,
        "abusive_words": abusive_words,
        "sentiment": sentiment,
        "source": "hybrid",
        "rules": rules_result,
        "ml": ml_result,
        "llm": llm_result
    }

    return build_response(payload)