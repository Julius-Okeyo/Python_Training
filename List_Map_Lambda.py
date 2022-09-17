from math import exp
list1 = [1,2,3,4,5,6,7,8,9]
Even_numbers = list(filter(lambda x: x%2==0,list1))
#Filter function returns only those values that fit certain criteria.
#The function returns a ‘Filter object’ and you need to encapsulate
# it with a list to return the values.
print(Even_numbers)
Mapped_values = map(lambda x: x*exp(x),list1)
#Map function returns a modified list where every value in the original
# list has been changed based on a function.
print(Mapped_values)