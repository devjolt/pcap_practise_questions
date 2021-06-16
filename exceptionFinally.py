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
print("If there is a finally block after the try block, it will:")

correct, incorrect1, incorrect2, incorrect3 = "always be executed", "sometimes be executed" , "never be executed", "cause an error"

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

