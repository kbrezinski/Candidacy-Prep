
arr = [1, 4, 1, 2, 7, 0, 9, 9, 6, 5, 2]
count = [0 for _ in range(10)]
final_arr = [None for _ in range(len(arr) - 1)]

# counter for the numbers
for num in arr:
    count[num] += 1

# create a summation, in-place
for i in range(2, len(count)):
    count[i] = count[i] + count[i - 1]

print(count)

# unravel the count
for num in arr:
    final_arr[count[num] - 1] = num
    count[num] -= 1

print(final_arr)
