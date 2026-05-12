a = [1,2,3,4,5,6,7,8,9,10]
newsum=0
for i in a :
    newsum += i

avg = newsum/len(a)
print(avg)
"""same concept i is being not used here as indexbut rather as element of a directly 
so when we do newsum  = 0 andinside loop doing newsum += i newsum vlaue increaing 
directly element by elemtn first 1 then 1+2 = 3 and so on and len gives us full length
number of a string
"""