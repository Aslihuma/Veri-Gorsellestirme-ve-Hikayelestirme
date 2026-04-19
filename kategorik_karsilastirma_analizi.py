import seaborn as sns
import matplotlib.pyplot as plt

# Örnek Veri: Şehirlere Göre Ortalama Proje Tamamlama Puanları
sehirler = ['İstanbul', 'Ankara', 'İzmir', 'Bursa', 'Trabzon']
puanlar = [88, 82, 85, 78, 91]

plt.figure(figsize=(10, 6))
sns.barplot(x=sehirler, y=puanlar, palette='magma')

plt.title('Şehir Bazlı Proje Başarı Ortalamaları', fontsize=14)
plt.ylabel('Ortalama Puan')
plt.ylim(0, 100)

plt.show()
