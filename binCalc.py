'''
 * Script by Matheus Avellar
 *   Binary Calculator
 *
 * In Python v3.3, there is no longer "raw_input", however most programs still run Python v2.7
 * For that reason, this script checks the version the user is running, and avoids errors.
 *
 *                  start()
 *                  /    \
 *        [3.3]  new()   old()  [2.7]
 *                  \    /
 *            ___getResult()____
 *       [+] /  [-] /    \ [*]  \ [/]
 *        add()  sub()   mult() div()
 *
'''

import os
import sys

version = float(str(sys.version_info.major) + "." + str(sys.version_info.minor))
isNew = False
if version >= 3.0:
    isNew = True

strings = {
    "operationError": "[!] You did not insert a valid operation!\n",
    "helloMessage": "\n\nRunning Python v" + str(version) + "\n\n\n -----=[Binary Python Calculator]=-----\n\n> by Matheus Avellar\n",
    "firstMessage": "Insert the first number > ",
    "operationMessage": "Insert the desired operation (+ - / *) > ",
    "thirdMessage": "Insert the second number > "
}

def start():
    print (strings["helloMessage"])
    if isNew == True:
        new()
    elif isNew == False:
        old()

def new(): # Python 3.3+
    num1 = input(strings["firstMessage"])
    opr = input(strings["operationMessage"])
    num2 = input(strings["thirdMessage"])
    getResult(num1, num2, opr)

def old(): # Python 2.7+
    num1 = raw_input(strings["firstMessage"])
    opr = raw_input(strings["operationMessage"])
    num2 = raw_input(strings["thirdMessage"])
    getResult(num1, num2, opr)

def getResult(num1, num2, opr):
    if opr == "+":
        add(num1, num2)
    elif opr == "-":
        sub(num1, num2)
    elif opr == "*":
        mult(num1, num2)
    elif opr == "/":
        div(num1, num2)
    else:
        print strings["operationError"]
        start()

def add(a,b):
    result = str(bin(int(a,2) + int(b,2))[2:])
    print a + " + " + b + " = " + result
    print str(int(a,2)) + " + " + str(int(b,2)) + " = " + str(int(result,2))

def sub(a,b):
    result = str(bin(int(a,2) - int(b,2))[2:])
    print a + " - " + b + " = " + result
    print str(int(a,2)) + " - " + str(int(b,2)) + " = " + str(int(result,2))

def mult(a,b):
    result = str(bin(int(a,2) * int(b,2))[2:])
    print a + " * " + b + " = " + result
    print str(int(a,2)) + " * " + str(int(b,2)) + " = " + str(int(result,2))

def div(a,b):
    result = str(bin(int(a,2) / int(b,2))[2:])
    print a + " / " + b + " = " + result
    print str(int(a,2)) + " * " + str(int(b,2)) + " = " + str(int(result,2))
'''
 * def cls(): #StackOverflow is lovely
 *     os.system(['clear','cls'][os.name == 'nt'])
'''
start()