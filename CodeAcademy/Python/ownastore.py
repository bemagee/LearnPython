prices = {"banana": 4, "apple": 2, "orange": 1.5, "pear": 3}
stock = {"banana": 6, "apple": 0, "orange": 32, "pear": 15}

for item in prices:
    for item2 in stock:
        print item
        print "price: " + str(prices[item])
        print "stock: " + str(stock[item2])
	print
