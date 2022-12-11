from Question import Question


question_prompts = [
    "What was the first FPS?\n(a) Wolfenstein\n(b) Quake\n(c) Doom\n\n",
    "\nWhat race in Starcraft constructs Pylons?\n(a) Terran\n(b) Protoss\n(c) Zerg\n\n",
    "\nWhat is the most powerfull gun in Quake2?\n(a) BFG\n(b) Rocket Launcher\n(c) Rail Gun\n\n"
]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "b"),
    Question(question_prompts[2], "a"),
]


def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("\nYou got " + str(score) + "/" + str(len(questions)) + " correct.")


run_test(questions)
