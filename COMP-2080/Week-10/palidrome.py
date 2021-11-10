
import random

lst = [random.randrange(0, 4) for _ in range(10)]
print(lst)

left = 0
right = len(lst) - 1
longest = []

def longestPali(left, right, longest):

    # base case both indexes cross
    if left > right:
        longest.append(lst[left])
        return longest

    elif lst[left] == lst[right]:
        longest.append(lst[left])
        return longestPali(left + 1, right - 1, longest)

    else:
        return max(len(longestPali(left + 1, right, longest)),
                    len(longestPali(left, right - 1, longest)))

print(longestPali(left, right, longest), longest)
