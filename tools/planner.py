import re
from chains.tutor_chain import generate_ai_study_plan


def extract_days(text):
    match = re.search(r"(\d+)\s*day", text.lower())
    if match:
        return match.group(1)
    return "7"


def extract_hours(text):
    match = re.search(r"(\d+)\s*hour", text.lower())
    if match:
        return match.group(1)
    return "2"


def extract_subject(text):
    text_lower = text.lower()

    subjects = [
        "physics",
        "chemistry",
        "biology",
        "math",
        "mathematics",
        "computer science",
        "artificial intelligence",
        "machine learning",
        "data science",
        "english",
        "database",
        "networking",
        "operating system",
        "software engineering",
        "web development",
        "python",
        "java",
        "c programming"
    ]

    for subject in subjects:
        if subject in text_lower:
            return subject.title()

    return "the given subject"


def study_planner_tool(user_request, context):
    subject = extract_subject(user_request)
    days = extract_days(user_request)
    hours = extract_hours(user_request)

    return generate_ai_study_plan(
        subject=subject,
        days=days,
        level="beginner",
        hours=hours,
        context=context
    )