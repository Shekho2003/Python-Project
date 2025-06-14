import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Dosya Yolu: creditcard.csv dosyasını okuyoruz
df = pd.read_csv("creditcard.csv")
df.head()

# Eksik değer kontrolü
missing_values = df.isnull().sum()
print("Eksik Veri Sayısı:\n", missing_values)

plt.figure(figsize=(10, 4))
sns.boxplot(data=df, x='Amount')
plt.title("Amount Sütununda Aykırı Değerler")
plt.show()

# IQR yöntemiyle aykırı değerleri filtreleme
Q1 = df['Amount'].quantile(0.25)
Q3 = df['Amount'].quantile(0.75)
IQR = Q3 - Q1
lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

outliers = df[(df['Amount'] < lower) | (df['Amount'] > upper)]
print(f"Aykırı değer sayısı: {len(outliers)}")

from sklearn.preprocessing import StandardScaler

# Yeni sütunlar oluşturarak standardize ediyoruz
df['normAmount'] = StandardScaler().fit_transform(df[['Amount']])
df['normTime'] = StandardScaler().fit_transform(df[['Time']])

# Orijinal sütunları çıkarıyoruz
df = df.drop(['Amount', 'Time'], axis=1)

# Sınıf sütunu zaten 0 ve 1'den oluşuyor (etiket), dönüştürmeye gerek yok.
df['Class'].value_counts()

plt.figure(figsize=(6,4))
sns.countplot(x='Class', data=df)
plt.title("Sınıf Dağılımı (0: Normal, 1: Fraud)")
plt.show()

from imblearn.over_sampling import SMOTE

X = df.drop('Class', axis=1)
y = df['Class']

sm = SMOTE(random_state=42)
X_res, y_res = sm.fit_resample(X, y)

# Yeni veri dağılımı
sns.countplot(x=y_res)
plt.title("Dengelenmiş Sınıf Dağılımı (SMOTE)")
plt.show()

from sklearn.preprocessing import StandardScaler

# Sadece öznitelikleri (features) al
X = df.drop('Class', axis=1)

# Normalizasyon (Z-score)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

inertia = []
k_range = range(1, 11)

for k in k_range:
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(X_scaled)
    inertia.append(kmeans.inertia_)

plt.plot(k_range, inertia, 'bo-')
plt.xlabel('Küme Sayısı (k)')
plt.ylabel('Inertia (WSS)')
plt.title('Elbow Yöntemi ile Optimal K Seçimi')
plt.show()

# Diyelim ki Elbow grafiğinde k = 2 anlamlı çıktı
kmeans = KMeans(n_clusters=2, random_state=42)
clusters = kmeans.fit_predict(X_scaled)

# Küme etiketlerini veri setine ekleyelim
df['KMeans_Cluster'] = clusters

# Her kümede kaç tane fraud (1) ve non-fraud (0) var?
pd.crosstab(df['KMeans_Cluster'], df['Class'])

from sklearn.cluster import DBSCAN

dbscan = DBSCAN(eps=2.5, min_samples=5)
db_labels = dbscan.fit_predict(X_scaled)

df['DBSCAN_Cluster'] = db_labels

# DBSCAN çıktısı analizi
df['DBSCAN_Cluster'].value_counts()

from sklearn.cluster import AgglomerativeClustering

agg = AgglomerativeClustering(n_clusters=2)
agg_labels = agg.fit_predict(X_scaled)

df['Agglomerative_Cluster'] = agg_labels

from sklearn.decomposition import PCA
import seaborn as sns

pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

plt.figure(figsize=(8,6))
sns.scatterplot(x=X_pca[:,0], y=X_pca[:,1], hue=df['KMeans_Cluster'], palette='Set1')
plt.title('K-Means Kümeleme PCA Görselleştirme')
plt.show()

