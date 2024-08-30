'''
#Function :
            function is a block of code defined with a name 
we use function when ever we need to perform some task  multiple times
withuot writting the same code again

it can take arguments and return the values

python works on 'DRY' principle
DON't repeat Yourself

Function improves efficeincy and reduces error because of readability
of a code


Advantage:
    1.Function encapsulate reusable code:
        This means your code more organized, easy to read and promotes code
        reuse.
    2.Moduler code design:
        broken down large program into small program/more managable pieces
    3.code reuseability
    4.abstraction:
    5.support code maintainbility

Type of functions:

1.Built in Function

2.Uesr defined function:

create a function:
1.use def keyword with fnction name to define function
2.Pass no. of parameter as per your requirements
3.Define a function with function body with a block of code is nothing
butaction you  return value
4.use return to return value

 

def function_name(parameter1,parameter2...):
    #funtion body
    return value
funtion_name(actual value)


calling funtion:
function_name(actual value)


def addition(num1,num2):
    result=num1+num2
    return result
print(addition(2,4))


#create a function without any  parameter
def msg():
    print("welcome to clg")

msg()
 


Docstring: documentation string
            descriptive text written by programmer to let other know what
            block of code dose
single line docstring
multiline docstring
 
def even_number(num):
    if num%2==0:
        return "even"
    else:
        return "odd"
print(even_number(24))
 



#scope and lifetime of variables:
the scope of variable is the area  where a variable
is declared

#local scope
#Gloabal scope
 
var="mago"

def var_scope():
    local_var1="ghost"
    print(local_var1)   #print success
    
var_scope()
print(var)
print(local_var1)#error 




        local variable                                     gloabal variable
        
1.variable declared inside the              1.variable declared outside of fuction
fuction
that is not accessible from
outside of function.

2.scope=>local                              2.scpe=>gloabal


function arguments:
    1.positional argument
    2.keyword arguments
    3.defalt arguments
    4.variable length aruguments

#1.postional argument:
    postional arguments are arguments that are passed to fuction in propper postion
 
    
def sub(num1,num2):
    return num1-num2

print(sub(3,8))
 
#2 keyword argument:

def msg(name,surname):
    print("hello",name,surname)
msg(name="marko",surname="ro")
msg(surname="ro",name="marko")

 


#3 default argument:

def msg(name="GT"):
    print("GTR",name)

msg()
msg("nissan")


 


#4 variable length argument:

def mul(num1,num2):
    return num1*num2
print(mul(4,2))
 

def mul(*num):
    result=1
    for i in num:
        result=result*i
    return result
print(mul(4,2))
print(mul(444,2))
 
def mul(*num):
    result=0
    for i in num:
        result=result+i
    return result
print(mul(4,4))

 
recusive function :-

afunction call
 

def fact(num):
    result=1
    for i in range(num,0,-1):
        result=result*i
    return result
print(fact(5))
 
#recursion:
def fact(num):
    if num==0:
        return 1
    else:
        return num*fact(num-1)
print(fact(5))


#17-08-2024
 


 
#write program to show fibonacci squence

#0,1,1,2,3,5  =>6

iterations=int(input("Enter number:"))
num1,num2=0,1
count=0


num1=0
num2=1
    #0      #6
if iterations<=0:
    print("Enter positive number")
elif iterations==1:
    print(num1)
else:    
    while(count<iterations):
        print(num1)    #0
        result=num1+num2  #0+1=>result=1
        num1=num2   #1 , num1=0=>1
        num2=result  #num2=1, num2=1
        count=count+1

#output:  0,1,1,2,3,5
 
    

def recur(num):
   if num<=1:
       return num
   else: 
        return recur(num-1)+recur(num-2)

iterations=6
if iterations<=0:
    print("Positive number")
else:
    for i in range(iterations):
        print(recur(i))



#Advantage of using  recursive function
1.Reduce length of code
2.readability of code improve the to code reduction
3.Useful for complex problem


#Anonymous Function:
     anaymous function is also called as lambda function
     a function without name is called as anonymous function

     lanbda function consist of number of arguments but only one expration

syntax:
    lanbda argument:expretion

    #diffrence between lambda function and normal function
 
num=20
result=lambda num1:num1**2
print(result(num))


 
result=lambda num1:num1**2
print(result(20))


'''
#show addition of given three number  40,50,60


num1=40
num2=50
num3=60
result=lambda  num:num1+num2+num3
print(result(num1))

 
