'''
lst = ['a','b','c','d','e','f']
def fun(s):
    del s[2]
    return s
print(''.join(fun(lst)))
'''

from random import randint

print("What is the output of the following code?")

starterList = []
for i in range(randint(3, 8)):
    starterList.append(chr(randint(97, 122)))

stringStarterList = ''
for character in starterList:
    stringStarterList += character

listAsString = "["
for character in starterList:
    listAsString += "'" + character + "', "
listAsString = listAsString[:-2] + "]"

value = randint(2, (len(starterList)-2))

line1 = f"lst = {listAsString}\ndef fun(s):\n\tdel s[{value}]\n\treturn s\nprint(''.join(fun(lst)))"
print(line1)

def fun(s):
    global value
    del s[value]
    return s
correctAnswer = (''.join(fun(starterList)))

answers = [correctAnswer, stringStarterList, stringStarterList[:value-2]+stringStarterList[value-1:], stringStarterList[:value-1]+stringStarterList[value:]]

order = []
for x in range(4):
    x = randint(1,4)
    while x in order:
        x = randint(1,4)
    order.append(x)

answersNumbered = {number:answer for number, answer in sorted(zip(order, answers))}
for key, value in answersNumbered.items():
    print(str(key) + ". " + str(value))

answer = False
while answer == False:
    try:
        answer = True if answersNumbered[int(input())] == correctAnswer else False
    except BaseException:
        print("Type a number. Just please.")
