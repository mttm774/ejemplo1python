 #program to illustrate protected access modifier in a class
 
# super class
class Student:
    
     # protected data members
     _name = None
     _roll = None
     _branch = None
    
     # constructor
     def __init__(self, name, roll, branch): 
          self._name = name
          self._roll = roll
          self._branch = branch
    
     # protected member function  
     def _displayRollAndBranch(self):
 
          # accessing protected data members
          print("Roll: ", self._roll)
          print("Branch: ", self._branch)

#publicos
class Geek:
      
     # constructor
     def __init__(self, name, age):
           
           # public data members
           self.geekName = name
           self.geekAge = age
 
     # public member function     
     def displayAge(self):
           
           # accessing public data member
           print("Age: ", self.geekAge)

# program to illustrate private access modifier in a class
 
class Geek:
    
     # private members
     __name = None
     __roll = None
     __branch = None
 
     # constructor
     def __init__(self, name, roll, branch): 
          self.__name = name
          self.__roll = roll
          self.__branch = branch
 
     # private member function 
     def __displayDetails(self):
           
           # accessing private data members
           print("Name: ", self.__name)
           print("Roll: ", self.__roll)
           print("Branch: ", self.__branch)
    
     # public member function
     def accessPrivateFunction(self):
            
           # accessing private member function
           self.__displayDetails()            