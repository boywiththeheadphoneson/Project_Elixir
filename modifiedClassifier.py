from sklearn import tree

features = [[140, 1], [130,1], [150, 0], [170, 0]]  #in features 1s are for smooth and 0s are for bumpy
labels = [0, 0, 1, 1]   #in labels 0s are for apple and 1s are for orange

w = input("Enter the weight: ")
t = input("Enter 1 for smooth and 0 for bumpy: ")

clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)
p = clf.predict([[w ,t]])
if (p==1):
    print("It is an Orange!")
elif(p==0):
    print("It is an Apple!")
else:
    print("Wrong Input!")








