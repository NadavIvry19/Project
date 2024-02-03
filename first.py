import random
import time

MAX = 12
MIN = 3
OPERATORS = ['+', '-', '*', '%']
TOTAL = 10


def prob():
    right = random.randint(MIN, MAX)
    left = random.randint(MIN, MAX)
    operator = random.choice(OPERATORS)

    expression = str(left) + ' ' + operator + ' ' + str(right)
    user_answer = eval(expression)
    return expression, user_answer


wrong = 0
input('press Enter to start!')
print('--------------------')

start_time = time.time()

for i in range(TOTAL):
    expr, answer = prob()
    while True:
        guess = input("Problem #" + str(i + 1) + ' ' + expr + " = ")
        if guess == str(answer):
            break
        wrong += 1

end_time = time.time()
total_time = round(end_time - start_time, 2)

print('-----------')
print('Nice work!, you did it in', total_time, 'seconds!')
print(f'you gave {wrong} wrong answers!')
