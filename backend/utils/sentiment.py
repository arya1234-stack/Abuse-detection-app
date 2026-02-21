from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Initialize once (important for performance)
analyzer = SentimentIntensityAnalyzer()

# =====================================================
# SENTIMENT ANALYSIS (VADER)
# =====================================================

def analyze_sentiment(text: str) -> dict:
    """
    Analyze sentiment using VADER.

    Returns:
        {
            "polarity": float (-1.0 → 1.0),
            "subjectivity": float (0.0 → 1.0) (approximate),
            "label": "positive" | "neutral" | "negative",
            "confidence": float (0.0 → 1.0)
        }
    """

    if not text or not text.strip():
        return {
            "polarity": 0.0,
            "subjectivity": 0.0,
            "label": "neutral",
            "confidence": 0.0
        }

    try:
        scores = analyzer.polarity_scores(text)

        compound = scores["compound"]   # -1 to +1
        pos = scores["pos"]
        neg = scores["neg"]
        neu = scores["neu"]

        # Label classification (official VADER thresholds)
        if compound >= 0.05:
            label = "positive"
        elif compound <= -0.05:
            label = "negative"
        else:
            label = "neutral"

        confidence = abs(compound)

        return {
            "polarity": round(compound, 3),
            "subjectivity": round(pos + neg, 3),  # approximation
            "label": label,
            "confidence": round(confidence, 3)
        }

    except Exception as e:
        print("⚠️ Sentiment error:", e)

        return {
            "polarity": 0.0,
            "subjectivity": 0.0,
            "label": "neutral",
            "confidence": 0.0
        }