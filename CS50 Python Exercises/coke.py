# Requirements: (Buy A Coke)
# Take Coins In (25, 5, 10) Denominations only.
# One Coke Cost 50 cents.
# Return Due or Owed Amounts.
# End Program when Owed 0 or More Cents.
###############################################
def main():
    coins = [25, 10, 5]
    due_amount = 50
    # Loop To Take Coins Until Due <= 0.
    while due_amount > 0:
        print("Amount Due:", due_amount)
        coin = int(input("Insert Coin: "))
        if coin in coins:
            due_amount -= coin
        else:
            pass

    owed_amount = abs(due_amount)
    print("Change Owed:", owed_amount)


if __name__ == '__main__':
    main()
