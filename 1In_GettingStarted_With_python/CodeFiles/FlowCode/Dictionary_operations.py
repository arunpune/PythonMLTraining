##Dictionary Operations

ab = { 'Swaroop' : 'swaroop@swaroopch.com',
    'Anup' : 'Anup@wall.org',
    'Pranay' : 'Pranay@ruby-lang.org',
    'Vishal' : 'Vishal@hotmail.com'
}

print (ab)
print(type(ab))

print ("Swaroop's address is", ab['Swaroop'])

# Deleting a key-value pair
del ab['Vishal']

print ('\nThere are {} contacts in the address-book\n'.format(len(ab)))

print (ab.items())
       
for name, address in ab.items():
    print ('Contact {} at {}'.format(name, address))

# Adding a key-value pair
ab['Chinmay'] = 'Chinmay@python.org'
print (ab)
       
if 'Chinmay' in ab:
    print ("\nChinmay's address is", ab['Chinmay'])

Addr_details = { 'Swaroop' : ['swaroop@swaroopch.com',9090909009],
    'Anup' : ['Anup@wall.org',9090999909]}

print (Addr_details.items())
print ("Swaroop's Mobile is", (Addr_details['Swaroop'])[1])
