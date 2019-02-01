#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  4 11:01:49 2019

@author: Luvpreet kaur
"""
##Importing Libraries
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score


## Fetching Training and Testing Data
train = fetch_20newsgroups(subset='train', shuffle=True)
test = fetch_20newsgroups(subset='test',shuffle=True)

##Exploring training data
print(train.target_names) #prints all the categories
print("\n".join(train.data[0].split("\n")[:3])) #prints first line of the first data file


###pipeline inclues
#1. CountVectorizer
#2. TfiDfTransformer
#3. Model

from sklearn.pipeline import Pipeline
text_classification = Pipeline([('CountVector',CountVectorizer()),('Tfidf',TfidfTransformer()),('model',MultinomialNB())])

##Implementing Model
model = text_classification.fit(train.data,train.target)


##Predicting values
y_pred = text_classification.predict(test.data)

##Measuring accuracy of model
print(accuracy_score(test.target, y_pred))




