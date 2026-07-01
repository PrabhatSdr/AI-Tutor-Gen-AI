class TutorMemory:
    def __init__(self):
        self.student_name = ""
        self.history = []
        self.weak_areas = []

    def set_student_name(self, name):
        self.student_name = name

    def add_history(self, user_input, ai_response):
        self.history.append({
            "user": user_input,
            "ai": ai_response
        })

    def add_weak_area(self, topic):
        if topic and topic not in self.weak_areas:
            self.weak_areas.append(topic)

    def get_context(self):
        context = f"Student Name: {self.student_name}\n"

        if self.weak_areas:
            context += f"Weak Areas: {', '.join(self.weak_areas)}\n"

        if not self.history:
            context += "No previous learning history."
            return context

        context += "\nRecent Learning History:\n"

        for item in self.history[-3:]:
            context += f"\nStudent: {item['user']}\nTutor: {item['ai'][:250]}...\n"

        return context