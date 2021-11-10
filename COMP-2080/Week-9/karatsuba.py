

a = 0b00000011 # 3
b = 0b01100001 # 96

def gen_mask(val, hi=False):

    bin_len = len(bin(val)) // 2
    if hi:
        return val & int(bin_len * '1' + bin_len * '0', 2)
    return val & int(bin_len * '0' + bin_len * '1', 2)


def binary_multiplication(a: int, b: int):

    print(gen_mask(b))
    print(gen_mask(b, hi=True))

    #binary_multiplication(a / 2, b / 2)

def binary_multiplication_Aux(a: int, b: int):
    pass

binary_multiplication(a, b)
