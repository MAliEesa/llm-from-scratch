import torch as t 
import torch.nn as nn 

tokens = t.tensor([1,2])

""""making word embedding table"""
word_embedding_table = nn.Embedding(3,4)
shape = word_embedding_table(tokens) # extracing the tokken shape from it
print(shape)

"""making positonal encoding table for this"""
positions = t.arange(2) # based on how many tokens we have 
positional_embedding_table = nn.Embedding(2,4)
pos_vector = positional_embedding_table(positions)
"""columns size of positonal encoding must match of that of word embedding
table """
final_vector = shape + pos_vector
print(final_vector)
