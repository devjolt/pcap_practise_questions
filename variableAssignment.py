from random import randint
import re

'''
output
x,y,z = 3,2,1
z,y,x = x,y,z
print(x,y,z)
123 etc

'''
print("What will the output of the following code?")

letters = []
for x in range(3):
    letter = chr(randint(97, 122))
    while letter in letters:
        letter = chr(randint(97, 122))
    letters.append(letter)

numbers = []
for x in range(3):
    number = randint(1, 10)
    while number in numbers:
        number = randint(1, 10)
    numbers.append(number)

orders1 = []
for x in range(3):
    order = randint(0, 2)
    while order in orders1:
        order = randint(0, 2)
    orders1.append(order)

orders2 = []
for x in range(3):
    order = randint(0, 2)
    while order in orders2:
        order = randint(0, 2)
    orders2.append(order)

line1 = f"{letters[0]}, {letters[1]}, {letters[2]} = {numbers[0]}, {numbers[1]}, {numbers[2]}"
line2 = f"{letters[orders1[0]]}, {letters[orders1[1]]}, {letters[orders1[2]]} = {letters[orders2[0]]}, {letters[orders2[1]]}, {letters[orders2[2]]}"
line3 = f"{letters[0]}, {letters[1]}, {letters[2]}"

pnt = "print("

print(line1)
print(line2)
print(pnt + line3 + ")")

exec(line1)
exec(line2)

correct = str(eval(line3))
correct = re.sub('[(,)]', '', correct)

answers = []
answers.append(correct.strip(","))
for x in range(2):
    answer = f"{numbers[randint(0,2)]} {numbers[randint(0,2)]} {numbers[randint(0,2)]}"
    while answer in answers:
        answer = f"{numbers[randint(0,2)]} {numbers[randint(0,2)]} {numbers[randint(0,2)]}"
    answers.append(answer)
answers.append("Error")

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
