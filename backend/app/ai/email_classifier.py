from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

from app.ai.email_training_data import TRAINING


class EmailClassifier:
    """TF-IDF + logistic regression classifier for recruiter email intent.

    The model is trained at application startup from a small curated dataset.
    This is intentionally transparent and reproducible for the portfolio project.
    """

    def __init__(self):
        texts = [text for text, _ in TRAINING]
        labels = [label for _, label in TRAINING]

        self.vectorizer = TfidfVectorizer(
            ngram_range=(1, 2),
            sublinear_tf=True,
            strip_accents="unicode",
        )
        features = self.vectorizer.fit_transform(texts)

        self.model = LogisticRegression(
            max_iter=2000,
            C=4.0,
            class_weight="balanced",
        )
        self.model.fit(features, labels)

    def predict(self, subject: str, body: str):
        text = f"{subject} {body}".lower().strip()
        features = self.vectorizer.transform([text])
        probabilities = self.model.predict_proba(features)[0]
        index = probabilities.argmax()
        label = str(self.model.classes_[index])
        confidence = float(probabilities[index])
        return label, confidence


classifier = EmailClassifier()
