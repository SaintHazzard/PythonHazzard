


class Person(object):
     def __init__(self, name, age):
          self.name = name
          self.age = age
     def __contains__(self, param1):
          return True if param1 in self.__dict__.keys() else False


p = Person('Robby Krieger', 23)
print('age' in p)



