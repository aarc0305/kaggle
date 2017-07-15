import numpy as np
np.random.seed(1337)  # for reproducibility
from keras.datasets import mnist
from keras.utils import np_utils
from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.optimizers import RMSprop
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
    Dense(10, input_dim=7),
    Activation('relu'),
    Dense(2),
    Activation('softmax'),
])

rmsprop = RMSprop(lr=0.001, rho=0.9, epsilon=1e-08, decay=0.0)

model.compile(optimizer=rmsprop,
              loss='categorical_crossentropy',
              metrics=['accuracy'])
print('Training ------------')
model.fit(inputArr, outputArr, batch_size=32)

