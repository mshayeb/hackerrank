import numpy as np
import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import linear_model
from sklearn import preprocessing
import re


#https://www.hackerrank.com/challenges/document-classification

def main():
    input_data, test_data = load_data()
    #print "test data : ", test_data
    input_features, input_classes , test_features = preprocess(input_data, test_data)
    clf = build_model(input_features, input_classes)
    predict(clf, test_features)
    
def predict(clf, test_features):
    pred = clf.predict(test_features)
    for p in pred:
        print p
    
                
def preprocess(input_data, test_data):
    data = list()
    classes = list()
    
    for d in input_data:
        data.append(d[1])
        classes.append(int(d[0]))
        
    vectorizer = TfidfVectorizer(sublinear_tf=True,ngram_range=(1,1), analyzer='word', stop_words='english')
    
    input_features = vectorizer.fit_transform(data)
    input_classes = np.array(classes)
    
    test_features = vectorizer.transform(test_data)

    return (input_features, input_classes , test_features)

    
def build_model(input_features, input_classes):
    clf = linear_model.PassiveAggressiveClassifier()
    clf.fit(input_features, input_classes)
    return clf

def load_data():
    filename = "trainingdata.txt"
    with open(filename, "r") as f:
        lines = f.readlines()
    
    input_data = list()
    test_data = list()
    
    for line in lines[1:]:
        line = line.split(' ', 1)
        input_data.append((line[0], line[1]))
        
    n = int(input())
    for i in range(n):
        test_data.append(raw_input())
  
        
    return (input_data, test_data)

if __name__ == "__main__":
    main()