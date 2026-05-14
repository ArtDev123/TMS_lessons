import csv

with open("prices.csv", "r", encoding="utf-8", newline="") as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    items = list(reader)

for row in items:
    row["price"] = round(float(row["price"]) * 1.2, 2)

with open("new_prices.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(items)
