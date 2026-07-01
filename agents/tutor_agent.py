from chains.tutor_chain import choose_tool, role_based_answer
from tools.calculator import calculator_tool
from tools.planner import study_planner_tool
from tools.summarizer import summarizer_tool


def tutor_agent(user_request, context):
    selected_tool = choose_tool(user_request)

    if selected_tool == "calculator":
        return calculator_tool(user_request)

    elif selected_tool == "study_planner":
        return study_planner_tool(user_request, context)

    elif selected_tool == "summarizer":
        return summarizer_tool(user_request)

    else:
        return role_based_answer(
            role="Teacher",
            question=user_request,
            context=context
        )