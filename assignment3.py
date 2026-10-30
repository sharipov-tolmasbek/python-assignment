def replace_value(values, index, new_value):
    values[index] = new_value
def find_first(values, target):
    for i in range(len(values)):
        if values[i] == target:
            return i
    return -1
def summarize(values):
    tupled_list = (min(values), max(values), sum(values))
    return tupled_list

days = int(input("Enter the number of days: "))
original = []
for i in range(days):
    reading_time = int(input(f"Enter reading time for day {i + 1} in minutes: "))
    original.append(reading_time)

updated = original[:]

index_correcting = int(input("Enter the index to correct: "))
new_reading_time = int(input("Enter the new reading time: "))
replace_value(updated, index_correcting, new_reading_time)

target = int(input("Enter the reading time to search for: "))

first_target = find_first(updated, target)
target_count = updated.count(target)

minimum, maximum, total = summarize(updated)

print(f"Original: {original}")
print(f"Updated: {updated}")
print(f"Sorted: {sorted(updated)}")
print(f"Minimum reading time: {minimum}")
print(f"Maximum reading time: {maximum}")
print(f"Total reading time: {total}")

if first_target== -1:
    print("Target not found")
else:
    print(f"First matching index: {first_target}")

print(f"Matching values: {target_count}")