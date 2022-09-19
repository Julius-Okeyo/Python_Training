'''
Attributes created in .__init__() are called instance attributes.
An instance attributes value is specific to a particular instance
of the class. All Dog objects have a name, age, and breed but the
values for the name and age attributes will vary depending on the
Dog instance.
On the other hand, class attributes are attributes that have the same
value for all class instances. You can define a class attribute by
assigning a value to a variable name outside of .__init__().
Use class attributes to define properties that should have the same
value for every class instance. Use instance attributes for properties
that vary from one instance to another.
Use the __init__() function to assign values to object properties,
or other operations that are necessary to do when the object is being
created:
Another useful magic method is __str__(). It is overridden to return
a printable string representation of any user defined class. We have
seen str() built-in function which returns a string from the object
parameter. For example, str(12) returns '12'. When invoked, it calls
the __str__() method in the int class.
'''
from plumbum import cli
class Pets(cli.Application):
    #class attribute
    global Record_dogs
    global Record_cats
    Record_dogs = {}
    Record_cats = {}
    number_of_dogs = int(input('Number of dogs: '))
    number_of_cats = int(input('Number of cats: '))
    class Dogs:
        def __init__(self,name,age,breed):
            global Record
            #Instance attributes
            self.name = name
            self.age = age
            self.breed = breed
            Record_dogs[self.name] = [self.age,self.breed]
        def __str__(self):
            #Methods like .__init__() and .__str__() are called dunder methods
            # because they begin and end with double underscores. There are many
            # dunder methods that you can use to customize classes in Python.
            return f'{self.name} is a {self.breed} of {self.age} years old'
        def main(self):
            pass

    def main(Dogs,number_of_dogs):
        for i in range (number_of_dogs):
            name = input('Dog_Name: ')
            age = input('Dog_Age: ')
            breed = input('Dog_Breed: ')
            name = Dogs(name,age,breed)
            print(name)
        print(Record_dogs)
    main(Dogs,number_of_dogs)

    class Cats:
        def __init__(self,name,age,breed):
            global Record_cats
            self.name = name
            self.age = age
            self.breed = breed
            Record_cats[self.name] = [self.age,self.breed]
        def __str__(self):
            return f'{self.name} is a {self.breed} of {self.age} years old'
        def main(self):
            pass

    def main(Cats,number_of_cats):
        for i in range (number_of_cats):
            name = input('Cat_Name: ')
            age = input('Cat_Age: ')
            breed = input('Cat_Breed: ')
            name = Cats(name,age,breed)
            print(name)
        print(Record_cats)
    main(Cats,number_of_cats)
if __name__ == '__main__':
    Pets.run()
