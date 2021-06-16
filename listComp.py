from random import randint

print("What is the output of the following code:\n")

x,y = 0,0
while x >= y:
    x, y = randint(0, 19), randint(1, 20)
values = [x,y]

line0 = "print"
line1 = f"(len([i for i in range({x},{y})]))\n"

print(line0+line1)

answers = []
answers.append(eval(line1))
answers.append(values[0])
answers.append(values[1])

poop = randint(0,1)
if poop == 0: answers.append(eval(line1)-1)
elif poop == 1: answers.append(eval(line1)+1)

order = []
for x in range(len(answers)):
    poop = randint(0, len(answers)-1)
    while poop in order:
        poop = randint(0, len(answers)-1)
    order.append(poop)

finalList = [answers[x] for x in order]
answers = {a:finalList[a] for a in range(4)}

for key, item in answers.items():
    print(f"{int(key)+1}. {item}")

answer = False
while answer == False:
    try:
        answer = True if answers[int(input())-1] == int(eval(line1)) else False
    except BaseException:
        ("Just a number here will do the job")
                                


