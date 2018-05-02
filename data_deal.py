# coding:utf-8
import csv

calculate_map = {}

csv_file = csv.reader(open("csvTrain.csv", 'r'))
features = []
name_to_id = []
out = []
for i, x in enumerate(csv_file):
    print len(x)
    if len(x) == 2801:
        if i == 0:
            for y in x:
                name_to_id.append(y)


        else:
            feature = []
            temp = {}
            for index, y in enumerate(x):
                feature.append(y)
                temp[name_to_id[index]] = y
                try:
                    num = float(y)
                    if calculate_map.has_key(num):
                        calculate_map[num] += 1
                    else:
                        calculate_map[num] = 1
                except:
                    pass
            if len(out) == 100:
                break
            out.append(temp)
            features.append(feature)


    else:
        continue

csv_file_out = open('little.csv', 'w')

writer = csv.DictWriter(csv_file_out, fieldnames=name_to_id)
writer.writeheader()
for x in out:
    writer.writerow(x)
csv_file_out.close()
# # csv 写入
# stu1 = ['marry', 26]
# stu2 = ['bob', 23]
# # 打开文件，追加a
# out = open('litte_csv.csv', 'a', newline='')
# # 设定写入模式
# csv_write = csv.writer(out, dialect='excel')
# # 写入具体内容
# for x in out:
#     csv_write.writerow(x)
# print ("write over")

# name_to_id = []
#
# calculate_map = {}
#
# i = 0
#
# features = []
#
# while 1:
#     lines = input_file.readlines(100000)
#     if not lines:
#         break
#     for line in lines:
#         temp = line.split(',')
#         # if calculate_map.has_key(len(temp)):
#         #     calculate_map[len(temp)] += 1
#         # else:
#         #     calculate_map[len(temp)] = 1
#
#         if len(temp) == 2796:
#             if i == 0:
#                 for x in temp:
#                     name_to_id.append(x)
#
#                     num = float(x)
#             else:
#                 feature = []
#                 for x in temp:
#                     feature.append(x)
#                 features.append(feature)
#         i += 1
#
# print features


items = calculate_map.items()
items.sort()
for key, value in items:
    print key, value  # print key,dict[key]
