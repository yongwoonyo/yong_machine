
# coding: utf-8

# In[1]:

import tensorflow as tf
from utils import util_2


# In[2]:

df = util_2.method_2()
df


# In[3]:

def sum_pop_over_than(year):
    pop_list = df[df['year'] == year]['pop'].values.tolist()
    sum = 0.0
    for i in pop_list:
        sum += i
    return sum


# In[4]:

sum_pop_2002 = tf.constant(sum_pop_over_than(2002)) # 6.5
pop_basic = tf.constant(10.0)

sess = tf.Session()
print(sess.run(sum_pop_2002 + pop_basic)) # 6.5 + 10.0 = 16.5


# In[ ]:



