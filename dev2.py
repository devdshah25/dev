

# Here we insert a function that prints a greeting, and execute it on the objects.
# It is a program using constructor.

class Person:
    
  def __init__(self, name, age): 
    self.name = name
    self.age = age
    
    # The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.

  def myfunc(self):
    print("Hello my name is " + self.name+".")
    
    
# To call the class and function.

p1 = Person("Dikshita Shetty",18)
p1.myfunc()
p2 = Person("Aditi Patekar",17)
p1.myfunc()

print("Program Over!!")
