import csv
lx=[]
ly=[]
with open('train.csv') as file:
	lines = csv.reader(file)
	for line in lines:

		#print str(line)
		if line[2] == 'SentimentText':
			continue
		lx.append(line[2])
		
		#print line[2]
		ly.append(line[1])
		#print line[1]

		
		
