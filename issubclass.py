from random import randint

print("What is the output of the following code:")

while True:
    try:
        classes = [chr(randint(65, 90)) for x in range(3)]

        randomClasses = []
        for thing in classes:
            if randint(1,2) == 1:
                randomClasses.insert(-1, thing)
                continue
            if randint(1,2) != 1:
                randomClasses.insert(0, thing)
                continue

        andOr = ["and", "or"]
        andOr = andOr[randint(0,1)]

        line1 = f"class {classes[0]}:\n\tpass"
        line2 = f"class {classes[1]}({classes[0]}):\n\tpass"
        line3 = f"class {classes[2]}({classes[1]}):\n\tpass"
        line40 = "print"

        line4 = f"(issubclass({randomClasses[0]},{randomClasses[1]}) {andOr} issubclass({randomClasses[0]},{randomClasses[2]}))"
    except BaseException:
        continue
    break

    
print(line1)
print(line2)
print(line3)
print(line40+line4)

exec(line1)
exec(line2)
exec(line3)

possible = ["0", "1", str(eval(line4)), "None"]

if possible[2] == "True": possible[3] = "False"
elif possible[2] == "False": possible[3] = "True"

def answerGen():
    global possible
    order = []
    for x in range(len(possible)):
        poop = randint(0,len(possible)-1)
        while poop in order:
            poop = randint(0,len(possible)-1) 
        order.append(poop)
    finalList = []
    for x in order:
        finalList.append(possible[x])
    return finalList
        
def makeDict():
    finalList = answerGen()
    answers = {1:0 , 2:0 , 3:0 ,4:0}
    answers[1] = finalList[0]
    answers[2] = finalList[1]
    answers[3] = finalList[2]
    answers[4] = finalList[3]
    return answers 

def response():
    answers = makeDict()
    global line4

    for key, value in answers.items():
        print(str(key) + ". " + value)

    answer = False
    while answer == False:
        try:
            answer = True if answers[int(input())] == str(eval(line4)) else False
        except BaseException:
            print("Give that another go")

response()

