class Cat:
  def __init__(self, name):
    self.name = "name"

  def create_dog(self):
    self.dog_inside_cat=Dog()

class Dog:
  def __init__(self):
    print("hi I'm dog")

sam=Cat('sam')
sam.create_dog()