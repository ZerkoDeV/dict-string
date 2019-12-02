prices = {
        "banana": 4,
        "apple": 2,
        "orange": 1.5,
        "pear": 3
}

stock = {
        "banana": 3,
        "apple": 0,
        "orange" : 4,
        "pear" : 5
}

for i in prices:
    print(i)
    print("price:", prices[i])
    print("stonks:", stock[i])
total = 0
for i in prices:
    total += prices[i] * stock[i]
print(total)