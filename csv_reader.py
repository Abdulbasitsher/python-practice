# with open("data.csv") as file:
#     data = file.readlines()

# csv_data = []

# for daata in data:
#     csv_data.append(daata.strip().split(","))
   
# print(csv_data)

import csv

with open("data.csv") as data:
    csv_data = csv.reader(data)
    print(csv_data)
    tempreture_data_list = []
    for row in csv_data:
        for index, row in enumerate(csv_data):
            if index >= 0:
                tempreture_data_list.append(int(row[1]))
    print(tempreture_data_list)    