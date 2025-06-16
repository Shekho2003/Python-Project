# Credit Card Fraud Detection

**İsim Soyisim:** ALİ ŞEYHO  
**Öğrenci Numarası:** 1321330115  
**Proje Adı:** Credit Card Fraud Detection  

---

## Proje Hakkında

Bu proje, kredi kartı işlemlerindeki dolandırıcılık faaliyetlerinin erken tespiti amacıyla geliştirilmiştir. Veri bilimi ve makine öğrenmesi teknikleri kullanılarak anomali tespiti, sınıflandırma ve dengesiz veri sorunları (imbalanced data) çözülmüştür. Python dili ve çeşitli veri bilimi kütüphaneleri ile kapsamlı veri ön işleme, görselleştirme, dengeleme ve kümeleme analizleri yapılmıştır.

---

## İçindekiler

- [Giriş](#giriş)  
- [Veri Seti](#veri-seti)  
- [Veri Ön İşleme](#veri-ön-işleme)  
- [Görsel Analizler ve Temel Bulgular](#görsel-analizler-ve-temel-bulgular)  
- [Segmentasyon (Kümeleme) Analizi](#segmentasyon-kümeleme-analizi)  
- [Kullanılan Kütüphaneler ve Araçlar](#kullanılan-kütüphaneler-ve-araçlar)  
- [Veri Madenciliği Süreci ve Aşamaları](#veri-madenciliği-süreci-ve-aşamaları)  
- [Yönetim Bilişim Sistemleri (YBS) Alanına Katkısı](#yönetim-bilişim-sistemleri-ybs-alanına-katkısı)  
- [Sonuç ve Stratejik Değerlendirme](#sonuç-ve-stratejik-değerlendirme)  
- [Kurulum ve Çalıştırma](#kurulum-ve-çalıştırma)  
- [İletişim](#iletişim)

---

## Giriş

Kredi kartı dolandırıcılıkları, finans sektöründe ciddi kayıplara yol açan önemli bir problemdir. Bu proje, gerçek dünya kredi kartı işlem verileri üzerinde makine öğrenmesi teknikleri kullanarak dolandırıcılık işlemlerini tespit etmeyi amaçlamaktadır. Anomali tespiti ve sınıflandırma modelleri geliştirilmiş, ayrıca veri dengesizliği SMOTE yöntemiyle giderilmiştir.

---

## Veri Seti

Veri seti, Kaggle platformundan temin edilen “Credit Card Fraud Detection” veri setidir. Veri seti; işlem zamanı, işlem tutarı ve işlem sınıfı (dolandırıcılık ya da normal) gibi bilgileri içermektedir. Sınıf dengesizliği (çok az dolandırıcılık işlemi) önemli bir zorluktur.

---

## Veri Ön İşleme

- Veri setinde eksik değer bulunmamaktadır.  
- İşlem tutarındaki aykırı değerler incelenmiştir.  
- İşlem tutarı ve diğer sayısal değişkenler StandardScaler ile normalleştirilmiştir.  
- Sınıf dengesizliği SMOTE yöntemi ile dengelenmiştir.  

---

## Görsel Analizler ve Temel Bulgular

- İşlem tutarındaki aykırı değerler grafiklerle analiz edilmiştir.  
- Sınıf dağılımı görselleştirilerek dengesizliğin boyutu gösterilmiştir.  
- SMOTE sonrası dengelenmiş sınıf dağılımı sunulmuştur.  

---

## Segmentasyon (Kümeleme) Analizi

- K-Means algoritması kullanılarak işlem verileri kümelenmiştir.  
- Elbow yöntemi ile optimal küme sayısı belirlenmiştir.  
- Kümeleme sonuçları anomali tespiti açısından yorumlanmıştır.  

---

## Kullanılan Kütüphaneler ve Araçlar

- pandas  
- numpy  
- matplotlib  
- seaborn  
- scikit-learn (StandardScaler, KMeans, PCA, DBSCAN, AgglomerativeClustering, metrics)  
- imblearn (SMOTE)  
- scipy (zscore)  

---

## Veri Madenciliği Süreci ve Aşamaları

1. Problem tanımı ve veri setinin analizi  
2. Veri temizleme ve aykırı değer incelemesi  
3. Veri normalizasyonu ve dengesizliğin giderilmesi  
4. Anomali tespiti ve sınıflandırma modellerinin geliştirilmesi  
5. Kümeleme algoritmaları ile segmentasyon analizi  
6. Sonuçların yorumlanması ve raporlanması  

---

## Yönetim Bilişim Sistemleri (YBS) Alanına Katkısı

Proje, finans sektöründe dolandırıcılık risklerinin azaltılması ve yönetilmesi için veriye dayalı karar destek sistemlerine katkı sağlamaktadır. Analizler, finans kurumlarının stratejik risk yönetimi ve operasyonel süreçlerinde kullanılabilir içgörüler sunmaktadır.

---

## Sonuç ve Stratejik Değerlendirme

Bu çalışma, dengesiz veri sorununu etkin şekilde yöneterek ve gelişmiş analiz teknikleri uygulayarak kredi kartı dolandırıcılığının erken tespiti konusunda başarılı sonuçlar elde etmiştir. Finansal kayıpların önlenmesi ve müşteri güveninin artırılması için önemli bir veri bilimi uygulamasıdır.

---

## Kurulum ve Çalıştırma

1. Python 3.7 veya üzeri yüklü olmalıdır.  
2. Gerekli kütüphaneler aşağıdaki komutla kurulabilir:  
   ```bash
   pip install -r requirements.txt
