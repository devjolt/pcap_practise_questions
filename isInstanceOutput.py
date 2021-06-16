'''
class X:
	pass
classY(X):
	pass
class Z(Y):
	pass
x=X()
z=Z()
print(instance(x,Z), isinstance(z,X))
'''
from random import randint

classList = []
for i in range(3):
    classy = randint(65,90)
    while classy in classList:
        classy = randint(65,90)
    classList.append(classy)
    continue

inst = []
for i in range(3):
    num = randint(0,2)
    while num in inst:
        num = randint(0,2)
    inst.append(num)

print("What will be the output of the following snippet?")

line1 =f"class {chr(classList[0])}:\n\tpass\nclass {chr(classList[1])}({chr(classList[0])}):\n\tpass\nclass {chr(classList[2])}({chr(classList[1])}):\n\tpass\n{chr(classList[inst[0]]+32)}={chr(classList[inst[0]])}()\n{chr(classList[inst[1]]+32)}={chr(classList[inst[1]])}()\n"
line2 ="print"
linex =f"(isinstance({chr(classList[inst[0]]+32)},{chr(classList[inst[1]])}), isinstance({chr(classList[inst[1]]+32)},{chr(classList[inst[0]])}))"

print(line1 + line2 + linex)

exec(line1)
correct = (eval(linex))

answers = [(False, True), (True, True), (False, False), (True, False)]

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


        
