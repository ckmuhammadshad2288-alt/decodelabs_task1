score = 0

print("Welcome to the General Knowledge Quiz!")
print("Answer the following 3 questions.\n")

answer = input("1. What is the capital of France? >
if answer.strip().lower() == "paris":
    print("Correct!\n")
    score += 1
else:
    print("Incorrect! The answer is Paris.\n")

answer = input("2. Which planet is known as the Re>
if answer.strip().lower() == "mars":
    print("Correct!\n")
    score += 1
else:
    print("Incorrect! The answer is Mars.\n")

answer = input("3. How many days are there in a le>
if answer.strip() == "366":
    print("Correct!\n")
    score += 1
else:
    print("Incorrect! The answer is 366.\n")

print("Quiz completed!")
print("Your final score:", score, "/ 3")
