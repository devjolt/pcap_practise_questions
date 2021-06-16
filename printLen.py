from random import randint
'''
The following code prints:
x="""
"""
printlen((x))

error
2
3
1
'''

thing = ['''"''', "'", "\n"]
letter = chr(randint(97, 122))
first = thing[randint(0,len(letter))]
second = thing[randint(0,len(letter))]
number1 = randint(1,3)
number2 = randint(1,5)

print("What is the output of the following code:\n")
line1 = f'''{letter} = {first*number1}{number2 * second}{first*number1}\nx=(len({letter}))'''

linex = f'''try:\n\t{letter} = {first*number1}{number2 * second}{first*number1}\n\tcorrect=(len({letter}))\nexcept SyntaxError:\n\tcorrect = "Error"'''

print(line1)
try:
    exec(linex)
except SyntaxError:
    correct = "Error"

if correct == "Error": correct, incorrect1, incorrect2, incorrect3 = "Error", number2 , number2 + 1, number2-1
else: correct, incorrect1, incorrect2, incorrect3 = correct, "Error" , correct + 1, correct - 1

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

