'''
 #range



for i in range(5):   
    print(i)  
for i in range(1,11):
    print(i)
   
for i in range( 1,11,2):    
    print(i)  
 

for i in range(11,1,-1):   
    print(i)  

for i in range(11):  
    print(i)
    print(' ')

 
 



string_1='hello python'
for i in string_1:
    print(i)
    
 


list1=[10,20,30,40,50]
for i in list1:
    print(i)
    print(" ")


list1=[10,20,30,40,50,True]
for i in list1:
    print(i)
    print(i)





tuple1=(10,20,30,40,50)
for i in tuple1:
    print(i)




list1=[10,20,30,40,50,1]
for i in range(len(list1)):
    print(i)
    print(" ")    



list1=[10,20,30,40,50]
for i in range(len(list1)):
    print(list1[i])
    print(" ")  


#write a program in python to show even numbers from given list


list1=[10,20,33,44,30,60,70]
for i in list1:
    if i%2==0:
        print(i)




#write a program in python to show even and odd numbers from given list


list1=[10,20,33,44,30,60,70]
even_list=[]
odd_list=[]
for i in list1:
    if i%2==0:
        even_list.append(i)
    else:
        odd_list.append(i)
print(even_list)
print(odd_list)
        

 
#nested for loop


for i in range(1,4):
    for j in range(1,4):
        print(j)
    print()


for i in range(1,4):
    print("i",j)
    for j in range(1,4):
        print("i",j)





#wtire a program to find square of  number from given
        
list1=[2,5,7,4,9]
square_list=[]
for i in list1:
    result=i**2
    square_list.append(result)
    print(square_list)
 



list1=[2,5,7,4,9]
square_list=[]
for i in list1:
    result=i*i
    square_list.append(result)
    print(square_list)

 

 #write a program to find sum of N number when n is provided by user

num=int(input("enter number:"))
result=0

for i in range(1,num+1):
    print(1)
    result=result+i
    print(result)
 
 

 
#write a program in python find  factorial of given number

 
num=int(input("enter number:"))
result=1

for i in range(1,num+1):
   result=result*i
print(result)
 
 

#write a python program to find  avrage  of list of number
#write a python program to find reverse number
#find largest number from given list
#find even number and find square of these even number
#find accurence of given number
#find out 

 


#while loop:
 while loop is a control flow statement in python used for
 itreating a block of code repeatly as long as specifide
 condition TRUE




 initialization of variable
 while(condition):
     statement/s
     increament/decreament
 
      


 
#write a program to show factorial of number using while loop




num=int(input("enter number:"))
i=1
fact=1
while(i<=num):
    fact=fact*i
    print(fact)
    i=i+1
print=(fact)    
    

 



#write a program in python to show  sum of digit number


num=int(input("enter number:"))

sum1=0

while(num>0):
    rem=num%10
    sum1=sum1+rem
    num=num//10
print(sum1)
 


num=int(input("enter number:"))#123
 
sum1=0

while(num>0):
    rem=num%10
    sum1=sum1*10+rem
    num=num//10
print(sum1)


 

num=int(input("enter number:"))#123
 
 

while(num>0):
    rem=num%10
    print(rem,end='')
    num=num//10

 

1.break:    python stops the current loop and control flow transfered
            to the following lines of code immeditely following the loop
            or
            if there is need to stop working of loop even if loop condition is
            trueve use break keyword
  

ex:
 

num=1
while (num<=10):
    if num==5:
        break
    print(num)
    num=num+1
print("hello  ")    
    
  
2.continue:
                it skips the current itaretion of a loop and immdiataly jump to next iteration
 
#count occurence of letter 'a' in given sizin

name=input("Enter Name:")
count=0
for char in name:
    print(char)
 



name=input("enter name:")
count=0
for char in name:
    if char!='a':
        continue
    else:
        count=count+1
print(count)
 
 

for i in range(10):
    if i==5:
        continue
    else:
        print(i)
 
    
#find even number from given range using continue

for i in range(1,10):
    if i%2!=0:
        continue
    else:
        print(i)


for i in range(10):
    if i%2!=0:
        continue
    else:
        print(i)


for i in range(10):
    if i%2==0:
        continue
    else:
        print(i)

 
        
#3.pass:
            it is null statement nothing happended when this
            statement is occured is given block of code

 


list1=[10,20,30,40]
for i in list1:
    pass
#panno ke upper rakha weight.

 


#parttens with loop

1.decide the number of rows after
2.that decide how many column in given partten
3.you have itterate yhe column
4.print star or number or character
5.add a new line after each iteration of the outer loop
    print()       
 

#for show star partten verticaly
for i in range(1,6):
    print("*")
 
#for show star partten horizontaly
for i in range(1,6):
    print("*",end=" ")
 
for i in range(1,6):
    for j in range(1,i+1):
        print("*",end=" ")
    print()
 
 
#display square in star partten

for i in range(1,6):
    for j in range(1,6):
        print("*",end=" ")
    print()    



#for invertted peramid
for i in range(6,0,-1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()



 

#normal and iveverted peramid print at same time
for i in range(1,6):
    for j in range(1,i+1):
        print("*",end=" ")
    print()
for i in range(6,0,-1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()
 

 

num=int(input("enter number:"))
for i in range(1,num):
    for j in range(1,i+1):
        print(j,end=" ")
    print()

#normal and iveverted peramid print at same time
for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
for i in range(6,0,-1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()    
 
 
 
#triangle pyramid

 
num=int(input("enter number:"))
k=2*num-2
for i in range(0,num):
    for j in range(0,k):
        print(end=" ")
    k=k-1
    for j in range(0,i+1):
        print("*",end=" ")
    print(" ")
'''
#triangle inverted pyramid

 
num=int(input("enter number:"))
k=2*num-2
for i in range(0,num):
    for j in range(0,k):
        print(end=" ")
    k=k-1
    for j in range(0,i+1):
        print("*",end=" ")
    print(" ")    
