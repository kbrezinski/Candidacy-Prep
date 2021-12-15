
coverage = [24, 51, 11,
            5, 72, 28,
            66, 12, 100]


def cell_tower(coverage):
    opt = [None for _ in range(len(coverage))]
    return cell_tower_aux(opt, mapping=coverage, index=0, coverage=0, ans=[])


def cell_tower_aux(opt, mapping, index, coverage, ans):

    # base case when end is reached
    if index > len(mapping) - 1:
        return coverage, ans

    if opt[index] is not None:
        return opt[index]

    # add this tower
    add, ans1 = cell_tower_aux(opt, mapping, index=index + 2,
                               coverage=coverage + mapping[index],
                               ans=ans + [(index, mapping[index])])

    # skip this tower
    skip, ans2 = cell_tower_aux(opt, mapping, index=index + 1,
                                coverage=coverage, ans=ans)

    if add > skip:
        opt[index] = add, ans1
        print(f"Added tower at {index} | {ans1} ")
        return add, ans1
    else:
        opt[index] = skip, ans2
        print(f"Skipped tower at {index} ")
        return skip, ans2


print(cell_tower(coverage))
