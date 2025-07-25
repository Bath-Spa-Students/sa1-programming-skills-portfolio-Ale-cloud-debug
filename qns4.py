# Exercise 4: Primitive Quiz

# Making a list of questions and their correct answers
quiz = {
    "What is the capital of France?": "paris",
    "What is the capital of Germany?": "berlin",
    "What is the capital of Italy?": "rome",
    "What is the capital of Spain?": "madrid",
    "What is the capital of Portugal?": "lisbon",
    "What is the capital of Netherlands?": "amsterdam",
    "What is the capital of Greece?": "athens",
    "What is the capital of Austria?": "vienna",
    "What is the capital of Switzerland?": "bern",
    "What is the capital of Norway?": "oslo"
}

# Just saying hi
print("Hey! Let's do a quick capital cities quiz 😄")

# Looping through the questions
for question, correct_answer in quiz.items():
    # Ask the question
    user_answer = input(question + " ")

    # Make both answers lowercase to ignore case differences
    if user_answer.strip().lower() == correct_answer:
        print("✅ Correct!\n")
    else:
        print(f"❌ Oops, wrong. The right answer is {correct_answer.title()}.\n")

# Ending message
print("Quiz done! Thanks for playing 🎉")
