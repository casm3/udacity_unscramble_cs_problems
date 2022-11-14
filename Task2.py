"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
from collections import defaultdict
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    number_and_phone_time = defaultdict(int)

    for number in calls:
        number_and_phone_time[number[0]] += int(number[3])
        number_and_phone_time[number[1]] += int(number[3])

number_more_time = max(
    number_and_phone_time, key=number_and_phone_time.get
    )

print(
    f"{number_more_time} spent the longest time,"
    f" {number_and_phone_time[number_more_time]} seconds,"
    f" on the phone during September 2016.")

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone
during September 2016.".
"""
