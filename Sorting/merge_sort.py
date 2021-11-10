

def merge_sort(arr):

    # base case
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left: list, right: list) -> list:
    l, r = 0, 0
    result = []

    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1

        result += left[l:]
        result += right[r:]

        return result


arr = [38, 27, 43, 3, 9, 82, 10]


print(merge_sort(arr))

