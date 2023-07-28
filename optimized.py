
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
    all_shares.sort(key=lambda x: x[2], reverse=True)
    best_combination = []
    share_price_list = []
    share_profit_list = []
    max_spend = MAX_SPEND
    for i in all_shares:
        share_name = i[0]
        share_price = abs(i[1])  
        share_profit = i[2]
        profit_by_share = (share_price * share_profit) / 100        
        if (max_spend - share_price) >= 0 and share_price != 0:
            best_combination.append(share_name)
            share_price_list.append(share_price)
            share_profit_list.append(profit_by_share)
            max_spend -= share_price
    investement = sum(share_price_list)
    final_profit = sum(share_profit_list)
    print("Best combination : ", best_combination)
    print("Investement : ", round(investement, 2), "$")
    print("Profit : ", round(final_profit, 2), "$")
    return

    
get_best_combination("data/dataset1_Python+P7.csv")