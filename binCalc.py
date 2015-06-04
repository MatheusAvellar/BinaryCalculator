"""
 * Script by Matheus Avellar
 *   Binary Calculator
 *
"""

import sys

class _:
    n1 = "0"
    n2 = "0"
    opr = "+"
    ex = 0
    neg = ""
    isNew = False
    swapped = False


class c:
    PURPLE = "\033[95m"
    BLUE = "\033[94m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    FAIL = "\033[91m"
    END = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


version = float(str(sys.version_info.major) + "." + str(sys.version_info.minor))
if version >= 3.0:
    _.isNew = True


def init():
    if _.isNew:
        print ("Sorry, this version of Python is too recent. Please use v2.7")
    else:
        print (c.BOLD + "\nPython v%s\n -=[Binary Calculator ~ By Matheus Avellar]=-" + c.END + "\n") % (version)
        _.n1 = raw_input(c.BLUE + "Insert the first number > " + c.END)
        _.opr = raw_input(c.BLUE + "Insert the operation > " + c.END)
        _.n2 = raw_input(c.BLUE + "Insert the second number > " + c.END)
        fix()
        validate(_.opr)


def validate(opr):
    if opr == "+":
        add([_.n1, _.n2])
    elif opr == "-":
        if _.n2 > _.n1:
            _.n2, _.n1 = _.n1, _.n2
            _.swapped = True
        sub([_.n1, _.n2])
    elif opr == "*":
        mul()
    elif opr == "/":
        div()
    else:
        print ("\n-----------------\n" + c.YELLOW + "[validate()] @ l075 | (" + opr + ") is not a valid operation!\n" + c.END)
        init()


def fix():
    if len(_.n1) > len(_.n2):
        _.n2 = "0" + _.n2
        fix()
    elif len(_.n2) > len(_.n1):
        _.n1 = "0" + _.n1
        fix()


def _1(num):
    num = "1" + str(num)
    return num


def _0(num):
    num = "0" + str(num)
    return num


def add(array):
    _temp_value = ""
    if len(array) > 1:
        for i in xrange(0, len(array[0])):
            r = len(array[0]) - i - 1
            f = int(array[0][r]) + int(array[1][r]) + _.ex
            if f == 3:
                _temp_value = _1(_temp_value)
                _.ex = 1
            elif f == 2:
                _temp_value = _0(_temp_value)
                _.ex = 1
            elif f == 1:
                _temp_value = _1(_temp_value)
                _.ex = 0
            else:
                _temp_value = _0(_temp_value)
                _.ex = 0
            if i == len(array[0]) - 1 and _.ex == 1:
                _temp_value = _1(_temp_value)
                array.pop(0)
                array[0] = _temp_value
                add(array)
            elif i == len(array[0]) - 1 and _.ex == 0:
                array.pop(0)
                array[0] = _temp_value
                add(array)
    else:
        print (c.GREEN + "Result > " + c.END + array[0] + "\n")

def sub(array):
    _temp_value = ""
    if len(array) > 1:
        for i in xrange(0, len(array[0])):
            r = len(array[0]) - i - 1
            f = int(array[0][r]) - int(array[1][r]) - _.ex
            if f == -2:
                _temp_value = _0(_temp_value)
                _.ex = 1
            elif f == -1:
                _temp_value = _1(_temp_value)
                _.ex = 1
            elif f == 0:
                _temp_value = _0(_temp_value)
                _.ex = 0
            elif f == 1:
                _temp_value = _1(_temp_value)
                _.ex = 0
            if i == len(array[0]) - 1 and _.ex == 1:
                _temp_value = _1(_temp_value)
                array.pop(0)
                array[0] = _temp_value
                sub(array)
            elif i == len(array[0]) - 1 and _.ex == 0:
                array.pop(0)
                array[0] = _temp_value
                sub(array)
    else:
        _res = "-" if _.swapped else ""  # If n2 was greater than n1
        print(c.GREEN + "Result > " + c.END + _res + array[0] + "\n")


init()