import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.utils.data import DataLoader, TensorDataset

# 步骤1：数据准备
df1 = pd.read_excel("Backend/预测算法/data1.xlsx")
df2 = pd.read_excel("Backend/预测算法/data2.xlsx")
data = pd.concat([df1, df2], axis=1)
data = data.T
X = data.iloc[:, :-1].values
y = data.iloc[:, -1].values

# 输出特征数量和样本数量
num_samples, num_features = X.shape
print(f'样本数量: {num_samples}, 特征数量: {num_features}')

# 步骤2：数据预处理（标准化）
#X_scaled = StandardScaler()
#X_scaled = scaler.fit_transform(X)

# 步骤3：数据划分
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
X_train_tensor = torch.tensor(X_train, dtype=torch.float32)
X_test_tensor = torch.tensor(X_test, dtype=torch.float32)
y_train_tensor = torch.tensor(y_train, dtype=torch.float32)
y_test_tensor = torch.tensor(y_test, dtype=torch.float32)

# 创建数据加载器
train_dataset = TensorDataset(X_train_tensor, y_train_tensor)
test_dataset = TensorDataset(X_test_tensor, y_test_tensor)

train_loader = DataLoader(dataset=train_dataset, batch_size=16, shuffle=True)
test_loader = DataLoader(dataset=test_dataset, batch_size=16)


# 步骤4：构建全连接神经网络模型
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


model = Net()

# 定义损失函数和优化器
criterion = nn.BCELoss()            #二元交叉熵损失函数
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

# 步骤5：模型训练
num_epochs = 10
for epoch in range(num_epochs):
    for inputs, labels in train_loader:
        outputs = model(inputs)
        labels = labels.view(-1, 1)
        loss = criterion(outputs, labels)

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

    print(f'Epoch {epoch + 1}, Loss: {loss.item()}')

# 步骤6：模型评估
model.eval()
with torch.no_grad():
    correct = 0
    total = 0
    for inputs, labels in test_loader:
        outputs = model(inputs)
        predicted = (outputs.data > 0.5).float()
        total += labels.size(0)
        correct += (predicted.view(-1) == labels).sum().item()

accuracy = 100 * correct / total
print(f'Accuracy: {accuracy}%')
# 步骤6：模型评估
model.eval()
all_labels = []
all_predictions = []
all_probabilities = []
with torch.no_grad():
    for inputs, labels in test_loader:
        outputs = model(inputs)
        probabilities = outputs.data.numpy()
        predictions = (outputs.data > 0.5).float().numpy()
        all_labels.extend(labels.numpy())
        all_predictions.extend(predictions)
        all_probabilities.extend(probabilities)

# 转换为numpy数组
all_labels = np.array(all_labels)
all_predictions = np.array(all_predictions)
all_probabilities = np.array(all_probabilities)

# 计算指标
accuracy = accuracy_score(all_labels, all_predictions)
precision = precision_score(all_labels, all_predictions)
recall = recall_score(all_labels, all_predictions)
f1 = f1_score(all_labels, all_predictions)
roc_auc = roc_auc_score(all_labels, all_probabilities)

print(f'Accuracy: {accuracy * 100:.2f}%')
print(f'Precision: {precision:.2f}')
print(f'Recall: {recall:.2f}')
print(f'F1 Score: {f1:.2f}')
print(f'ROC-AUC: {roc_auc:.2f}')

""" # 步骤7：模型保存
model_save_path = 'Backend/预测算法/NetClassifier.pth'  # 保存模型的路径
torch.save(model.state_dict(), model_save_path)
 """