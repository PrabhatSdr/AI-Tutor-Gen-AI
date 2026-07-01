from chains.tutor_chain import (
    explain_topic,
    generate_notes,
    generate_quiz,
    evaluate_quiz,
    role_based_answer,
    solve_step_by_step,
    summarize_material,
    generate_ai_study_plan,
    full_study_workflow
)

from core.memory import TutorMemory
from agents.tutor_agent import tutor_agent
from tools.calculator import calculator_tool


memory = TutorMemory()


def show_header():
    print("""
══════════════════════════════════════════════
             AI Academic Tutor
══════════════════════════════════════════════
""")


def show_menu(student_name):
    print(f"""
👤 Student: {student_name}

Choose an option:

1.  Ask Academic Question
2.  Explain Topic
3.  Generate Revision Notes
4.  Take Interactive Quiz
5.  Step-by-Step Problem Solving
6.  Role-Based Tutor
7.  Full Study Workflow
8.  Calculator
9.  AI Study Planner
10. Summarize Study Material
11. Smart Agent
12. View Memory
13. Exit
""")


def pause():
    input("\nPress Enter to continue...")


def take_interactive_quiz():
    topic = input("Enter quiz topic: ")

    print("\nGenerating quiz...\n")
    quiz = generate_quiz(topic)

    print("\n========== QUIZ ==========\n")
    print(quiz)

    print("\nEnter your answers.")
    print("Example: 1-a, 2-b, 3-c, 4-d, 5-a")

    answers = input("Your answers: ")

    print("\nEvaluating your answers...\n")

    result = evaluate_quiz(topic, quiz, answers)

    print("\n========== RESULT ==========\n")
    print(result)

    memory.add_history(f"Quiz on {topic}", result)


def main():
    show_header()

    name = input("Enter your name: ")
    memory.set_student_name(name)

    while True:
        show_menu(name)
        choice = input("Choose an option: ")

        context = memory.get_context()

        if choice == "1":
            question = input("Enter your academic question: ")

            answer = role_based_answer(
                role="Teacher",
                question=question,
                context=context
            )

            print("\nTutor Response:\n")
            print(answer)

            memory.add_history(question, answer)
            pause()

        elif choice == "2":
            topic = input("Enter topic: ")
            level = input("Enter level beginner/intermediate/advanced: ")

            answer = explain_topic(
                topic=topic,
                level=level,
                context=context
            )

            print("\nExplanation:\n")
            print(answer)

            memory.add_history(topic, answer)
            pause()

        elif choice == "3":
            topic = input("Enter topic: ")

            answer = generate_notes(
                topic=topic,
                context=context
            )

            print("\nRevision Notes:\n")
            print(answer)

            memory.add_history(topic, answer)
            pause()

        elif choice == "4":
            take_interactive_quiz()
            pause()

        elif choice == "5":
            problem = input("Enter problem: ")

            answer = solve_step_by_step(
                problem=problem,
                context=context
            )

            print("\nStep-by-Step Solution:\n")
            print(answer)

            memory.add_history(problem, answer)
            pause()

        elif choice == "6":
            print("\nAvailable roles:")
            print("Teacher, Examiner, Study Coach, Subject Expert")

            role = input("Choose role: ")
            question = input("Enter question: ")

            answer = role_based_answer(
                role=role,
                question=question,
                context=context
            )

            print("\nRole-Based Response:\n")
            print(answer)

            memory.add_history(question, answer)
            pause()

        elif choice == "7":
            topic = input("Enter topic: ")

            answer = full_study_workflow(
                topic=topic,
                context=context
            )

            print(answer)

            memory.add_history(topic, answer)
            pause()

        elif choice == "8":
            expression = input("Enter calculation: ")

            answer = calculator_tool(expression)

            print(answer)

            memory.add_history(expression, answer)
            pause()

        elif choice == "9":
            subject = input("Enter subject: ")
            days = input("Enter number of days: ")
            level = input("Enter your level beginner/intermediate/advanced: ")
            hours = input("How many hours can you study per day?: ")

            print("\nGenerating personalized study plan...\n")

            answer = generate_ai_study_plan(
                subject=subject,
                days=days,
                level=level,
                hours=hours,
                context=context
            )

            print(answer)

            memory.add_history(f"Study plan for {subject}", answer)
            pause()

        elif choice == "10":
            material = input("Paste study material: ")

            answer = summarize_material(material)

            print("\nSummary:\n")
            print(answer)

            memory.add_history("Summarized study material", answer)
            pause()

        elif choice == "11":
            request = input("Enter your request: ")

            print("\nSmart Agent Working...\n")

            answer = tutor_agent(
                user_request=request,
                context=context
            )

            print(answer)

            memory.add_history(request, answer)
            pause()

        elif choice == "12":
            print("\nLearning Memory:\n")
            print(memory.get_context())
            pause()

        elif choice == "13":
            print("\nThank you for using AI Academic Tutor.")
            break

        else:
            print("\nInvalid choice. Please try again.")
            pause()


if __name__ == "__main__":
    main()