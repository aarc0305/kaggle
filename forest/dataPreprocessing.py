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
outputArr = np.zeros((m,7))
print 'input shape: '+str(inputArr.shape)
print 'output shape: '+str(outputArr.shape)

print l[0]


for i in range(m):
	if int(l[i,n-1])==1:
		outputArr[i] = [1,0,0,0,0,0,0]
	elif int(l[i,n-1])==2:
		outputArr[i] = [0,1,0,0,0,0,0]
	elif int(l[i,n-1])==3:
		outputArr[i] = [0,0,1,0,0,0,0]
	elif int(l[i,n-1])==4:
		outputArr[i] = [0,0,0,1,0,0,0]
	elif int(l[i,n-1])==5:
		outputArr[i] = [0,0,0,0,1,0,0]
	elif int(l[i,n-1])==6:
		outputArr[i] = [0,0,0,0,0,1,0]
	else:
		outputArr[i] = [0,0,0,0,0,0,1]
for i in range(m):
	inputArr[i,0] = float(l[i,0])/3849.
	inputArr[i,1] = float(l[i,1])/360.
	inputArr[i,2] = float(l[i,2])/52.
	inputArr[i,3] = float(l[i,3])/1343.
	inputArr[i,4] = float(l[i,4])/554.
	inputArr[i,5] = float(l[i,5])/6890.
	inputArr[i,6] = float(l[i,6])/254.
	inputArr[i,7] = float(l[i,7])/254.
	inputArr[i,8] = float(l[i,8])/248.
	inputArr[i,9] = float(l[i,9])/6993.

	for j in range(n-11):
		inputArr[i,j+10] = int(l[i,j+10])
print inputArr[0]
print outputArr[0]

#test.csv
ltest = []
with open('test.csv') as file:
	lines = csv.reader(file)
	for line in lines:
		ltest.append(line)
ltest.remove(ltest[0])
ltest=np.array(ltest)	
ltest = np.delete(ltest, [0], 1)

mtest,ntest = ltest.shape
inputTestArr = np.zeros((mtest,ntest-1))
print 'input test shape: '+str(inputTestArr.shape)

print ltest[0]

for i in range(mtest):
	inputTestArr[i,0] = float(ltest[i,0])/3849.
	inputTestArr[i,1] = float(ltest[i,1])/360.
	inputTestArr[i,2] = float(ltest[i,2])/52.
	inputTestArr[i,3] = float(ltest[i,3])/1343.
	inputTestArr[i,4] = float(ltest[i,4])/554.
	inputTestArr[i,5] = float(ltest[i,5])/6890.
	inputTestArr[i,6] = float(ltest[i,6])/254.
	inputTestArr[i,7] = float(ltest[i,7])/254.
	inputTestArr[i,8] = float(ltest[i,8])/248.
	inputTestArr[i,9] = float(ltest[i,9])/6993.

	for j in range(ntest-11):
		inputTestArr[i,j+10] = int(ltest[i,j+10])
print inputTestArr[0]