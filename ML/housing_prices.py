# housing_prices.py
import numpy as np
from sklearn import linear_model
import math

#question
#https://www.hackerrank.com/challenges/predicting-house-prices

def get_input():
    str = raw_input().split()
    num_features = int(str[0])
    num_records = int(str[1])
    
    all_input = list()
    for i in range(num_records):
        line = raw_input().split()
        for j in range(num_features + 1):
            all_input.append(line[j])
            
    input_data = np.array(all_input)
    
    input_data.shape = (num_records, num_features+1)
    input_data = input_data.astype(float)
    
    str = raw_input()
    num_records = int(str)
    
    all_input = list()
    for i in range(num_records):
        line = raw_input().split()
        for j in range(num_features):
            all_input.append(line[j])
    test_data = np.array(all_input)
    test_data.shape = (num_records, num_features)
    test_data = test_data.astype(float)
    
    
    return (input_data, test_data)

def build_model(train_data):
    (no_records, no_features) = train_data.shape
    no_features = no_features -1
    #print "no. of records : ", no_records
    #print "no. of features : ", no_features
    
    x = train_data[:, : no_features]
    y = train_data[:, no_features]
    
    clf = linear_model.LinearRegression()
    clf.fit(x, y)
    #print "coefficient : ", clf.coef_
    return clf
    
def evaluate(model, test_data):
    return model.predict(test_data)

    
def main():
    data = get_input()
    train_data = data[0]
    test_data = data[1]
    model = build_model(train_data)
    predicted_value = evaluate(model, test_data)
    
    for x in predicted_value.tolist():
        print math.ceil(x*100)/100
if __name__ == "__main__":
    main()