stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 420
}

total = 0

n = int(input("How many stocks do you want to buy? "))

for i in range(n):
    name = input("Enter stock name: ").upper()
    quantity = int(input("Enter quantity: "))

    if name in stocks:
        investment = stocks[name] * quantity
        total += investment
        print("Investment:", investment)
    else:
        print("Stock not available!")

print("Total Investment:", total)

with open("investment.txt", "w") as file:
    file.write("Total Investment: " + str(total))

print("Result saved successfully!")