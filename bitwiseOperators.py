from random import randint

bitwiseOps = ["<<", ">>", "&", "|"]
bitwiseOp1 = bitwiseOps[randint(0,(len(bitwiseOps)-1))]
bitwiseOp2 = bitwiseOps[randint(0,(len(bitwiseOps)-1))]

regularOps = ["+", "-"]
regularOp = regularOps[randint(0,(len(regularOps)-1))]

numbers = [x for x in range(1,4)]
number1 = numbers[randint(0,(len(numbers)-1))]
number2 = numbers[randint(0,(len(numbers)-1))]
number3 = numbers[randint(0,(len(numbers)-1))]
number4 = numbers[randint(0,(len(numbers)-1))]

line = f"{number1} {bitwiseOp1} {number2}\n"

print("What is the output of the following code:\n")
print(line)

try:
    thing = eval(line)
except BaseException:
    thing = "Error"

if thing == 0: correct, incorrect1, incorrect2, incorrect3 = thing, "Error", numbers[randint(0, len(numbers)-1)] + numbers[randint(0, len(numbers)-1)], numbers[randint(0, len(numbers)-1)]
elif thing == "Error": correct, incorrect1, incorrect2, incorrect3 = thing, numbers[randint(0, len(numbers)-1)] + numbers[randint(0, len(numbers)-1)], 0, numbers[randint(0, len(numbers)-1)]-numbers[randint(0, len(numbers)-1)]
else: correct, incorrect1, incorrect2, incorrect3 = thing, "Error", 0, numbers[randint(0, len(numbers)-1)] + numbers[randint(0, len(numbers)-1)]

order = []
for i in range(4):
    n = randint(1,4)
    while n in order:
        n = randint(1,4)
    order.append(n)

answers = [correct, incorrect1, incorrect2, incorrect3]

answersDict = {key: value for key, value in sorted(zip(order, answers))}

for key, value in answersDict.items():
    print(str(key) + ". " + str(value))

answer = False
while answer == False:
    try:
        answer = True if answersDict[int(input())] == correct else False
    except ValueError:
        print("Just one of the numbers above. Is that too much?")

        
                                                                                                                   
