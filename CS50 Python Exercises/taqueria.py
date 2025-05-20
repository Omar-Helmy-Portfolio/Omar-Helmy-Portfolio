# Requirements:
# Take list of items
# one after the other, until ctrl+d
# calculate their cost
# add $, and round to nearest 2 decimal places
# treat user input insensitively, ignore non-items
# Assume every item in dic is titlecased (need to lower)
########################################################
# Algortihm:
# Input dictionary
# sum = 0
# reprompt loop until ctrl+d
## try input.strip.lower excpet EOFError: break
## if input in dic: total += dic(input)
## print($ + total)
## else: break
########################################################
menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}


def main():
    total = 0.0

    while True:
        try:
            item = input("item: ").strip().lower().title()
        except EOFError:
            print("")
            break
        else:
            if item in menu:
                total += menu[item]
                print(f"Total: ${total:.2f}")
            else:
                continue


if __name__ == '__main__':
    main()
