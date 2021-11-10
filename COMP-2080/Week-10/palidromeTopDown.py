
import random

lst = ['k','r','r','a','r','y','a','k']

def longestPali(lst):
    n = len(lst)
    longest = [[False] * n for _ in range(n)]
    longestPaliAux(lst, longest, 0, n - 1)
    print(longest)


def longestPaliAux(lst, longest, i, j):

    # Check if table entry is empty
    if not longest[i][j]:
        # Check if frame size is 1
        if i == j:
            longest[i][j] = lst[i]
        # Check if first and last symbols are equal
        elif lst[i] == lst[j]:
            # Check if frame size is 2 and the same char
            if j == (i + 1):
                longest[i][j] = lst[i] + lst[j]
            # Otherwise recurse down both ends and append same char
            else:
                longest[i][j] = longestPaliAux(lst, longest, i + 1, j - 1) + lst[i] + lst[j]
        else:
            s1 = longestPaliAux(lst, longest, i, j - 1)
            s2 = longestPaliAux(lst, longest, i + 1, j)
            if s1 > s2:
                longest[i][j] = s1
            else:
                longest[i][j] = s2
    return longest[i][j]

longestPali(lst)
