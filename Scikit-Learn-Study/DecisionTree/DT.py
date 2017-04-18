from sklearn.feature_extraction import DictVectorizer
import csv
from sklearn import preprocessing
from sklearn import tree
allElectronicData = open(r'./test.csv', 'rb')
reader = csv.reader(allElectronicData)
headers = reader.next()

print(headers)