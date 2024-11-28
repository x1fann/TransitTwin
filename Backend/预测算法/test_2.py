import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import classification_report, accuracy_score
from joblib import dump, load
import time
import json

# 记录开始时间
start_time = time.time()

# 步骤1：加载保存模型
model_save_path = 'Backend/预测算法/SVMClassifier.pkl'
svm_model = load(model_save_path)

# 步骤2：准备数据
new_data = pd.read_excel('Backend/预测算法/test_data.xlsx')
new_data = new_data.T
new_X = new_data.values

# 步骤3：使用模型进行预测
y_pred = svm_model.predict(new_X)  # 对新数据进行预测

# 步骤4：初始化保存结果的列表
result_list = []

# 步骤5：输出预测结果及对应的数据列编号
for i, pred in enumerate(y_pred):
    if pred >= 0.5:  # 只保留预测为1的列编号
        result_list.append(i)

# 步骤6：将结果列表转换为 JSON 字符串并打印输出
result_json = json.dumps(result_list)
print(result_json)

# 记录结束时间
# end_time = time.time()

# 计算总运行时间
# total_time = end_time - start_time

#print(f"执行时间: {total_time} 秒")