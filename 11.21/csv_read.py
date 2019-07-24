'''读取csv文件'''
import csv
data = csv.reader(open('info.csv','r'))

for user in data:
    print(user)
    # print(user[0])   #读取每一行的第1个数据