import csv
from keras.datasets import imdb
from keras.preprocessing import sequence
from keras.preprocessing.text import Tokenizer
from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation, Flatten
from keras.layers.embeddings import Embedding
import numpy as np
lx=[]
ly=[]
with open('train.tsv') as file:
	lines = csv.reader(file)
	for line in lines:

		linemodify = line[0].split("\t")
		if linemodify[2] == 'Phrase':
			continue
		lx.append(linemodify[2])
		
		#print (linemodify[2])
		if(len(linemodify) == 4):
			#print (linemodify[3])
			ly.append(int(linemodify[3]))
		else:
			ly.append(2)
y_train=np.zeros((156060,5))
y_train.reshape(156060,5)
print(len(ly))
for i in range(len(ly)):
	if ly[i]==0:
		y_train[i]=[1,0,0,0,0]
	elif ly[i]==1:
		y_train[i]=[0,1,0,0,0]
	elif ly[i]==2:
                y_train[i]=[0,0,1,0,0]
	elif ly[i]==3:
                y_train[i]=[0,0,0,1,0]
	else:
		y_train[i]=[0,0,0,0,1]
token = Tokenizer(num_words=2000)
token.fit_on_texts(lx)
print(token.document_count)
x_train_seq = token.texts_to_sequences(lx)
x_train = sequence.pad_sequences(x_train_seq, maxlen=50)

model = Sequential()
model.add(Embedding(output_dim=32,input_dim=2000,input_length=50))
model.add(Dropout(0.2))
model.add(Flatten())
model.add(Dense(256,activation='relu'))
model.add(Dropout(0.35))
model.add(Dense(5,activation='sigmoid'))
model.compile(loss='binary_crossentropy',optimizer='adam',metrics=['accuracy'])
model.fit(x_train,y_train,batch_size=100,epochs=10)
