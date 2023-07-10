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

def invest_limit(path):
    price = (get_data(path))[1]
    benefit = (get_data(path))[2]
 


def get_best_combination(path):
    shares_list = get_data(path)
    profit = 0
    best_combination = []
    cost = []
    for i in range(3):
        combination = list(combinations(shares_list, i))
        for e in combination[1]:
            cost.append(e)
       
    print(cost)

    
get_best_combination("data/dataset0_Python+P7.csv")   
