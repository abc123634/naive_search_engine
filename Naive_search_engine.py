
# coding: utf-8

# # Goal: find the most "similar" Q&A for an user query 

# In[228]:

import numpy as np
import pandas as pd
import sklearn
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
from sklearn.metrics.pairwise import cosine_similarity
import re
import time


# In[38]:

from bs4 import BeautifulSoup
get_ipython().magic('pinfo BeautifulSoup')


# In[78]:

soup = BeautifulSoup(open("/Users/leemeng/Documents/Data/takakuureru/all.html"), 'html.parser')
soup


# In[88]:

questions = soup.findAll('dt')
answers = soup.findAll('dd')
len(questions)


# In[122]:

doc_list = list()
for q, a in zip(questions, answers):
    str1 = str(q) + str(a)
    d = re.sub(r'[<>dt/a-z]','',str1)
    d = re.sub('\n', '', d)
    documents[idx] = d
    doc_list.append(d)
df = pd.DataFrame(doc_list, columns=["content"])
df.head(3)


# In[124]:

start = time.time()


# In[229]:

tf = TfidfVectorizer(analyzer='char', ngram_range=(1,3), max_df=0.7, use_idf=True)
tfidf_matrix = tf.fit_transform(df['content'])
tfidf_matrix.shape


# In[299]:

query = ["支払いについて知りたい"]
tfidf_query = tf.transform(query)
tfidf_query.shape


# In[300]:

cosine_similar = linear_kernel(tfidf_query, tfidf_matrix)
cosine_similar.shape


# In[301]:

doc_indices = cosine_similar[0].argsort()[:-6:-1]
doc_indices


# In[302]:

df.iloc[doc_indices,]


# In[125]:

print("Trained: %s seconds" %(time.time() - start))


# In[ ]:




# In[ ]:



