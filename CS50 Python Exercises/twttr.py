# Requirements:
# Take A Word or A Sentence.
# Take Vowels Out.
# Return The Output With the Same Upper Or Lower Cases.
###########################################################
# Algorithm:
# Take Sentence.
# Convert To List.
# Loop Inside List.
    # Check If Item In (A,I,E,O,U) (.lower or .upper item)
    # If True, list.remove(item)
    # else, pass
# join list
###########################################################
# Implementation:
def main():
    word = input("Input: ")
    chars = list(word)
    chars = remove_vowels(chars)
    word = "".join(chars)
    print("Output:", word)


def remove_vowels(chars):
    vowels = ["a", "e", "i", "o", "u"]
    for vow in vowels:
        for char in chars:
            if char.lower() == vow:
                chars.remove(char)
            else:
                pass
    return chars


if __name__ == '__main__':
    main()
