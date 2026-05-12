students = {"ali" : 95,"sara":78,"lal": 93,"gulo":90,"mario":96}
total = 0
for i,k in students.items() :
    total += k

result = total/len(students)
for i,k in students.items() :
    if k<result:
        print(i,"below average ")
    else:
        print(i,"above average")

"due to using .items i wlllaways be the key and k the nextvaribale in th eloop is the vlaue "