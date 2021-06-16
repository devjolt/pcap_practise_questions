from random import randint

'''
if the class constructor is declared as below
class Class:
def __init__(self):
pass
which is valid:

object = Class(1)
=Class(1,2)
=Class(None)
=Class()
'''

clss = ''
for i in range(3): clss += chr(randint(65, 90))

inst = ''
for i in range(3): inst += chr(randint(97, 122))

print("If the class constructor is declared as below:\n")

line = f"class {clss}:\n\tdef __init__(self):\n\t\tpass"

print(line)

print("\nWhich is valid?")

correct, incorrect1, incorrect2, incorrect3 = f"{inst} = {clss}()", f"{inst} = {clss}(1)", f"{inst} = {clss}(1,2)", f"{inst} = {clss}(None)"

answers = [correct, incorrect1, incorrect2, incorrect3]

order = []
for x in range(4):
    num = randint(1,4)
    while num in order:
        num = randint(1,4)
    order.append(num)

answersDict = {num:answer for num, answer in sorted(zip(order, answers))}

print()

for key, value in answersDict.items():
    print(str(key) + ". " + str(value))

answer = False
while answer  == False:
    try:
        answer = True if answersDict[int(input())] == correct else False
    except BaseException:
        print("Number please")
