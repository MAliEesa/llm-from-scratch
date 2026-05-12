dict1 = {"h":0,"e":1,"l":2,"o":3,"w":4,"r":5,"d":6," ":7}
dict2 = {0:"h",1:"e",2:"l",3:"o",4:"w",5:"r",6:"d",7:" "}

"encode function"
def encode (x):
    result = []
    for i in x:
            n = dict1[i]
            result.append(n)
    return result

"decode function"
def decode (x):
    result = []
    for i in x:
         z = dict2[i]
         result.append(z)

    return ''.join(result)

token = input()
encode = encode(token)
decode = decode(encode)
print(encode)
print(decode)