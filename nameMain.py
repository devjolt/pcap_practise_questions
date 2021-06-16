from random import randint

'''
what will the output  of the following in a module:
print(__name__)
__main__
moduleName.py
__moduleName__.py
main
'''

print("What will the output of the following single line of code in a module:\n")

things = ["__name__", "__name__", "__name__", "__main__", "main", "__moduleName__.py"]
thing = things[randint(0,5)]

line1 = f"print({thing})"

print(line1)

if thing == '__name__': correct, incorrect1, incorrect2, incorrect3 = things[0], things[5], things[4], "Error"
else: correct, incorrect1, incorrect2, incorrect3 = "Error", things[0], things[5], things[4] 

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

