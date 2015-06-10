# https://www.hackerrank.com/challenges/quora-answer-classifier

import sys
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn import preprocessing

lines = sys.stdin.readlines()

N = int(lines[0].strip().split()[0])
M = int(lines[0].strip().split()[1])

training_X = []
training_Y = []

for i in xrange(1,N):
	line = lines[i].strip().split()
	training_Y.append(int(line[1]))
	X = []
	for j in xrange(M):
		X.append(0.0)
	for j in range(2,len(line)):
		data = line[j].split(':')
		X[int(data[0])-1] = float(data[1])
	training_X.append(X)

training_X = preprocessing.scale(training_X)

model=RandomForestClassifier(n_estimators=20)
model.fit(training_X,training_Y)

q = int(lines[N+1].strip())
test_X = []
test_X_id = []
for i in xrange(q):
	line = lines[N+2+i].strip().split()
	test_X_id.append(line[0])
	X = []
	for j in xrange(M):
		X.append(0.0)
	for j in range(2,len(line)):
		data = line[j].split(':')
		X[int(data[0])-1] = float(data[1])
	test_X.append(X)

test_Y = model.predict(preprocessing.scale(test_X))

for i in xrange(q):
	if test_Y[i] < 0:
		print test_X_id[i],'-1'
	else:
		print test_X_id[i],'+1'