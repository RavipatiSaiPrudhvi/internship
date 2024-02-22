def run_quiz(questions):
    score = 0
    for question, answer in questions.items():
        print(question)
        user_answer = input("Your answer: ").lower()
        if user_answer == answer.lower():
            print("Correct!\n")
            score += 1
        else:
            print("Incorrect!\n")
    print("Quiz ended! You got {} out of {} questions correct.".format(score, len(questions)))


if __name__ == "__main__":
    quiz_questions = {
        "What is the capital of France?": "Paris",
        "Who wrote 'Romeo and Juliet'?": "William Shakespeare",
        "What is the powerhouse of the cell?": "Mitochondria"
    }

    print("Welcome to the Quiz Game!\n")
    run_quiz(quiz_questions)
