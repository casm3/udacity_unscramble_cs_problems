"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv


unique_numbers = set()

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)
    for number in texts:
        unique_numbers.add(number[0])
        unique_numbers.add(number[1])

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

    for number in calls:
        unique_numbers.add(number[0])
        unique_numbers.add(number[1])

print(
    f"There are {len(unique_numbers)} different"
    f" telephone numbers in the records."
    )


"""
TASK 1:
How many different telephone numbers are there in the records?
Print a message:
"There are <count> different telephone numbers in the records."
"""
