"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

    all_texters = set()

    for record in texts:
        all_texters.add(record[0])
        all_texters.add(record[1])

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

    all_callers = set()
    receivers = set()

    for record in calls:
        all_callers.add(record[0])
        receivers.add(record[1])

    difference_set = all_callers - (receivers.union(all_texters))

    telemarketers_list = list(difference_set)
    telemarketers_list.sort()

    print("These numbers could be telemarketers: ")
    for telemarketer in telemarketers_list:
        print(telemarketer)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order
with no duplicates.
"""
