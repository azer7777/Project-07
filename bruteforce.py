from itertools import combinations
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
    final_profit = 0
    all_combinations = []    
    best_combination = ""
    for i in range(len(all_shares)):
        all_combinations += list(combinations(all_shares, i + 1))
        for one_combination in all_combinations:
            share_name_list = []
            share_price_list = []
            share_profit_list = []            
            for i in one_combination:
                share_name, share_price, share_gain = i[0], i[1], i[2]
                profit_by_share = (share_price * share_gain) / 100            
                share_price_list.append(share_price)
                share_profit_list.append(profit_by_share)
                share_name_list.append(share_name)                               
            spend = sum(share_price_list)
            profit = sum(share_profit_list)
            if spend <= MAX_SPEND and profit >= final_profit:
                investement = spend
                final_profit = profit
                best_combination = share_name_list
    print("Best combination : ", best_combination)
    print("Investement : ", round(investement, 2), "$")
    print("Profit : ", round(final_profit, 2), "$")
    return

    
get_best_combination("data/dataset4_Python+P7.csv")   
