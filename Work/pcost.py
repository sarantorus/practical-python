# pcost.py
#
# Exercise 1.27

def portfolio_cost(filename):
    
    totalcost=0
        
    with open(filename,'rt') as f:
        headers=next(f)
        for line in f:
            
           row=line.split(',')
           nshares = int(row[1])
           stockprice=float(row[2])
           totalcost+=nshares*stockprice
    return totalcost

cost= portfolio_cost('Data/portfolio.csv')
print('Total Cost',cost)





