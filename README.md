# nlp-application-tracking-system — NLP Application Tracking & Hiring Transparency

ClearHire is an end-to-end application tracking system for candidates. It records job applications, analyzes recruiter email communication, updates application status, maintains a timeline, and provides a plain-language explanation of the detected next step.

> **Transparency principle:** ClearHire only reports information that has been provided to the system. It does not claim access to a company's private hiring system and does not invent recruiter decisions.

## What the project demonstrates

- REST API development with **FastAPI**
- **JWT authentication** for protected endpoints
- Relational persistence with **SQLAlchemy** and SQLite/PostgreSQL
- **NLP text classification** using TF-IDF + Logistic Regression
- Five-class recruiter email intent detection:
  - acknowledgement
  - assessment
  - interview
  - rejection
  - offer
- Confidence scoring from model class probabilities
- Automatic application-status and timeline updates
- Explainable status messages
- React + Vite frontend
- pytest API/model tests
- Docker-based local deployment structure

## Architecture

```text
                    ┌──────────────────────┐
                    │      React + Vite    │
                    │    Candidate UI      │
                    └──────────┬───────────┘
                               │ REST + JWT
                               ▼
                    ┌──────────────────────┐
                    │       FastAPI        │
                    │ Authentication/API   │
                    └──────────┬───────────┘
                               │
             ┌─────────────────┼─────────────────┐
             ▼                 ▼                 ▼
       Application DB     NLP Classifier     Timeline
       SQLite/Postgres    TF-IDF + LR        + Explanation
                               │
                               ▼
                 ┌─────────────────────────┐
                 │ Recruiter Email Intent  │
                 │ 5 classes + confidence  │
                 └─────────────────────────┘
```

## NLP pipeline

```text
Email subject + body
        ↓
Text normalization
        ↓
TF-IDF vectorization
(unigrams + bigrams)
        ↓
Logistic Regression
        ↓
Predicted intent + probability
        ↓
Application status
        ↓
Timeline event + explanation
```

The runtime classifier is trained from a small, human-readable curated dataset in `backend/app/ai/email_training_data.py`. This makes the project reproducible and easy to inspect.

## Local setup — Windows Command Prompt

### 1. Backend

From the repository root:

```cmd
python -m venv .venv
.venv\Scripts\activate
pip install -r backend\requirements.txt
```

Start the API:

```cmd
cd backend
uvicorn app.main:app --reload
```

API documentation:

```text
http://127.0.0.1:8000/docs
```

### 2. Frontend

Open a second VS Code terminal:

```cmd
cd frontend
npm install
npm run dev
```

Open:

```text
http://localhost:5173
```

## Run the NLP evaluation

From the repository root, with the virtual environment active:

```cmd
python ml\training\evaluate_classifier.py
```

The evaluation uses a separate 10-example holdout set. It is deliberately small and curated, so the resulting metric should **not** be described as production model accuracy.

## Run tests

From the repository root:

```cmd
pip install -r requirements-dev.txt
pytest
```

The tests cover:

- health endpoint
- registration/login
- protected application creation
- recruiter email classification
- all five classifier intents

## Example

Input:

```text
Subject:
Interview Invitation

Body:
We would like to invite you to a technical interview.
Please confirm your availability.
```

Possible result:

```text
Classification: INTERVIEW
Confidence: model probability
Application status: INTERVIEW
```

The application timeline is updated with the detected event.

## Repository structure

```text
nlp-application-tracking-system/
├── backend/
│   ├── app/
│   │   ├── ai/
│   │   │   ├── email_classifier.py
│   │   │   ├── email_training_data.py
│   │   │   └── status_explainer.py
│   │   ├── api/
│   │   ├── db/
│   │   ├── models/
│   │   └── schemas/
│   └── tests/
├── frontend/
│   └── src/
├── ml/
│   ├── notebooks/
│   └── training/
│       ├── train_classifier.py
│       └── evaluate_classifier.py
├── docs/
│   ├── api-reference.md
│   ├── architecture.md
│   ├── database-schema.md
│   └── nlp-classifier.md
├── deployment/
├── .github/
├── requirements-dev.txt
└── README.md
```

## Limitations

The current classifier is a portfolio-scale demonstration trained on a small curated dataset. Real-world recruiter communication is more varied, so a production system would require a larger privacy-reviewed labeled dataset, stronger validation, monitoring, and model/version management.

## Resume-ready description

**nlp-application-tracking-system — NLP Application Tracking & Hiring Transparency**

- Built a FastAPI + React application that tracks job applications and converts recruiter email signals into structured application-status updates.
- Developed a five-class NLP classifier using **TF-IDF n-gram features and Logistic Regression**, returning class probabilities and human-readable explanations.
- Implemented **JWT-secured REST APIs**, application timelines, automated status transitions, and pytest coverage for authentication and NLP workflows.
