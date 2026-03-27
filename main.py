from colorama import Fore, Style, init
from colorama import init
init(autoreset=True)
from utils import *
import csv
import os
import matplotlib.pyplot as plt

FILE_NAME = "trades.csv"


def initialize_file():
    # Create CSV file with headers if it doesn't exist
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Instrument", "Position", "Entry", "Exit", "Lot", "Profit"])

def add_trade():
    date = input("Enter date (YYYY-MM-DD): ")
    instrument = input("Instrument (NIFTY/GOLD): ")
    position = input("Position (Buy/Sell): ")
    
    entry = float(input("Entry price: "))
    exit_price = float(input("Exit price: "))
    lot = int(input("Lot size: "))

    profit = calculate_profit(position, entry, exit_price, lot)

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, instrument, position, entry, exit_price, lot, profit])

    if profit > 0:
     print(Fore.GREEN + f"\nTrade saved. Profit: ₹{profit}\n" + Style.RESET_ALL)
    else:
     print(Fore.RED + f"\nTrade saved. Loss: ₹{profit}\n" + Style.RESET_ALL)
def show_equity_curve():
    trades = load_trades()

    if len(trades) == 0:
        print("No trades to display.\n")
        return

    equity = []
    total = 0

    for t in trades:
        total += t
        equity.append(total)

    plt.plot(equity)
    plt.title("Equity Curve")
    plt.xlabel("Trade Number")
    plt.ylabel("Profit/Loss")
    plt.grid()
    plt.show()

def main():
    initialize_file()

    while True:
        print("------ Trading Journal Analyzer ------")
        print("1. Add Trade")
        print("2. Show Statistics")
        print("3. Show Trade History")
        print("4. Show Equity Curve")
        print("5. Search Trades")
        print("6. Monthly Analysis")
        print("7. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            add_trade()
        elif choice == "2":
            show_statistics()
        elif choice=="3":
            show_trades()
        elif choice == "4":
           show_equity_curve()

        elif choice == "5":
          search_trades()

        elif choice=="6":
           monthly_analysis()

        elif choice == "7":
         print("Exiting Program")
         break

if __name__ == "__main__":
    main()