'''
the following snippet will output:

def f(var2,var1):
	return par2+ par1
print(f(var2=1, 2)
will output 3, 2, 1 erroneous
'''

from random import randint

varGen = []
for i in range(3):
    n = chr(randint(97,122))
    while n in varGen:
        n = chr(randint(97,122))
    varGen.append(n)
    continue

numGen = []
for i in range(3):
    n = randint(1,5)
    while n in numGen:
        n = randint(1,5)
    numGen.append(n)
    continue

operators = ["+", "-", "*", "%", "//"]
operator = operators[randint(0,4)]

if randint(0,1) == 1 : first, second = varGen[0], varGen[1]
else: first, second = varGen[1], varGen[0]
                
print("What will be the output of the following snippet?\n")

correct = 0

line1 = f"def {varGen[2]}({varGen[0]},{varGen[1]}):\n\treturn {first} {operator} {second}\nprint({varGen[2]}({first}={numGen[0]}, {numGen[1]}))\n"
linex = f"def {varGen[2]}({varGen[0]},{varGen[1]}):\n\treturn {first} {operator} {second}\ncorrect={varGen[2]}({first}={numGen[0]}, {numGen[1]}))"
print(line1)

if first == varGen[1]: correct, incorrect1, incorrect2, incorrect3 = "the code is erroneous", numGen[0], numGen[1], eval(f"{numGen[0]}{operator}{numGen[1]}")
else:
    exec(linex)
    correct, incorrect1, incorrect2, incorrect3 = correct, numGen[randint(0,1)], eval(f"{numGen[0]}{operator}{numGen[1]}"), "the code is erroneous"

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
