'''
Exam block #1: Basic Concepts (17%)
Objectives covered by the block (5 exam items)

fundamental concepts: interpreting and the interpreter, compilation and the compiler, language elements, lexis, syntax and semantics, Python keywords, instructions, indenting
literals: Boolean, integer, floating-point numbers, scientific notation, strings
comments
the print() function
the input() function
numeral systems (binary, octal, decimal, hexadecimal)
numeric operators: ** * / % // + –
string operators: * +
assignments and shortcut operators

Exam block #2: Data Types, Evaluations, and Basic I/O Operations (20%)
Objectives covered by the block (6 exam items)

operators: unary and binary, priorities and binding
bitwise operators: ~ & ^ | << >>
Boolean operators: not and or
Boolean expressions
relational operators ( == != > >= < <= ), building complex Boolean expressions
accuracy of floating-point numbers
basic input and output operations using the input(), print(), int(), float(), str(), len() functions
formatting print() output with end= and sep= arguments
type casting
basic calculations
simple strings: constructing, assigning, indexing, slicing comparing, immutability

Exam block #3: Flow Control – loops and conditional blocks (20%)
Objectives covered by the block (6 exam items)

conditional statements: if, if-else, if-elif, if-elif-else
multiple conditional statements
the pass instruction
building loops: while, for, range(), in
iterating through sequences
expanding loops: while-else, for-else
nesting loops and conditional statements
controlling loop execution: break, continue

Exam block #4: Data Collections – Lists, Tuples, and Dictionaries (23%)
Objectives covered by the block (7 exam items)

simple lists: constructing vectors, indexing and slicing, the len() function
lists in detail: indexing, slicing, basic methods (append(), insert(), index()) and functions (len(), sorted(), etc.), del instruction, iterating lists with the for loop, initializing, in and not in operators, list comprehension, copying and cloning
lists in lists: matrices and cubes
tuples: indexing, slicing, building, immutability
tuples vs. lists: similarities and differences, lists inside tuples and tuples inside lists
dictionaries: building, indexing, adding and removing keys, iterating through dictionaries as well as their keys and values, checking key existence, keys(), items() and values() methods
strings in detail: ASCII, UNICODE, UTF-8, immutability, escaping using the \ character, quotes and apostrophes inside strings, multiline strings, copying vs. cloning, advanced slicing, string vs. string, string vs. non-string, basic string methods (upper(), lower(), isxxx(), capitalize(), split(), join(), etc.) and functions (len(), chr(), ord()), escape characters

Exam block #5: Functions (20%)
Objectives covered by the block (6 exam items)

defining and invoking your own functions and generators
return and yield keywords, returning results,
the None keyword,
recursion
parameters vs. arguments,
positional keyword and mixed argument passing,
default parameter values
converting generator objects into lists using the list() function
name scopes, name hiding (shadowing), the global keyword
'''

from random import randint

responses = [["A program written in a high level programming language", True],
             ["Machine code executed by computers", False],
             ["Another name for source file", False]]

def question():
    print("What is source code?")

def answer():
    try:
        response = str(input())
    except ValueError:
        print("That's not a letter")
    finally:
        return response

def printAnswers():
    global responses
    ms = {}
    first = randint(0, 2)
    print(f"a: {responses[first][0]}")
    ms["a"]= responses[first][1]
    second  = first
    while second == first: second = randint(0, 2)
    print(f"b: {responses[second][0]}")
    ms["b"] = responses[second][1]
    third = first
    while third == first or third ==second: third = randint(0, 2)
    print(f"c: {responses[third][0]}")
    ms["c"] = responses[third][1]

    print(f"{ms[answer()]}")
    
def main():
    question()
    printAnswers()

main()
