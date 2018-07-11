# Problem 22
# Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names,
# begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value
# by its alphabetical position in the list to obtain a name score. For example, when the list is sorted into alphabetical
# order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score
# of 938 × 53 = 49714. What is the total of all the name scores in the file?

import csv, os
os.chdir(r'E:\Data\ProjectEuler')
data = []
alphabet = 'abcdefghijklmnopqrstuvwxyz'
total_sum = 0
with open('P22_Names.txt', 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in csvreader:
        data.append(row)
data = data[0][0].split(',')
data = [data[item].replace('"', '') for item in range(len(data))]
data = sorted(data)
for item in range(len(data)):
    sum = 0
    for i in str(data[item]):
        if i.isupper() == True:
            i = i.lower()
        index = 1
        while i != alphabet[index-1]:
            index += 1
        sum += index
    total_sum += ((item + 1) * sum)
print(total_sum)