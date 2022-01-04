
import math

'''
Implementation of a multiplicative hash function. 
'''


def multi_hash(key: int):

    # a must approx (math.sqrt(5) - 1) / 2, so choose s that ensures that
    w = 32
    s = 2654435769
    a = s / (2 ** w)  # shows the ratio
    print(f"Ration of s / 2**w: {a=}")

    r_o = (key * s) % (2 ** 32)  # mod(2**32) removes most significant bits
    print("Shows all 32 bits of result -", end=' ')
    print(f"{r_o=:032b}")

    print("Shows first 14 bits of result -", end=' ')
    print(f"{r_o >> (32 - 14)=:014b}")
    return r_o >> (32 - 14)


key = multi_hash(key=123456)
assert key == 67, "Incorrect"

