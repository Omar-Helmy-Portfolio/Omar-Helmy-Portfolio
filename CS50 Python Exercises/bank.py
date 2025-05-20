def main():
    greet = input("Enter A Greeting Please: ")
    greeting = greet.lower().strip()
    words = greeting.split()
    check_words(words[0])

def check_words(word):
    #if word.strip(",-*#&") == "hello":
    if "hello" in word:
        print("$0")
    elif word[0] == "h":
        print("$20")
    else:
        print("$100")


if __name__ == "__main__":
    main()
