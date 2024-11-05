import random
import time


OPERATORS = ["+", "-", "*"]
MIN_VALUE = 3
MAX_VALUE = 15
TOTAL_QUESTIONS = 10

input("press Enter to start ")
print("------------------------")
print()
wrong = 0
start_time = time.time()

def generate_problem():
    left = random.randint(MIN_VALUE, MAX_VALUE)
    right = random.randint(MIN_VALUE, MAX_VALUE)
    operator = random.choice(OPERATORS)
    expr = str(left)+" "+ operator +" "+ str(right)
    ans = eval(expr)
    return expr, ans


for i in range(TOTAL_QUESTIONS):
    expr, ans = generate_problem()
    while True:
        guess = input(f"Problem # {i+1} : {expr} = ")
        if guess == str(ans):
            break
        wrong += 1
        
end_time = time.time()
total_time = round(end_time - start_time, 2)

print()
print("--------------------")
print(f"Well Done you have done it in {total_time} seconds! with {wrong} wrong attempts")