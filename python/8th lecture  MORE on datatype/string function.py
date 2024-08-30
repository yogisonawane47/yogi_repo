'''
string: character enclosed within single, double or tripple qoutes is called string.
        Each character is encoded as ASCII or UNICODE character
        string is represented by class

 
project="python project"
print(type(project))


#Define string in python
name="mack"
print(name)


name='bot'
print(name)



msg='' hello
        mack''


print(msg)



msg="""hello bot"""
print(msg)

 


#string indexing
name="bentenissan"
print(name[0])  #b
print(name[2])  #n
print(name[:])  #bentenissan
print(name[0:]) #bentenissan
print(name[0:2])#be
print(name[:-1])#bentenissa
print(name[-2])#last 2nd letter 'a'
print(name[-3:-1])#last 3rd and 2nd letter 'sa'
print(name[::-1])#nassinetneb write word in revers



 


#string reassigning
#strings are immutable
project="python project"
print(project)
 

project="python project"
project[0] #dostnot use
  

project="python project"
#project[0]='c'
print(project)
 


#deleting string
project="python project"
#deleting[0]
del project
print(project)

 

#string formatting  \n  \t \v
project="python project it's my first project"
print(project)


project="python project it's my first project \n hello world"
print(project)
 

project="python project it's my first project \t hello world"
print(project)
 

project="python project it's my first project \v hello world"
print(project)
 

#format method:
#1.using curly braces
print("{} core web {} are two modules from PFSD".format("core web design","sql"))
#2.positional argument: 
print("{1} core web {0} are two modules from PFSD".format("core web design","sql"))
#3.keyword argument:
print("{x} core web {y} are two modules from PFSD".format(x="core web design",y="sql"))

 

#string function
#1.capitalize()first letter capital
project="project sql"
print(project.capitalize())
#2.upper
project="project sql"
print(project.upper())
#3.lower case
project="project sql"
print(project.lower())
#4 casefold
project="project sql"
print(project.casefold())
#5 swapcasae
project="project sql"
print(project.swapcase())
#6 count
project="python project python programming"
print(project.count("python",0,30))
#
project="1234"
print(project.isalnum())
#
project="python1234"
print(project.isalnum())
#
project="python1234"
print(project.isalpha())
# 
project="pythonprogramming" #is not space is true
print(project.isalpha())
#
project="python programming"  #is  space then op is false
print(project.isalpha())
#
list1=["hello","python","programming"]
print(" ".join(list1))        
#
list1=["hello","python","programming"]
print(":".join(list1)) 
#
project="Python Programming"
print(project.istitle())
#
project="python programming"#jarstring che starting small alphabet
print(project.istitle())      #asel ter te false show hoil true sathi
                            #satring alphabet capital lihave

#
project="python programming" 
print(len(project))
#
project="python programming" 
print(project.lstrip())
 
#
project="python programming" 
print(project.replace("python","cython"))
#
project="python programming" 
print(project.title())
#
project="python programming" 
print(project.split(" "))
#
project="python programming" 
print(project.split("pro"))
'''
 
 
