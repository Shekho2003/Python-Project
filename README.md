# ✨💳 Credit Card Fraud Detection 💳✨

---

### 👤 İsim Soyisim: **ALİ ŞEYHO**  
### 🆔 Öğrenci Numarası: **132130115**  
### 📁 Proje Adı: **Credit Card Fraud Detection**

---

## 🌟 Proje Özeti

Bu **parlak** ve **gelişmiş** proje, kredi kartı dolandırıcılığı tespiti için tasarlanmıştır. Gerçek dünyadan alınan karmaşık ve **dengesiz** veri seti üzerinde derinlemesine analizler yapılmış, makine öğrenimi teknikleri ile anomali tespiti ve sınıflandırma yöntemleri geliştirilmiştir.  
Finansal güvenliği artırmaya yönelik bu çalışma, **veri biliminde altın standartları** hedeflemektedir.

---

## 📊 İçindekiler

1. [🚀 Giriş](#-giriş)  
2. [📂 Veri Seti](#-veri-seti)  
3. [🧹 Veri Ön İşleme](#-veri-ön-işleme)  
4. [📈 Görsel Analizler ve Temel Bulgular](#-görsel-analizler-ve-temel-bulgular)  
5. [🔍 Segmentasyon (Kümeleme) Analizi](#-segmentasyon-kümeleme-analizi)  
6. [🛠 Kullanılan Kütüphaneler ve Araçlar](#-kullanılan-kütüphaneler-ve-araçlar)  
7. [⚙ Veri Madenciliği Süreci ve Aşamaları](#-veri-madenciliği-süreci-ve-aşamaları)  
8. [🏢 Yönetim Bilişim Sistemleri (YBS) Alanına Katkısı](#-yönetim-bilişim-sistemleri-ybs-alanına-katkısı)  
9. [📌 Sonuç ve Stratejik Değerlendirme](#-sonuç-ve-stratejik-değerlendirme)  
10. [💻 Kurulum ve Çalıştırma](#-kurulum-ve-çalıştırma)  
11. [✉ İletişim](#-iletişim)

---

## 🚀 Giriş

Kredi kartı dolandırıcılığı, finans dünyasının **en karanlık sorunlarından biridir.** Bu proje, bu karanlıkta bir ışık yakmak için hazırlandı.  
Anomali tespiti ve sınıflandırma modelleriyle **gerçek zamanlı dolandırıcılık tespiti**, veri biliminde altın değerinde bir başarıdır.  
**SMOTE ile dengelenmiş veri**, sağlam analizlerin ve model başarısının temelidir.

---

## 📂 Veri Seti

- **Kaggle'dan temin edilen** "Credit Card Fraud Detection" veri seti kullanılmıştır.  
- İşlem zamanı, tutarı ve dolandırıcılık etiketi (0: Normal, 1: Dolandırıcılık) içermektedir.  
- Sınıf dengesizliği sebebiyle özel dengeleme teknikleri uygulanmıştır.

---

## 🧹 Veri Ön İşleme

- Eksik değer **bulunmamaktadır**.  
- Aykırı değerler detaylıca incelenmiştir.  
- Sayısal veriler **StandardScaler** ile normalize edilmiştir.  
- **SMOTE** yöntemiyle sınıf dengesizliği giderilmiştir.  

---

## 📈 Görsel Analizler ve Temel Bulgular

- İşlem tutarındaki aykırı değerlerin detaylı görselleştirilmesi.  
- Orijinal ve SMOTE sonrası **sınıf dağılımlarının karşılaştırılması.**  
- Anomali ve normal işlemler arasındaki temel farkların grafiklerle açıklanması.

---

## 🔍 Segmentasyon (Kümeleme) Analizi

- **K-Means kümeleme** algoritması kullanılarak işlem verileri anlamlı gruplara ayrıldı.  
- **Elbow yöntemi** ile optimal küme sayısı belirlenerek analiz derinleştirildi.  
- Kümeleme sonuçları dolandırıcılık tespiti açısından yorumlandı ve modelin başarısına katkısı değerlendirildi.

---

## 🛠 Kullanılan Kütüphaneler ve Araçlar

- **pandas**, **numpy**  
- **matplotlib**, **seaborn**  
- **scikit-learn** (StandardScaler, KMeans, PCA, DBSCAN, AgglomerativeClustering, silhouette_score)  
- **imblearn** (SMOTE)  
- **scipy** (zscore)  

---

## ⚙ Veri Madenciliği Süreci ve Aşamaları

1. Problemin tanımı ve veri keşfi  
2. Veri temizleme ve ön işleme  
3. Veri normalizasyonu ve SMOTE ile dengesizliğin giderilmesi  
4. Anomali tespiti için sınıflandırma modellerinin geliştirilmesi  
5. Kümeleme yöntemleri ile segmentasyon  
6. Sonuçların analiz edilmesi ve raporlanması  

---

## 🏢 Yönetim Bilişim Sistemleri (YBS) Alanına Katkısı

Bu proje, **YBS alanında finansal dolandırıcılık risklerini minimize eden karar destek sistemlerine ışık tutar.**  
Veri odaklı stratejiler geliştirilerek kurumların risk yönetimi ve operasyonel verimliliği artırılabilir.  
Gerçek zamanlı dolandırıcılık tespiti sayesinde, müşteri güveni ve kurum itibarında **altın değerinde iyileşme** sağlanabilir.

---

## 📌 Sonuç ve Stratejik Değerlendirme

- **Başarılı dolandırıcılık tespiti** için dengesiz verinin dengelenmesi kritik rol oynamaktadır.  
- Kümeleme ve sınıflandırma teknikleri, kredi kartı işlemlerini etkili şekilde analiz etmiştir.  
- Proje, finans sektöründe veri bilimi uygulamalarının **stratejik önemini kanıtlamaktadır.**

---

## 💻 Kurulum ve Çalıştırma

1. Python 3.7+ yüklü olmalı.  
2. Gerekli paketleri yüklemek için:  
   ```bash
   pip install -r requirements.txt
