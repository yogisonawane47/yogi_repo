'''
List:

List is collection of diffrent type of data 

characteristics of list:
1.ordered :
    List are in order
2.changable:
    lists are muteable
3.lists elements are accessed by index value
4.Hetetrogeneous:
    diffrent type of data included in lists
5.duplicate element:
    Lists allow duplicate element
 

#how  to create list?
#empty lists

lists=[]
print(type(lists))


lists1=[]
print(type(lists1))


lists=[1,2,3,4,5]
print(lists)
print(type(lists))


lists=[1,"priya",3,14,True]
print(lists)
print(type(lists))



lists=["mobile","laptop","mouse","laptop bag"]
print(lists)

#indexing list:
#slice operator is used []

print(lists[0])
print(lists[1])
print(lists[2])
print(lists[3])
print(lists[-2])


#accessing element of lists:
print(lists[0:2])
print(type(lists[0:2]))


 
#ittrating list:

lists=["pyton programing","SQL","core web design","Django",88,98]
for i in lists:
    print(i)

 

lists=["pyton programing","SQL","core web design","Django",88,98]
#itterating with index:
for i in range(len(lists)):
    print(lists[i])
 

#Adding element into lists:
#1.insert
#2.append
#3.extend
 
#1.insert: this use for value insert a specific/specifide position
    
list1=["red","green","yellow","white","blue","black"]
list1.insert(2,"voilet")
print(list1)

#2.append: this use for value insert a  last postion

list1=["red","green","yellow","white","blue","black"]
list1.append("megenta")
print(list1)

#3.entend:new line attached in already created line

list1=["red","green","yellow","white","blue","black"]
list1.extend(["megenta","pink","coco"])
print(list1)

 

#modify the list:this using you can replace the value that mean modify.

lists=["pyton programing","SQL","core web design","Django",88,98]

lists[1]=20
print(lists)

#this using you can replace/modify multiple value.
lists=["pyton programing","SQL","core web design","Django",88,98]

lists[2:4]=200,300
print(lists)
 
Removing an element from list:
1.remove()      remove the firts occurence of an element # value
2.pop(index)    remove and return the iteam at given index 
3.clear()
4.del
 
lists=["pyton programing","SQL","core web design","Django",88,98]
lists.remove(88)
print(lists)



print(lists.pop(3))   #they show deleted value

lists.clear()   #they delete only values AND show empty list
print(lists)

del lists           #they completly delted with content


 
#concatenating list:
#+
#extened()

list1=[1,2,3,4]     # they attached both difftent list
list2=[2,4,6,8]
 
print(list1+list2)

 
#extend()

list1.extend(list2)
print(list1)

  


#copying list:
#=

list1=[1,2,3,4]
list2=list1
print(list2)


list1.append(5)
print(list1)
print(list2)
 
#copy()
list3=[1,2,3,4]
list4=list3.copy()
print(list4)

 
list3.append(45)
print(list3)    #[1, 2, 3, 4, 45]
print(list4)    #[1, 2, 3, 4]
 
 

list1=["madhav","core web design","kartik","django","madhu"]
list1.sort()
print(list1)


list1=["madhav","core web design","kartik","django","madhu"]
list1.reverse()
print(list1)



#built in function:
1.max()
2.min()
3.sum()
 

list1=[1,2,3,4,5,6,7]
print(max(list1))
print(min(list1))
print(sum(list1))



#count() cheack occurence of specied element
print(list1.count(78))


#index() returen index value of specified element
list1=[66,78,46,78]
print(list1.index(46))




#list comprehecsions:
#this is complex method to create a list using an existing list

syntax:
    output_list={expreation(variable) for variable in inputlist
                 [if variable condition] [if variable condition2]

 
 
#print first 5 number
num=int(input("enter number:"))
newlist=[i for i in range(num)]
print(newlist)


 

list1=[1,2,3,4]
for i in list:
    print(i**2)

new_list=[i**2 for i in list1]
print(new_list)
 

list1=[1,2,3,4,5,6,7,8,9]
new_list=[]
for i in list1:
    print(i)
    if i%2==0:
        new_list.append(i**2)
print(new_list)


#or

new_list=[i**2 for i in list1 if i%2==0]
print(new_list)

 
#multidimention list
#list within list/index cha index

list1=[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
print(list1[1][2])
 

list1=[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
list1[0].extend([20,30,40])
print(list1)

list1.insert(3,[20,30,40])
print(list1)


#tuple
#tuples are orded collection of heterogeneus date that are unchangeable
#define tuple:

tuple1=()
print(type(tuple1))
print(type(tuple1))


tup=tuple()
print(type(tup))

tuple1=(1,2,"kaustub",True)
print(tuple1)
print(type(tuple1))

tuple1=(1 )  #they only print int
print(tuple1)
print(type(tuple1))


tuple1=("madhav")
print(type(tuple1))


tuple1=("python","SQL","core web ","Django","SQL")
print(tuple1.count("SQL"))

print(tuple1,index("SQL"))




#Diffrence between list and tuple
List                                           Tuple
1.List is mutable                          1.tuple is immutable
2.List element is enclosed within []       2.elements enclosed within () parenthsis
3.list are slower than tuple               3.Tuple are faster than list
4.list consume more memory                 4.consume less memory as compared to list
5.element can be modified after            5.can't change elements
    the assigment

 


#set
set is an unorder collection of data iteam that are unique
set is defined with{}

 


set1={1,2,3,4,5}
print(set1)
print(type(set1))
 

set1=set() 
print(type(set1))

 

set1={1,2,3,4,5}
set1.add("kashi")
print(set1)

set1.update(["kaju"])
print(set1)

#1.what is PEP?
#2.what is PEP-8?

#(Python Enhasment Proposel)
#    it provide convention for righting clean,
#    readable and cosistant python code
#3.what is diffrent way to adding list?
#4.how python emplement dynamic typing?
#--> python implements dynamic typing by aloing vairiable to
#   refrance object without explicite the type of variable
#   at run type. 


'''


#tuple packing
tuple1=10,20
















