from random import *

exceptions = ["BaseException", "Exception"]
exceptionSelection = exceptions[randint(0, len(exceptions)-1)]

letters = [chr(randint(97,122)) for x in range(3)]

print("What is the output of the following code:\n")

answer = ''

line1 = f"try:\n\traise Exception\nexcept {exceptionSelection}:\n\tprint('{letters[0]}', end='')\nelse:\n\tprint('{letters[1]}',end='')\nfinally:\n\tprint('{letters[2]}')"
linex = f"try:\n\traise Exception\nexcept {exceptionSelection}:\n\tanswer+='{letters[0]}'\nelse:\n\tanswer+='{letters[1]}'\nfinally:\n\tanswer+='{letters[2]}'"

print(line1)

exec(linex)

print(answer)

answers = [answer]
for i in range(3):
    finalLetter = answer
    while finalLetter == answer:
        while finalLetter in answers:
            letter = ''
            letter += letters[randint(0,2)]
            if randint(0,1) == 1: letter += letters[randint(0,2)]
            finalLetter = letter
    answers.append(finalLetter)

answers.sort()

answerDict = {x+1:answers[x] for x in range(4)}

for key, value in answerDict.items():
    print(str(key) + ". " + str(value))

response = False
while response == False:
    try:
        response = True if answerDict[int(input())] == answer else False
    except ValueError:
        print("Just type a stinking number")




