
import numpy as np

A = np.random.randint(10, size=[4, 4])
B = np.random.randint(10, size=[4, 4])

def matMul(A: np.ndarray, B: np.ndarray):
    shape = A.shape[0]
    mid = shape // 2
    C = np.empty([shape, shape])

    matMulAux(0, mid)
    matMulAux(mid + 1, shape)

def matMulAux(lo: int, hi: int):
    if lo == hi:
        pass
