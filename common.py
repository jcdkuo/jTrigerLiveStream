# -*- coding: UTF-8 -*-

def IF_TRUE_THEN_DO(condition, do_function):
    if (condition):
        do_function()
    else:
        print(condition "is not Ture!")


def IF_EQUAL_THEN_DO(condition1, condition2, do_function):
    if (condition1 == condition2):
        do_function()
    else:
        print("The conditions are not the same!")
        print("condition1 = " + condition1)
        print("condition2 = " + condition2)
