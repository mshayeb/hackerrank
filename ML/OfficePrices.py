import numpy as np
from sklearn import linear_model
 
def flatten(lol):
    return [y for x in lol for y in x]
 
 
def comb(v, ans, max_deg, used_deg, idx, curf):
    if idx>=len(v):
        if max_deg>=used_deg:
            ans.append(curf)
        return
    for i in range(max_deg+1):
        comb(v, ans, max_deg, used_deg+i, idx+1, curf*(v[idx]**i))
 
def gen_all_features(v, k):
    nv = []
    comb(v, nv, k, 0, 0, 1)
    return nv
 
(f,n) = map(int, raw_input().split())
x = []
y = []
for i in range(n):
    v = map(float, raw_input().split())
    #print gen_all_features(v[:-1])
    x.append(gen_all_features(v[:-1], 4))
    y.append(v[-1])
 
clf = linear_model.LinearRegression(fit_intercept=False)
clf.fit(x,y)
 
tc = int(raw_input())
for i in range(tc):
    v = map(float, raw_input().split())
    print np.dot(gen_all_features(v, 4), clf.coef_)