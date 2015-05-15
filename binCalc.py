"""
 * Script by Matheus Avellar
 *   Binary Calculator
 *
 * In Python v3.3, there is no longer "raw_input", however most programs still run Python v2.7
 * For that reason, this script checks the version the user is running, and tries to avoid errors.
 * It is more recommended that you run this on 2.7 though.
 *
 *                  start()
 *                  /    \
 *        [3.3]  new()   old()  [2.7]
 *                  \    /
 *                 validate()
 *                     |
 *                  result()
 *
"""

import sys

version = float(str(sys.version_info.major) + "." + str(sys.version_info.minor))

main = {
    "num1": "0",
    "num2": "0",
    "opr": "+",
    "ex": 0,
    "neg": "",
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


def new():  # Python 3.3
    main["num1"] = input(main["strings"]["firstMessage"])
    main["opr"] = input(main["strings"]["operationMessage"])
    main["num2"] = input(main["strings"]["thirdMessage"])
    fix()
    validate(main["opr"])


def old():  # Python 2.7
    main["num1"] = raw_input(main["strings"]["firstMessage"])
    main["opr"] = raw_input(main["strings"]["operationMessage"])
    main["num2"] = raw_input(main["strings"]["thirdMessage"])
    fix()
    validate(main["opr"])


def validate(opr):
    if opr == "+" or opr == "-" or opr == "*" or opr == "/":
        result()
    else:
        print ("[validate()] @ l075 | " + main["strings"]["operationError"])
        start()


def fix():
    _a = str(len(main["num1"]))
    _b = str(len(main["num2"]))
    if _a > _b:
        main["num2"] = "0" + main["num2"]
        fix()
    elif _b > _a:
        main["num1"] = "0" + main["num1"]
        fix()
    elif main["opr"] == "-" and int(main["num1"]) < int(main["num2"]):
        invert()
        main["neg"] = "-"


def invert():
    n3 = main["num1"]
    main["num1"] = main["num2"]        
    main["num2"] = n3



def _1():
    main["result"] = "1" + main["result"]


def _0():
    main["result"] = "0" + main["result"]


def result():
    if main["opr"] == "+":
        for i in xrange(0, len(main["num1"])):
            e = len(main["num1"]) - i - 1
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
            if i == (e + 1) and main["ex"] == 1:
                _1()
        finalN1 = int(main["num1"],2)
        finalN2 = int(main["num2"],2)
        finalR = int(main["result"],2)

        print ("  " + main["num1"])           #
        print ("+ " + main["num2"])           # Binary result
        print ("- - - - - - -")               #
        print ("= " + main["result"])         #
        print ("")
        print ("  " + str(finalN1))           #
        print ("+ " + str(finalN2))           # Decimal result
        print (" - - - - - - -")              #
        print ("= " + str(finalR))            #
        print ("")
        print ("  " + str(hex(finalN1)[2:]))  #
        print ("+ " + str(hex(finalN2)[2:]))  # Hexadecimal result
        print (" - - - - - - -")              #
        print ("= " + str(hex(finalR)[2:]))   #
    elif main["opr"] == "-":
        for i in xrange(0, len(main["num1"])):
            e = len(main["num1"]) - i - 1
            f = int(main["num1"][e]) - int(main["num2"][e]) - main["ex"]
            if f == -2:
                _0()
                main["ex"] = 1
            elif f == -1:
                _1()
                main["ex"] = 1
            elif f == 0:
                _0()
                main["ex"] = 0
            elif f == 1:
                _1()
                main["ex"] = 0
            if i == (e + i) and main["ex"] == 1:
                _1()

        if main["neg"] != "":
            invert()

        finalN1 = int(main["num1"],2)
        finalN2 = int(main["num2"],2)
        finalR = int(main["result"],2)

        print ("  " + main["num1"])                        #
        print ("- " + main["num2"])                        # Binary result
        print ("- - - - - - -")                            #
        print ("= " + main["neg"] + main["result"])        #
        print ("")
        print ("  " + str(finalN1))                        #
        print ("- " + str(finalN2))                        # Decimal result
        print (" - - - - - - -")                           #
        print ("= " + main["neg"] + str(finalR))           #
        print ("")
        print ("  " + str(hex(finalN1)[2:]))               #
        print ("- " + str(hex(finalN2)[2:]))               # Hexadecimal result
        print (" - - - - - - -")                           #
        print ("= " + main["neg"] + str(hex(finalR)[2:]))  #


start()
