import sys
import math
# def parity(x):
#     result = 0
#     while x:
#         result ^= x & 1
#         x >>= 1
#     return result

def parity(x):
    n = len(bin(x))
    print(n)
    n = int(n)
    count = 0
    while True:
        count += 1
        if n == 1:
            print ("O({})".format(count))
            return x & 1
        if n%2 != 0:
            x = (((x >> 1) ^ x) & 1) | ((x >> 1)& ~(1 << 0))
            n -= 1
        else:
            n = int(n/2)
            x ^= (x >> n)
        # n = int(n/2)
        
    return x & 1

# print (parity(0b111111111111111111111111111111111010100001001010010101010011010101010010101010101010101000000011111100010010101011101010101010101010101000101010101001010000000000))
print (parity(0b1110111))