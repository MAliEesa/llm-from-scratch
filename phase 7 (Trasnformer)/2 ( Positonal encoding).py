import torch as t
import torch.nn as nn

"""word_embedding means that its the embedded table of the tokens 
we did this inthe last program here ofr testing we are making new but 
for understanign if we have 3 tokens [1,56,23] 1 = king , 55 = is 23 = strong
now on the basis of this we maded th embedding that was this for exmaple 
nn.Embedding(vocab_size, columns of our choce )
nn.Embedding(5,6) rule is vocab size must be greator then the tokens itself
if tokens are 4 use 5 vocab size else error but here we are doing mnaually 
it making a random vector matrix so we cna make the fake_Word_Embedding using 
randn , it dont requres any vocab size just rows andf colums so it can make 
vector of size 2 to -2 according to the rows and columns so below line makes
the fake token embeding table we need for positnonal encoding """
fake_Word_Embedding = t.randn(4,6)

"""now we had written t.arange(4) as for positional encoding we need positionas
to give to our word embedding table so t.arange(give end number,eg 3) 
it wil ocunt form zero to that number here as we have 3 so it counts 0,1,2 
the numebr itself not included and important thing if we want to use negative 
numbers we will do arange(-3,must be apostive number ) arange(-3,0) so now it
counts -3,-2,-1 another exmaple arange(-3,2) will count -3,-2,-1,0 ,1 but for 
our postional encoding a position can be on negative number like for exmaple
token 45 is king ok we make mbedding tbale of king
[0.9, 0.3, 0.8, 0.5, 0.7, 0.6] each means
[warrior,tall,strong,funny,gentle,male] now 
warrior cant be at position -4 that wont work so positons must go
[0,1,2,3,4,5] thats why we will alaways use postive positions  """
positions = t.arange(4)

"""now we are making apostinal embedding table as we have 4 postions so we must
put 4 else error why cuase positions starting from 0,1,2,3 so less the vocab
size will work """
postional_embedding_table = nn.Embedding(4,6)
pos_vectors = postional_embedding_table(positions)

"""now here we are givning positons to our tokens actually """
final_vector = fake_Word_Embedding + pos_vectors

print(fake_Word_Embedding)
print(pos_vectors)
print(final_vector)

"""The rule is simple:

Number of positions = number of tokens you have
Positional embedding columns = same as word embedding columns"""
