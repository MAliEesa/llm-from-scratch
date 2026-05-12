"""so bascilay we are gona do attention mechanaisim meaning how each word relates 
to another actually so thats our main purpose to do here """
import torch as t 
import torch.nn as nn
m_1 = t.randn(2,4)
w_q = t.randn(4,5)
w_k = t.randn(4,5)
w_v = t.randn(4,5)
"""now gona do the q k v thing here we are gona multply and store then move to
next"""
q = m_1 @ w_q # @ for dot product and amtrix multipication 
k = m_1 @ w_k
v = m_1 @ w_v

print(q,"\n",q.shape,"\n",k,"\n",k.shape,"\n",v,"\n",v.shape)

"""now to get scores of q k v we are gona mutpley eahc wiht each other we will 
do seocnd thing transpose so that first one columns must matach second oine rows
"""

scores = q @ k.T 
print(scores,"\n",scores.shape)

"""so we made our score but its not readeable so we are gona use softmax to put
it in percentage like readable"""

att_score = t.softmax(scores,dim=1)
print(att_score)

att_sc2 = att_score @ v 
print(att_sc2)