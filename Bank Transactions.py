def maximizeTransactions(transactions):
    total = max_transactions = 0
    start = end = 0

    while end < len(transactions):
        total += transactions[end]

        if total < 0:
            total -= transactions[start]
            start += 1
        else:
            max_transactions = max(max_transactions, end - start + 1)

        end += 1

    return max_transactions

print(maximizeTransactions([3, 2, -5, -6, -1, 4]))