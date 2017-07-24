import csv
lx=[]
ly=[]
with open('train.tsv') as file:
	lines = csv.reader(file)
	for line in lines:

		linemodify = line[0].split("\t")
		if linemodify[2] == 'Phrase':
			continue
		lx.append(linemodify[2])
		
		print linemodify[2]
		if(len(linemodify) == 4):
			print linemodify[3]
			ly.append(linemodify[3])
		else:
			ly.append('2')
