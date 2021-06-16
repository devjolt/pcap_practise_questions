'''
class A:
    def __init__(self,v):
        self._a=v+1

a=A(0)
print(a._a)
'''
from random import randint

LETGen = chr(randint(97-32,122-32))
'''
for i in range(3):
    n = chr(randint(97-32,122-32))
    while n in letGen:
        n = chr(randint(97-32,122-32))
    letGen.append(n)
    continue
'''

letGen = []
for i in range(2):
    n = chr(randint(97,122))
    while n in letGen:
        n = chr(randint(97,122))
    letGen.append(n)
    continue

numGen = randint(1,5)

things = ["+", "-"]
thing = things[randint(0, (len(things)-1))]

seperators = ["", "_", "__"]
seperator = seperators[randint(0, (len(seperators))-1)]

letterOptions = [f"{letGen[1]}", f"{seperator}{letGen[1]}", f"{LETGen}"]
letter = letterOptions[randint(0, (len(letterOptions)-1))]


if letter != letGen[1]: correct, incorrect1, incorrect2, incorrect3 = "AttributeError", eval(f"0{thing}{numGen}"), f"None", 0
elif seperator == "__": correct, incorrect1, incorrect2, incorrect3 = "AttributeError", eval(f"0{thing}{numGen}"), f"None", 0
else: correct, incorrect1, incorrect2, incorrect3 = eval(f"0{thing}{numGen}"), "AttributeError", f"None", 0

print("What will be the output of the following snippet?\n")

line1 = f"class {LETGen}:\n\tdef __init__(self,{letGen[0]}):\n\t\tself.{seperator}{letGen[1]}={letGen[0]}{thing}{numGen}\n"
line2 = f"{letGen[1]}={LETGen}(0)\nprint({letter}.{seperator}{letGen[1]})"

print(line1)
print(line2)

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
