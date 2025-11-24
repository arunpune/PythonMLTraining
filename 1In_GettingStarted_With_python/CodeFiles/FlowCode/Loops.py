##IF statments
a = 4
if a == 5:
    print("True")
print("True123")

##IF else
a = 0
if a == 0:
    print("True")
else:
    print("False")
print ("Who am I")

##If Else If

var = 45
if (var < 200 and var > 50):
   print ("Expression value is less than 200")
   if var == 150:
      print ("Which is 150")
   elif var == 100:
      print ("Which is 100")
   elif var == 50:
      print ("Which is 50")
elif var < 50:


###For loop
n = 10
for i in range(1,n,1):
    print(i)
print('DDD') 

##WHile Loop
n = 5
i = 1
while(i <= n):
    if (i==3):
        print(i)
    i = i + 1

   print ("Expression value is less than 50")
else:
   print ("Could not find true expression")

print ("Good bye!")

###Break
for letter in 'Python':     # First Example
   if letter == 'h':
      break
   print ('Current Letter :', letter)
print ('Out of For')


##Continue

for letter in 'Django':     # First Example
      if letter == 'D':
          continue
      print ('Current Letter:', letter)
