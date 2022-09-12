'''
Python supports negative indexes. What are they and why are they used?
The sequences in Python are indexed. It consists of positive and
negative numbers. Positive numbers use 0 as the first index, 1 as the
second index, and so on. Hence, any index for a positive number n is n-1.

Unlike positive numbers, index numbering for the negative numbers starts
from -1 and it represents the last index in the sequence. Likewise, -2
represents the penultimate index. These are known as negative indexes.
Negative indexes are used for:

1. Removing any new-line spaces from the string, thus allowing the string to
except the last character, represented as S[:-1]
2. Showing the index to representing the string in the correct order.
'''

list = [1,3,2,4,12,4,5,2]
print(list[-1])
# When a range of indices is given e.g. 2:5 it is inclusive of the start
# of the range i.e. 2 but exclusive of the end i.e. 5. In the example
# below python will print the elements on the 2nd, 3rd, and 4th positions.
print(list[2:5])
string = 'test_string'
print(string[:-3])
# Negative index range also comforms to the start and end rules.
print(string[-8:-3])
