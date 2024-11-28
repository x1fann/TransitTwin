import csv

input_filename = 'acceleration_1.csv'  # 原始CSV文件名
output_filename = 'acceleration_2.csv'  # 修改后的CSV文件名

with open(input_filename, mode='r', newline='', encoding='utf-8') as infile, \
     open(output_filename, mode='w', newline='', encoding='utf-8') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)
    
    for row in reader:
        # 修改第一列的值，为每个数字加上'object'前缀
        row[0] = f'object{row[0]}'
        writer.writerow(row)

print("CSV文件已修改并保存。")
