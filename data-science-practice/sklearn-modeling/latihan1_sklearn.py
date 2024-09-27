# Latihan 4: Regresi Linear Sederhana dengan Scikit-learn:

from sklearn.linear_model import LinearRegression
import numpy as np

# Data (x: Jumlah belajar, y: nilai ujian)
x = np.array([[1], [2], [3], [4], [5]])
y = np.array([1, 2 , 3, 3.5, 4.5])

# Membuat model regresi linear
model = LinearRegression()

# Melatih model dengan data
model.fit(x, y) 

# Prediksi nilai ujian ketika jumlah belajar 6 jam
prediksi = model.predict(np.array([[6]]))

# Menampilkan hasil prediksi
print(f"Prediksi nilai ujian untuk 6 jam belajar: {prediksi[0]}")