# Requirements:
# Take an Input
# Valid or Not Depending on:
# Start with 2 Letters At Least.
# Min: 2 characters, Max: 6
# Numbers Must Be at End
# Numbers Cannot Start with 0
# No Periods, Spaces, Punctuations marks
####################################################
# Algorithm:
# import string
# Input
# Condition: IsVAlid
# check for 2 letters at start:
    ## Function: slice string & check using .isalpha
    ## if true return true, else false
# Check length using len():
    ## Fuction: if 2 < len < 6
    ## if true return true, else false
# check punctuation and space:
    ## loop: check string.punctuation in input
    ## ## if true return invalid, else true
# Check If There Are Any Numbers:
    #True: check numbers at end: loop, .isdigit()
        ## create a list for isdigit()
        ## loop to build a list of true or false depending on .isdigit
        ## If First True index in input is zero, return false
        ## If "False" Found In List from "First True index", return false
####################################################
# Implementation:
import string


def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if check_len(s) and check_first_2letters(s) and punct(s):
        if s.isalpha():
            return True
        else:
            return numbered(s)
    else:
        return False


def check_len(s):
    if 2 <= len(s) <= 6:
        return True
    else:
        return False


def check_first_2letters(s):
    return s[0:2].isalpha()


def punct(s):
    for symb in string.punctuation:
        if symb in s or " " in s:
            check = False
            break
        else:
            check = True
    return check


def numbered(s):
    is_digit = []
    for item in s:
        if item.isdigit():
            is_digit.append("True")
        else:
            is_digit.append("False")

    first_true_index = is_digit.index("True")
    # Check If First Number is Zero
    if s[first_true_index] == "0":
        return False
    else:
        pass
    # Check If Plate End is All Numbers.
    if "False" in is_digit[first_true_index: ]:
        return False
    else:
        return True


if __name__ == '__main__':
    main()

