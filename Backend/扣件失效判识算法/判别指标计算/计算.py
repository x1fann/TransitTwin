import csv

def process_csv(input_file_path, output_file_path):
    with open(input_file_path, 'r', newline='') as infile, \
         open(output_file_path, 'w', newline='') as outfile:
        
        reader = csv.reader(infile)
        writer = csv.writer(outfile)
        
        for row in reader:
            # 转换为数值类型，忽略空白行
            if row:
                numbers = [float(value) for value in row]
                max_val = max(numbers)
                min_val = min(numbers)
                sum_max_min = (max_val + min_val)/2
                
                # 计算新的行数据
                processed_row = [value / sum_max_min for value in numbers]
                
                # 写入新的csv文件
                writer.writerow(processed_row)

# 示例使用
input_file_path = 'E:/数字孪生/扣件失效数据/test.csv'  # 更改为你的文件路径
output_file_path = 'E:/数字孪生/扣件失效数据/test1.csv'

process_csv(input_file_path, output_file_path)


