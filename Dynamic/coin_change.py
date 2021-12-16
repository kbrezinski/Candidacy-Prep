
# Greedy approach to coin change problem
def greedy_coin(coins, change):

    total_coins = 0
    coin_list = []

    for coin in reversed(coins):
        if coin <= change:
            coin_i = change // coin  # 40 // 25 = 1
            change -= (coin_i * coin)  # 40 - (1 * 25) = 15

            total_coins += coin_i  # 0 + 1
            coin_list.extend(coin_i * [coin])

    return total_coins, coin_list


# Dynamic approach to coin change problem; NOT WORKING
def dynamic_coin(coins, change):

    # Dynamic auxiliary function
    def dynamic_coin_aux(coins, change, curr, coin_list, tot_coins):

        # base case where change remaining is 0 or no more coins left to consider
        if change <= 0 or curr < 0:
            return tot_coins
        # if current denomination is too big for the current change
        if coins[curr] > change:
            return dynamic_coin_aux(coins, change, curr - 1, coin_list, tot_coins)

        # first case choose current denomination
        coins_i = change // coins[curr]
        case1 = dynamic_coin_aux(
            coins, change - (tot_coins * coins[curr]),
            curr - 1, coin_list + [tot_coins * [coins[curr]]], tot_coins + coins_i)

        # second case skip current denomination
        case2 = dynamic_coin_aux(coins, change, curr - 1, coin_list, tot_coins)

        return min(case1, case2)

    return dynamic_coin_aux(coins, change, len(coins) - 1, coin_list=[], tot_coins=0)


coins = [1, 5, 10, 20, 25, 50, 100]
change = 40

print(greedy_coin(coins, change))
print(dynamic_coin(coins, change))
