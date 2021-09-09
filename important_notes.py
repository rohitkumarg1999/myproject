# method overloading and overriding
'''
            # overloading #
pyhton does not supported the python method  overloading,constructer overloading ,
NOte: it only support the operater overloading
ie: 2+3=5
at the same place
"rohit" + "mohit"=rohitmohit
      ################# magixc methods  ##############
class Book:
    def __init__(self,pages):
        self.pages=pages
    def __add__(self,other):
        total=self.pages+other.pages
        return total
    def __mul__(self,other):
        rel=self.pages*other.pages
        return rel
    
b1=Book(100)
b2=Book(200)
print(b1+b2)
print(b1*b2)
'''




######################### MEthod Overriding #######################
'''
method overding is is concept if any class having a  method in class if that class is inherited by other
child class and same name of method is declare in the child class may be different differt argument by creating
the object of the child class we cant not access parent class method because it is overide by the child class method
.funtion in parent class can not be access by child class object .because child class
funtion is overide on the parent class method.



####code 
class A:
    def target(self):
        print("i will become millionaire by 2035")
class B(A):
    def target(self):
        print("i will become millionaire by 2030 ")

rohit=B()
rohit.target()


  ##################second example
 ie:class A:
    def __init__(self,x):
        self.x=x
        print("class A onstructor val : ",self.x)
        A.fun1()
    def fun1(self):
        print("this is class A function")
        
class B(A):
    def __init__(self,y,x):
        super().__init__(x)
        self.y=y
        print("the constructor value of class B is ",y)
        
    def fun1(self,x):
        print("this is class B funtion")
 



'''
                                   ##################### inheritence #######################
'''

inheritence s concept in python through this one class of method  and their behaviour is inherited by other class
class chiled class and inherited class called parent class or super class thorough this the object od the child class
is able to access the method and variable of the parent class  called inheritence.
ie-
  class A:
    def __init__(self,x):
        self.x=x
        print("class A onstructor val : ",self.x)
        
    def fun2(self):
        print("this is class A function")
        
class B(A):
    def __init__(self,y,x):
        super().__init__(x)
        self.y=y
        print("the constructor value of class B is ",y)
        
    def fun1(self,x):
        print("this is class B funtion")
obj1=B(10,20)
obj1.fun2()
obj1.fun1()

'''


                             ###########################multilevel inheritence ####################

'''
i.e:

class A:
    def __init__(self):
        self.x=10
        
        print("class A onstructor val : ",self.x)
    
    def fun1(self):
        print("this is class A function")
        
class B(A):
    def __init__(self):
        super().__init__()
        self.y=20
        
    
        print("class B constructor value ",self.y)
        
    def fun2(self):
        print("this is class B function")
class C(B):
    def __init__(self):
        super().__init__()
        self.z=30
        
        print(" class C constructor value ",self.z)
    def fun3(self):
        print("this is class C function")


        
obj1=C()
obj1.fun1()
obj1.fun2()
obj1.fun3()'''

                      #################multiple Inheritence######################


'''
it is nothing but inheritence in which two are more then two classess are inherited by the chiled class at once 

class A:
    def __init__(self):
        print("constructor A")
    def funA(self):
        print("tis is class A fun")
class B:
    def __init__(self):
        print("constructor  B")
    def funB(self):
        print("this is class B fun")


class C(A,B):
    def __init__(self):
        A.__init__(self)
        B.__init__(self)
        print("constructor C")
    def funC(self):
        print("this is class C fun")
obj1=C()
obj1.funA()
obj1.funB()
obj1.funC()


                             
'''                                      ########################Access modifirs in pyhton########################

'''
three forms of access modifiers, which are Public, Protected and Private in a class.
                                        ##########public access modifiers :############
hey can be access from anywhere inside class ,outside the class
#code
class Geek:
    
       
     # constructor
    def __init__(self, name, age): 
            
           # public data mambers  
           self.geekName = name 
           self.geekAge = age 
  
     # public memeber function       
    def displayAge(self): 
            
           # accessing public data member 
           print("Age: ", self.geekAge) 
  

obj = Geek("R2J", 20) 
  
# accessing public data member 
print("Name: ", obj.geekName)
obj.geekAge=50                   #changing the public variable outside  the class 
print("change NAME",obj.geekAge)
  
# calling public member function of the class 
obj.displayAge()'''


                       ##########################protected Access modifier ###########################

'''                      
protected member are member those can  access inside the class .we use (_underscore befor the name)
it can also be accessible outside the class but we need to put underscore before the instance variable
it is just convetionthat it is protected .but by default every variable is public

#code
class Student:
    def __init__(self,x,y):
        self._name=x
        self._roll=y
    def display(self):
        print("name of person",self._name)
        print("roll number of the person",self._roll)
obj=Student("rohit",16246)

obj.display()
obj._name="mohit"
obj._roll=16232

obj.display()



'''
                                              #########################private acesss modifiers##########################

'''private access modifiers are most secure ,teyare only accesible inside the class we use duble undescore befor the varible
and n private member same in case of private member we use the duble underscore (__)


class People:
    __name=None
    __roll=None
    __branch=None
    def __init__(self,name,roll,branch):
        self.__name=name
        self.__roll=roll
        self.__branch=branch
    def __display(self):
        print("name of people:",self.__name)
        print("roll number of peole",self.__roll)
        print("branch of people:",self.__branch)
    def accessprivatemember(self):
        self.__display()

obj=People("rohit",16246,"CSE")
obj.accessprivatemember()
obj._People__display()#accessing private member funtion ouside the class
print(obj._people__name)#accesing private member outside the class

'''
                              ####################Abstraction #####################

'''
Abstraction means hiding the complexity and only showing the essential features of the object.
So in a way, Abstraction means hiding the real implementation and we, as a user, knowing only how to use it.
class which is child class of the ABC class ,and you can say that abstarct class is the blueprint for other class
class contain one or more abtract method called abstract class



#code
from abc import ABC,abstractmethod
class Polygon(ABC):
    
    def noofside(self):
        pass
class Triangle(Polygon): 
  
    # overriding abstract method 
    def noofsides(self): 
        print("I have 3 sides") 
  
class Pentagon(Polygon): 
  
    # overriding abstract method 
    def noofsides(self): 
        print("I have 5 sides")
obj1=Pentagon()
obj1.noofsides()
obj2=Triangle()
obj2.noofsides()
'''


                                         ####################Encapsulation##################

'''
Encapsulation is one of the fundamental concepts in object-oriented programming (OOP). It describes
the idea of wrapping data and the methods that work on data within one unit his puts restrictions on
accessing variables and methods directly and can prevent the accidental modification of data
'''

#code
class Base:
    def __init__(self):
         
        # Protected member
        self._a = 2
 
# Creating a derived class    
class Derived(Base):
    def __init__(self):
         
        # Calling constructor of
        # Base class
        Base.__init__(self) 
        print("Calling protected member of base class: ")
        print(self._a)
 
obj1 = Derived()
         
obj2 = Base()



                                       ############################# 




    






    
        


    
    


              
