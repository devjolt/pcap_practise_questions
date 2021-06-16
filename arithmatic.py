from random import randint
'''
output
v = 1+1//2+1/2+2
print(v)
4
3.5
3
4.0
'''

print("What is the output of the following code:\n")

values = [randint(1,2) for x in range(6)]

opperators = ["/", "//", "%"]

letter = chr(randint(97, 122))
    
line1 = f"{letter} = {values[0]} + {values[1]} {opperators[randint(0,(len(opperators)) - 1)]} {values[2]} + {values[3]} {opperators[randint(0,(len(opperators)) - 1)]} {values[4]} + {values[5]}"
line2 = f"print({letter})"
linex = f"thing = {values[0]} + {values[1]} {opperators[randint(0,(len(opperators)) - 1)]} {values[2]} + {values[3]} {opperators[randint(0,(len(opperators)) - 1)]} {values[4]} + {values[5]}"
print(line1)
print(line2)

exec(linex)

if type(thing) == int: correct, incorrect1, incorrect2, incorrect3 = thing/1, thing+values[0], thing-values[0], thing/2
else: correct, incorrect1, incorrect2, incorrect3 = thing/1, thing+values[0], thing-values[0], thing/2

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
