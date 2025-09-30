

# Input berat badan (kg) dan tinggi badan (m)
berat = float(input("Masukkan berat badan (kg): "))
tinggi = float(input("Masukkan tinggi badan (m): "))
tinggi = tinggi / 100  # Konversi cm ke m jika diperlukan
# Rumus BMI
bmi = berat / (tinggi ** 2)

print("BMI Anda adalah:", round(bmi, 2))

# Menentukan kategori BMI
if bmi < 18.5:
    print("Kategori: Underweight (Kurus)")
elif 18.5 <= bmi < 25:
    print("Kategori: Normal")
elif 25 <= bmi < 30:
    print("Kategori: Overweight (Kelebihan berat badan)")
else:
    print("Kategori: Obesitas")
