from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

def analyze_sentiment(text: str) -> dict:
    """
    Analyze sentiment using VADER.

    Returns:
        {
            "polarity": float (-1.0 → 1.0),
            "subjectivity": float (0.0 → 1.0),
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

        polarity = float(scores["compound"])

        # VADER does not provide subjectivity directly
        # We'll estimate subjectivity as pos + neg
        subjectivity = float(scores["pos"] + scores["neg"])

        # Label classification (VADER standard thresholds)
        if polarity >= 0.05:
            label = "positive"
        elif polarity <= -0.05:
            label = "negative"
        else:
            label = "neutral"

        confidence = min(abs(polarity), 1.0)

        return {
            "polarity": round(polarity, 3),
            "subjectivity": round(subjectivity, 3),
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