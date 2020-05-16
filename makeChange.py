# get the number of coins used to created the given amount of change
def getMinCoins(cents):
    # limit to making change with coins only
    if cents < 0 or cents > 99:
        raise ValueError("Incorrect amount of change")
    standardCoins = [25, 10, 5, 1]
    numCoins = 0
    i = 0
    for coin in standardCoins:
        while cents >= standardCoins[i]:
            cents -= coin
            numCoins += 1
        i += 1
    return numCoins


if __name__ == "__main__":
    change = [33, 50, 0, 99, 75]
    for amount in change:
        print(f"{getMinCoins(amount)} coins are needed to make change for {amount} cents")
