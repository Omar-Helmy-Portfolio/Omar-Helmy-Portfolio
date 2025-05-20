# Requirements:
# take items, 1 per line
# count each item occurences
# return list of items (Capitalized) in order with number of occurences.
###########################################################################
# Algorithm:
# Create List
# while true:try input items lower cased and stripped
# add item to list
# except EOFError: count_items(list) function and break
## Count_items:
## create unique list
## create count listxxxxxxx
## for item in List:
### if item in unique: continue
### else: add item to unique & print count(item) + item.capitalize
############################################################################
def main():
    items = []
    while True:
        try:
            item = input().strip().lower()
            items.append(item)
        except EOFError:
            count_items(items)
            break


def count_items(items):
    items.sort()
    items_unique = []
    for item in items:
        if item in items_unique:
            continue
        else:
            items_unique.append(item)
            print(items.count(item), item.upper())


if __name__ == '__main__':
    main()


