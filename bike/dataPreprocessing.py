import csv
import numpy as np

l=[]
with open('train.csv') as file:
	lines = csv.reader(file)
	for line in lines:
		l.append(line)
l.remove(l[0])

l=np.array(l)
l = np.delete(l, [0,9,10], 1)
m,n = l.shape
inputArr = np.zeros((m,n-1))
outputArr = np.zeros((m,1))
print 'input shape: '+str(inputArr.shape)
print 'output shape: '+str(outputArr.shape)

print l[0]



for i in range(m):
	outputArr[i,0]=int(l[i,8])
for i in range(m):
	inputArr[i,0]=int(l[i,0])
	inputArr[i,1]=int(l[i,1])
	inputArr[i,2]=int(l[i,2])
	inputArr[i,3]=int(l[i,3])
	inputArr[i,4]=float(l[i,4])/45.
	inputArr[i,5]=float(l[i,5])/45.
	inputArr[i,6]=float(l[i,6])/100.
	inputArr[i,7]=float(l[i,7])/60.

print inputArr[1]
print outputArr[0]