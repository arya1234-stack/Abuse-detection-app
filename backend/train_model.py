# train_model.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.preprocessing import LabelEncoder
import joblib
from utils.preprocessing import normalize_text

# ---------------- Load dataset ----------------
df = pd.read_csv("data/train.csv")

print("\nAvailable Columns:", df.columns.tolist())

# ---------------- Select columns (for your dataset) ----------------
text_col = "comment_text"
label_col = "toxic"

print(f"\nUsing '{text_col}' as text column")
print(f"Using '{label_col}' as label column")

# ---------------- Clean text ----------------
df[text_col] = df[text_col].astype(str).apply(normalize_text)

print("\nClass distribution:")
print(df[label_col].value_counts())

# ---------------- Encode labels ----------------
encoder = LabelEncoder()
df["label_encoded"] = encoder.fit_transform(df[label_col])

# Save encoder
joblib.dump(encoder, "label_encoder.joblib")

X = df[text_col]
y = df["label_encoded"]

# ---------------- Train-test split ----------------
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# ---------------- Pipeline ----------------
pipeline = Pipeline([
    ("tfidf", TfidfVectorizer(
        ngram_range=(1, 2),
        max_features=15000,
        min_df=2
    )),
    ("clf", LogisticRegression(
        max_iter=3000,
        class_weight="balanced"
    ))
])

# ---------------- Train ----------------
print("\nTraining model...")
pipeline.fit(X_train, y_train)

# ---------------- Evaluate ----------------
y_pred = pipeline.predict(X_test)

print("\nClassification Report:")
print(classification_report(
    y_test,
    y_pred,
    target_names=["Not Toxic", "Toxic"]
))

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

accuracy = pipeline.score(X_test, y_test)
print(f"\nModel accuracy: {accuracy * 100:.2f}%")

# ---------------- Save model ----------------
joblib.dump(pipeline, "abuse_model.joblib")

print("\n✅ Model saved as 'abuse_model.joblib'")
print("✅ Label encoder saved as 'label_encoder.joblib'")