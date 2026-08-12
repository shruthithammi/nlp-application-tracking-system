# Model Evaluation

## Evaluation setup

The classifier is trained on 50 curated examples:

- 10 acknowledgement
- 10 assessment
- 10 interview
- 10 rejection
- 10 offer

A separate 10-example holdout set is used for the sanity-check evaluation.

Run:

```cmd
python ml\training\evaluate_classifier.py
```

## Current result

| Metric | Result |
|---|---:|
| Holdout examples | 10 |
| Accuracy | 90.0% |
| Macro precision | 0.933 |
| Macro recall | 0.900 |
| Macro F1 | 0.893 |

Per-class F1:

| Class | F1 |
|---|---:|
| Acknowledgement | 1.000 |
| Assessment | 1.000 |
| Interview | 0.800 |
| Offer | 1.000 |
| Rejection | 0.667 |

### Interpretation

The classifier is functioning correctly on most of the curated holdout examples, but the rejection/interview confusion shows a real limitation of the tiny dataset. These metrics should not be presented as production-grade accuracy.

For a production system, the next step would be a substantially larger, privacy-reviewed dataset with train/validation/test splits and systematic error analysis.