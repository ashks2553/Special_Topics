import pandas as pd
import random
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, confusion_matrix, silhouette_score
import matplotlib.pyplot as plt
import seaborn as sns

# 1. تولید داده‌ها
مقادیر_کیفی = {
    "ضعیف": 0, "متوسط": 1, "خوب": 2, "عالی": 3,
    "مرد": 0, "زن": 1,
    "ندارد": 0, "دارد": 1,
    "کم": 0, "زیاد": 2,
    "شهری": 0, "روستایی": 1
}

data = {
    "سن": [random.randint(17, 20) for _ in range(100)],
    "جنسیت": [random.choice([0, 1]) for _ in range(100)],
    "معدل": [round(random.uniform(14, 20), 2) for _ in range(100)],
    "ساعت_مطالعه_روزانه": [random.randint(1, 8) for _ in range(100)],
    "مشارکت_کلاسی": [random.choice([0, 1, 2, 3]) for _ in range(100)],
    "دسترسی_به_معلم_خصوصی": [random.choice([0, 1]) for _ in range(100)],
    "وضعیت_اقتصادی": [random.choice([0, 1, 2]) for _ in range(100)],
    "تعداد_کتاب_غیردرسی": [random.randint(0, 50) for _ in range(100)],
    "شرکت_در_آزمون_های_آزمایشی": [random.randint(0, 20) for _ in range(100)],
    "میزان_استرس": [random.choice([0, 1, 2]) for _ in range(100)],
    "سابقه_تحصیلی_والدین": [random.choice([0, 1, 2, 3]) for _ in range(100)],
    "دسترسی_به_اینترنت": [random.choice([0, 1]) for _ in range(100)],
    "محل_زندگی": [random.choice([0, 1]) for _ in range(100)],
    "تعداد_اعضای_خانواده": [random.randint(1, 8) for _ in range(100)],
    "شرکت_در_کلاس_های_کنکور": [random.choice([0, 1]) for _ in range(100)],
    "سلامت_جسمی": [random.choice([0, 1, 2, 3]) for _ in range(100)],
    "علاقه_به_رشته_هدف": [random.choice([0, 1, 2, 3]) for _ in range(100)],
    "نوع_مدرسه": [random.choice([0, 1, 2]) for _ in range(100)],
    "میزان_استفاده_از_موبایل": [random.choice([0, 1, 2]) for _ in range(100)],
    "سابقه_مشاوره_تحصیلی": [random.choice([0, 1]) for _ in range(100)],
    "عملکرد_کنکور": [random.choice([0, 1, 2, 3]) for _ in range(100)]
}

df = pd.DataFrame(data)

# 2. آماده‌سازی داده‌ها
X = df.drop('عملکرد_کنکور', axis=1)  # ویژگی‌ها
y = df['عملکرد_کنکور']  # برچسب هدف

# نرمال‌سازی داده‌ها
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# تقسیم داده به آموزش و آزمون
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.3, random_state=42)

# 3. اجرای الگوریتم KNN
print("\n--- اجرای الگوریتم KNN ---")
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)

# پیش‌بینی و ارزیابی
y_pred_knn = knn.predict(X_test)
print("\nنتایج طبقه‌بندی با KNN:")
print(classification_report(y_test, y_pred_knn))
print("ماتریس اشتباه:")
print(confusion_matrix(y_test, y_pred_knn))

# 4. اجرای الگوریتم K-Means
print("\n--- اجرای الگوریتم K-Means ---")

# تعیین تعداد خوشه‌های بهینه
wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, init='k-means++', random_state=42)
    kmeans.fit(X_scaled)
    wcss.append(kmeans.inertia_)

plt.figure(figsize=(10, 6))
plt.plot(range(1, 11), wcss, marker='o', linestyle='--')
plt.title('روش آرنج برای تعیین K بهینه')
plt.xlabel('تعداد خوشه‌ها')
plt.ylabel('WCSS')
plt.show()

# اجرای K-Means با K=4 (چون 4 سطح عملکرد داریم)
kmeans = KMeans(n_clusters=4, init='k-means++', random_state=42)
kmeans.fit(X_scaled)

# اضافه کردن برچسب خوشه‌ها به داده اصلی
df['خوشه_KMeans'] = kmeans.labels_

# ارزیابی خوشه‌بندی
silhouette_avg = silhouette_score(X_scaled, kmeans.labels_)
print(f"\nمیانگین امتیاز سیلوئت: {silhouette_avg:.3f}")

# 5. تجسم نتایج (با استفاده از PCA برای کاهش ابعاد)
from sklearn.decomposition import PCA

pca = PCA(n_components=2)
principal_components = pca.fit_transform(X_scaled)

plt.figure(figsize=(12, 6))

# نمودار KNN
plt.subplot(1, 2, 1)
sns.scatterplot(x=principal_components[:, 0], y=principal_components[:, 1], hue=y, palette='viridis')
plt.title('توزیع واقعی عملکرد دانش‌آموزان (KNN)')

# نمودار K-Means
plt.subplot(1, 2, 2)
sns.scatterplot(x=principal_components[:, 0], y=principal_components[:, 1], hue=df['خوشه_KMeans'], palette='viridis')
plt.title('خوشه‌بندی دانش‌آموزان با K-Means')

plt.tight_layout()
plt.show()

# 6. مقایسه خوشه‌ها با عملکرد واقعی
cross_tab = pd.crosstab(df['خوشه_KMeans'], df['عملکرد_کنکور'])
print("\nمقایسه خوشه‌ها با عملکرد واقعی:")
print(cross_tab)