import random
import time

OPERATORS = ["+", "-", "*"]
MIN_OPERAND = 4
MAX_OPERAND = 12
total_problem = 10


def generate_problem():
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)
    operator = random.choice(OPERATORS)

    ex = str(left) + " " + operator + " " + str(right)
    answer = eval(ex)
    return ex, answer


wrong = 0
input("Press enter to start!")
print("----------------------")

start_time = time.time()

for i in range(total_problem):
    ex, answer = generate_problem()
    while True:
        guess = input("Problem #" + str(i + 1) + ": " + ex + " = ")
        if guess == str(answer):
            break
        wrong += 1

end_time = time.time()
total_time = round(end_time - start_time, 2)

print("----------------------")
print("Nice work! You finished in", total_time, "seconds!")