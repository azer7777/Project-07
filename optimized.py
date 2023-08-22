
import csv

MAX_SPEND = 500



def get_data(path):
    all_shares = []
    with open(path, 'r') as file:
        csvreader = csv.reader(file)
        next(csvreader)
        for row in csvreader:
            all_shares.append((row[0], float(row[1]), float(row[2])))
    return all_shares


def get_best_combination(path):
    all_shares = get_data(path)
    n = len(all_shares)   
    dp = [[0] * (MAX_SPEND + 1) for _ in range(n + 1)]    
    for i in range(1, n + 1):
        share_name, share_price, share_profit = all_shares[i - 1]
        share_price = abs(share_price)
        
        for budget in range(MAX_SPEND + 1):
            if share_price != 0 and budget >= share_price:
                dp[i][budget] = max(dp[i - 1][budget],
                                    dp[i - 1][budget - int(share_price)] + (share_price * share_profit) / 100)
            else:
                dp[i][budget] = dp[i - 1][budget]    
    best_combination = []
    budget = MAX_SPEND
    for i in range(n, 0, -1):
        if dp[i][budget] != dp[i - 1][budget]:
            share_name, share_price, _ = all_shares[i - 1]
            best_combination.append(share_name)
            budget -= int(share_price)    
    investement = MAX_SPEND - budget
    final_profit = dp[n][MAX_SPEND]   
    print("Best combination : ", best_combination)
    print("Investment : ", round(investement, 2), "$")
    print("Profit : ", round(final_profit, 2), "$")

    
get_best_combination("data/dataset1_Python+P7.csv")



