import json as j
class tokenizer :
    def __init__ (self): 
        self.vocab = {}
        self.id_num = {}
        self.merge_rules = []
        self.vocab_size = 0

    "saving"
    def save(self, filename):
        data = {
            "vocab": self.vocab,
            "merge_rules": self.merge_rules,
            "id_num": self.id_num
        }
        with open(filename, "w") as f:
            j.dump(data, f)
    
    "loading"
    def load(self,filename):
        with open(filename,"r")as q:
            data = j.load(q)
        self.vocab = data["vocab"]
        self.id_num = data["id_num"]
        for i in data["merge_rules"]:
            self.merge_rules.append(tuple(i))

    "Traning function"
    def train(self,text,v):
        for i,k in enumerate(sorted(set(text))):
            self.vocab[k] = i
        self.vocab_size = v
        split = list(text)
        while len(self.vocab) < self.vocab_size:
            temp_dict = {}
            for i in range(len(split)-1):
                pair = (split[i],split[i+1])
                if pair in temp_dict :
                    temp_dict[pair] += 1
                else :
                    temp_dict[pair] = 1
            if not temp_dict:
                break
            fre_pair = max(temp_dict,key=temp_dict.get)
            self.merge_rules.append(fre_pair)
            new_token = fre_pair[0]+fre_pair[1]
            self.vocab[new_token] = len(self.vocab)
            new_split = []
            k = 0
            while k < len(split):
                if k < len(split)-1 and split[k] == fre_pair[0] and split[k+1] == fre_pair[1]:
                    new_split.append(split[k]+split[k+1])
                    k +=2
                else :
                    new_split.append(split[k])
                    k +=1
            split = new_split
        for a,b in self.vocab.items():
            self.id_num[b] = a
    
    "ecnode function"
    def encode (self,text):
        split_encode = list(text)
        for i in self.merge_rules:
            k = 0
            new_split = []
            while k < len(split_encode):
                if k < len(split_encode)-1 and split_encode[k] == i[0] and split_encode[k+1] == i[1]:
                    new_split.append(split_encode[k]+split_encode[k+1])
                    k+=2
                else:
                    new_split.append(split_encode[k])
                    k+=1
            split_encode = new_split
        r = []
        for i in split_encode:
            r.append(self.vocab[i])
        return r 
    
    "decode function"
    def decode (self,text):
        r = []
        for i in text:
            n = self.id_num[i]
            r.append(n)
        return "".join(r) 

"Initlaizing and passing"
inp_trai = input("write input for traning data")
inp_enco = input("write input for encode")
token = tokenizer()
token.train(inp_trai,60)
print(token.merge_rules)
encoded = token.encode(inp_enco)
decoded = token.decode(encoded)
print(encoded)
print(decoded)