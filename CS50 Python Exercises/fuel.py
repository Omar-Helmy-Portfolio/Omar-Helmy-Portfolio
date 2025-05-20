# Requirements:
# Prompt user for x/y
# x,y are integers
# Output Percentage, rounded to nearest integer
# output E,F as Empty and Full for 1%, 99%
######################################################
# Algorithm:
# input a fraction
# split function to get n1, n2
# TRy float(input)
### if not ok, reprompt user
### if ok, continue
# Calculate percentage
# int Percentage
# check if <=1% : output E
# check if >=99% : output F
# else: output percentage
########################################################
# Implementation:
def main():
    while True:
        try:
            fraction = input("Fraction as X/Y: ")
            percent = percentage(fraction)
            if percent > 100:
                continue
            elif percent <= 1:
                print("E")
            elif percent >= 99:
                print("F")
            else:
                print(str(percent) + "%")
            break
        except (ValueError, ZeroDivisionError):
            pass


def percentage(fraction):
    x,y = fraction.split("/")
    x,y = int(x),int(y)
    percent = x/y * 100
    return round(percent)


if __name__ == '__main__':
    main()
