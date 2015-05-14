"""
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
 *        add()  sub()   mul() div()
 *
"""

import os
import sys

version = float(str(sys.version_info.major) + "." + str(sys.version_info.minor))

main = {
    "num1": "0",
    "num2": "0",
    "opr": "+",
    "ex": 0,
    "isNew": False,
    "strings": {
        "operationError": "[!] You did not insert a valid operation!\n",
        "helloMessage": "\n\nPython v" + str(
            version) + "\n\n\n -=[Binary Python Calculator]=--\n\n> by Matheus Avellar\n",
        "firstMessage": "Insert the first number > ",
        "operationMessage": "Insert the desired operation (+ - / *) > ",
        "thirdMessage": "Insert the second number > "
    },
    "result": ""
}

if version >= 3.0:
    main["isNew"] = True


def start():
    print (main["strings"]["helloMessage"])
    if main["isNew"]:
        new()
    else:
        old()


def new():  # Python 3.3+
    main["num1"] = input(main["strings"]["firstMessage"])
    main["opr"] = input(main["strings"]["operationMessage"])
    main["num2"] = input(main["strings"]["thirdMessage"])
    getfunc(main["opr"])


def old():  # Python 2.7+
    main["num1"] = raw_input(main["strings"]["firstMessage"])
    main["opr"] = raw_input(main["strings"]["operationMessage"])
    main["num2"] = raw_input(main["strings"]["thirdMessage"])
    fix()
    getfunc(main["opr"])


def getfunc(opr):
    if opr == "+":
        add()
    elif opr == "-":
        print ("[getfunc()] @ l071 | -")
    elif opr == "*":
        print ("[getfunc()] @ l073 | *")
    elif opr == "/":
        print ("[getfunc()] @ l075 | /")
    else:
        print ("[getfunc()] @ l077 | " + main["strings"]["operationError"])
        start()


def fix():
    _a = str(len(main["num1"]))
    _b = str(len(main["num2"]))
    # print ("[fix()] @ l084 | " + main["num1"] + " " + main["opr"] + " " + main["num2"])
    if _a > _b:
        main["num2"] = "0" + main["num2"]
        fix()
    elif _b > _a:
        main["num1"] = "0" + main["num1"]
        fix()


def _1():
    main["result"] = "1" + main["result"]


def _0():
    main["result"] = "0" + main["result"]


def add():
    for i in xrange(0, len(main["num1"])):
        e = len(main["num1"]) - i - 1
        # print ("[add()] @ l104 | " + str(e) + " ~ " + str(i))
        f = int(main["num1"][e]) + int(main["num2"][e]) + main["ex"]
        if f == 3:
            _1()
            main["ex"] = 1
        elif f == 2:
            _0()
            main["ex"] = 1
        elif f == 1:
            _1()
            main["ex"] = 0
        else:
            _0()
            main["ex"] = 0
        # print ("[add()] @ l118 | " + str(i) + " // " + str(main["ex"]) + " // " + str(len(main["num1"])))
        if i == len(main["num1"]) - 1 and main["ex"] == 1:
            _1()
    finalN1 = int(main["num1"],2)
    finalN2 = int(main["num2"],2)
    finalR = int(main["result"],2)

    print ("  " + main["num1"])
    print ("+ " + main["num2"])
    print ("- - - - - - -")
    print ("= " + main["result"])
    print ("")
    print ("  " + str(finalN1))
    print ("+ " + str(finalN2))
    print (" - - - - - - -")
    print ("= " + str(finalR))
    print ("")
    print ("  " + str(hex(finalN1)[2:]))
    print ("+ " + str(hex(finalN2)[2:]))
    print (" - - - - - - -")
    print ("= " + str(hex(finalR)[2:]))


def cls():  # StackOverflow is lovely
    os.system(['clear', 'cls'][os.name == 'nt'])


start()