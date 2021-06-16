'''
output:
print("a","b","c", sep= "'")
abc
a'b'c
a b b
the code is erroneous
'''


from random import randint

letGen = []
for i in range(3):
    n = chr(randint(97,122))
    while n in letGen:
        n = chr(randint(97,122))
    letGen.append(n)
    continue

things = ["=", "=", "=", "-", ",", ":", ""]
thing = things[randint(0, (len(things)-1))]


args = ["sep", "end"]
arg = args[randint(0, (len(args))-1)]

seperators = ["+", "-", "*", "%", "&", "!", "*", "@", ","]
seperator = seperators[randint(0, (len(seperators))-1)]

if thing != "=": correct, incorrect1, incorrect2, incorrect3 = "the code is erroneous", f"{letGen[0]}{letGen[1]}{letGen[2]}", f"{letGen[0]}{seperator}{letGen[1]}{seperator}{letGen[2]}", f"{letGen[0]}{letGen[1]}{letGen[2]}{seperator}"
elif arg == "sep": correct, incorrect1, incorrect2, incorrect3 = f"{letGen[0]}{seperator}{letGen[1]}{seperator}{letGen[2]}", f"{letGen[0]}{letGen[1]}{letGen[2]}", f"{letGen[0]}{letGen[1]}{letGen[2]}{seperator}", "the code is erroneous"
elif arg == "end": correct, incorrect1, incorrect2, incorrect3 = f"{letGen[0]}{letGen[1]}{letGen[2]}{seperator}", f"{letGen[0]}{letGen[1]}{letGen[2]}", f"{letGen[0]}{seperator}{letGen[1]}{seperator}{letGen[2]}", "the code is erroneous"

print("What will be the output of the following snippet?\n")

line1 = f"print('{letGen[0]}', '{letGen[1]}', '{letGen[2]}', {arg}{thing} '{seperator}')\n"

print(line1)

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
