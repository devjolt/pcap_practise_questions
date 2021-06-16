'''
what will be the output:
x = 16
while x>0:
	print('*', end='')
	x//=2
******
the code will enter an infinite loop
'''

from random import randint

rangeGen = []
for i in range(2):
    n = randint(0,10)
    while n in rangeGen:
        n = randint(1,10)
    rangeGen.append(n)
    continue

char = (chr(randint(42, 46)))

choice = ["<", ">", "<=", ">="]
smallerGreater = choice[randint(0,3)]


print("What will be the output of the following snippet?\n")




count = 0




line1 = f"x = {rangeGen[0]*2}\nwhile x {smallerGreater}{rangeGen[1]//2}:\n\tprint('{char}',end='')\n\tx//=2\n"
linex = f"x = {rangeGen[0]*2}\nwhile x {smallerGreater}{rangeGen[1]//2}:\n\tcount+=1\n\tx//=2"
print(line1)

if smallerGreater == "<" and rangeGen[0] == 0:correct, incorrect1, incorrect2, incorrect3 = "the code will enter an infinite loop", '', rangeGen[0] * char, rangeGen[0]//2 * char
else:
    exec(linex)

    if count == 0:correct, incorrect1, incorrect2, incorrect3 = '', rangeGen[0] * char, rangeGen[0]//3 * char, "the code will enter an infinite loop"
    else: correct, incorrect1, incorrect2, incorrect3 = count*char, '', rangeGen[0]//3 * char, "the code will enter an infinite loop"

answers = [correct, incorrect1 , incorrect2, incorrect3]

order = []
for i in range(4):
    num = randint(1,4)
    while num in order:
        num = randint(1,4)
    order.append(num)

answerDict = {key: value for key, value in sorted(zip(order, answers))}

for key, value in answerDict.items():
    print(str(key) + ". " + str(value))

answer = False
while answer == False:
    try:
        answer = True if answerDict[int(input())] == correct else False
    except BaseException:
        print("Numbers. Type numbers. One of the four above.")
