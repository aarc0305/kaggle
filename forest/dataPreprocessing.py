import csv
import numpy as np

l=[]
with open('train.csv') as file:
	lines = csv.reader(file)
	for line in lines:
		l.append(line)
l.remove(l[0])
l = np.delete(l, [0], 1)
l=np.array(l)

m,n = l.shape
inputArr = np.zeros((m,n-1))
outputArr = np.zeros((m,1))
print 'input shape: '+str(inputArr.shape)
print 'output shape: '+str(outputArr.shape)

print l[0]


for i in range(m):
	outputArr[i,0]=int(l[i,n-1])
for i in range(m):
	for j in range(n-1):
		inputArr[i,j] = int(l[i,j])
print inputArr[0]
print outputArr[0]

