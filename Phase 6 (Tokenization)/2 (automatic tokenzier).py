dict1 = {}
dict2 = {}

"encode function"
def encode(x):
    r = []
    for i in x:
        n = dict1[i]
        r.append(n)
    return r

"decode fucntion"
def decode (x):
    r = []
    for i in x:
        n = dict2[i]
        r.append(n)
    return "".join(r)

token = input()
s = set(token)
s = sorted(s)
"in enumerate use i become tthe index and k becoms the key there is no key i acts as index numbers"
for i,k in enumerate(s) :
    dict1[k] = i
    dict2[i] = k
encode = encode(token)
decode = decode(encode)
print(encode)
print(decode)