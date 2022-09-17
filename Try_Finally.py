'''
Closing Files in Python
When we are done with performing operations on the file,
we need to properly close the file.

Closing a file will free up the resources that were tied
with the file. It is done using the close() method
available in Python.

Python has a garbage collector to clean up unreferenced
objects but we must not rely on it to close the file.

f = open("test.txt", encoding = 'utf-8')
# perform file operations
f.close()
This method is not entirely safe. If an exception occurs
when we are performing some operation with the file, the
code exits without closing the file.

A safer way is to use a try...finally block.
'''

try:
    f = open('C:/Users/User/Python_Training/Try_Finally.py',encoding='utf-8')
    print(f.read())
    temp = f.read()
    f = open('C:/Users/User/Copy.py','w')
    f.write(temp)

finally:
    f.close()