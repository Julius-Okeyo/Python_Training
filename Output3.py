'''
What is the output of the following code?
'''

A0 = dict(zip(('a','b','c','d','e'),(1,2,3,4,5)))
# zip function binds the keys to their corresponding values.

A1 = range(10)

# To compare the values in a dictionary to a some other
# values you must call the values() function. Otherwise
# calling the dictionary name alone returns the keysas
# observed below.
A2 = sorted([i for i in A1 if i in A0.values()])
A3 = sorted([A0[s] for s in A0])

A4 = [i for i in A1 if i in A3]


A5 = [[i,i*i] for i in A1]

print(A0,A1,A2,A3,A4,A5)