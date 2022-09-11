'''Due to the counter-intuitive behavior of arbitrary-precision
arithmetic(long arithmetic), python supports very large integers
wit long type but the limit of float precision is (2^53)+1.'''
a = (1<<53)+1
print(a)
#print(1+1.0>a)
