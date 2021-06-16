'''
str = 'abcdef'
def fun(s):
    del s[2]
    return s
print(fun(str))
'''
from random import randint

print("What is the output of the following code?")

promptString = ''
for i in range(randint(3, 8)):
    promptString += chr(randint(97, 122))

value = randint(2, (len(promptString)-2))

line1 = f"str = '{promptString}'"
line2 = f"def fun(s):\n\tdel s[{value}]\n\treturn s\nprint(fun(str))"

print(line1)
print(line2)

'''
exec(line1)
exec(line2)
'''

correctAnswer = "error"

answers = [correctAnswer, promptString[:value], promptString[:value-1] + promptString[value:], promptString[:value] + promptString[value+1:]]

order = []
for x in range(4):
    x = randint(1,4)
    while x in order:
        x = randint(1,4)
    order.append(x)
'''
answersNumbered = {}
for number, answer in sorted(zip(order, answers)):
    answersNumbered[number+1] = answer
print(answersNumbered)
'''
answersNumbered = {number:answer for number, answer in sorted(zip(order, answers))}
for key, value in answersNumbered.items():
    print(str(key) + ". " + str(value))

answer = False
while answer == False:
    try:
        answer = True if answersNumbered[int(input())] == correctAnswer else False
    except BaseException:
        print("Type a number. Just please.")
