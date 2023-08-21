import requests
import matplotlib.pyplot as plt

surah_info_url = 'https://api.alquran.cloud/v1/meta'
response = requests.get(surah_info_url)
data = response.json()

surahs = data['data']['surahs']['references']

surahs_sorted = sorted(surahs, key=lambda x: x['number'], reverse=True)

nama_surah = [surah['englishName'] for surah in surahs_sorted]
jumlah_ayat = [surah['numberOfAyahs'] for surah in surahs_sorted]

plt.figure(figsize=(10, 20))
# Mengganti bar dengan plot untuk membuat grafik garis
plt.plot(nama_surah, jumlah_ayat, color='blue', marker='o')  
plt.ylabel('Jumlah Ayat') 
plt.xlabel('Surah')  
plt.title('Jumlah Ayat pada Setiap Surah Al-Quran (dari An-Nas hingga Al-Fatihah)')
plt.xticks(rotation=90) 
plt.tight_layout()

for i, ayat in enumerate(jumlah_ayat):
    plt.text(i, ayat + 3, str(ayat), ha='center', fontsize=10, va='bottom')

plt.show()
