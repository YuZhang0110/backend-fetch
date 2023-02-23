# README
This code implements a solution to spend points based on rules defined in the problem statement. The solution reads the transactions from a CSV file and spends the points based on the rules, returning the payer point balances after the points are spent.

# Requirements
Python 3.x
csv library

# Usage
To run the code, you will need to pass two arguments to the script:

The amount of points to spend
The name of the CSV file containing the transactions
For example, to spend 5000 points, the command would be:

```python3
mycode.py 5000 transactions.csv
```

# testsuit
test_spend_point.py is a test file. Type to run. There are three test cases one is fail and two are success. Run this command to test.
```
python3 test_spend_points.py
```

# Input Format
The input is a CSV file containing the transactions data. The file should have the following format:

```
"payer","points","timestamp"
"DANNON",1000,"2020-11-02T14:00:00Z"
"UNILEVER",200,"2020-10-31T11:00:00Z"
"DANNON",-200,"2020-10-31T15:00:00Z"
"MILLER COORS",10000,"2020-11-01T14:00:00Z"
"DANNON",300,"2020-10-31T10:00:00Z"
```
Each row of the file represents a single transaction, with the payer, points, and timestamp separated by commas.

# Output Format
The output is a dictionary in Python, where the keys are the payer names and the values are the payer point balances after the points are spent. For example:

```{
"DANNON": 1000,
"UNILEVER": 0,
"MILLER COORS": 5300
}
```

# Implementation Details
The code is implemented in Python and uses the csv library to read the transactions data from the CSV file. The transactions are sorted by timestamp, and the points are spent based on the rules defined in the problem statement. The payer point balances are stored in a defaultdict, which is then returned as a dictionary.

# Conclusion
This code provides a solution to the problem of spending points based on the rules defined in the problem statement. By using the csv library and sorting the transactions by timestamp, the code is able to spend the points and return the payer point balances in an efficient and accurate manner.