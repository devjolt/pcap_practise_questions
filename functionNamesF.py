'''
knowing that the function names f() resides in the module
named m and the code contains the following import statement:
from f import m
chose the right way to invoke the function
'''
from random import randint

function = chr(randint(97,123))
module = chr(randint(97,123))

if randint(0,1) == 1: first, second, correct, incorrect = function, module, "it cannot be called", f"{function}()"
else: second, first, correct, incorrect = function, module, f"{function}()", "it cannot be called"

print(f'''Knowing that the function knowing that the function named {function}() resides in the module
named {module} and the code contains the following import statement:

from {first} import {second}

Choose the right way to invoke the function.''')

if first == second: correct, incorrect = "it cannot be called", f"{function}()"

answers = [correct, incorrect, f"{module}.{function}()", f"{function}"]

order = []
for i in range(4):
    a = randint(1, 4)
    while a in order:
        a = randint(1,4)
    order.append(a)
    
answersOrdered = {num:ans for num, ans in sorted(zip(order, answers))}

for key,item in answersOrdered.items():
    print(str(key) + ". " + str(item))

response = False
while response == False:
    try:
        response = True if answersOrdered[int(input())] == correct else False
    except BaseException:
        print("A number. You need to type a number.")
    
