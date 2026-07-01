from chains.tutor_chain import summarize_material


def summarizer_tool(user_request):
    cleaned_text = user_request.replace("summarize", "")
    cleaned_text = cleaned_text.replace("summary", "")
    cleaned_text = cleaned_text.strip()

    if not cleaned_text:
        return "Please provide study material to summarize."

    return summarize_material(cleaned_text)