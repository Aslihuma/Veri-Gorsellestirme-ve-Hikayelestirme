import matplotlib.pyplot as plt
import pandas as pd

# Örnek Veri: Aylık Eğitim Platformu Kayıt Sayıları
veriler = {
    'Ay': ['Ocak', 'Şubat', 'Mart', 'Nisan', 'Mayıs', 'Haziran'],
    'Kayit_Sayisi': [150, 210, 180, 340, 410, 390]
}
df = pd.DataFrame(veriler)

plt.figure(figsize=(10, 5))
plt.plot(df['Ay'], df['Kayit_Sayisi'], marker='o', linestyle='-', color='purple', linewidth=2)

# Estetik Dokunuşlar
plt.title('Aylık Yeni Öğrenci Kayıt Trendi', fontsize=14)
plt.xlabel('Dönem', fontsize=12)
plt.ylabel('Kayıt Sayısı', fontsize=12)
plt.grid(True, alpha=0.3)

plt.show()
