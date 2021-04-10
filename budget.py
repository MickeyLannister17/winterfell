class Animal:
    animal_type = 'mammal' # Animal type is tied to the class object (Animal)

    # instance method

    def __init__(self, name, number_of_legs): # An instance of the class object(rat/cat)
        self.name = name
        self.number_of_legs = number_of_legs

    def can_run(self):
        print('{}  {}'.format())


# Types of methods: class method, static method
# instantiating

animal_one = Animal('Rat', 2)  # instantiating the class (Animal)
animal_two = Animal('Cat', 4)  # rat and cat are passed into the self.name function
print(animal_one.animal_type)

animal_one.can_run()
animal_two.can_run()