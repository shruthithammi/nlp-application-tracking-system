"""Curated training and small held-out evaluation data for recruiter email classification.

The runtime classifier intentionally uses a small, human-readable dataset so the
project remains easy to inspect and reproduce. In a production system this would
be replaced or supplemented with a larger, privacy-reviewed labeled dataset.
"""

TRAINING = [
    # acknowledgement
    ("thank you for applying we have received your application", "acknowledgement"),
    ("this email confirms that your application was received", "acknowledgement"),
    ("your application has been successfully submitted", "acknowledgement"),
    ("we have received your application for the position", "acknowledgement"),
    ("thank you for your interest in joining our company your application is under review", "acknowledgement"),
    ("we received your resume and application", "acknowledgement"),
    ("your application has been received and will be reviewed", "acknowledgement"),
    ("this is confirmation that we received your application", "acknowledgement"),
    ("we appreciate your application and will be in touch", "acknowledgement"),
    ("your application was successfully received by our recruiting team", "acknowledgement"),

    # assessment
    ("please complete the online assessment by friday", "assessment"),
    ("you are invited to take the coding assessment", "assessment"),
    ("assessment is the next step in the hiring process", "assessment"),
    ("please complete the technical test", "assessment"),
    ("you have been selected to proceed to our online assessment", "assessment"),
    ("please take the coding test using the assessment link", "assessment"),
    ("complete the skills assessment before the deadline", "assessment"),
    ("we would like you to complete an online test", "assessment"),
    ("your next step is a technical assessment", "assessment"),
    ("please use the link below to start your assessment", "assessment"),

    # interview
    ("we would like to invite you to an interview", "interview"),
    ("please select a time for your technical interview", "interview"),
    ("schedule an interview with our hiring team", "interview"),
    ("we would like to schedule a technical interview with you", "interview"),
    ("you have been selected for an interview", "interview"),
    ("our hiring manager would like to meet you for an interview", "interview"),
    ("please choose a convenient time for your interview", "interview"),
    ("we are pleased to invite you to the next interview round", "interview"),
    ("your next step is an interview with the engineering team", "interview"),
    ("please confirm your availability for the interview", "interview"),

    # rejection
    ("unfortunately we will not be moving forward", "rejection"),
    ("your application was not selected", "rejection"),
    ("we regret to inform you that your application was rejected", "rejection"),
    ("we have decided not to move forward with your application", "rejection"),
    ("we are unable to proceed with your candidacy", "rejection"),
    ("you were not selected for the next stage", "rejection"),
    ("thank you for your interest but we will not be moving forward", "rejection"),
    ("we have chosen to move forward with other candidates", "rejection"),
    ("your application will not proceed to the next round", "rejection"),
    ("we regret that we cannot offer you further consideration", "rejection"),

    # offer
    ("we are pleased to offer you the position", "offer"),
    ("congratulations your offer letter is attached", "offer"),
    ("employment offer next steps", "offer"),
    ("we are delighted to offer you a position with our company", "offer"),
    ("we would like to extend an offer of employment", "offer"),
    ("please review the attached offer letter", "offer"),
    ("congratulations we are offering you the role", "offer"),
    ("your employment offer is ready for review", "offer"),
    ("we are pleased to move forward with an offer", "offer"),
    ("please confirm your acceptance of the offer", "offer"),
]


HOLDOUT = [
    ("thank you for submitting your application we will review it", "acknowledgement"),
    ("your application has been received by our talent acquisition team", "acknowledgement"),

    ("please complete the online skills assessment using the link below", "assessment"),
    ("the next step is to complete a technical assessment", "assessment"),

    ("we would like to arrange an interview with the hiring manager", "interview"),
    ("please confirm your availability for a technical interview", "interview"),

    ("after careful consideration we will not proceed with your application", "rejection"),
    ("we have decided to pursue other candidates for this role", "rejection"),

    ("we are excited to extend an employment offer to you", "offer"),
    ("please review the attached employment offer and confirm acceptance", "offer"),
]