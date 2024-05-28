import random
import time

def quiz():
    num_questions = 10
    correct_answers = 0

    for _ in range(num_questions):
        num1, num2 = random.randint(0, 9), random.randint(0, 9)
        answer = None

        print(f"{num1} x {num2}")
        start_time = time.time()

        for _ in range(3):
            try:
                answer = int(input("答え: "))
                if answer == num1 * num2:
                    print("正解！")
                    correct_answers += 1
                    time.sleep(1)
                    break
                else:
                    print("Incorrect. Try again.")
            except ValueError:
                print("Please enter a valid integer.")
        else:
            if answer is None or time.time() - start_time >= 8:
                print("Time's up or no correct answer given.")

    print(f"Score: {correct_answers} / {num_questions}")

quiz()

