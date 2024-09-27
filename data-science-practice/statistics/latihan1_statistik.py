# Latihan 5: Menghitung Modus, Median, dan Mean dari Data

# Mengimpor pustaka statistics untuk menghitung mean, median, dan modus
import statistics

# Daftar angka
data = [10, 20, 20, 30, 40, 50, 50, 50]  # Daftar angka yang akan dihitung

# Menghitung mean (rata-rata)
mean_value = statistics.mean(data) 

# Menghitung median (nilai tengah)
median_value = statistics.median(data) 

# Menghitung modus (nilai yang paling sering muncul)
mode_value = statistics.mode(data) 

# Menampilkan hasil
print(f"Mean: {mean_value}") # Menampilkan rata-rata
print(f"Median: {median_value}") # Menampilkan median
print(f"Mode: {mode_value}") # Menampilkan modus

