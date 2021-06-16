'''
How many lines will be sent?
ls = [[c for c in range(2)] for r in range(3)]
for x in ls:
	if len(x) < 2:
		print()
two
one
three
zero
'''
from random import randint

rangeGen = []
for i in range(3):
    n = randint(1,10)
    while n in rangeGen:
        n = randint(1,10)
    rangeGen.append(n)
    continue

smallerGreater = ["<", ">", "<=", ">="]

print("How many lines will be sent by the following snippet?\n")

count = 0

line1 = f"ls = [[c for c in range({rangeGen[0]})] for r in range({rangeGen[1]})]"
line2 = f"for x in ls:\n\tif len(x) {smallerGreater[randint(0,3)]} {rangeGen[2]}:\n\t\t"
prnt = "print('')"
ans = "count+=1"
print(line1)
print(line2+prnt)
exec(line1)
exec(line2+ans)

if count == 0: correct, incorrect1, incorrect2, incorrect3 = count, rangeGen[0], rangeGen[1], rangeGen[2]
else: correct, incorrect1, incorrect2, incorrect3 = count, rangeGen[0], rangeGen[2], 0

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
