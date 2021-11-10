    # 16, 8, 4, 2, 1
fir = 0b0101 # 5
sec = 0b0011 # 3

string = '0101'
integer = 4

#print(bin(fir << 2), fir << 2)
print(bin(fir & sec))
print(bin(fir | sec))
print(bin(fir ^ sec))
print(bin(~fir))
