from random import randint
'''
The following code prints:
x="""
"""
printlen((x))

error
2
3
1
'''


values = []
for x in range(3):
    values.append(randint(1,5))

symbols = ["<", ">", "==",]

andOr = ["and", "or"]

letters = []
for x in range(3):
    letter = chr(randint(97, 122))
    while letter in letters:
        letter = chr(randint(97, 122))
    letters.append(letter)

print(f"What value is assigned to {letters[0]}:")
    
line1 = f"{letters[0]} = {values[0]}\n{letters[1]} = {values[1]}\n{letters[2]} = {values[2]}"
line2 = f"{letters[0]} = {letters[1]} {symbols[randint(0,1)]} {letters[2]} or {letters[2]} {symbols[randint(0,1)]} {letters[1]} and {letters[1]} {symbols[randint(0,1)]} {letters[2]} or {letters[2]} {symbols[randint(0,1)]} {letters[1]}"

print(line1)
print(line2)

exec(line1)
exec(line2)

correct = x
if correct == True: correct, incorrect1, incorrect2, incorrect3 = correct, "False" , 0, values[0]
else: correct, incorrect1, incorrect2, incorrect3 = "False", "True" , 0, values[0]

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
