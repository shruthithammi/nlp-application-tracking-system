# Recruiter Email NLP Classifier

ClearHire classifies recruiter messages into five application-stage intents:

- `acknowledgement`
- `assessment`
- `interview`
- `rejection`
- `offer`

## Pipeline

1. Combine email subject and body.
2. Convert text to TF-IDF features with word unigrams and bigrams.
3. Predict the class with logistic regression.
4. Return the highest class probability as the model confidence.
5. Map the class to an application status and timeline explanation.

## Training data

The repository contains 50 curated training examples (10 per class) and a
separate 10-example holdout set (2 per class). The holdout is only a small
portfolio-project sanity check, not evidence of production-level accuracy.

## Evaluate

From the repository root, with the Python virtual environment active:

```text
python ml/training/evaluate_classifier.py
```

The evaluation reports accuracy, precision, recall and F1 on the 10 held-out
examples.

## Why this is better than the first version

The original classifier was trained on only 15 short examples (3 per class).
The expanded dataset gives the model more varied phrasing and keeps a small
held-out set separate for repeatable evaluation.
