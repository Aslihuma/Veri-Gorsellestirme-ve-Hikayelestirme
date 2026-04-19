import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Örnek Veri: Çalışma Saati vs. Sınav Notu
veri = {
    'Calisma_Saati': [2, 5, 8, 10, 15, 20, 25, 30, 35, 40],
    'Sinav_Notu': [45, 50, 55, 60, 75, 80, 85, 90, 95, 100]
}
df = pd.DataFrame(veri)

plt.figure(figsize=(8, 6))
sns.regplot(x='Calisma_Saati', y='Sinav_Notu', data=df, color='seagreen')

plt.title('Çalışma Saati ile Başarı Arasındaki İlişki', fontsize=14)
plt.show()
