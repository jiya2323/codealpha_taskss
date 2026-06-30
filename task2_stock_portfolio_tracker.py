# Stock Portfolio Tracker

import csv

# Hardcoded stock prices dictionary
STOCK_PRICES = {
    "AAPL":  180,
    "TSLA":  250,
    "GOOGL": 140,
    "AMZN":  185,
    "MSFT":  415,
    "META":  520,
    "NFLX":  630,
    "NVDA":  875
}


def show_available_stocks():
    print("\n  Available Stocks:")
    print("  " + "-" * 28)
    print(f"  {'Symbol':<8}  {'Price (USD)'}")
    print("  " + "-" * 28)
    for symbol, price in STOCK_PRICES.items():
        print(f"  {symbol:<8}  ${price}")
    print("  " + "-" * 28)


def get_portfolio():
    portfolio = {}
    print("\n  Enter stock symbol and quantity.")
    print("  Type 'done' when finished.\n")

    while True:
        stock = input("  Stock symbol: ").upper().strip()

        if stock == "DONE":
            break

        if stock not in STOCK_PRICES:
            print(f"  '{stock}' not found. Please choose from the list above.\n")
            continue

        try:
            qty = int(input(f"  Quantity for {stock}: "))
            if qty <= 0:
                print("  Quantity must be a positive number.\n")
                continue
        except ValueError:
            print("  Please enter a valid number.\n")
            continue

        portfolio[stock] = portfolio.get(stock, 0) + qty
        print(f"  Added {qty} shares of {stock}\n")

    return portfolio


def display_portfolio(portfolio):
    if not portfolio:
        print("\n  No stocks added to portfolio.")
        return 0

    total = 0
    print("\n" + "=" * 50)
    print("       STOCK PORTFOLIO SUMMARY")
    print("=" * 50)
    print(f"  {'Stock':<8} {'Qty':>6} {'Price':>10} {'Value':>12}")
    print("  " + "-" * 42)

    for stock, qty in portfolio.items():
        price = STOCK_PRICES[stock]
        value = price * qty
        total += value
        print(f"  {stock:<8} {qty:>6} ${price:>9} ${value:>11,}")

    print("  " + "-" * 42)
    print(f"  {'TOTAL':>36}  ${total:>11,}")
    print("=" * 50)
    return total


def save_to_file(portfolio, total):
    choice = input("\n  Save results? (yes/no): ").lower().strip()
    if choice != "yes":
        return

    fmt = input("  Format (txt/csv): ").lower().strip()

    if fmt == "csv":
        filename = "portfolio_result.csv"
        with open(filename, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Stock", "Quantity", "Price per Share", "Total Value"])
            for stock, qty in portfolio.items():
                price = STOCK_PRICES[stock]
                value = price * qty
                writer.writerow([stock, qty, f"${price}", f"${value:,}"])
            writer.writerow([])
            writer.writerow(["", "", "TOTAL", f"${total:,}"])
        print(f"  Saved as '{filename}'")

    else:
        filename = "portfolio_result.txt"
        with open(filename, "w") as f:
            f.write("STOCK PORTFOLIO TRACKER\n")
            f.write("=" * 40 + "\n")
            f.write(f"{'Stock':<8} {'Qty':>6} {'Price':>10} {'Value':>12}\n")
            f.write("-" * 40 + "\n")
            for stock, qty in portfolio.items():
                price = STOCK_PRICES[stock]
                value = price * qty
                f.write(f"{stock:<8} {qty:>6} ${price:>9} ${value:>11,}\n")
            f.write("-" * 40 + "\n")
            f.write(f"TOTAL INVESTMENT: ${total:,}\n")
        print(f"  Saved as '{filename}'")


def main():
    print("\n" + "=" * 50)
    print("       STOCK PORTFOLIO TRACKER")
    print("=" * 50)

    show_available_stocks()
    portfolio = get_portfolio()
    total = display_portfolio(portfolio)

    if total > 0:
        save_to_file(portfolio, total)

    print("\n  Thank you for using Stock Portfolio Tracker!\n")


if __name__ == "__main__":
    main()