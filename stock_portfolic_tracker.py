
# Stock Portfolio Tracker
# CodeAlpha Internship - Task 2

def stock_portfolio_tracker():

    stock_prices = {
        "AAPL": 180,
        "TSLA": 250,
        "GOOGL": 140,
        "MSFT": 410,
        "AMZN": 175
    }

    portfolio = {}

    print("================================")
    print("   STOCK PORTFOLIO TRACKER")
    print("================================")

    print("\nAvailable Stocks:")
    for stock, price in stock_prices.items():
        print(f"{stock}: ${price} per share")

    while True:
        stock = input(
            "\nEnter stock symbol (or DONE to finish): "
        ).strip().upper()

        if stock == "DONE":
            break

        if stock not in stock_prices:
            print("Invalid stock symbol!")
            continue

        try:
            quantity = int(input("Enter number of shares: "))

            if quantity <= 0:
                print("Quantity must be greater than zero.")
                continue

        except ValueError:
            print("Please enter a valid whole number.")
            continue

        portfolio[stock] = (
            portfolio.get(stock, 0) + quantity
        )

        print(f"{quantity} shares of {stock} added.")

    print("\n================================")
    print("       PORTFOLIO SUMMARY")
    print("================================")

    if not portfolio:
        print("Your portfolio is empty.")
        return

    total_investment = 0

    for stock, quantity in portfolio.items():
        price = stock_prices[stock]
        value = price * quantity
        total_investment += value

        print(f"\nStock: {stock}")
        print(f"Quantity: {quantity}")
        print(f"Price per share: ${price}")
        print(f"Total value: ${value}")

    print("\n--------------------------------")
    print(f"Total Investment: ${total_investment}")
    print("--------------------------------")

    choice = input(
        "\nSave summary to a file? (y/n): "
    ).strip().lower()

    if choice == "y":
        with open("portfolio_summary.txt", "w") as file:
            file.write("STOCK PORTFOLIO SUMMARY\n")

            for stock, quantity in portfolio.items():
                value = stock_prices[stock] * quantity
                file.write(
                    f"{stock}: {quantity} shares, "
                    f"Total value: ${value}\n"
                )

            file.write(
                f"\nTotal Investment: ${total_investment}\n"
            )

        print("Portfolio saved successfully!")

    print("\nThank you for using Stock Portfolio Tracker!")


if __name__ == "__main__":
    stock_portfolio_tracker()
