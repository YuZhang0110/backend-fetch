import csv
import sys
from collections import defaultdict
from typing import Dict, List, Tuple

def spendPoints(points2Spend: int, transactionsFile: str) -> Dict[str, int]:
    payerPoints = defaultdict(int)
    transactions = readTransactionsFromFile(transactionsFile)
    transactions = sortTransactionsByTimestamp(transactions)

    for payer, points, timestamp in transactions:
        if payerPoints[payer] < 0:
            points2Spend -= payerPoints[payer]
        else:
            if points2Spend >= points:
                points2Spend -= points
            else:
                payerPoints[payer] += points - points2Spend
                points2Spend = 0


    return dict(payerPoints)

def readTransactionsFromFile(fileName: str) -> List[Tuple[str, int, str]]:
    transactions = []
    with open(fileName, 'r') as file:
        reader = csv.reader(file)
        next(reader) # skip header row
        for row in reader:
            payer, points, timestamp = row
            transactions.append((payer, int(points), timestamp))
    return transactions

def sortTransactionsByTimestamp(transactions: List[Tuple[str, int, str]]) -> List[Tuple[str, int, str]]:
    return sorted(transactions, key=lambda x: x[2])

if __name__ == '__main__':
    points2Spend = int(sys.argv[1])
    transactionsFile = sys.argv[2]
    result = spendPoints(points2Spend, transactionsFile)
    print(result)
