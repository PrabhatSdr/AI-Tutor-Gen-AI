from langchain_core.prompts import ChatPromptTemplate


explanation_prompt = ChatPromptTemplate.from_template("""
You are a friendly AI academic tutor.

Student context:
{context}

Explain the topic:
{topic}

Student level:
{level}

Rules:
- Use simple language
- Use bullet points
- Give one small example
- Keep it clear and student-friendly
""")


notes_prompt = ChatPromptTemplate.from_template("""
You are a revision notes generator.

Student context:
{context}

Create revision notes for:
{topic}

Format:
1. Definition
2. Key Points
3. Important Terms
4. Short Summary
""")


quiz_prompt = ChatPromptTemplate.from_template("""
Generate an interactive quiz for this topic:
{topic}

Rules:
- Generate exactly 5 MCQ questions
- Each question must have 4 options: a, b, c, d
- Do NOT provide the answer key
- Keep the quiz clear

Format:

1. Question text?
a) option
b) option
c) option
d) option
""")


quiz_evaluation_prompt = ChatPromptTemplate.from_template("""
You are an examiner.

Topic:
{topic}

Quiz:
{quiz}

Student Answers:
{answers}

Evaluate the answers.

Provide:
1. Correct Answers
2. Student Score out of 5
3. Explanation for each answer
4. Weak areas to revise
5. Short motivational feedback
""")


role_prompt = ChatPromptTemplate.from_template("""
Student context:
{context}

You are acting as a {role}.

Student question:
{question}

Role instructions:
Teacher: Explain clearly and simply.
Examiner: Ask exam-style questions and mention marks.
Study Coach: Give study strategy and motivation.
Subject Expert: Give deeper technical explanation.
""")


reasoning_prompt = ChatPromptTemplate.from_template("""
Student context:
{context}

Solve this academic problem step by step:

{problem}

Rules:
- Break the answer into clear steps
- Explain each step simply
- Give the final answer clearly
""")


summary_prompt = ChatPromptTemplate.from_template("""
Summarize this study material:

{material}

Rules:
- Keep it short
- Mention only important points
- Do not add unrelated content
""")


study_planner_prompt = ChatPromptTemplate.from_template("""
You are an academic study coach.

Create a personalized study plan.

Student context:
{context}

Subject:
{subject}

Total days:
{days}

Student level:
{level}

Daily study hours:
{hours}

Rules:
- Create a different task for each day
- Do not repeat the same sentence every day
- Divide into learning, practice, revision, and mock test phases
- Include what to study and what to practice
- Keep the plan realistic

Format:

Study Plan for {subject}

Day 1:
- Topic:
- Activities:
- Practice:
- Goal:
""")


tool_router_prompt = ChatPromptTemplate.from_template("""
You are an AI tool router for an academic tutor.

User request:
{user_request}

Available tools:
calculator - use for math calculations
study_planner - use for creating study plans
summarizer - use for summarizing study material
tutor - use for general academic questions

Return ONLY one word:
calculator
study_planner
summarizer
tutor
""")