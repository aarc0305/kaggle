import csv
import numpy as np
from keras.utils import np_utils
from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.optimizers import RMSprop

l=[]
with open('spam_train.csv') as file:
	lines = csv.reader(file)
	for line in lines:
		l.append(line)
print l[0]

l=np.array(l)
l = np.delete(l, [0], 1)
m,n = l.shape
inputArr = np.zeros((m,n-1))
outputArr = np.zeros((m,1))

for i in range(m):
	outputArr[i,0]=int(l[i,n-1])
for i in range(m):
	for j in range(n-1):
		inputArr[i,j] = float(l[i,j])
print inputArr[0]
outputArr = np_utils.to_categorical(outputArr, num_classes=2)

print 'input shape: '+str(inputArr.shape)
print 'output shape: '+str(outputArr.shape)

model = Sequential([
    Dense(15, input_dim=n-1),
    Activation('relu'),
    Dense(10),
    Activation('relu'),
    Dense(2),
    Activation('softmax'),
])

rmsprop = RMSprop(lr=0.001, rho=0.9, epsilon=1e-08, decay=0.0)

model.compile(optimizer=rmsprop,
              loss='categorical_crossentropy',
              metrics=['accuracy'])
print('Training ------------')
model.fit(inputArr, outputArr, epochs=50, batch_size=32)

#spam_test.csv
ltest=[]
with open('spam_test.csv') as file:
        lines = csv.reader(file)
        for line in lines:
                ltest.append(line)
ltest=np.array(ltest)
ltest = np.delete(ltest, [0], 1)
mtest,ntest = ltest.shape
inputTestArr = np.zeros((mtest,ntest))
print 'input test shape: '+str(inputTestArr.shape)

for i in range(mtest):
	for j in range(ntest):
		inputTestArr[i,j] = float(ltest[i,j])
print inputTestArr[0]

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


#result
with open ('result.csv', mode='w') as write_file:
	writer = csv.writer(write_file)
	writer.writerow(["id","label"])
	for i in range(len(outputresult)):
		writer.writerow([i+1,outputresult[i]])
