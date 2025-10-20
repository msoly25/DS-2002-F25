import os
import sys
import pandas as pd
import json

def _load_lookup_data(lookup_dir):
    all_lookup_df = []

    for filename in os.listdir(lookup_dir):
        if filename.endswith(".json"):
            filepath = os.path.join(lookup_dir, filename)
            with open(filepath, "r") as f:
                data = json.load(f)

            df = pd.json_normalize(data["data"])
            df["name"] = df.get("name", pd.Series(["UNKNOWN"] * len(df)))

            df["card_market_value"] = (
                df.get("tcgplayer.prices.holofoil.market", pd.Series([None] * len(df)))
                .fillna(df.get("tcgplayer.prices.normal.market", pd.Series([None] * len(df))))
                .fillna(0.0)
            )

            df = df.rename(columns={
                "id": "card_id",
                "name": "card_name",
                "number": "card_number",
                "set.id": "set_id",
                "set.name": "set_name"
            })

            required_cols = ["card_id", "card_name", "card_number", "set_id", "set_name", "card_market_value"]
            all_lookup_df.append(df[required_cols].copy())

    if not all_lookup_df:
        return pd.DataFrame(columns=["card_id", "card_name", "card_number", "set_id", "set_name", "card_market_value"])

    lookup_df = pd.concat(all_lookup_df, ignore_index=True)
    lookup_df = lookup_df.sort_values(by="card_market_value", ascending=False)
    lookup_df = lookup_df.drop_duplicates(subset=["card_id"], keep="first")

    return lookup_df

def _load_inventory_data(inventory_dir):
    inventory_data = []

    for filename in os.listdir(inventory_dir):
        if filename.endswith(".csv"):
            filepath = os.path.join(inventory_dir, filename)
            df = pd.read_csv(filepath)
            inventory_data.append(df)

    if not inventory_data:
        return pd.DataFrame(columns=["binder_name", "page_number", "slot_number", "set_id", "card_number", "card_id"])

    inventory_df = pd.concat(inventory_data, ignore_index=True)
    inventory_df["card_id"] = inventory_df["set_id"].astype(str) + "-" + inventory_df["card_number"].astype(str)

    return inventory_df

def update_portfolio(inventory_dir, lookup_dir, output_file):
    lookup_df = _load_lookup_data(lookup_dir)
    inventory_df = _load_inventory_data(inventory_dir)

    print("Lookup columns:", lookup_df.columns.tolist())

    if inventory_df.empty:
        print("Error: Inventory is empty.", file=sys.stderr)
        empty_df = pd.DataFrame(columns=[
            "index", "binder_name", "page_number", "slot_number",
            "card_id", "set_name", "card_market_value"
        ])
        empty_df.to_csv(output_file, index=False)
        return

    merged_df = pd.merge(
        inventory_df,
        lookup_df[["card_id", "card_name", "set_name", "card_market_value"]],
        on="card_id",
        how="left"
    )

    print("Merged columns:", merged_df.columns.tolist())

    merged_df["card_market_value"] = merged_df["card_market_value"].fillna(0.0)
    merged_df["set_name"] = merged_df["set_name"].fillna("NOT_FOUND")

    merged_df["index"] = (
        merged_df["binder_name"].astype(str) + "-" +
        merged_df["page_number"].astype(str) + "-" +
        merged_df["slot_number"].astype(str)
    )

    final_cols = [
        "index", "binder_name", "page_number", "slot_number",
        "card_id", "set_name", "card_market_value"
    ]

    merged_df[final_cols].to_csv(output_file, index=False)
    print(f"Portfolio successfully written to {output_file}")

def main():
    update_portfolio(
        inventory_dir="./card_inventory/",
        lookup_dir="./card_set_lookup/",
        output_file="card_portfolio.csv"
    )

def test():
    update_portfolio(
        inventory_dir="./card_inventory_test/",
        lookup_dir="./card_set_lookup_test/",
        output_file="test_card_portfolio.csv"
    )

if __name__ == "__main__":
    print("Running update_portfolio.py in Test Mode...", file=sys.stderr)
    test()

