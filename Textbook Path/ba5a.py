def Coins (coins, money):
    res = []
    for i in coins:
        if money % i == 0:
            res.append(money // i)
    coins_seq = {}
    while money != 0:
        coins_seq[max(coins)] = money // max(coins)
        money = money % max(coins)
        coins.remove(max(coins))
    res.append(sum(coins_seq.values()))
    return min(res)
if __name__ == "__main__":
    with open("input.txt", "r") as f:
        money = int(f.readline().strip())
        coins = [int(l) for l in f.readline().strip().split(",")]
    res = Coins(coins, money)
    print(res)