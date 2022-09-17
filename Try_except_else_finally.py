animal = input()
try:
    #The try block lets you test a block of code for errors.
    #If animal has less than three characters a error will arise.
    x = animal[-3]
except:
    #The except block lets you handle the error.
    print('Animal can only be a dog or a cat')
else:
    #The else block lets you execute code when there is no error in the try block.
    if animal == 'dog':
        print('Dogs bark!') 
    if animal == 'cat':
        print('Cats meaow!')
finally:
    #The finally block lets you execute code, regardless of the result of the try- and except blocks.
    print(animal,' is a very popular animal')
