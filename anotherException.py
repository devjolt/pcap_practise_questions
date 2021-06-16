'''
Output
try:
	raise Exception
except:
	print("c")
except BaseException:
	print("a")
except Exception:
	print ("b")

c
it will cause an error xxxx
b
a



-print snippet bit
-print try raise exception
-print three of a bank of 4 options with randomly generated letters

offer a choice of: 1 error, one combination of letters, two other letters (one of which is the correct answer)


'''
from random import randint


try:
	raise Exception
except SyntaxError:
	print("c")
except:
	print("a")
except BaseException:
	print ("b")



letter = []
for i in range(4):
    l = chr(randint(65,90))
    while l in letter:
        l = chr(randint(65,90))
    letter.append(l)
    continue

exceptionList = ["SyntaxError", "Exception", "BaseException", ""]

num = []
for i in range(3):
    n = randint(0,3)
    while n in num:
        n= randint(0,3)
    num.append(n)

print("What will be the output of the following snippet?\n")

line1 = "try:\n\traise Exception"

line2 = f"except {exceptionList[num[0]]}:\n\tprint('{letter[num[0]]}')"
line3 = f"except {exceptionList[num[1]]}:\n\tprint('{letter[num[1]]}')"
line4 = f"except {exceptionList[num[2]]}:\n\tprint('{letter[num[2]]}')"

print(line1)
print(line2)
print(line3)
print(line4)

if exceptionList[num[0]] == "" or exceptionList[num[1]] == "": correct = "Error"
elif exceptionList[num[0]] == "SyntaxError": correct = letter[num[1]]
else: correct = letter[num[0]]

answers = ["Error", letter[num[1]], letter[num[0]], letter[num[2]]]

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
