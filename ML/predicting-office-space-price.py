import numpy as np
from sklearn import linear_model
import sys
from sklearn.preprocessing import PolynomialFeatures

#question
#https://www.hackerrank.com/challenges/predicting-office-space-price
  
  
# from mpl_toolkits.mplot3d import Axes3D
# import matplotlib.pyplot as plt
#  
# def plot_data(training_x, training_y):
# #     fig = plt.figure()
# #     ax = fig.add_subplot(111)
# #     for c, m, z1, zh in[('r', 'o', -50, -25)]:
# #         xs = training_x
# #         ys = training_y
# #         ax.scatter(xs, ys, c=c, marker=m)
# #           
# #     ax.set_xlabel('charged')
# #     ax.set_ylabel('life')
#     
#     x =  training_x[:,0]
#     y =  training_y[:,0]
#     m, b = np.polyfit(x, y, 1)
#     plt.plot(x, y, '.')
#     plt.plot(x, m*x + b, '-')
#     plt.show()


def get_input():
    training_x = list()
    training_y = list()
    with open("trainingdata.txt", "r") as f:
        lines = f.readlines()
    
    for line in lines:
        line = line.split(",")
        training_x.append(float(line[0]))
        training_y.append(float(line[1]))
        
        
    return training_x, training_y
    
    
def build_model(training_x, training_y):
    
    training_x1 = list()
    training_y1 = list()
    training_x2 = list()
    training_y2 = list()
    
    for i in range(len(training_y)):
        if training_x[i] < 4.0:
            training_x1.append(training_x[i])
            training_y1.append(training_y[i])
        else:
            training_x2.append(training_x[i])
            training_y2.append(training_y[i])
        
    training_x1 = np.array(training_x1)
    training_y1 = np.array(training_y1)
    training_x2 = np.array(training_x2)
    training_y2 = np.array(training_y2)
    
    training_x1 = training_x1.astype(float)
    training_y1 = training_y1.astype(float)
    training_x2 = training_x2.astype(float)
    training_y2 = training_y2.astype(float)
    
    training_x1.shape = (len(training_x1), 1)
    training_y1.shape = (len(training_y1), 1)
    training_x2.shape = (len(training_x2), 1)
    training_y2.shape = (len(training_y2), 1)
    
    clf1 = linear_model.LinearRegression()
    clf1.fit(training_x1, training_y1)
    
    clf2 = linear_model.LinearRegression()
    clf2.fit(training_x2, training_y2)
    
#     x1 =  training_x1[:,0]
#     y1 =  training_y1[:,0]
#     x2 =  training_x2[:,0]
#     y2 =  training_y2[:,0]
#     m1, b1 = np.polyfit(x1, y1, 1)
#     m2, b2 = np.polyfit(x2, y2, 1)
#     plt.plot(x1, y1, '.')
#     plt.plot(x1, m1*x1 + b1, '-')
#     plt.plot(x2, y2, '.')
#     plt.plot(x2, m2*x2 + b2, '-')
#     plt.show()
    
    #print "coefficient : ", clf.coef_
    ip = get_test_input()
    
    if ip < 4.0:
        return clf1.predict(ip)
    else:
        return clf2.predict(ip)
    

def get_test_input():
    return float(sys.stdin.readline())
    
def main():
    training_x, training_y = get_input()
    predicted_value = build_model(training_x, training_y)
    print round(predicted_value,2)
    #for x in predicted_value.tolist():
    #    print math.ceil(x*100)/100
if __name__ == "__main__":
    main()