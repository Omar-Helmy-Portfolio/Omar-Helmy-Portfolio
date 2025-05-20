def main():
    ans = input("What is the Answer to the Great Question of Life, the Universe, and Everything?\n >")
    check_ans(ans.lower().strip())


def check_ans(ans):
    if ans == "42" or ans == "forty-two" or ans == "forty two":
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
