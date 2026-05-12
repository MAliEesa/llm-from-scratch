import torch as t
import torch.nn as nn
matrix_1 = t.randn(20,16) # randn makes a matrxi that will be the size (row,column) and it will stor it in floating points between 2 to -2 we do this to intialzie for the vectors
matrix_2 = t.randn(6,8)
token_id = t.tensor([4,5]) # tensor store thing in torch making so torch can trakc it using grad
vector_1 = [matrix_1[4],matrix_1[5]]
vector_2 = [matrix_2[4]]
print(vector_1)
print(vector_2)

"now for automatic system using nn.Embedding"
print("start")
matrix_3 = nn.Embedding(6,6)
vector_3 = matrix_3(token_id) #it wil be automaticlaly filled due to tensoir tracking it also her we are using a class now a fucntion 
print(vector_3) # your vocab size shoudl be bigger then the whole tokens our biggest was five right but embedding vocab size is 4 so error 
