from colorama import init
init(autoreset=True)
import csv
import pandas as pd

FILE_NAME = "trades.csv"
def calculate_profit(position, entry, exit_price, lot):
    if position.lower() == "buy":
        profit = (exit_price - entry) * lot
    else:
        profit = (entry - exit_price) * lot
    return profit

def load_trades(filter_instrument=None):
    df = pd.read_csv(FILE_NAME)

    if filter_instrument:
        df = df[df["Instrument"].str.lower() == filter_instrument.lower()]

    return df["Profit"].tolist()

from colorama import Fore, Style

def show_statistics():
    instrument = input("Enter instrument (NIFTY/GOLD) or press Enter for ALL: ")
    if instrument == "":
     trades = load_trades()
    else:
     trades = load_trades(instrument)

    if len(trades) == 0:
        print("No trades recorded.\n")
        return

    # BASIC STATS
    total_trades = len(trades)
    total_profit = sum(trades)
    winning_trades = len([t for t in trades if t > 0])
    win_rate = (winning_trades / total_trades) * 100

    best_trade = max(trades)
    worst_trade = min(trades)
    average_profit = total_profit / total_trades

    profits = [t for t in trades if t > 0]
    losses = [t for t in trades if t < 0]

    profit_factor = sum(profits) / abs(sum(losses)) if losses else 0

    # 🔥 DRAWDOWN CALCULATION
    equity = []
    total = 0

    for t in trades:
        total += t
        equity.append(total)

    peak = equity[0]
    max_drawdown = 0

    for value in equity:
        if value > peak:
            peak = value
        drawdown = peak - value
        if drawdown > max_drawdown:
            max_drawdown = drawdown
        if instrument == "":
         print("\nShowing stats for ALL trades")
        else:
         print(f"\nShowing stats for {instrument.upper()} trades")
    # PRINT
    print("\n------ Trading Statistics ------")
    print("Total Trades:", total_trades)
    print("Winning Trades:", winning_trades)
    print("Win Rate: {:.2f}%".format(win_rate))

    if total_profit > 0:
        print(Fore.GREEN + f"Total Profit: ₹ {total_profit}" + Style.RESET_ALL)
    else:
        print(Fore.RED + f"Total Loss: ₹ {total_profit}" + Style.RESET_ALL)

    print("Best Trade: ₹", best_trade)
    print("Worst Trade: ₹", worst_trade)
    print("Average Profit: ₹", round(average_profit, 2))
    print("Profit Factor:", round(profit_factor, 2))
    print("Max Drawdown: ₹", max_drawdown)

    print("-------------------------------\n")


from colorama import Fore, Style

def show_trades():
    print("\n1. Show All Trades")
    print("2. Show Winning Trades")
    print("3. Show Losing Trades")

    choice = input("Choose option: ")

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)

        print("\n------ Trade History ------")

        for i, row in enumerate(reader):
            if i == 0:
                print(row)  # header
                continue

            profit = float(row[-1])

            # 🔥 APPLY FILTER + COLOR
            if choice == "1":
                if profit > 0:
                    print(Fore.GREEN + str(row) + Style.RESET_ALL)
                else:
                    print(Fore.RED + str(row) + Style.RESET_ALL)

            elif choice == "2" and profit > 0:
                print(Fore.GREEN + str(row) + Style.RESET_ALL)

            elif choice == "3" and profit < 0:
                print(Fore.RED + str(row) + Style.RESET_ALL)

        print("---------------------------\n")

def search_trades():
    print("\nSearch By:")
    print("1. Date")
    print("2. Instrument")

    choice = input("Choose option: ")

    keyword = input("Enter search value: ").lower()

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)

        print("\n------ Search Results ------")

        for i, row in enumerate(reader):
            if i == 0:
                print(row)
                continue

            # 🔍 SEARCH LOGIC
            if choice == "1" and keyword in row[0].lower():
                print(row)

            elif choice == "2" and keyword in row[1].lower():
                print(row)

        print("----------------------------\n")

def monthly_analysis():
    df = pd.read_csv(FILE_NAME)

    df["Date"] = pd.to_datetime(df["Date"])
    df["Month"] = df["Date"].dt.to_period("M")

    monthly = df.groupby("Month")["Profit"].sum()

    print("\n------ Monthly Performance ------")

    for month, profit in monthly.items():
        print(f"{month} → ₹ {round(profit,2)}")

    best_month = monthly.idxmax()
    worst_month = monthly.idxmin()

    print(f"\nBest Month: {best_month}")
    print(f"Worst Month: {worst_month}")

    print("-------------------------------\n")