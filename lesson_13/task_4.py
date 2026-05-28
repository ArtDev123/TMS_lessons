from typing import Generator

raw_transactions = [
    "user1,SUCCESS,1500",
    "user2,FAILED,300",
    "user3,SUCCESS,4500",
    "user1,SUCCESS,200",
    "user4,PENDING,90",
    "invalid_line_without_commas",
    "user2,SUCCESS,1200",
]


def parse_lines(lines: list[str]) -> Generator[dict[str, str], None, None]:
    for line in lines:
        parts = line.split(",")
        if len(parts) != 3:
            continue
        yield {"user": parts[0], "status": parts[1], "amount": parts[2]}


def filter_successful(
    parsed_stream: Generator[dict[str, str], None, None],
) -> Generator[dict[str, str], None, None]:
    for transaction in parsed_stream:
        if transaction["status"] == "SUCCESS":
            yield transaction


def convert_amount(
    filtered_stream: Generator[dict[str, str], None, None],
) -> Generator[dict[str, str | int], None, None]:
    for transaction in filtered_stream:
        transaction["amount"] = int(transaction["amount"])
        yield transaction


pipeline = convert_amount(
    filter_successful(parse_lines(raw_transactions))
)

total_user1 = 0
total_user2 = 0
for tx in pipeline:
    if tx["user"] == "user1":
        total_user1 += tx["amount"]
    elif tx["user"] == "user2":
        total_user2 += tx["amount"]

print(f"user1: {total_user1}")
print(f"user2: {total_user2}")
