## Animal is-a object (yes,  sort of confusing) look at the extra credit
class Animal(object):
  pass

## Dog is-a Animal
class Dog(Animal):

  def __init__(self, name):
    ## Dog instance name
    self.name = name

## Cat is-a Animal
class Cat(Animal):

  def __init__(self, name):
    ## Cat instance name
    self.name = name

## Person is-a object
class Person(object):

  def __init__(self, name):
    ## Person instance name
    self.name = name
    
    ## Person has-a pet of some kind
    self.pet = None

## Employee is-a person
class Employee(Person):

  def __init__(self, name, salary):
    ## Define Person instance name
    super(Employee, self).__init__(name)
    ## Employee instance salary
    self.salary = salary

## Fish is-a object
class Fish(object):
  pass

## Salmon is-a fish
class Salmon(Fish):
  pass

## Halibut is a fish
class Halibut(Fish):
  pass

## Instance of Dog with name Rover
rover = Dog("Rover")

## Instance of Cat with name Satan
satan = Cat("Satan")

## Instance of Person with name Mary
mary = Person("Mary")

## Mary has-a Cat
mary.pet = satan

## Instance of Employee named Frank and salary is 120000
frank = Employee("Frank", 120000)

## Employee has-a Pet
frank.pet = rover

## Instance of Fish
flipper = Fish()

## Instance of Salmon
crouse = Salmon()

## Instance of Halibut 
harry = Halibut()