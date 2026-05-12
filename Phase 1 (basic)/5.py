# program to calcuale avrage of students 
students_list = [ ("ali",95),("sara",23),("ahmad",100),("fatimah",34),("samiya",98)]
total = 0
for u in students_list:
    total += u[1]  # u[k]  this will not work  cause htne ti becomes first iteration is 
    # u bcoems ali and k becomes 95 now ali[95] in python we we do this it will try to
    # give us the 95 element in ali which dont exist so index error 

result = total/len(students_list) # result is 70
for k in students_list :
    if k[1]<result:
        print(k[0], " is below average ")
    else:
        print(k[0]," is above average ")
"""in this program we used list of tuples in python tuples are unmutable meaning 
after making they cant be changed anymore i menat like edited butnot opration applciable like
apend etc etc  """

"""in tuple if tuple is simple like (2,3,4,5) its indexing wil star form 0 moving up like 3
now in tuples like this ((2,3),(4,5)) now indexing changes it becoems this instead
[0][0] = (2) [0][1] = 3 smae forward for the next oenbceoms [1][0]= 4 ,[1][1] = 6"""

"""in python when we write for i in a or naything okay a is bcoems somehting called
an iterator it knows how to gives the next element wihotu any ++ so each time it
will give only one elemet but no need for ++ ++ dont exist in python """

"""an din tuples case one importnt thgin if we have simple (1,2,3,4,5) for i in tuple 
i wil get like 1,2,3,4,5 directlybut inc ase of tuple int tuples """