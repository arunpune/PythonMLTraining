'''
passs by reference

pass by value
'''

'''
pass by value, if a change is made to a variable, the change is only in the scope of the function. 
the change is not outside the function. 
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
    


