# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 09:06:16 2019
Making a Built in Function
@author: HP
"""

"""
create a funciton
"""
"""
def classify_on_age(age):
    classification =''
    if age < 13:
        classification ='hello kid'
    elif age >= 13 and age < 20:
        classification ='hello teenager'
    elif age >= 20 and age <= 25:
        classification= 'hello young adult'
    else:
        classification='hello aged professional'
    
    return classification


output = classify_on_age(30)
print (output)
"""

"""
Overloading a function
-default arguments
    -positional notation assigment    
        the argument assignment from left to right
    
"""
"""
def fun1(a,b,c):
    
    print(a,b,c)
    
fun1(40,50,60)
#none is printed, because nothing is returned
print(fun1(10,20,30))
"""

"""
Default values
"""
"""
def fun1(a,b,c):
    
    print(a,b,c)
    
fun1(40,50)
#none is printed, because nothing is returned
print(fun1(10,20))


def fun2(a,b,c=10):
    
    print(a,b,c)
    
fun2(40,50,1)

#another way to send arguments 
def fun3(a,b,c=10):
    
    print(a,b,c)
    
fun2(a=40,b=50,c=2)
"""
"""
#When you want to send unlimited number of arguments
use *args for passing unlimited arguments. instea of args you can use any varibale, *var
the value are passed as a tuple


#*args takes data as tuples or values, any number of values
def fun4(*args):
    print(type(args),args)    

fun4(10,'Python',30,40)
"""
#**args takes data as key-value pairs, any number of key-values pairs, data type is dicionary
"""
def fun5(**keyaw):
    print(type(keyaw),keyaw)    

fun5(a=10,b='Python',age=50)
"""

'''
#*args takes data as key-value pairs, any number of key-values pairs, data type is dicionary

def fun6(a,b,c=10,*args,**keyaw):
    print(a,b,c)
    print(type(args),args)
    print(type(keyaw),keyaw)    

fun6(10,20,30,40,50,60,name='arun',age=35,business='soft')

#there are several built-in functions
print(abs(10))
ascii(65)

import string
print(string.printable)
print(chr(65),ord('A'))

'''
'''
passs by reference

pass by value
'''

'''
pass by value, if a change is made to a variable, the change is only in the scope of the function. 
the change is not outside the function. 
'''

'''
#calling a function by passing the values
a=10
def surenchangeit(b):
    print('value of b',b)
    b=100
    print('New value of b',b)
    
surenchangeit(a)    
print('New value of a',a)
 
'''

#calling a function by passing by reference
c=[10,20,30]
#print('New value of c',c)
def changethem(d):
    print('value of d',d)
    d[0]=99
    d[1]=98
    print('New value of d',d)
print('New value of c',c)
changethem(c)    
print('New value of c',c)
'''


def add_by_val(l1,l2):
    l1=l2
    #here we are overwriting data in l1 with L2
    #which also means l1 and l2 point to same data location
    print('inside',l1)
    print('inside',l2)
    return l1

l1=[10,12]
l2=[30,40]
add_by_val(l1,l2)


the change is made inside the function.
pass by reference 


def add_by_ref(l1,l2):
    l1.append(25)
    print('inside',l1)
    print('inside',l2)
    return l1

l1=[10,12]
l2=[30,40]

add_by_ref(l1,l2)

print('outside',l1)
print('outside',l2)
'''
#add(10,12)
    
'''

#lambada function

"""def func(a):
    return a +10 if a >10 else a*20

func = lambda a: a *10  if a >10 else a*20
print (func(10))


a =10
print (a  if a >10 else a )


def squareit(x=10,y=13):
    return x*y

print(squareit(13))

squareit2 = lambda x,y: x*y

print (squareit2(10,20))
li = [10,20,30,40]
print (list(map(lambda x:x*5,li)))




x = (3,4,5)
print x

"""

#######File Handling     


#Example
f = open("demofile.txt", "r")
print(f.read())



#Reading parts of file
f = open("demofile.txt", "r")
print(f.read(5)) #Return the 5 first characters of the file


#Reading first line
f = open("demofile.txt", "r")
print(f.readline()) #readline() is used to return one line


#Reading first line
f = open("demofile.txt", "r")
print(f.readline()) 
print(f.readline()) # using readline() twice prints first two line


#Loop through the file
#Read the file line by line
f = open("demofile.txt", "r")
for x in f:
  print(x)
  

#Example: Append
f = open("demofile.txt", "a")
f.write("Append Now the file has one more line!")  
f = open("demofile.txt", "r")
print(f.read())




#Example: Overwrite
f = open("demofile.txt", "w")
f.write("Woops! I have deleted the content!")
'''
'''
f = open("demofile.txt", "r")
print(f.read())

'''