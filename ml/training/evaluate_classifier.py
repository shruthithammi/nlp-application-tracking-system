"""Evaluate the recruiter email classifier on held-out examples.

Run from the backend environment with:
    python ml/training/evaluate_classifier.py

The reported score is only for this small, curated holdout set. It should not be
presented as a production accuracy estimate.
"""

from pathlib import Path
import sys

from sklearn.metrics import accuracy_score, classification_report

ROOT = Path(__file__).resolve().parents[2]
BACKEND = ROOT / "backend"
if str(BACKEND) not in sys.path:
    sys.path.insert(0, str(BACKEND))

from app.ai.email_classifier import EmailClassifier
from app.ai.email_training_data import HOLDOUT


if __name__ == "__main__":
    classifier = EmailClassifier()
    texts = [text for text, _ in HOLDOUT]
    expected = [label for _, label in HOLDOUT]
    predicted = [classifier.predict("", text)[0] for text in texts]

    accuracy = accuracy_score(expected, predicted)
    print(f"Holdout examples: {len(HOLDOUT)}")
    print(f"Accuracy: {accuracy:.2%}")
    print()
    print(classification_report(expected, predicted, digits=3, zero_division=0))
