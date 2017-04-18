from sklearn.feature_extraction import DictVectorizer
import csv
from sklearn import preprocessing
from sklearn import tree
allElectronicData = open(r'./test.csv', 'rb')
reader = csv.reader(allElectronicData)
headers = reader.next()

print(headers)

featureList = []
labelList = []

for row in reader:
    labelList.append(row[len(row)-1])
    rowDict = {}
    for i in range(1, len(row) -1):
        rowDict[headers[i]] = row[i]

    featureList.append(rowDict)

print(featureList)

#vectorize feature
vec = DictVectorizer()
dummyX = vec.fit_transform(featureList).toarray()
print("dummyX: " + str(dummyX))
print(vec.get_feature_names())

print("labelList: " + str(labelList))

lb = preprocessing.LabelBinarizer()
dummyY = lb.fit_transform(labelList)
print ("dummyY: " + str(dummyY))

clf = tree.DecisionTreeClassifier(criterion="entropy")
clf = clf.fit(dummyY,dummyY)
print ("clf: " + str(clf))