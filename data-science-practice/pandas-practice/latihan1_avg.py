# Latihan 1: Menghitung Rata-Rata dari Daftar Nilai Siswa:

# Mengimpor library pandas dengan alias 'pd'
import pandas as pd

# Membuat dictionary 'data' dengan dua kolom: 'Nama' dan 'Nilai'
# Kolom 'Nama' berisi list nama-nama siswa, dan 'Nilai' berisi list nilai mereka
data = {
    'Nama': ['A', 'B', 'C', 'D'],
    'Nilai': [80, 90, 75, 85]
}

# Mengubah dictionary 'data' menjadi DataFrame yang disimpan dalam variabel 'df'
# DataFrame ini berbentuk seperti tabel dengan baris dan kolom
df = pd.DataFrame(data)

# Menghitung rata-rata dari kolom 'Nilai' dalam DataFrame 'df'
# Fungsi 'mean()' digunakan untuk menghitung rata-rata nilai numerik
rata_rata = df['Nilai'].mean()

# Menampilkan hasil rata-rata ke layar
# Hasil ini akan dicetak sebagai "Rata-rata nilai: nilai"
print("Rata-rata nilai:", rata_rata)

