x = 13
print(all([x < 14,x > 10, x == 13]))
#all() returns True if bool(x) is True for all
#values of x in the iterable. If the iterable
#is empty it returns True.
print(any([x > 20, x < 16, x == 10]))
#any() returns True if bool(x) is True for any
#values of x in the iterable. If the iterable
#is empty it returns False.