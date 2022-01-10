
activities = [(1, 4), (3, 5), (0, 6), (5, 7), (3, 9), (5, 9),
              (6, 10), (8, 11), (8, 12), (2, 14), (12, 16)]

s = [(0, 0)]


def activity_selector_rec(a, i, m):

    if i > m:
        return None

    if activities[i][0] > s[-1][1]:
        s.append(activities[i])
        print(f"Appending item: {i + 1}:{activities[i]}")

    activity_selector_rec(a, i + 1, m)


def activity_selector_iter(a):
    activity_len = len(a)
    for i in range(activity_len):
        if activities[i][0] > s[-1][1]:
            s.append(activities[i])
            print(f"Appending item: {i + 1}:{activities[i]}")


activity_selector_rec(a=activities, i=0, m=len(activities) - 1)
# activity_selector_iter(a=activities)
