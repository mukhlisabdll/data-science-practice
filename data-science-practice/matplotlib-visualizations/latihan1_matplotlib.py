# Latihan 3: Membuat Grafik Garis Sederhana dengan Matplotlib:

import matplotlib.pyplot as plt

# Data 
years = [2018, 2019, 2020, 2021, 2022]
values = [100, 200, 300, 400, 500]

# Membuat grafik garis 
plt.plot(years, values)

# Memberikan judul dan label sumbu 
plt.title("Pertumbuhan Nilai")
plt.xlabel("Tahun")
plt.ylabel("Nilai")

# Menampilkan grafik
plt.show()