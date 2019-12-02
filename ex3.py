groceries = ['banana','orange','apple']
stock = {
 "banana": 6,
 "apple": 0,
 "orange": 32,
 "pear": 15
}
prices = {
 "banana": 4,
 "apple": 2,
 "orange": 1.5,
 "pear": 3
}

def compute_bill(foods):
    total = 0
    for food in foods:
        if(stock[food] > 0):
            total+=prices[food]
            stock[food]-=1
    return total

data = compute_bill(['banana','orange'])
print(data)