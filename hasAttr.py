from random import randint

class A:
    a=1
    def __init(self):
        self.a=0

p=A()

print(hasattr(p,'a'))


'''
what will be the output of the following code?
class A:
A=1
def __init(self):
self.a=0

print(hasattr(A,'A'))
False
True
0
1
'''

print("What will the output of the following code:\n")

value = randint(97, 122)
letter = chr(value)
LETTER = chr(value-32)

stuff = [letter, LETTER]

first = stuff[randint(0,1)]
second = stuff[randint(0,1)]

nums = []
for x in range(2):
    n = randint(1,4)
    while n in nums:
        n = randint(1,4)
    nums.append(n)

line1 = f"class {LETTER}:\n\t{LETTER} = {nums[0]}\n\tdef __init(self):\n\t\tself.{stuff[randint(0,1)]}={nums[1]}\nprint(hasattr({first},'{second}'))"
linex = f"class {LETTER}:\n\t{LETTER} = {nums[0]}\n\tdef __init(self):\n\t\tself.{stuff[randint(0,1)]}={nums[1]}\nstuff=(hasattr({first},'{second}'))"

print(line1)

try:
    exec(linex)
except BaseException:
    stuff = "Error"

if stuff == True: correct, incorrect1, incorrect2, incorrect3 = "True", "False", "Error", "None"
elif stuff == False: correct, incorrect1, incorrect2, incorrect3 = "False", "True", "Error", "None"
elif stuff == "Error": correct, incorrect1, incorrect2, incorrect3 = "Error", "False", "True", "None"
    
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

