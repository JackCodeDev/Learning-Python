import pandas
with open("file1.txt") as file1:
    data_list_1 = file1.readlines()
    new_data_1 = [int(i.strip()) for i in data_list_1]
    print(new_data_1)
with open("file2.txt") as file2:
    data_list_2 = file2.readlines()
    new_data_2 = [int(i.strip()) for i in data_list_2]
    print(new_data_2)

common_list = [num for num in new_data_1 if num in new_data_2]
print(common_list)
