from sklearn import tree

#in features 1s are for smooth and 0s are for bumpy
features = [[140, 1], [130,1], [150, 0], [170, 0]]
#in labels 0s are for apple and 1s are for orange
labels = [0, 0, 1, 1]
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)
print (clf.predict ([[150, 0]]))
