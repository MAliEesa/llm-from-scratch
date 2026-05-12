"""lets play with loops """
x = (
    (
        (2,3),(4,5),(6,7),(8,9),
        (10,11),(12,13),(14,15),(16,17)
    )
)
for i in x :
    print(i)
    print(i[0])
    print(i[1])

"""here everything is correct working cuase in brckets in putted
the inner so in the end outerbrackets menas one so i inert only 
(a,b) at a time not the hwole """

# now the whole one lets try it yay 
x = (
    ((1,2),(3,4)),
    ((5,6),(7,8))
)
for i in x :
    print(i)
    print(i[0])
    print(i[1])

"""but we still cant use the inner tuples wy for that we need
two loops one for outer one for inner """
x = (
    ((1,2),(3,4)),
    ((5,6),(7,8))
)
for i in x:
    print(i)
    for j in i :
        print(j)
        print("start")
        print(j,end = " ")
    print()

"""now lets test python to stop gong on the new line """
print("new try")

x = (
    ((1,2),(3,4)),
    ((5,6),(7,8))
)
for i in x :
    for j in i :
        print(j,end=" ")
    print()

"""but if we dont want space between i then we dont need to write
the extra print its only purpose is to make the cursor goe
on ne wline if we dont do it thec ruso rmeian on smae line 
everything be printing on the same line """

print("wihtout space in i ")
x = (
    ((1,2),(3,4)),
    ((5,6),(7,8))
)
for i in x :
    for j in i :
        print(j,end=" ")

print("the end")

"""now experimenting wiht triple outer tuples tuples"""
x = (
    (
        ((1,2),(3,4)),
        ((5,6),(7,8))
    ),
    (
        ((2,2),(3,4)),
        ((5,6),(7,8))
    )
)
for i in x :
    print(i,end = " ")
    print()
# should print the whole thing 
for i in x :
    for j in i :
        print(j,end=" ")
        print()
#should only print the inside of each but it will look like i 
for i in x :
    for j in i :
        for k in j :
            print(k,end=" ")
            print()