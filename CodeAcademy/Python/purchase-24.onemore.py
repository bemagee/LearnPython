sub_total = 0.0
final_bill = 0.0
groceries = ["banana", "orange", "apple"]

stock = { "banana": 6,
            "apple": 0,
            "orange": 32,
            "pear": 15
        }
	        
prices = { "banana": 4,
            "apple": 2,
            "orange": 1.5,
            "pear": 3
         }

# Write your code below!
def compute_bill(food):
    if stock[food] > 0:
        print "Items = " + str(stock[food])
        print "Price of Item = " + str(prices[food])
        stock[food] -= 1
        total = prices[food]
    total += total
    print "Your final bill is " + str(total)

for item in groceries:
    print "Item before calling compute_bill = " + item
    compute_bill(item)

