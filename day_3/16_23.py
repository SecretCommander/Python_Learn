word1 = "python"
print("word1: ", word1)
word1_length = len(word1)
print("Length of word1: ", word1_length)
word1_convert_float = float(word1_length)
print("word1 converted to float: ", word1_convert_float)
word1_convert_string = str(word1_convert_float)
print("word1 converted to string: ", word1_convert_float)

check_even = input("Masukkan Angka: ")
if int(check_even) % 2 == 0:
    print("Angka genap")
else: 
    print("Angka ganjil")

check_floor = 7 // 3
if int(check_floor) == int(2.7):
    print("Hasil floor 7 // 3 sama dengan 2.7 converted")
else:
    print("Hasil floor 7 // 3 tidak sama dengan 2.7 converted")

if type('10') == type(10):
    print("Tipe data '10' sama dengan tipe data 10")
else:
    print("Tipe data '10' tidak sama dengan tipe data 10")
    
if type(9.8) == type(int(10)):
    print("Tipe data 9.8 sama dengan tipe data int(10)")
else:
    print("Tipe data 9.8 tidak sama dengan tipe data int(10)")

hours = input("Masukkan Jam Kerja: ")
rate_per_hour = input("Masukkan Gaji Perjam: ")
weekly_earning = int(hours) * int(rate_per_hour)
print("Your weekly earning is ", weekly_earning)

years_lived = input("Masukkan umur anda dalam tahun: ")
seconds_lived = int(years_lived) * 365 * 24 * 60 * 60
print("Anda sudah hidup selama ", seconds_lived, " detik")

for i in range(1, 6):
    print(i, " ", 1 , " ", i, " ", i**2, " ", i**3)
