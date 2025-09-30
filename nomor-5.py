import math  # untuk fungsi sqrt (akar kuadrat)

def hitung_jarak(x1, y1, x2, y2):
    # selisih koordinat
    dx = x2 - x1
    dy = y2 - y1
    
    # rumus jarak Euclidean
    jarak = math.sqrt(dx**2 + dy**2)
    return jarak

# contoh penggunaan
print("Program menghitung jarak antara dua titik")
x1 = float(input("Masukkan x1: "))
y1 = float(input("Masukkan y1: "))
x2 = float(input("Masukkan x2: "))
y2 = float(input("Masukkan y2: "))

hasil = hitung_jarak(x1, y1, x2, y2)
print("Jarak antara titik ({}, {}) dan ({}, {}) adalah: {:.2f}".format(x1, y1, x2, y2, hasil))
