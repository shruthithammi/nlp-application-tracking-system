MESSAGES = {
    "acknowledgement": "An acknowledgement message was detected. This confirms communication was received, but it does not indicate an assessment or interview.",
    "assessment": "An assessment-related message was detected. The next recorded step is to complete the assessment mentioned by the recruiter.",
    "interview": "An interview-related message was detected. Your next recorded step is an interview or interview scheduling action.",
    "rejection": "A rejection message was detected. This status is based on recruiter communication recorded in the system.",
    "offer": "An offer-related message was detected. Review the recruiter communication for the official offer details.",
}
def explain_status(label: str, confidence: float):
    return f"{MESSAGES.get(label, 'A recruiter communication was detected but no reliable next step was identified.')} Classification confidence: {confidence:.0%}."
