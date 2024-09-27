# Latihan 2: Menggunakan Pandas untuk Data Wrangling:

import pandas as pd

# Memuat data dari CSV 
df = pd.read_csv('C:\\data-science-practice\\datasets\\Salary_Data.csv')

# Melihat 5 baris pertama data
print(df.head())

# Menghitung statistik dasar
print(df.describe())

# Menghapus data yang hilang (NaN)
df_cleaned = df.dropna()

# Menyimpan data bersih ke file baru
df_cleaned.to_csv('cleaned_Salary_Data.csv', index=False)