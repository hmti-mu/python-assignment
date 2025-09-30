def ada_huruf_kecil(teks: str):
    huruf_kecil = []  # list untuk menyimpan huruf kecil
    
    for char in teks:
        if char.islower():  # cek apakah karakter huruf kecil
            huruf_kecil.append(char)  # tambahkan ke list
    
    if huruf_kecil:  # jika list tidak kosong
        return True, huruf_kecil
    else:
        return False, []

# contoh penggunaan
kalimat = input("Masukkan kalimat: ")

ada, daftar = ada_huruf_kecil(kalimat)

if ada:
    print("Kalimat mengandung huruf kecil.")
    print("Huruf kecil yang ditemukan:", daftar)
else:
    print("Kalimat tidak mengandung huruf kecil.")