from random import randint


'''
what will be the result of executing the following code?
class A:
def a(self):
print('a')
class B:
def a(self):
print('b')
class C(A,B):
def c(self):
self.a()

o=C()
o.b()
exception
print a
b
c
'''

print("What will the output of the following code?")

numbers = []
for x in range(4):
    number = randint(97, 122)
    while number in numbers:
        number = randint(97, 122)
    numbers.append(number)

LETTERS = []
for x in range(3):
    LETTERS.append(chr(numbers[x-1]-32))

letters = []
for x in range(4):
    letters.append(chr(numbers[x-1]))

clss =LETTERS[randint(0,2)]
mthd =letters[randint(0,2)]

line1 = f"class {LETTERS[0]}:\n\tdef {letters[0]}(self):\n\t\tprint('{letters[0]}')"
line2 = f"class {LETTERS[1]}:\n\tdef {letters[0]}(self):\n\t\tprint('{letters[1]}')"
line3 = f"class {LETTERS[2]}({LETTERS[0]},{LETTERS[1]}):\n\tdef {letters[2]}(self):\n\t\tself.{letters[0]}()"
line4 = f"{letters[3]}={clss}()\n{letters[3]}.{mthd}()"

print(line1)
print(line2)
print(line3)
print(line4)

exec(f"try:\n\tclass {LETTERS[0]}:\n\t\tdef {letters[0]}(self):\n\t\t\treturn('{letters[0]}')\n\tclass {LETTERS[1]}:\n\t\tdef {letters[0]}(self):\n\t\t\treturn('{letters[1]}')\n\tclass {LETTERS[2]}({LETTERS[0]},{LETTERS[1]}):\n\t\tdef {letters[2]}(self):\n\t\t\tself.{letters[0]}()\n\t{letters[3]}={clss}()\n\tcorrect = str({letters[3]}.{mthd}())\nexcept BaseException:\n\tcorrect = 'Error'")

print(correct + "<")

if correct == "Error": incorrect1, incorrect2, incorrect3 = f"{letters[0]}", f"{letters[1]}", "None"
elif correct == letters[0]: incorrect1, incorrect2, incorrect3 = f"{letters[1]}", "Error", "None"
elif correct == letters[1]: incorrect1, incorrect2, incorrect3 = f"{letters[0]}", "Error", "None"

answers = [correct, incorrect1, incorrect2, incorrect3]
print(answers)

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
