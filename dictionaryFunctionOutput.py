'''
output
def fun(d, k,v):
	d[k]=v
'''
from random import randint

var1 = chr(randint(97,123))
var2 = chr(randint(97,123))

if randint(0,1) == 1: prnt = "print(d)"
else: prnt = ''

print("What is the output on the console of the following code:")

def fun(d,k,v):
    d[k]=v
    return(d)
dic = {}
correct = fun(dic, var1, var2)

line1=f'''
def fun(d,k,v):
    d[k]=v
    {prnt}'''
line2='''d = {}'''
line3=f'''fun(d, "{var1}", "{var2}")\n'''

print(line1)
print(line2)
print(line3)

if prnt == '': correct, incorrect = "there is no output", '{'+f"'{var1}':'{var2}'" + '}'
else:incorrect, correct = "there is no output", '{'+f"'{var1}':'{var2}'" + '}'
answers = [correct, incorrect, '{'+f"'{var2}':'{var1}'" + '}', "ValueError"]

order = []
for i in range(4):
    a = randint(1, 4)
    while a in order:
        a = randint(1,4)
    order.append(a)
    
answersOrdered = {num:ans for num, ans in sorted(zip(order, answers))}

for key,item in answersOrdered.items():
    print(str(key) + ". " + str(item))

response = False
while response == False:
    try:
        response = True if answersOrdered[int(input())] == correct else False
    except BaseException:
        print("A number. You need to type a number.")
