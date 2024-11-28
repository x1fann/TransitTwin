import numpy as np
import json
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.utils.data import DataLoader, TensorDataset
import time

# 记录开始时间
start_time = time.time()

# 步骤1：原有代码及Net类定义
df1 = pd.read_excel("Backend/预测算法/data1.xlsx")
df2 = pd.read_excel("Backend/预测算法/data2.xlsx")
data = pd.concat([df1, df2], axis=1)
data = data.T
X = data.iloc[:, :-1].values
y = data.iloc[:, -1].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
X_train_tensor = torch.tensor(X_train, dtype=torch.float32)
X_test_tensor = torch.tensor(X_test, dtype=torch.float32)
y_train_tensor = torch.tensor(y_train, dtype=torch.float32)
y_test_tensor = torch.tensor(y_test, dtype=torch.float32)

train_dataset = TensorDataset(X_train_tensor, y_train_tensor)
test_dataset = TensorDataset(X_test_tensor, y_test_tensor)

train_loader = DataLoader(dataset=train_dataset, batch_size=16, shuffle=True)
test_loader = DataLoader(dataset=test_dataset, batch_size=16)

class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.fc1 = nn.Linear(X_train.shape[1], 64)
        self.fc2 = nn.Linear(64, 32)
        self.fc3 = nn.Linear(32, 1)

    def forward(self, x):
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = torch.sigmoid(self.fc3(x))
        return x


# 步骤2：加载保存好的模型
model = Net()
model_save_path = 'Backend/预测算法/NetClassifier.pth'
model.load_state_dict(torch.load(model_save_path, weights_only=True))
model.eval()  # 设置模型为评估模式

# 步骤3：加载要预测的新数据，只取特征列
new_data = pd.read_excel('Backend/预测算法/test_data.xlsx')
new_data = new_data.T
new_X = new_data.values

scaler = StandardScaler()
scaler.fit(new_X)  # 计算新数据的scaler参数
new_X_scaled = scaler.transform(new_X)
new_X_tensor = torch.tensor(new_X_scaled, dtype=torch.float32) # 转换为PyTorch张量

# 步骤4：模型推断
with torch.no_grad():
    predictions = model(new_X_tensor)

# 将预测结果转换为numpy数组
predicted_numpy = predictions.cpu().numpy()

 # 直接输出预测结果
#print("预测结果：")
#print(predicted_numpy) 

# 初始化保存结果的列表
result_list = []
# 输出预测结果及对应的数据列编号
for i, pred in enumerate(predicted_numpy):
    if pred >= 0.5:
        result_list.append(i)
# 将结果列表转换为 JSON 字符串并打印输出
result_json = json.dumps(result_list)
print(result_json)

# 记录结束时间
#end_time = time.time()

# 计算总运行时间
#total_time = end_time - start_time

#print(f"执行时间: {total_time} 秒")