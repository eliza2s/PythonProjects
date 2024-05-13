import random
import time

OPERATORS = ["+", "-", "*"]
MIN_OPERAND =2
MAX_OPERAND = 10
TOTAL_QUESTIONS = 10

def generate_problems():
    left_operand = random.randint(MIN_OPERAND, MAX_OPERAND)
    right_operand = random.randint(MIN_OPERAND, MAX_OPERAND)
    operator = random.choice(OPERATORS)

    expression = str(left_operand) + operator + str(right_operand)
    actual_answer = eval(expression)
    return expression, actual_answer

wrong_answers=0
input("press enter to start")
print("----------------------")
start_time= time.time()

for i in range(TOTAL_QUESTIONS):
    expression, actual_answer = generate_problems()
    while True:
        your_answer = input("question number "+ str(i+1) +" : "+ expression + " = ")
        if your_answer == str(actual_answer):
           break
        else:
            wrong_answers+= 1
end_time=time.time()
total_time = round(end_time-start_time,1)

print("you finished in "+ str(total_time)+ "seconds")
print("----------------------")





