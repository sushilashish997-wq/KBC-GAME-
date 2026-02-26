questions = [
    {
        "question": "What is the capital of India?",
        "options": ["Bharat", "Bihar", "India", "Delhi"],
        "answer": 4
    },
    {
        "question": "What is the capital of Nepal?",
        "options": ["Nepal", "Bhutan", "China", "Kathmandu"],
        "answer": 4
    },
    {
        "question": "What is the capital of Pakistan?",
        "options": ["Karachi", "Lahore", "Afghanistan", "India"],
        "answer": 1
    }
]

level = [10000, 20000, 30000]

print("Welcome to KBC Game")

for i in range(len(questions)):
    print(f"\nQuestion for Rs.{level[i]}: {questions[i]['question']}")

    for j in range(len(questions[i]['options'])):
        print(f"{j+1}. {questions[i]['options'][j]}")

    answer = int(input("Enter your answer (1-4): "))

    if answer == questions[i]['answer']:
        print("Correct! You have won Rs.", level[i])
    else:
        print("Wrong answer. Game over!")
        break
else:
    # This runs ONLY if the loop finishes fully (no break)
    print("\n🎉 Congratulations! You have completed all questions 🎉")
