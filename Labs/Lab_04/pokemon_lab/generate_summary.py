import os
import sys
import pandas as pd

def generate_summary(portfolio_file):
    if not os.path.exists(portfolio_file):
        print(f"Error: File '{portfolio_file}' not found.", file=sys.stderr)
        sys.exit(1)

    df = pd.read_csv(portfolio_file)

    if df.empty:
        print("Portfolio file is empty. No data to summarize.")
        return

    total_portfolio_value = df["card_market_value"].sum()

    most_valuable_index = df["card_market_value"].idxmax()
    most_valuable_card = df.loc[most_valuable_index]

    print("\n📊 Portfolio Summary")
    print(f"Total Market Value: ${total_portfolio_value:,.2f}")
    print("Most Valuable Card:")
    print(f"  Name: {most_valuable_card.get('card_name', 'UNKNOWN')}")
    print(f"  ID: {most_valuable_card['card_id']}")
    print(f"  Value: ${most_valuable_card['card_market_value']:,.2f}\n")

def main():
    generate_summary("card_portfolio.csv")

def test():
    generate_summary("test_card_portfolio.csv")

if __name__ == "__main__":
    print("Running generate_summary.py in Test Mode...", file=sys.stderr)
    test()
