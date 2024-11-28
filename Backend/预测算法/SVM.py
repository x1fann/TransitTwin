import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import classification_report, accuracy_score
from joblib import dump, load

# 步骤1：数据准备
df1 = pd.read_excel("Backend/预测算法/data1.xlsx")
df2 = pd.read_excel("Backend/预测算法/data2.xlsx")
data = pd.concat([df1, df2], axis=1)
data = data.T
X = data.iloc[:, :-1]
y = data.iloc[:, -1]

# 步骤2：数据预处理（这里仅做标准化处理）
#scaler = StandardScaler()
#X_scaled = scaler.fit_transform(X)

# 步骤3：数据划分
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.8, random_state=42)

# 步骤4：模型训练
svm_model = SVC(kernel='linear')  # 使用线性核
svm_model.fit(X_train, y_train)

# 步骤5：模型评估
y_pred = svm_model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))

# 步骤6：保存模型到本地文件
dump(svm_model, 'Backend/预测算法/SVMClassifier.pkl')