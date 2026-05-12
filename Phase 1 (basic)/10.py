"""now we are gone learn how to use all typles of list typles dictonaries in one 
another """

# list in lists 
x = [[1,2],[3,4]]
for i in x  :
    print(i)
print()

# list in tuples 
x = [(2,3),4,5]
for i in x :
    print(i)
print()

# list in dictonary 
x = {
    "Ali" : [95,65,45,76],
    "sara" : [23,54,65,43]
}

print(x.items()) # it wil give the whole dict with tuples

for i,k in x.items() :
    print(i,k)

x = {
    "Al" : [95,65,45,76],
    "sa" : [23,54,65,43]
}

for i,k in x :
    print(i,k) 
print()

"""its gone give erroe if th ekey has more the two characters each char of the dict is storing
into each variablabut if they has ezactly too it cna work  """
    
"""ok in dict list will not work if used in keys cuase keys should
be mutable """

# tuple in tuples
x = ((1,2),(3,4))
for i in x :
    print(x)
print()

# list in tuples
x = ([1,2,3,4,5])
for i in x :
    print(i)
print()

# tuple in dict
x = {
    "Ali" : (2,3,4,5),
    (2,3) : "sara"
} 
for i,k in x.items(): #items lets us get both value and kes fomr dict
    print(i,k)
print() # as tuples are unmutbale so ut can be used in both 

# dict in dict
x = {
    34:{"x":2},
    56 : {"y":3}
}
for i,k in x.items(): 
    print(i,k)
"""cant use one dict as akey innaothe rit wil throe erroe as that
is mutbale while key cant be mutbale """