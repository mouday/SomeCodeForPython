# '''
# 假设用于找零的钱币包括四种，即
# 25美分（quarter）,
# 10美分（dime）,
# 5美分（nickel）,
# 1美分（penny）
# 方案一动态规划

# 假设需要找钱数为n，要求解最少的钱币数目，可以分为如下几种情况：

# 1枚penny钱币 + 需要找零为 (n - 1)时的最少的钱币数目
# 1枚nickel钱币 + 需要找零为 (n - 5)时的最少的钱币数目
# 1枚dime钱币 + 需要找零为 (n - 10)时的最少的钱币数目
# 1枚quarter钱币 + 需要找零为 (n - 25)时的最少的钱币数目
# '''
print("hello world")

def recMC(coinValueList, change):
    print("0")
    minCoins = change
    if change in coinValueList:
        return 1
    else:
        for i in [c for c in coinValueList if c < change]:
            numCoins = 1 + recMC(coinValueList, change - i)
            if numCoins < minCoins:
                minCoins = numCoins
    return minCoins

print(recMC([1, 5, 10, 25], 63))
