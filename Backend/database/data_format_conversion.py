"""
本脚本将csv文件从wide format(宽数据格式)转换为long format(长数据形式)
"""
import csv

# 原始文件路径
input_csv_path = 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/acceleration.csv'
# 转换后文件路径
output_csv_path = 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/acceleration_1.csv'

# 读取原始CSV文件
with open(input_csv_path, mode='r', newline='') as infile:
    reader = csv.reader(infile)
    headers = next(reader)  # 读取首行时刻值
    
    # 创建转换后的CSV文件
    with open(output_csv_path, mode='w', newline='') as outfile:
        writer = csv.writer(outfile)
        # 对于原始CSV中的每一行（每个节点）
        for row in reader:
            node_name = row[0]  # 节点名称
            # 对于每个时刻值和对应的振动位移
            for timestamp, displacement in zip(headers[1:], row[1:]):
                # 写入新行到转换后的CSV文件
                writer.writerow([node_name, timestamp, displacement])