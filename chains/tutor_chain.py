from core.llm import get_llm
from core.prompts import (
    explanation_prompt,
    notes_prompt,
    quiz_prompt,
    quiz_evaluation_prompt,
    role_prompt,
    reasoning_prompt,
    summary_prompt,
    study_planner_prompt,
    tool_router_prompt
)

llm = get_llm()

explanation_chain = explanation_prompt | llm
notes_chain = notes_prompt | llm
quiz_chain = quiz_prompt | llm
quiz_evaluation_chain = quiz_evaluation_prompt | llm
role_chain = role_prompt | llm
reasoning_chain = reasoning_prompt | llm
summary_chain = summary_prompt | llm
study_planner_chain = study_planner_prompt | llm
tool_router_chain = tool_router_prompt | llm


def explain_topic(topic, level, context):
    response = explanation_chain.invoke({
        "topic": topic,
        "level": level,
        "context": context
    })
    return response.content


def generate_notes(topic, context):
    response = notes_chain.invoke({
        "topic": topic,
        "context": context
    })
    return response.content


def generate_quiz(topic):
    response = quiz_chain.invoke({
        "topic": topic
    })
    return response.content


def evaluate_quiz(topic, quiz, answers):
    response = quiz_evaluation_chain.invoke({
        "topic": topic,
        "quiz": quiz,
        "answers": answers
    })
    return response.content


def role_based_answer(role, question, context):
    response = role_chain.invoke({
        "role": role,
        "question": question,
        "context": context
    })
    return response.content


def solve_step_by_step(problem, context):
    response = reasoning_chain.invoke({
        "problem": problem,
        "context": context
    })
    return response.content


def summarize_material(material):
    response = summary_chain.invoke({
        "material": material
    })
    return response.content


def generate_ai_study_plan(subject, days, level, hours, context):
    response = study_planner_chain.invoke({
        "subject": subject,
        "days": days,
        "level": level,
        "hours": hours,
        "context": context
    })
    return response.content


def choose_tool(user_request):
    response = tool_router_chain.invoke({
        "user_request": user_request
    })

    tool_name = response.content.strip().lower()

    allowed_tools = ["calculator", "study_planner", "summarizer", "tutor"]

    if tool_name not in allowed_tools:
        return "tutor"

    return tool_name


def full_study_workflow(topic, context):
    explanation = explain_topic(topic, "beginner", context)
    notes = generate_notes(topic, context)
    quiz = generate_quiz(topic)

    return f"""
================ EXPLANATION ================
{explanation}

================ REVISION NOTES ================
{notes}

================ PRACTICE QUIZ ================
{quiz}
"""