import re
import sympy as sp


def calculator_tool(user_request):
    try:
        expression = user_request.lower()

        remove_words = [
            "calculate",
            "what is",
            "solve",
            "find",
            "answer",
            "please",
            "?"
        ]

        for word in remove_words:
            expression = expression.replace(word, "")

        expression = expression.strip()

        allowed_pattern = r"^[0-9+\-*/().\s]+$"

        if not re.match(allowed_pattern, expression):
            return """
Tool Used: Calculator

Please enter a clear basic mathematical expression.

Example:
25 * 4 + 10
"""

        result = sp.sympify(expression)

        return f"""
Tool Used: Calculator

Expression:
{expression}

Result:
{result}
"""

    except Exception:
        return """
Tool Used: Calculator

I could not calculate this expression.

Example:
25 * 4 + 10
"""