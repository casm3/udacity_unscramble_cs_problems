# Big O notation Evaluation

For simplicity the time required to instantiate the `set` and `defaultdict` data structures will be `O(1)`, even if it allocates more space in order to run away from collisions.

## Task 0

```py
import csv
with open('texts.csv', 'r') as f: # O(1)
    reader = csv.reader(f) # O(1)
    texts = list(reader) # O(len(reader)) -> O(n)
    print(
        f"First record of texts, {texts[0][0]}"
        f" texts {texts[0][1]} at time {texts[0][2]}"
    ) 
    """ 
    O(2) texts[0][0]
    O(2) texts[0][1]
    O(2) texts[0][2]
    O(1) print
    """

    # Partial Time Complexity: O(n + 9) -> O(n)

with open('calls.csv', 'r') as f: # O(1)
    reader = csv.reader(f) # O(1)
    calls = list(reader) # O(len(reader)) -> O(n)
    print(
        f"Last record of calls, {calls[-1][0]}"
        f" calls {calls[-1][1]} at time {calls[-1][2]},"
        f" lasting {calls[-1][3]} seconds"
    )
    """ 
    O(2) calls[-1][0]
    O(2) calls[-1][1]
    O(2) calls[-1][2]
    O(2) calls[-1][3]
    O(1) print
    """

    # Partial Time Complexity: O(n + 11) -> O(n)

    # Estimated Final Time Complexity: O(2n) -> O(n)
```

## Task 1

```py
import csv


unique_numbers = set() # O(1)

with open('texts.csv', 'r') as f: # O(1)
    reader = csv.reader(f) # O(1)
    texts = list(reader) # O(n)
    for number in texts: # O(n)
        unique_numbers.add(number[0]) # O(1)
        unique_numbers.add(number[1]) # O(1)

with open('calls.csv', 'r') as f: # O(1)
    reader = csv.reader(f) # O(1)
    calls = list(reader) # O(n)

    for number in calls: # O(n)
        unique_numbers.add(number[0]) # O(1)
        unique_numbers.add(number[1]) # O(1)

print(
    f"There are {len(unique_numbers)} different"
    f" telephone numbers in the records."
    )

    """
    O(1) len(unique_numbers)
    O(1) print
    """

    # Estimated Final Time Complexity: O(2n + 2n + 2n + 7) -> O(6n + 7) -> O(n)
```

## Task 2

```py
from collections import defaultdict
import csv
with open('texts.csv', 'r') as f: # O(1)
    reader = csv.reader(f) # O(1)
    texts = list(reader) # O(n)

with open('calls.csv', 'r') as f: # O(1)
    reader = csv.reader(f) # O(1)
    calls = list(reader) # O(n)
    number_and_phone_time = defaultdict(int) # O(1)

    for number in calls: # O(n)
        number_and_phone_time[number[0]] += int(number[3]) # O(2)
        number_and_phone_time[number[1]] += int(number[3]) # O(2)
    # Average case was considered to dictionary access, collision is far
    # to happen with this amount of data 

number_more_time = max(
    number_and_phone_time, key=number_and_phone_time.get
) # O(n)

print(
    f"{number_more_time} spent the longest time,"
    f" {number_and_phone_time[number_more_time]} seconds,"
    f" on the phone during September 2016."
)
    """
    O(1) number_and_phone_time[number_more_time]
    O(1) print
    """

    # Estimated Final Time Complexity: O(4n + n + n + n + 7) -> O(7n + 7) -> O(n)
```

## Task 3

```py
import csv

with open('texts.csv', 'r') as f: # O(1)
    reader = csv.reader(f) # O(1)
    texts = list(reader) # O(n)

with open('calls.csv', 'r') as f: # O(1)
    reader = csv.reader(f) # O(1)
    calls = list(reader) # O(n)

    all_bangalore_calls = set() # O(1)
    fixed_codes = set() # O(1)
    fixed_lines = set() # O(1)

    for record in calls: # O(n)
        if record[0].startswith("(080)"):  # O(1) + O(5)
            all_bangalore_calls.add(record[1]) # O(1)
            if record[1].startswith("(0"): # O(2)
                fixed_codes.add(
                    record[1][1:].split(")")[0]
                )  
                # O(1) + O(m-1) + O(1)
                # The worst case for m is approximately ten numbers
                if record[1].startswith("(080)"): # O(1) + O(5)
                    fixed_lines.add(record[1]) # O(1)

    code_list = list(fixed_codes) # O(n)
    code_list.sort() # O(n log n)

    print(
        "The numbers called by people in Bangalore have codes:"
    ) # O(1)

    for code in code_list: # O(n)
        print(code) # O(1)
    print("") # O(1)

    percentage = "%.2f" % ((len(fixed_lines)/len(all_bangalore_calls)) * 100)
    # O(5)
    print(
        f"{percentage} percent of calls from fixed lines in Bangalore are "
        "calls to other fixed lines in Bangalore."
    ) # O(1)

    # Estimated Final Time Complexity: O(n log n + 16n*m + 5n + 15) -> O(n log n)
```

### Task 4

```py
import csv

with open('texts.csv', 'r') as f: # O(1)
    reader = csv.reader(f) # O(1)
    texts = list(reader) # O(n)

with open('calls.csv', 'r') as f: # O(1)
    reader = csv.reader(f) # O(1)
    calls = list(reader) # O(n)

    telemarketers = set() # O(1)

    for record in calls: # O(n)
        if record[0].startswith("140"): # O(3)
            telemarketers.add(record[0]) # O(2)

    telemarketers_list = list(telemarketers) # O(n)
    telemarketers_list.sort() # O(n log n)

    print("These numbers could be telemarketers: ") # O(1)
    for telemarketer in telemarketers_list: # O(n)
        print(telemarketer) # O(1)

    # Estimated Final Time Complexity: O(n log n + 9n + 6) -> O(n log n)
```
