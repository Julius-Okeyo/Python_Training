global Record_dogs
global Record_cats
Record_dogs = {}
Record_cats = {}
number_of_animals = int(input('Number of animals: '))
class Dogs:
    def __init__(self,name,age,breed,animal_type):
        global Record
        #Instance attributes
        self.name = name
        self.age = age
        self.breed = breed
        self.animal_type = animal_type
        if self.animal_type == 'dog':
            Record_dogs[name] = [age,breed]
    def __str__(self):
        return f'{self.name} is a {self.breed} of {self.age} years old'\
        if self.animal_type == 'dog' else\
        f'{self.name} is a {self.color} {self.breed} of {self.age} years old'
    def main(self):
        pass
class Cats(Dogs):
    def __init__(self,name,age,breed,animal_type,color):
        super().__init__(name,age,breed,animal_type)
        self.color = color
        Record_cats[name] = [age,breed,color]

for i in range (number_of_animals):
    animal_type = input('dog/cat: ')
    name = input('Name: ')
    age = input('Age: ')
    breed = input('Breed: ')
    if animal_type == 'cat':
        color = input('Color: ')
        name = Cats(name,age,breed,animal_type,color)
    else:
        name = Dogs(name,age,breed,animal_type)
    print(name)
print(Record_dogs)
print(Record_cats)
