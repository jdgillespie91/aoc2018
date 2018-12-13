from itertools import repeat

# Read the data file
with open('day1.txt') as f:
    frequency_changes = [int(x) for x in f.read().split('\n') if x]

# Part One
print(sum(frequency_changes))

# Part Two
seen_frequencies = set()
frequency = 0

# Iterate over frequency changes continuously.
for changes in repeat(frequency_changes):

    # Iterate over frequency changes, storing the frequency and breaking if we see a repeat.
    for frequency_change in changes:
        frequency += frequency_change

        if frequency in seen_frequencies:
            repeated_frequency = frequency
            break

        seen_frequencies.add(frequency)

    # If we don't break from the inner loop, start again.
    else:
        continue

    # If we break from the inner loop, break from this one too.
    break

print(repeated_frequency)
