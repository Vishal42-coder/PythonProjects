questions = [
    {
        "question" : "What is the capital of India?",
        "options" : ["A. Mumbai", "B. Delhi", "C. Rajasthan", "D. Hyderabad"],
        "answer" : "B"
    },
    {
        "question" : "Which language is used for web development?",
        "options" : ["A. Java", "B. Python", "C. Rust", "D. HTML"],
        "answer" : "D"
    },
    {
        "question" : "What is the output of 4 + 26 * 32 / 6?",
        "options" : ["A. 5", "B. 10", "C. 0.9", "D. 21"],
        "answer" : "B"
    }
]

def start_quiz(questions):
    score = 0

    for question in questions:
        print('\n' + question['question'])
        for option in question['options']:
            print(option)

        user_answer = input("Enter your answer(A/B/C/D): ").upper()
        if user_answer == question['answer']:
            print('✅Correct!')
            score += 1

        else:
            print('❌Wrong! Correct answer is', question['answer'])

    print("\nQuiz Completed!")
    print(f"Your final score: {score}/{len(questions)}")

start_quiz(questions)

