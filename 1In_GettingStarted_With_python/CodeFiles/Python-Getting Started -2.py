
# coding: utf-8

# # Python-Getting Started

# Assigning single value to a variable…

# In[1]:


a = 10
name = 'Victor'
salary = 2000.23
print (a)
print (name)
print (salary)


# Assigning multiple value to a variable…

# In[2]:


a=b=c=10
x,y,z=10,20,30
print(y)
print(a)


# String Literals

# In[3]:


name1="John"
name2='James'
print(name1)
print(name2)
text1='helloWorld'
text1
multiline='''st1
...st2
...st3'''


# Special Literals: None

# In[4]:


val1 = 10
val2 = None
val1,val2
print(val2)


# > # Operators

# Arithmetic Operator
# +, -, *, /, %

# In[5]:


1+2


# In[6]:


1-2


# In[7]:


2%1


# Assignment Operator =,+=, -=, *=

# In[8]:


a=10 
a*=10 #a=10*10
print(a)


# Comparison Operator <, >, <=, >=, !=

# In[9]:


a = 10
b = 20 
a > b


# Logical Operator: and, or , not 

# In[10]:


a=10<10 and 2>-1
print(a)


# Bitwise Operator &,|,>>,<<,~

# In[11]:


7 | 5
7 & 5


# Identity Operator is, is not

# In[12]:


x = 10
x is 10


# In[13]:


x = 10
x is not 10


# Membership Operator in, not in

# In[14]:


pets=['dog','cat','wolf']
'lion' in pets
'wolf' in pets
'me' in 'appointment'


# # Datatypes in Python

# > # Number 

# In[15]:


message = "Hello World"
num = 1234
pi = 13.6
print(type(message)) #return a string
print(type(num)) #return an integer
print(type(pi)) #return a float


# > # Strings

# In[16]:


var1 = 'Hello-World!'
var2 = 'PythonTutorial'

print(var1[0]) # prints the first character in the string `H`
print(var2[1:5]) # prints the substring 'ytho'


# find()

# In[17]:


#find() – Returns the position of the string
str='Attachment'
str.find('Me')


# replace()

# In[18]:


#replace() – Replaces one character/string with other
str='Replacement'
str.replace('ed','e')


# split()

# In[19]:


#split() – Creates a split on the basis of a character
str='word1,word2,word3'
str.split(',')


# > # Tuples

# In[20]:


myGroup = ('a', 'b', 'c', 'd')


# concatenation

# In[21]:


#Concatenation - Adds two string/character
myGroup += ('f',)
print(myGroup)


# repetation

# In[22]:


#Repetition -  Duplicate string/character by given number of times
myGroup * 2


# indexing

# In[23]:


#Indexing - Shows the indexed character/string
myGroup = ('a', 'b', 'c', 'd', 'f')
myGroup[2]


# slicing

# In[24]:


#Slicing – Shows a specific set of indexed character/string
myGroup = ('a', 'b', 'c', 'd', 'f')
myGroup[1:4]


# > # List

# In[25]:


myGroup = ('a', 10, 7.12, 'data')


# concatenation

# In[26]:


#Concatenation – Add elements to the list
myList = ['a', 1, 3.14, 'python']
myList+=['d',]
print(myList)


# repetation

# In[27]:


#Repetition
myList = ['a', 1, 3.14, 'python']
myList*2


# slicing

# In[28]:


#Slicing
myList = ['a', 1, 3.14, 'python']
myList = myList[1:3]
myList


# append

# In[29]:


#append(value)
myList = ['a', 1, 3.14, 'python']
myList.append('d')
myList


# extend

# In[30]:


#extend(list)
myList = ['a', 1, 3.14, 'python']
myList.extend (['c', 'd']) 
myList


# insert

# In[31]:


#insert(index, value)
myList = ['a', 1, 3.14, 'python']
myList.insert(2, 'd')
myList


# > # Dictionary

# Example

# In[32]:


myDict = { 1: 'John' , 2: 'Bob', 3: 'Alice' }


# Empty dictionary

# In[47]:


#empty dictionary 
myDict = {}


# Integer keys

# In[48]:


#dictionary with integer keys
myDict = {1: 'apple', 2: 'ball'}


# In[49]:


#dictionary with mixed keys
myDict = {'name': 'John', 1: [2, 4, 3]}


# mixed keys

# In[50]:


#dictionary with mixed keys
myDict = {'name': 'John', 1: [2, 4, 3]}


# In[51]:


#paring
#from sequence having each item as a pair
myDict = dict([(1,'apple'), (2,'ball')])


# In[62]:


#accessing dictionary
myDict = {1: 'word1', 2: 'word2'}
myDict[1]


# In[63]:


#len()
myDict = {1: 'word1', 2: 'word2'}
len(myDict)


# In[69]:


#key()
myDict = {1:'apple', 2:'ball'}
len(myDict)
myDict.keys()


# In[70]:


#values()
myDict = {1: 'apple', 2: 'ball'}
myDict.values()
['apple', 'ball']


# > # Sets

# # Example

# In[71]:


mySet = {1, 2, 3}


# In[72]:


#Creating set
mySet = {1, 2, 3, 3}
print (mySet)


# # File Handling

# # Open - Do not run

# In[76]:


#Syntax-not in Jupyther
f = open("path of file")


# In[77]:


#Example-not in Jupyther
f = open("path of file","rt")


# # Read

# In[78]:


#Example
#f = open("demofile.txt", "r")
f = open("Cars.csv", "r")
print(f.read())


# In[79]:


#Reading parts of file
#f = open("demofile.txt", "r")
f = open("Cars.csv", "r")
print(f.read(5)) #Return the 5 first characters of the file


# In[80]:


#Reading first line
#f = open("demofile.txt", "r")
f = open("Cars.csv", "r")
print(f.readline()) #readline() is used to return one line


# In[81]:


#Reading first line
#f = open("demofile.txt", "r")
f = open("Cars.csv", "r")
print(f.readline()) 
print(f.readline()) # using readline() twice prints first two line


# In[82]:


#Loop through the file
#Read the file line by line
#f = open("demofile.txt", "r")
f = open("Cars.csv", "r")
for x in f:
  print(x)


# # Write/Create

# In[83]:


#Example: Append
f = open("demofile.txt", "a")
f.write("Now the file has one more line!")


# In[84]:


#Example: Overwrite
f = open("demofile.txt", "w")
f.write("Woops! I have deleted the content!")


# In[85]:


# Create a new file
f = open("myfile.txt", "x")


# # Delete

# In[86]:


# Deleting the file
import os
os.remove("demofile.txt")

