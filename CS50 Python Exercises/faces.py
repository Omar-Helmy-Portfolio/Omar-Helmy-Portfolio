# Main Function: Asks User For Input, Calls Convert, Print Result.
def main():
    sentence = input("Enter Sentence: ")
    converted = convert(sentence)
    print(converted)


# Function to Replace symbols With Smily and Sad Faces.
def convert(sentence):
    replaced = sentence.replace(":)", "🙂")
    replaced = replaced.replace(":(", "🙁")
    return replaced


main()


