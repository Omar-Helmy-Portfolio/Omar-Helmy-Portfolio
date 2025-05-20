def main():
    # Input Camel Case.
    camel_case = input("Name: ")
    # Turn To List.
    chars = list(camel_case)
    # Iterate in List To find Capitals & Their Index.
    # Add _ before index, then Lower Capital & Add It
    for char in chars:
        if char.isupper():
            char_place = chars.index(char)
            chars.remove(char)
            chars.insert(char_place,char.lower())
            chars.insert(char_place, "_")
    # Join chars List To Form Snake Case Name.
    snake_case = "".join(chars)
    print(snake_case)


if __name__ == "__main__":
    main()


