import csv
import os

path=r'C:\Users\koenig\Desktop\sysinfo.csv'

with open(path) as fo:
	data=csv.DictReader(fo)
	for record in data:
		print(record['ip'])
		result=os.system("ping -n 1 {} > null".format(record['ip']))
		if result == 0:
			print("{} is connected".format(record['ip']))
		else:
			print("{} is not connected".format(record['ip']))
