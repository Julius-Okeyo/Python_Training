'''
Returns a tuple with a named entry, which means there will be a name
assigned to each value in the tuple. It overcomes the problem of
accessing the elements using the index values. With namedtuple( ) it
becomes easier to access these values, since you do not have to remember
the index values to get specific elements.
'''

from collections import namedtuple
Named_Tuple = namedtuple('Department','Name,HOD,Number_of_employees')
Named_Tuple = Named_Tuple('IT','Julius Okeyo',55)
print(Named_Tuple)
print(Named_Tuple.HOD)