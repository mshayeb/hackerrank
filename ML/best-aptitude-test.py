# https://www.hackerrank.com/challenges/the-best-aptitude-test

import sys
import numpy as np

lines = sys.stdin.readlines()

T = int(lines[0].strip())

for i in xrange(T):
	N = int(lines[7*i+1].strip())	
	GPA = np.array(lines[7*i+2].strip().split()).astype(float)
	stdev_GPA = np.std(GPA)
	tests = []
	corr = []
	for j in range(5):
		tests.append(np.array(lines[7*i+3+j].strip().split()).astype(float))
		stdev = np.std(tests[j])
		if stdev != 0 and stdev_GPA != 0:
			corr.append(np.cov(GPA,tests[j])[0][1]/(stdev_GPA * stdev))
		else:
			corr.append(-1)
	print corr.index(max(corr))+1	

