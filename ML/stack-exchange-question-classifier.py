import numpy as np
import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import BernoulliNB
from sklearn import preprocessing
import re

choosen_topics = [ "gis", "security", "photo", "mathematica", "unix", "wordpress", "scifi", "electronics", "android", "apple"]
topic_index = { choosen_topics[i]:i for i in range(len(choosen_topics))}

def main():
    input_data, test_data = load_data()
    input_features, input_classes , test_features = preprocess(input_data, test_data)
    clf = build_model(input_features, input_classes)
    predict(clf, test_features)
    
    
def text_to_words( text):
    letters_only = re.sub("[^a-zA-Z]", " ", text) 
    words = letters_only.lower().split()                             
    return( " ".join(words))    

def predict(clf, test_features):
    pred = clf.predict(test_features)
    for p in pred:
        print choosen_topics[p]    
    
                
def preprocess(input_data, test_data):
    data = list()
    classes = list()
    
    for d in input_data:
        data.append(text_to_words(d["question"]) + " " + text_to_words(d["excerpt"]))
        classes.append(d["topic"])
    classes =[topic_index[key] for key in classes]
        
    vectorizer = TfidfVectorizer(sublinear_tf=True,max_df=0.5,ngram_range=(1,1),stop_words="english", analyzer='word')
    
    input_features = vectorizer.fit_transform(data)
    input_classes = np.array(classes)
    
    data = list()

    for d in test_data:
        data.append(text_to_words(d["question"]) + " " + text_to_words(d["excerpt"]))
        
    test_features = vectorizer.transform(data)

    return (input_features, input_classes , test_features)

    
def build_model(input_features, input_classes):
    clf = BernoulliNB()
    clf.fit(input_features, input_classes)
    return clf

def load_data():
    filename = "training.json"
    with open(filename, "r") as f:
        lines = f.readlines()
    
    input_data = list()
    test_data = list()
    
    for line in lines[1:]:
        line = json.loads(line)
        input_data.append({"question": line["question"], "excerpt": line["excerpt"], "topic": line["topic"]})
        
    n = int(input())
    for i in range(n):
        line = json.loads(raw_input())
        test_data.append({"question": line["question"], "excerpt": line["excerpt"]})
  
        
    return (input_data, test_data)

if __name__ == "__main__":
    main()