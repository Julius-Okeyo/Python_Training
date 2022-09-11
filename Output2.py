'''
Python supports very large integers
with long type but the limit of float
precision is (2^53)+1.
'''
# << operator shifts bitwise representation
#of input left by pushing zeros in from the
#right and let the leftmost bits fall off.

# >> operator shift right by pushing copies
# of the leftmost bit in from the left, and
# let the rightmost bits fall off.
print(bin(1))
a = (1<<53)+1
print(bin(a))
print(1+1.0>a)
