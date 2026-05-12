import json
my_data = {"h":1 , "b":2 , "c":3 , "w":4 , "m":5}

# for saving
with open("myfile.json","w")as f:
    json.dump(my_data,f)
    # if we dont use with we need to anualy close it then by using close()

# for loading
with open("myfile.json","r")as new_my:
    n_data = json.load(new_my)
    # due ot with we dont need to close it 

print(my_data)

"exmaple wihout with"
x = (1,2,3,4,5) 

# now save function 
f = open("mydata.json","w")
json.dump(x,f)
f.close()

#now loading 
f = open("mydata.json","r")
x = json.load(f)
f.close()

print(x)