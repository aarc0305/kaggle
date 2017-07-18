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
inputArr = np.zeros((m,15))
outputArr = np.zeros((m,1))
print 'input shape: '+str(inputArr.shape)
print 'output shape: '+str(outputArr.shape)

print l[0]



for i in range(m):
	outputArr[i,0]=int(l[i,8])
for i in range(m):
	#season one hot encoding
	if(int(l[i,0]) == 1):
		inputArr[i,0] = 1
		inputArr[i,1] = 0
		inputArr[i,2] = 0
		inputArr[i,3] = 0
	elif(int(l[i,0]) == 2):
		inputArr[i,0] = 0
		inputArr[i,1] = 1
		inputArr[i,2] = 0
		inputArr[i,3] = 0
	elif(int(l[i,0]) == 3):
		inputArr[i,0] = 0
		inputArr[i,1] = 0
		inputArr[i,2] = 1
		inputArr[i,3] = 0
	else:
		inputArr[i,0] = 0
		inputArr[i,1] = 0
		inputArr[i,2] = 0
		inputArr[i,3] = 1
	#holiday one hot encoding
	if(int(l[i,1])==0):
		inputArr[i,4] = 1
		inputArr[i,5] = 0
	else:
		inputArr[i,4] = 0
		inputArr[i,5] = 1
	#workingday one hot encoding
	if(int(l[i,2])==0):
		inputArr[i,6] = 1
		inputArr[i,7] = 0
	else:
		inputArr[i,6] = 0
		inputArr[i,7] = 1	
	#weather one hot encoding
	if(int(l[i,3])==1):
		inputArr[i,8] = 1
		inputArr[i,9] = 0
		inputArr[i,10] = 0
	elif(int(l[i,3])==2):
		inputArr[i,8] = 0
		inputArr[i,9] = 1
		inputArr[i,10] = 0
	else:
		inputArr[i,8] = 0
		inputArr[i,9] = 0
		inputArr[i,10] = 1
	inputArr[i,11]=float(l[i,4])/45.
	inputArr[i,12]=float(l[i,5])/45.
	inputArr[i,13]=float(l[i,6])/100.
	inputArr[i,14]=float(l[i,7])/60.

print inputArr[5]
print outputArr[0]