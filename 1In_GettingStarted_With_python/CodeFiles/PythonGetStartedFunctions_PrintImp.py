

'''
##############################
1. create a funciton
##############################


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

#################################
#Output: 
hello aged professional
################################
'''

'''
##############################
#2. Overloading
##############################


"""
Overloading a function
-default arguments
    -positional notation assigment    
        the argument assignment from left to right
    
"""
#2.a
def fun1(a,b,c):
    
    print(a,b,c)
    
fun1(40,50,60)
#none is printed, because nothing is returned
print(fun1(10,20,30))


#################################
#Output
40 50 60
10 20 30
None
#################################

'''

'''
#2.a Default Values - Does not work 

def fun1(a,b,c):
    
    print(a,b,c)
    
fun1(40,50)


#################################
#Output

#fun1() missing 1 required positional argument: 'c'
#################################

'''

'''
#2.b. Default Values 


def fun2(a,b,c=10):
    
    print(a,b,c)
    
fun2(40,50,1)

#################################
#Output
40 50 1
#################################
'''

'''
#2.c - Default values without sending anyparameters

def fun3(a,b,c=10):
    
    print(a,b,c)
    
fun3(40,50)

#################################
#Output
40 50 10
#################################

##############################
#3. UNLIMITED ARGUMENTS
##############################


#When you want to send unlimited number of arguments
use *args for passing unlimited arguments. instea of args you can use any varibale, *var
the value are passed as a tuple


#*args takes data as tuples or values, any number of values

def fun4(*args):
    print(type(args),args)    

fun4(10,'Python',30,40)

#################################
#Output
<class 'tuple'> (10, 'Python', 30, 40)
#################################

'''


'''
##############################
#4. UNLIMITED ARGUMENTS - Key value pairs
#**args takes data as key-value pairs, any number of key-values pairs, data type is dicionary

##############################

def fun5(**keyaw):
    print(type(keyaw),keyaw)    

fun5(a=10,b='Python',age=50)


#################################
#Output
<class 'dict'> {'a': 10, 'b': 'Python', 'age': 50}
#################################
'''

'''
##############################
#5. UNLIMITED ARGUMENTS - of several formats - single, tuple and Key value pairs
#...single paramters, *args, **args 

##############################

def fun6(a,b,c=10,*args,**keyaw):
    print(a,b,c)
    print(type(args),args)
    print(type(keyaw),keyaw)    

fun6(10,20,30,40,50,60,name='arun',age=35,business='soft')


#################################
#Output
10 20 30
<class 'tuple'> (40, 50, 60)
<class 'dict'> {'name': 'arun', 'age': 35, 'business': 'soft'}
#################################
'''

##############################
#6. #there are several built-in functions
#To Write Examples
#https://www.programiz.com/python-programming/methods/built-in/all
##############################


##############################
#6.1. Abs
##############################

# random integer
integer = -20
print('Absolute value of -20 is:', abs(integer))

#random floating number
floating = -30.33
print('Absolute value of -30.33 is:', abs(floating))



##############################
#6.2. Bin
##############################


number = 5
print('The binary equivalent of 5 is:', bin(number))

#########INTELLIPAAT#####################
#7. By Val/ByRe
#To Write Examples
#The By Val and By Ref become complicated when we try to use Mutable and Immutable objects
##############################

#7.a-Intelli- calling a funciton by Value.
#The value of a is NOT because we are using a immutable data type - integer 
'''
a=10
def ChangeIt(b):
    print('value of b is',b)
    print('value of a is',a)
    b=100
    print('value of b is',b)
    print('value of a is',a)

ChangeIt(a)

#Output
#value of b is 10
#value of a is 10
#value of b is 100
#value of a is 10


#7.b-Intelli- calling a funciton by Ref.
#The value is of c is changed because we are using a mutable data type - LIST 
c=[10,20,30]

def NoChangeThem(d):
	print('value of d is',d)
	d[0]=99
	d[1]=98
	print('value of d is',d)

NoChangeThem(c)
#value of c is changed
print('value of c is',c)

'''
#########ARUN#####################
#7. By Val/ByRe
#To Write Examples
#https://medium.com/@tyastropheus/tricky-python-ii-parameter-passing-for-mutable-immutable-objects-10e968cbda35
#The By Val and By Ref become complicated when we try to use Mutable and Immutable objects
##############################
'''
#7.a)Immutable-ByVal-Value is not changed 
##(ByValue)Passing Immutable Objects like Integer- value is not changed
def increment(n):
    n += 1
    #though we are increment n+1 there is no change in the data
a = 3
increment(a)
print(a)
#Output
#a = 3   # a is still referring to the same object
'''

#7.b)Immutable-ByRef-Value is changed by using the return value
#Passing Immutable Objects- value is changed by using the return value

#Does that mean we will never be able to manipulate immutable objects by passing it to functions? 
#Turns out, we can still “modify” immutable objects by capturing the return of the function.

'''
def increment(n):
    n += 1
    return n

a = 3
a = increment(a)  # the return value of increment() is captured!
print(a)
#Output#a = 4   # a now refers to the new object created by the function
'''
'''
#7.c) Mutable-ByRef-Value is changed. we passing a mutable object: The value is changed by using append-
#Passing Mutable Objects
def increment(n):
   #n.append([4])
   n.append(4)

L = [1, 2, 3]
increment(L)
print('L:',L)
#Output#L = [1, 2, 3, 4]   # a changed!
'''

#7.d)Mutable-ByValue-Value is NOT changed. we passing a mutable object: The value is not changed by using =
#Passing Mutable Objects
#
'''
def assign_value(n, v):
   n = v

L1 = [1, 2, 3]
L2 = [4, 5, 6]
assign_value(L1, L2)
print('L1:',L1)
print('L2:',L2)



#Output 
#L1: [1, 2, 3]
#L2: [4, 5, 6]


########################################################

#8 - Example 1 lambada function
########################################################
#example 1 lambada arguments: expression

x= lambda a : a+10
print(x(5))

#Output:15
#############
#example 2.a Orginal Function without lambda
#############
#Orginal Function without lambda

def func1(a):
    return a +10 if a >10 else a*20

print(func1(10))
#Orginal Function With lambda
func = lambda a: a *10  if a >10 else a*20
print (func(10))

#Output
#200
#200

#############
#example 3 Using Lambda in another funciton
#############
def myfunc(n):
        return lambda a: a+n
 
mysum=myfunc(3)
print(mysum(10))
####
#Output

#13


#################################

#Example 4 lambada arguments: expression
#################################

def squareit(x=10,y=13):
    return x*y

print(squareit(13))

squareit2 = lambda x,y: x*y

print (squareit2(10,20))

#################################

#Example 5 lambada arguments: expression
#################################

li = [10,20,30,40]
print (list(map(lambda x:x*5,li)))


x = (3,4,5)
print (x)


###Output
169
200
[50, 100, 150, 200]
(3, 4, 5)
'''

'''
########################################################

#9 - Python File Handling - SLIDE 62
########################################################
#Example - open 2 parameters, file and mode
f = open("demofile.txt", "r")
#f = open("Cars.csv", "r")
print(f.read())


#Slide 64 Example2 - returns first 2 characters
f = open("demofile.txt", "r")
#f = open("Cars.csv", "r")
print(f.read(2))


#Slide 64 Example3 - used to return one line
f = open("demofile.txt", "r")
#f = open("Cars.csv", "r")
print(f.readline())


#Slide 64 Example4 - used to return one line

f = open("demofile.txt", "r")
#f = open("Cars.csv", "r")
print(f.readline()) 
print(f.readline()) # using readline() twice prints first two line

#Slide 65 Example5 - 

#Loop through the file
#Read the file line by line
f = open("demofile.txt", "r")
#f = open("Cars.csv", "r")
for x in f:
  print(x)
  
#Slide 66 Example5 - 
  
#Example: Append
f = open("demofile.txt", "a")
f.write("Now the file has one more line!")  
'''
'''
#Example: Overwrite
f = open("demofileOverwrite.txt", "w")
f.write("Woops! I have deleted the content2!")

# Deleting the file
import os
os.remove("myfile1.txt")

# Create a new file. If file exists it will give an error
f = open("myfile1.txt", "x")
'''