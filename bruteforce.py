from itertools import combinations
import csv

MAX_SPEND = 500



def get_data(path):
    share_list = []
    with open(path, 'r') as file:
        csvreader = csv.reader(file)
        next(csvreader)
        for row in csvreader:
            share_list.append(row)
    return share_list

def invest_limit():
    pass

def get_best_combination(path):
    shares_list = get_data(path)
    profit = 0
    best_combination = []
    for i in range(len(shares_list) + 1):
        combination += list(combinations(shares_list, i))
        
        
        
        
    print(combination)

    
get_best_combination("data/dataset1_Python+P7.csv")   
