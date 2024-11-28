import json
# 初始化保存结果的列表
result_list = [1291,1292,1293]
# 将结果列表转换为 JSON 字符串并打印输出
result_json = json.dumps(result_list)
print(result_json)