import pandas as pd

# 输入和输出文件的路径
input_file_path = 'C:/Users/Admin/Desktop/Cesium-1.109/Backend/扣件失效判识算法/扣件失效数据/原始数据/35m失效.csv'
output_file_path = 'C:/Users/Admin/Desktop/Cesium-1.109/Backend/扣件失效判识算法/扣件失效数据/原始数据/35m失效转置.csv'

# 使用pandas读取csv文件
df = pd.read_csv(input_file_path)

# 转置DataFrame
df_transposed = df.T

# 将转置后的DataFrame保存到新的csv文件
df_transposed.to_csv(output_file_path, header=False)

print(f"已保存到 '{output_file_path}'")
