# Latihan 7: Membuat Grafik Scatter Plot 

# Mengimpor pustaka Matplotlib untuk membuat  visualisasi
import matplotlib.pyplot as plt

# Data
x = [1, 2, 3, 4, 5, 6, 7, 8, 9] # Data untuk sumbu X
y = [1, 4, 9, 16, 25, 36, 49, 64, 81] # Data untuk sumbu Y

# Membuat scatter plot
plt.scatter(x, y, color='red') # Membuat scatter plot dengan titik berwarna merah

# Menambahkan judul dan label sumbu 
plt.title("Hubungan antara X dan Y") # Menambahkan judul grafik
plt.xlabel("Nilai X") # Menambahkan label pada sumbu X
plt.ylabel("Nilai Y") # Menambahkan label pada sumbu Y

# Menampilkan scatter plot
plt.show() # Menampilkan scatter plot di layar