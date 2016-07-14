# This Python file uses the following encoding: utf-8
from __future__ import print_function
import os
import ctypes

for d, _, files in os.walk('lib'):
    for f in files:
        if f.endswith('.a'):
            continue
        ctypes.cdll.LoadLibrary(os.path.join(d, f))

import boto3
import json
import numpy as np
import sklearn
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
from sklearn.metrics.pairwise import cosine_similarity
import re
import time

def lambda_handler(event, context):
    # do sklearn stuff here

	content = "<dt>question1</dt> <dd>answer1</dd><dt>question2</dt> <dd>answer2</dd>"

	questions = re.findall('<dt.*?>(.*?)</dt>', content)
	answers = re.findall('<dd.*?>(.*?)</dd>', content)

	doc_list = list()
	for q, a in zip(questions, answers):
	    str1 = str(q) + str(a)
	    d = re.sub(r'[<>dt/]','',str1)
	    d = re.sub('\n', '', d)
	    doc_list.append(d)
	
	start = time.time()


	tf = TfidfVectorizer(analyzer='char', ngram_range=(1,3), max_df=0.7, use_idf=True)
	tfidf_matrix = tf.fit_transform(doc_list)
	print(tfidf_matrix.shape)


	query = ["question1"]
	tfidf_query = tf.transform(query)
	print(tfidf_query.shape)

	cosine_similar = linear_kernel(tfidf_query, tfidf_matrix)
	print(cosine_similar.shape)

	doc_indices = cosine_similar[0].argsort()[:-6:-1]
	print(doc_indices)

	print("Trained: %s seconds" %(time.time() - start))

	return {"result": "We made it!"}


