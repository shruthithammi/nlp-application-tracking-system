"""Inspect the curated recruiter-email training set.

The web application trains the transparent TF-IDF + logistic-regression model
at startup. This script provides a simple reproducible training-data check.
"""

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
BACKEND = ROOT / "backend"
if str(BACKEND) not in sys.path:
    sys.path.insert(0, str(BACKEND))

from app.ai.email_classifier import EmailClassifier
from app.ai.email_training_data import TRAINING


if __name__ == "__main__":
    classifier = EmailClassifier()
    print(f"Training examples: {len(TRAINING)}")
    for label in classifier.model.classes_:
        count = sum(1 for _, y in TRAINING if y == label)
        print(f"  {label}: {count}")
    print("Model: TF-IDF (1-2 grams) + Logistic Regression")
