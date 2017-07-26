
# coding: utf-8

# In[1]:

import pandas as pd


# In[2]:

def method_2():
    data = {'state' : ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'],
         'year' : [2000, 2001, 2002, 2001, 2002],
         'pop' : [1.5, 1.7, 3.6, 2.4, 2.9]
        }
    df = pd.DataFrame(data)
    return df


# In[3]:

if __name__ == '__main__':
    df = method_2()
    print(df)


# In[ ]:



