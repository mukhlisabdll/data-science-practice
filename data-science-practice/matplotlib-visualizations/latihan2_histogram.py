# Latihan 6: Membuat Histogram dengan Matplotlib

import matplotlib.pyplot as plt  # Mengimpor pustaka Matplotlib untuk membuat grafik

# Data
data = [22, 23, 22, 26, 28, 30, 29, 31, 30, 32, 33, 35, 34, 33, 32, 30]  # Data umur yang akan di-plot

# Membuat histogram
plt.hist(data, bins=5, color='blue', edgecolor='black')  # Membuat histogram dengan 5 bin, warna biru, dan tepi hitam

# Menambahkan judul dan label sumbu
plt.title("Distribusi Umur")  # Menambahkan judul grafik
plt.xlabel("Umur")  # Menambahkan label pada sumbu X
plt.ylabel("Frekuensi")  # Menambahkan label pada sumbu Y

# Menampilkan histogram
plt.show()  # Menampilkan histogram di layar
