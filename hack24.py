### HACK-24: Improve Browse by Subject ###

import csv

#open the files with file handles
fhand_ind = open('Workbook1.txt', 'rU')

lines  = fhand_ind.readlines()

second_level_bisac = []

sub_colonial = 'Colonial Period (1600-1775)' 
sub_19 = '19th Century'
sub_20 = '20th Century'
sub_state = 'State & Local'


for line in lines:
	line = line.split('\t')
	codes = line[1]
	print line[1]
	code_split = line[1].split['/']
	# print codes
	# previous = next_ = None
	# l = len(codes)
	# for index, obj in enumerate(objects):
	#     if (obj == sub_colonial) or (obj == sub_19) or (obj == sub_20) or (obj == sub_state):
	#         if index < (l - 1):
	#             second_level_bisac.append(objects[index + 1])








