# import csv
# import os
# with open('train/train_GTSDB.csv') as csvfile:
#     readCSV = csv.reader(csvfile, delimiter=',')
#     for row in readCSV:
#         print(row)
#         print(row[0])
#         #print(row[0],row[1],row[2],)


import csv
import os
#line = ['filename', 'width', 'height', 'class', 'xmin', 'ymin', 'xmax', 'ymax']
#line = list(line)
with open('train.csv','w') as endfile:
	writer = csv.writer(endfile) #, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL
	writer.writerow(['filename', 'width', 'height', 'class', 'xmin', 'ymin', 'xmax', 'ymax'])
	with open('GTSDB.csv','r') as csvfile:
		readCSV = csv.reader(csvfile)
		#readCSV = list(readCSV)
		for row in readCSV:
			if row[0] != 'filename':
				for filename in os.listdir('train'):
					if row[0] == filename:
						#list(row)
						print(row)
						writer.writerow(row)

        				#print(row[0],row[1],row[2],)
csvfile.close()
endfile.close()


# import csv

# row = ['2', ' Marie', ' California']

# with open('train/GT-00.csv', 'r') as readFile:
# 	reader = csv.reader(readFile)
# 	lines = list(reader)
# 	lines[2] = row

# with open('people.csv', 'w') as writeFile:
#     writer = csv.writer(writeFile)
#     writer.writerows(lines)

# readFile.close()
# writeFile.close()