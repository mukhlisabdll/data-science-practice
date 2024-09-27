# Latihan 9: Menghitung Persentase Kenaikan dalam Data
sales = [1000, 1200, 1500, 1800, 2000] # Data penjualan untuk setiap tahun

# Menghitung persentase kenailkan setiap tahun
for i in range(1, len(sales)): # Looping mulai dari elemen kedua hingga akhir
    growth = ((sales[i] - sales[i-1]) / (sales[i-1])) * 100 # Menghitung persentase kenaikan
    print(f"Kenaikan persentase dari tahun {i} ke {i+1}: {growth:.2f}%") # Menampilkan hasil kenaikan dalam persen