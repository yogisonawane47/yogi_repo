'''
#class:- a class is a user define blueprint or prototype from which object are created.
#1.class is blueprint or code templet for object creation which binds/join the data members
#and method into single unit.

#*.what is an object?
#--> object is a instance of a class.
#object have two characterstics they have sate and behaveor.
#state mean atrribute and datamembers.
#and behaveour mean method.

#every object following properties

#syntax:
#class class-name:
#"this is docstring"
#<statement-1...>
#<statement-2...>
#.
#.
#.
#.
#<statement-n...>



#object:-
#object-name=class-name(arguments)

 

#now create class:

class student:
    pass

#now create object:

obj1=student()



#what is constructor in python?
#--> a constructor is a special method  used to create and intialize .
#this method define in the class.
#1.the constroctor excute automatically when at the time of object creation.
#2.the primary use of this method is to declear data member or  instance variable.

#syntax of def : def__inti__(self):

#where def is keyword use define function.
#__init__() -->  this mehod is reserve method.this method gets called as soon as object of class is instantiated.

#self:- the self refers to the current object.

#type of constructor:

#1. default constructor-->
 
class student:
    def show(self):
        print("This is show method")

stud1=student()
stud1.show()

 
#2.non parameterize constructor-->

class student:
    def __init__(self):
        self.name="madhav"
        self.address="khandala"

    def show(self):
        print(self.name,self.address)
stud1=student()
stud1.show()
  

#3.parameterized constructor-->


class student:
    def __init__(self,name,roll,address):
        self.name=name
        self.roll=roll
        self.address=address

    def show(self):
        print(self.name,self.roll,self.address)
stud1=student("keshav",1,"keral")
stud1.show()
 
#destructor--> when a object is deleted or destroy
#syntax-->
    def __del__(self):
        statement:

#Instant variable in python:- If  the value of variable varies object to object then
#                              this variable called instant variable.and you can modify
#                                instantly that's mean change value at run time.

#how to access instance variable?
#--> 



#without show-->

class student:
    def __init__(self,name,roll,address):
        self.name=name
        self.roll=roll
        self.address=address

     
stud1=student("keshav",1,"keral")
print(stud1.name,stud1.roll,stud1.address) 


#calss variable-->

class student:
    class_name="institude"
    def __init__(self,name,roll,address):
        self.name=name
        self.roll=roll
        self.address=address

    def show(self):
        print(self.name,self.roll,self.address,student.class_name)
stud1=student("keshav",1,"keral")
stud1.show() 

#22-08-2024

#instance method:- instance method performs a set of actions on the data/value provided
#                   by instance variable.
#each object has its own copy of instance attribute
#instance variables are not shared between objects.


class student:
     
    def __init__(self,name,roll,address):
        self.name=name        #instance variable
        self.roll=roll
        self.address=address

    def show(self):                 #instancce method
        print(self.name,self.roll,self.address,student.class_name)
stud1=student("keshav",1,"keral")
stud1.show()

 
#class method:- it is use to access or modify the class state class methods that are called on
#               the class itself not on a specific object instance.
#               class methods are bound to only class not objects of the class it can access only
#               class variables.

#class variable is decleared inside the class but outside of any method.

class emp:
    company_name="vincarrt"
    def __init__(self,empid,empname,empcontact):
        self.empid=empid
        self.empname=empname
        self.empcontact=empcontact
    def show(self):
        print("empis is:",self.empid,"empname:",self.empname,"emp contact:",self.empcontact,emp.company_name)

emp1=emp(1,"keshav",12345678909)
emp1.show()




class emp:
    company_name="vincarrt"
    def __init__(self,empid,empname,empcontact):
        self.empid=empid
        self.empname=empname
        self.empcontact=empcontact
    def show(self):
        print("empis is:",self.empid,"empname:",self.empname,"emp contact:",self.empcontact,self.company_name)

emp1=emp(1,"keshav",12345678909)
emp1.show()
 


 


class emp:
    company_name="vincarrt"
    def __init__(self,empid,empname,empcontact):
        self.empid=empid
        self.empname=empname
        self.empcontact=empcontact
    def show(self):
        print("empis is:",self.empid,"empname:",self.empname,"emp contact:",self.empcontact,emp.company_name)

    @classmethod
    def change_name(cls):
        print("current company name:",emp.company_name)
        print("current company name:",cls.company_name)

emp1=emp(1,"keshav",12345678909)
emp1.show()
emp1.change_name()

 
#syntax for company name change:-
class emp:
    company_name="vincarrt"
    def __init__(self,empid,empname,empcontact):
        self.empid=empid
        self.empname=empname
        self.empcontact=empcontact
    def show(self):
        print("empis is:",self.empid,"empname:",self.empname,"emp contact:",self.empcontact,emp.company_name)

    @classmethod
    def change_name(cls,company_name):
        print("current company name:",emp.company_name)
        print("current company name:",cls.company_name)
        
        cls.company_name=company_name
        print("new company name:",cls.company_name)
        
emp1=emp(1,"keshav",12345678909)
emp1.show()
emp1.change_name("koniesegg")

 

#static method:- this is genral purpose utility method that perform a task in isolation
#                   this method doent requrie any self,cls.
#               for static method we require @staticmethod decorator.

 


class emp:
    company_name="vincarrt"
    def __init__(self,empid,empname,empcontact):
        self.empid=empid
        self.empname=empname
        self.empcontact=empcontact
    def show(self):
        print("empis is:",self.empid,"empname:",self.empname,"emp contact:",self.empcontact,emp.company_name)
    @staticmethod
    def projects(project):
        print("project name is",project)

emp1=emp(1,"keshav",12345678909)
emp1.show()
emp1.projects("E commerce website")


 

#inheritance:- the process of inheriting other properties of the parent class
#             into a child class.
#             is called inheritence.

#             Existing class_super class-parent class-Base class
#             new class-subclass-child class-derived class.
#             in inheritance child class acquire all the data
#             memberce and method from the parent class.


#syntax:-


    class Baseclass:
        Body of base class
    class dericeclass (Baseclass):
        Body of derived class

#types of inheritance:-

        1.single inheritance
        2.Multiple inheritance
        3.Multilevel inheritance
        4.Hierarchical inheritance
        5.Hybrid inheritance

 

#singel inheritance
class person:
    def person_info(self):
        print("Inside the person class")
        
class emp(person):
    def emp_info(self):
        print("inside the emp class")

emp1=emp()
emp1.emp_info()
emp1.person_info()


 
#multiple inheritance:-

class person:
     def __init__(self,name,age):
         self.name=name
         self.age=age
     def person_info(self):
         print("name",self.name,"age",self.age)


class company:
    def company_info(self,company_name):
        print("name:",company_name)

class emp(person,company):
    def emp_info(self,salary):
        print("Salary",salary)
        
emp1=emp("kong",56)
emp1.person_info()
emp1.company_info("vincart")

 


#multilevel inheritence:-


class person:
     def __init__(self,name,age):
         self.name=name
         self.age=age
     def person_info(self):
         print("name",self.name,"age",self.age)
 
class emp(person):
    def display(self,empdept):
        print("Department is:",empdept)

class manager(emp,person):
    def man_info(self,manager_name):
        print("manager is:",manager-name)
        
 
emp1=emp("max",34)
emp1.person_info()
emp1.display("Designer")
emp1.manager_info("lamark")


 
#23-08-2024
#(BY using you can creat addition calculator!!!)

class First:
     def getnum(self):
          self.num=int(input("Enter number:"))

class second(First):
     def getnum1(self):
          self.num1=int(input("Enter number:"))

class result_of_number(second):
     def result(self):
          addition=self.num+self.num1
          print("Addition:",addition)

res=result_of_number()
res.getnum()
res.getnum1()
res.result()

 
#hierarchical inheritance:- more than one childe derived from single parent class.


class vehical:
     def info(self):
          print("This is veicle class")

class car(vehical):
     def car_info(self):
          print("This is car info")

class bike(vehical):
     def bike_info(self):
          print("This is bike info")

bk=bike()
bk.bike_info()
bk.info()

#bk.car_info() there is come error because bk is child and also car is child they dosn't call each other.


 


#Hybrid inheritance:-

          p
     c         c
     c         c





class vehical:
     def info(self):
          print("This is veicle class")

class car(vehical):
     def car_info(self):
          print("This is car info")

class bike(vehical):
     def bike_info(self):
          print("This is bike info")


class truck(vehical):
     def truck_info(self):
          print("This is truck info")

class boat(vehical):
     def boat_info(self):
          print("This is boat info")






#super:-when a class inherits all properties and behavior from the parent class is called inheritance.
#          In child class we can refer parent class by using super () function.
#          The super () function returns a temporary object of parent class
#          that allows us to call parent class method inside a child class method.

#Benifits:-Not required to remember or specify the parent class name to access its method.
#               super() -single,multiple

 


class company:
     def company_name(self):
          return "momo"
     
class employee(company):
     def info(self):
         c_name=super().company_name()
         print("company name",c_name)
         
emp=employee()
emp.info()


 


#decorator:-

def div(num,num1):
     print(num/num1)

#print(div(4,2))
#print(div(2,4))



def newdiv(func):
     def inner(num,num1):
          if num<num1:
               num,num1=num1,num
          return func(num,num1)
     return inner

#div1=newdiv(div)
#div1(2,4)

#OR

@newdiv
def div(num,num1):
     print(num/num1)
div(2,4)

 

#Encapsulation:-  It is process of bundelling data member and methods into single unit .
#                   using Encapsulation
#                   we can hide an object internal representation from the outside.
#                   This is called as information hiding

#Encapsulation allows us to restrict accessing variable and method directly.

#access specifiers:-
#                    1.public:- Accessible anywhere from outside of class.
#                    2.protected:- Accessible that class and its subclasses.
#                    3.private:-Accessible within that class.
 
#public:-
class Employee:
     def __init__(self,name,project,salary):
          self.name=name           #public
          self.project=project     #protected
          self.salary=salary       #private

emp=Employee("mangesh","jesko project",70000)
print(emp.name,emp.project,emp.salary)


#private:-
class Employee:
     def __init__(self,name,project,salary):
          self.name=name           #public
          self.project=project     #protected
          self.__salary=salary       #private

emp=Employee("mangesh","jesko project",70000)
print(emp.name,emp.project,emp.__salary)



#Access private member outside of a class using two wayed:
#1.using instand method
#2.name mangling

#1.using instand method 
class Employee:
     def __init__(self,name,project,salary):
          self.name=name            
          self.project=project      
          self.__salary=salary       
     def show(self):
         print(self.name,self.project,self.__salary)


emp=Employee("mangesh","jesko project",70000)
emp.show()

#2.name mangling

class Employee:
     def __init__(self,name,project,salary):
          self.name=name           #public
          self.project=project     #protected
          self.__salary=salary       #private

emp=Employee("mangesh","jesko project",70000)
print(emp._Employee__salary)



#26-08-2024
 
#protected member:- are accessible within the class and its subclasses
#protected are with single underscore!!!!
class company:
     def __init__(self):
      self._project="first_project"
  
class Employee(company):
    def __init__(self,name):
        self.name=name
        company.__init__(self)
    def show(self):
        print("Employee name:",self.name)
        print(self._project)

c=Employee("mahesh")
c.show()
print("project is:",c._project)


 

#getter and setter method
#getter to access data member
#setter to modify the data member

class employee:
    def __init__(self,name,salary):
        self.name=name
        self.__salary=salary

    def get_salary(self):
        return self.__salary
    def set_salary(self,salary):
        self.__salary=salary
        
emp=employee("laki",20000)
print(emp.name,emp.get_salary())
emp.set_salary(29000)
print(emp.name,emp.get_salary())



 

#advantage:1.security of data
#          2.data hiding

 

#Abstraction:- abstraction is used to hide the internal functionality of the function from the users.
#the users only interact with basic implementaion of the function but inner working of code is hidden

#in python abstract can be achieved by
#by using abstract classes and interfaces

#Abstract Class:-
#                A class consist of one or more abstract method

#abstract method:-
#abstract method do not contain their implementation

#abstract class can be inherited by the subclass and abstract method its defination in the subclass.

 

from abc import ABC,abstractmethod

class shop(ABC):
    def __init__(self,product,description,price,quantity):
        self.product=product
        self.description=description
        self.price=price
        self.quantity=quantity
    @abstractmethod
    def sale(self):
        pass
    
class mobile(shop):
    def sale(self,discount=20):
        if self.quantity>=10:
            print("You are eligible for discount of 20%")
        self.total_price=self.price*self.quantity
        self.discount=self.total_price-(self.total_price*(discount/100))
        print("product is.",self.product)
        print("Description is :",self.description)
        print("Total price",self.discount)
prod=mobile("Huwaai Mobile","Samrtphon",90000,12)
prod.sale()



'''

#polymorphism:
#An ability of an object to take many from.


student=['mahesh','kashi','yogi','kaushal']
print(len(student))




#27-08-2024
#raise keyword:-
#the raise keyword is used to raise the excecption

n=int(input("Enter numberER:"))

ifn>0:
    raise ValueError("Positive number")
else:
    raise TypeError("Negative Number")


