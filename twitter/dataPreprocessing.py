import csv
from keras.preprocessing import sequence
from keras.preprocessing.text import Tokenizer
from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation, Flatten
from keras.layers.embeddings import Embedding
import numpy as np
lx=[]
ly=[]
with open('train.csv') as file:
	lines = csv.reader(file)
	count = 0
	for line in lines:
		if count == 0:
			count = count+1
			continue
		lx.append(line[2])
		ly.append(int(line[1]))
X_train = np.array(lx)
y_train = np.array(ly)

token = Tokenizer(num_words = 2000)
token.fit_on_texts(X_train)

X_train = token.texts_to_sequences(X_train)
X_train = sequence.pad_sequences(X_train, maxlen=100)

print token.document_count
		
model = Sequential()
model.add(Embedding(output_dim=32,input_dim=2000,input_length=100))
model.add(Dropout(0.2))
model.add(Flatten())
model.add(Dense(256,activation='relu'))
model.add(Dropout(0.35))
model.add(Dense(1,activation='sigmoid'))
model.compile(loss='binary_crossentropy',optimizer='adam',metrics=['accuracy'])
model.fit(X_train,y_train,batch_size=100,epochs=10)
		
