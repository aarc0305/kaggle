import numpy as np
np.random.seed(1337)  # for reproducibility
from keras.datasets import mnist
from keras.utils import np_utils
from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.optimizers import Adam
import csv

l=[]
with open('train.csv') as file:
	lines = csv.reader(file)
	for line in lines:
		l.append(line)
l.remove(l[0])

l=np.array(l)
l = np.delete(l, [0,3,8,10], 1)
m,n = l.shape
inputArr = np.zeros((m,n-1))
outputArr = np.zeros((m,1))
for element in l:
	#sex
	if element[2] == 'male':
		element[2] = 0
	else:
		element[2]=1
	#Embarked
	if element[7] == 'S':
		element[7] = 0
	elif element[7] == 'C':
		element[7]=0.5
	else:
		element[7] = 1
	#age
	if len(element[3]) == 0:
		element[3]=40


for i in range(m):
	outputArr[i,0]=int(l[i,0])
for i in range(m):
	inputArr[i,0]=int(l[i,1])*(-1)
	inputArr[i,1]=int(l[i,2])
	inputArr[i,2]=float(l[i,3])/100.
	inputArr[i,3]=int(l[i,4])/8.
	inputArr[i,4]=int(l[i,5])/6.
	inputArr[i,5]=float(l[i,6])/600.
	inputArr[i,6]=float(l[i,7])
outputArr = np_utils.to_categorical(outputArr, num_classes=2)
print 'input shape: '+str(inputArr.shape)
print 'output shape: '+str(outputArr.shape)


model = Sequential([
    Dense(15, input_dim=7),
    Activation('relu'),
    Dense(10),
    Activation('relu'),
    Dense(2),
    Activation('softmax'),
])

adam = Adam(lr=0.001, beta_1=0.9, beta_2=0.999, epsilon=1e-08)

model.compile(optimizer=adam,
              loss='categorical_crossentropy',
              metrics=['accuracy'])
print('Training ------------')
model.fit(inputArr, outputArr, epochs=100, batch_size=32)

#test.csv
ltest = []
with open('test.csv') as file:
	lines = csv.reader(file)
	for line in lines:
		ltest.append(line)
ltest.remove(ltest[0])
ltest=np.array(ltest)	
ltest = np.delete(ltest, [0,2,7,9], 1)
print 'ltest before modify: '+str(ltest[0])

for element in ltest:
	#sex
	if element[1] == 'male':
		element[1] = 0
	else:
		element[1]=1
	#Embarked
	if element[6] == 'S':
		element[6] = 0
	elif element[6] == 'C':
		element[6]=0.5
	else:
		element[6] = 1
	#age
	if len(element[2]) == 0:
		element[2]=40
	#ticket fare
	if len(element[5]) == 0:
		element[5]=0

print 'ltest after modify: '+str(ltest[0])

mtest,ntest = ltest.shape
inputTestArr = np.zeros((mtest,ntest))
print 'inputTestArr shape: '+str(inputTestArr.shape)
for i in range(mtest):
	inputTestArr[i,0]=int(ltest[i,0])*(-1)
	inputTestArr[i,1]=int(ltest[i,1])
	inputTestArr[i,2]=float(ltest[i,2])/100.
	inputTestArr[i,3]=int(ltest[i,3])/8.
	inputTestArr[i,4]=int(ltest[i,4])/6.
	inputTestArr[i,5]=float(ltest[i,5])/600.
	inputTestArr[i,6]=float(ltest[i,6])
#print inputTestArr[0]
results = model.predict(inputTestArr)
#print results
print type(results)
outputresult = []
for result in results:
	max = 0
	index = 0
	for i in range(2):
		if result[i] > max:
			max = result[i]
			index = i
	outputresult.append(index)
print outputresult
with open ('result.csv', mode='w') as write_file:
	writer = csv.writer(write_file)
	writer.writerow(["PassengerId","Survived"])
	for i in range(len(outputresult)):
		writer.writerow([i+892,outputresult[i]])
