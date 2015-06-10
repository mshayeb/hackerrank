# https://www.hackerrank.com/challenges/craigslist-post-classifier-the-category

import json, sys
#from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB, BernoulliNB
from sklearn.svm import LinearSVC
from sklearn.linear_model import LogisticRegression
import re
import numpy as np

def print_top_50(vectorizer, clf, labels):
    features = vectorizer.get_feature_names()
    for i, label in enumerate(labels):
        top50 = np.argsort(clf.coef_[i])[-30:]
        print '{}: {}\n'.format(label, ' '.join(features[j] for j in top50))

def my_preprocessor(string):
    return re.sub('[-@~%^&*+#$/\.?!<>;:,\'\"\\(){}]', ' ', string).lower()

def main():

    data = []
    category = []

    with open('training.json', 'r') as f:
        f.next()
        for line in f:
            post = json.loads(line)
            data.append(post['heading'])
            category.append(post['category'])
                
    vectorizer = TfidfVectorizer(stop_words='english', min_df=0, max_df=.2, ngram_range=(1, 2), max_features=9000, preprocessor=my_preprocessor)
    train = vectorizer.fit_transform(data)

    clf = LinearSVC()
#    clf = MultinomialNB(alpha=0.2, fit_prior=True)
#    clf = BernoulliNB(alpha=0.2, fit_prior=False)
#    clf = LogisticRegression()

    category = np.array(category)

    clf.fit(train, category)
    print 'training completed!'
    labels = ['activities', 'appliances', 'artists', 'automotive', 'cell-phones', 'childcare', 'general', 'household-services', 'housing', 'photography', 'real-estate', 'shared', 'temporary', 'therapeutic', 'video-games', 'wanted-housing']
#    print_top_50(vectorizer, clf, labels)

    n = input()
    test = []
    if n == 0:
        sys.exit(1)
    sections = []
    for i in xrange(n):
        post = json.loads(raw_input())
        test.append(post['heading'])
        sections.append(post['section'])
    test = vectorizer.transform(np.array(test))
    confidence = clf.decision_function(test)
    output = []
    for i in xrange(n):
        section = sections[i]
        if section == 'for-sale':
            vals = confidence[i, [1, 4, 9, 14]]
            m = max(vals)
            fields = np.array(['appliances', 'cell-phones', 'photography', 'video-games'])
            output.append(fields[vals==m][0])
        elif section == 'housing':
            vals = confidence[i, [8, 11, 12, 15]]
            m = max(vals)
            fields = np.array(['housing', 'shared', 'temporary', 'wanted-housing'])
            output.append(fields[vals==m][0])
        elif section == 'community':
            vals = confidence[i, [0, 2, 5, 6]]
            m = max(vals)
            fields = np.array(['activities', 'artists', 'childcare', 'general'])
            output.append(fields[vals==m][0])
        elif section == 'services':
            vals = confidence[i, [3, 7, 10, 13]]
            m = max(vals)
            fields = np.array(['automotive', 'household-services', 'real-estate', 'therapeutic'])
            output.append(fields[vals==m][0])
    
    with open('output_svc_restricted.txt', 'w') as f:
        f.write('\n'.join(output))
#    print '\n'.join(output)

if __name__ == '__main__':
    main()