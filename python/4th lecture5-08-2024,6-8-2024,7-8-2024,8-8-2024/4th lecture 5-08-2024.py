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
    
'''

#write a python program to find  avrage  of list of number
#write a python program to find reverse number
#find largest number from given list
#find even number and find square of these even number
#find accurence of given number
#find out 



















