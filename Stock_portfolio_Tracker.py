stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150,
    "MSFT": 400
}

stock_name = input("Enter stock name: ").upper()
stock_quantity = int(input("Enter stock quantity: "))

if stock_name in stock_prices:
    total_investment = stock_prices[stock_name] * stock_quantity

    print("\n----- Stock Portfolio -----")
    print("Stock Name:", stock_name)
    print("Price Per Stock:", stock_prices[stock_name])
    print("Quantity:", stock_quantity)
    print("Total Investment:", total_investment)

    file = open("portfolio.txt", "w")
    file.write("----- Stock Portfolio -----\n")
    file.write(f"Stock Name: {stock_name}\n")
    file.write(f"Price Per Stock: {stock_prices[stock_name]}\n")
    file.write(f"Quantity: {stock_quantity}\n")
    file.write(f"Total Investment: {total_investment}\n")
    file.close()

    print("\nData saved successfully in portfolio.txt")

else:
    print("Stock not found!")