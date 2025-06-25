#Silahkan Masukkan Kode Kalian Di Sini
import math

# Pakai try except untuk hindari inputan acak dari user. Kalau inputan acak, eval akan bermasalah
try:
    # Ambil input dari user
    fungsi_str = input("Masukkan fungsi f(x) dalam bentuk string (gunakan 'x' sebagai variabel): ")
    a = float(input("Masukkan batas bawah (a): "))
    b = float(input("Masukkan batas atas (b): "))
    n = int(input("Masukkan jumlah subinterval/trapesium (n): "))

    while n < 0:
        print ("Jumlah trapesium harus lebih dari 0")
    

    # Fungsi menghitung f(x)
    def f(x):
        # langsung melakukan penghitungan dari fungsi str
        # misal x**2 dengan x=3 maka dia langsung hitung
        return eval(fungsi_str) 

    # Hitung h
    h = (b-a)/n

    # hitungn dengan metode trapezoid
    total = f(a) + f(b)

    for i in range (1, n):
        x = a + i * h
        total += 2 * f(x) 

    # Hitung integral
    integral = (h/2) * total
    print(f"Nilai integral dari {fungsi_str} dari {a} sampai {b} dengan {n} subinterval adalah: {integral}")
    

except Exception as e:
    print("Terjadi kesalahan : ", e)
    print("Cek kembali input. Gunakan format yang valid seperti x**2" + "\n")