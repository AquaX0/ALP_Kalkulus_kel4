# 🧮 ALP_Kalkulus_kel4 - Metode Numerik untuk Turunan dan Integral

## 📌 Nama Proyek
**Proyek Akhir Kalkulus – Metode Numerik untuk Turunan dan Integral**  
Disusun oleh Kelompok 4 sebagai bagian dari tugas akhir mata kuliah *Analisis Lanjut Pemrograman (ALP)*.
Proyek ini merupakan bagian dari tugas akhir mata kuliah **Kalkulus** yang bertujuan untuk mengimplementasikan metode numerik menggunakan bahasa pemrograman Python.

Metode numerik adalah pendekatan yang digunakan untuk menghitung nilai turunan dan integral ketika solusi analitik sulit atau tidak dapat dilakukan. Dalam proyek ini, kami mengembangkan sebuah aplikasi berbasis teks yang dapat:

- Menerima input fungsi dari pengguna dalam bentuk string Python (contoh: `x**2 + 3*x`, `sin(x)`).
- Menghitung turunan menggunakan metode Forward Difference dan Central Difference.
- Menghitung integral tentu menggunakan metode Trapezoidal Rule dan Simpson’s 1/3 Rule.
- Memberikan hasil pendekatan numerik berdasarkan input batas interval dan banyaknya partisi.
- Mendukung input dalam satuan **radian** maupun **derajat**.

Semua fungsi diorganisasi dalam file Python modular dan dapat dipanggil secara terpisah maupun melalui antarmuka menu di `main.py`.

Tujuan akhirnya adalah menyediakan tool sederhana namun edukatif untuk membantu memahami konsep dasar metode numerik dalam kalkulus.

---

## 🎯 Tujuan Proyek
Proyek ini bertujuan untuk:
- Mengimplementasikan metode numerik untuk menghitung **turunan** dan **integral** fungsi matematika menggunakan Python.
- Menyediakan antarmuka berbasis teks (CLI) untuk pengguna agar bisa memilih metode numerik dan memasukkan fungsi secara dinamis.
- Melakukan evaluasi terhadap fungsi-fungsi numerik menggunakan pendekatan eksak dan pendekatan numerik.

---
## 🧠 Kegunaan Repository

Repository ini dibuat sebagai sumber belajar dan alat bantu interaktif untuk memahami konsep **turunan dan integral numerik** menggunakan Python.

Dengan repository ini, pengguna dapat:
- ✅ Menghitung turunan fungsi secara numerik tanpa kalkulus manual.
- ✅ Mengaproksimasi nilai integral tentu dari fungsi yang kompleks.
- ✅ Menganalisis perbedaan antara metode numerik (forward, central, trapezoidal, Simpson) terhadap hasil eksak.
- ✅ Belajar menerapkan teori kalkulus ke dalam kode Python secara langsung.
- ✅ Bereksperimen dengan berbagai fungsi matematika menggunakan input bebas dari pengguna.

---
## 🧩 Struktur Proyek

Struktur folder dari repository ini adalah sebagai berikut:

```
📦 ALP_Kalkulus_kel4/
 ┣ 📜 ForwardDifference.py        ← Implementasi metode Forward Difference
 ┣ 📜 CentralDifference.py        ← Implementasi metode Central Difference
 ┣ 📜 TrapezoidalNOrder.py        ← Implementasi metode Trapezoidal
 ┣ 📜 simpson.py                  ← Implementasi metode Simpson's 1/3
 ┣ 📜 BisectionMethod.py          ← Implementasi metode Bisection untuk Kasus A
 ┣ 📜 CaseA_ExtremumAnalysis.py   ← Kasus A: Analisis titik ekstrim lokal
 ┣ 📜 MainCalculus.py             ← Menu utama CLI interaktif
 ┣ 📜 README.md                   ← Dokumentasi proyek
 ┗ 📜 requirements.txt            ← Daftar dependensi Python
```
## ⚙️ Fungsi-Fungsi dalam Repository

### 🔷 1. ForwardDifference.py
```python
def forward_difference(f, x, h=1e-5)
```

Menghitung pendekatan turunan pertama dari fungsi `f(x)` di titik `x` menggunakan metode **Forward Difference**. Metode ini menggunakan selisih maju dengan langkah kecil `h`.

📘 **Rumus:**
\[
f'(x) \approx \frac{f(x + h) - f(x)}{h}
\]

📌 **Parameter:**
- `f`: fungsi satu variabel (misalnya `lambda x: x**2` atau hasil dari `lambdify`)
- `x`: titik tempat turunan dihitung (dalam satuan radian atau derajat sesuai input)
- `h`: langkah pergeseran (default = `1e-5`)

✅ **Return:**
- Nilai pendekatan turunan pertama di titik `x` menggunakan metode Forward Difference.

📎 **Contoh penggunaan:**
```python
from math import sin, pi
forward_difference(sin, pi/4)  # Hasil mendekati cos(pi/4)
```

---

### 🔷 2. CentralDifference.py
```python
def central_difference(f, x, h=1e-5)
```

Menghitung pendekatan turunan pertama dari fungsi `f(x)` di titik `x` menggunakan metode **Central Difference**. Metode ini mengambil nilai rata-rata dari selisih dua arah (maju dan mundur).

📘 **Rumus:**
\[
f'(x) \approx \frac{f(x + h) - f(x - h)}{2h}
\]

📌 **Parameter:**
- `f`: fungsi satu variabel (bisa berupa lambda atau hasil `lambdify`)
- `x`: titik tempat turunan dihitung
- `h`: ukuran langkah pendekatan (default = `1e-5`)

✅ **Return:**
- Nilai pendekatan turunan pertama di titik `x` menggunakan metode Central Difference.

📎 **Contoh penggunaan:**
```python
def f(x):
    return x**2

central_difference(f, 2)  # Output: sekitar 4.0
```
---

### 🔷 3. Trapezoidal.py  
File ini langsung mengeksekusi input pengguna dan menghitung integral tentu menggunakan **Metode Trapezoidal**.  
Langkah-langkah dalam kode:

1. Menerima input fungsi `f(x)` dari pengguna dalam bentuk string (contoh: `x**2`, `math.sin(x)`).
2. Meminta batas bawah `a`, batas atas `b`, dan jumlah partisi `n`.
3. Menghitung nilai integral menggunakan rumus:
\[
\int_a^b f(x)\,dx \approx \frac{h}{2} \left[f(a) + 2\sum_{i=1}^{n-1} f(x_i) + f(b)\right]
\]
4. Menampilkan hasil akhir di terminal.

Catatan: Fungsi `eval()` digunakan untuk mengeksekusi input fungsi string. Pastikan input valid (gunakan `x` sebagai variabel dan sintaks Python).

---

### 🔷 4. SimpsonOneThird.py
```python
def simpson_one_third(f, a, b, n)
```
Menghitung nilai integral tentu dari fungsi `f(x)` pada interval `[a, b]` menggunakan **metode Simpson’s 1/3 Rule**. Fungsi ini menerima fungsi numerik (seperti hasil `lambdify` atau `lambda`) dan jumlah segmen `n` **harus genap**.

📘 **Rumus yang digunakan:**

\[
\int_a^b f(x)\,dx \approx \frac{h}{3} \left[ f(a) + 4 \sum_{\text{ganjil}} f(x_i) + 2 \sum_{\text{genap}} f(x_i) + f(b) \right]
\]

📌 **Parameter:**
- `f`: fungsi satu variabel (bisa berupa lambda atau hasil dari `lambdify`)
- `a`: batas bawah integrasi
- `b`: batas atas integrasi
- `n`: jumlah segmen (wajib **genap**)

✅ **Return:**
- Nilai pendekatan integral tentu dari `f(x)` pada `[a, b]`.

📎 **Contoh penggunaan:**
```python
from math import sin, pi
hasil = simpson_one_third(sin, 0, pi, 10)
print(hasil)  # Output: sekitar 2.0001
```

🛑 Jika `n` bernilai ganjil, fungsi akan memunculkan error:
```
ValueError: n harus genap untuk Simpson's 1/3 rule.
```

---

## 🖥️ Cara Menjalankan Program

Untuk menjalankan program utama:

### 🔧 1. Persiapan

- Pastikan Python 3.7+ sudah terpasang di sistem.
- Jalankan terminal di direktori proyek.
- (Opsional) Buat virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

### ▶️ 2. Jalankan program

```bash
python MainCalculus.py
```

Program akan menampilkan menu:

```
=== MENU METODE NUMERIK ===
1. Turunan - Forward Difference
2. Turunan - Central Difference
3. Integral - Trapezoidal Rule
4. Integral - Simpson 1/3 Rule
5. Kasus A - Titik Ekstrim Lokal
6. Keluar
```

### 🧑‍💻 3. Input fungsi

- Masukkan fungsi `f(x)` dalam format Python. Contoh:
  - `x**2 + 3*x + 2`
  - `sin(x)`
  - `exp(-x**2)`

> Gunakan fungsi Python standar seperti `sin`, `cos`, `log`, `exp`, dll.

### 📐 4. Pilih satuan sudut

Setelah input fungsi, kamu akan diminta memilih satuan sudut:
- `1` → Derajat (akan dikonversi ke radian secara otomatis)
- `2` → Radian

### 📥 5. Input parameter

Bergantung pada metode yang dipilih, kamu akan diminta mengisi:
- `x` dan `h` untuk turunan
- `a`, `b`, dan `n` untuk integral

### ✅ 6. Output

Program akan menampilkan hasil turunan atau integral numerik berdasarkan metode yang dipilih.

📎 Contoh output:
```
=== HASIL INTEGRAL (Simpson 1/3 Rule) ===
f(x) = sin(x)
Interval: [0.0, 3.14159] (radians), n = 10
Hasil integral numerik: 1.99999
```

---

🛑 Catatan:
- Pastikan `n` genap saat memilih **Simpson 1/3 Rule**.
- Gunakan `x` sebagai variabel, bukan `t` atau `y`.
- Jangan gunakan `^` untuk pangkat, gunakan `**` (contoh: `x**2`, bukan `x^2`).

---

## 🎯 Kasus A - Titik Ekstrim Lokal

### 📋 Deskripsi Kasus
Kasus A bertujuan untuk menganalisis titik-titik ekstrim lokal dari sebuah fungsi menggunakan kombinasi metode numerik:
1. **Turunan numerik** menggunakan Central Difference
2. **Metode Bisection** untuk mencari akar dari turunan (titik stasioner)
3. **Perbandingan** dengan hasil turunan eksak menggunakan SymPy

### 🔬 Implementasi

#### 🔷 5. BisectionMethod.py
```python
def bisection_method(f, a, b, tolerance=1e-6, max_iterations=100)
def find_stationary_points(derivative_func, intervals, tolerance=1e-6)
```

**Metode Bisection** adalah algoritma numerik untuk mencari akar fungsi dalam interval tertentu. Algoritma ini bekerja dengan:
1. Memastikan `f(a)` dan `f(b)` memiliki tanda berbeda
2. Membagi interval `[a,b]` menjadi dua bagian di titik tengah `c = (a+b)/2`
3. Memilih sub-interval yang mengandung akar berdasarkan perubahan tanda
4. Mengulangi proses hingga mencapai toleransi yang diinginkan

📘 **Rumus iterasi:**
```
c = (a + b) / 2
Jika f(c) × f(a) < 0, maka b = c
Jika f(c) × f(a) > 0, maka a = c
```

📌 **Parameter:**
- `f`: fungsi yang akan dicari akarnya (dalam kasus ini f'(x))
- `a, b`: batas interval pencarian
- `tolerance`: toleransi error (default `1e-6`)
- `max_iterations`: maksimum iterasi (default 100)

✅ **Return:**
- `root`: nilai akar yang ditemukan
- `iterations`: jumlah iterasi yang digunakan

---

#### 🔷 6. CaseA_ExtremumAnalysis.py
```python
def case_a_extremum_analysis()
def demo_other_functions()
```

File ini mengimplementasikan **analisis lengkap titik ekstrim lokal** dengan langkah-langkah:

**🎯 Langkah 1: Definisi Fungsi**
- Fungsi uji: `f(x) = x³ - 6x² + 9x + 1`
- Turunan eksak: `f'(x) = 3x² - 12x + 9`
- Titik stasioner eksak: `x₁ = 1`, `x₂ = 3`

**🎯 Langkah 2: Turunan Numerik**
- Menggunakan metode **Central Difference** dengan `h = 1e-6`
- Membandingkan akurasi dengan turunan eksak

**🎯 Langkah 3: Pencarian Titik Stasioner**
- Menggunakan **Metode Bisection** untuk mencari akar f'(x)
- Interval pencarian: `[0, 2]` dan `[2, 4]`
- Membandingkan hasil numerik vs eksak

**🎯 Langkah 4: Analisis Jenis Ekstrim**
- Menggunakan **uji turunan kedua**: `f''(x) = 6x - 12`
- Klasifikasi: 
  - `f''(x) > 0` → Minimum lokal
  - `f''(x) < 0` → Maksimum lokal
  - `f''(x) = 0` → Titik infleksi

**🎯 Langkah 5: Validasi dan Perbandingan**
- Menghitung error antara metode numerik dan eksak
- Menampilkan tabel perbandingan hasil

### 📊 Contoh Output

```
============================================================
           KASUS A - TITIK EKSTRIM LOKAL
============================================================

1. FUNGSI YANG DIANALISIS:
   f(x) = x³ - 6x² + 9x + 1
   f'(x) eksak = 3*x**2 - 12*x + 9

2. TURUNAN NUMERIK:
   Menggunakan metode Central Difference dengan h = 1e-6

3. PENCARIAN TITIK STASIONER (AKAR f'(x)):
   Interval pencarian: [(0, 2), (2, 4)]

   a) Menggunakan turunan NUMERIK:
   Titik stasioner 1:
     x = 1.00000000
     f(x) = 5.00000000
     f'(x) numerik = 1.42e-08
     Iterasi: 20

   Titik stasioner 2:
     x = 3.00000000
     f(x) = 1.00000000
     f'(x) numerik = -1.42e-08
     Iterasi: 20

4. PERBANDINGAN HASIL:
   Solusi Eksak: x₁ = 1, x₂ = 3

   Perbandingan Numerik vs Eksak:
   --------------------------------------------------
   |  Metode   |   x₁    |   x₂    |  Error₁ | Error₂ |
   --------------------------------------------------
   | Numerik   | 1.000000 | 3.000000 | 1.49e-08 | 1.49e-08 |
   | Bisection | 1.000000 | 3.000000 | 1.49e-08 | 1.49e-08 |
   --------------------------------------------------

5. ANALISIS JENIS EKSTRIM:
   Menggunakan uji turunan kedua f''(x) = 6x - 12
   f''(x) = 6*x - 12
   Titik 1: x = 1.000000
           f''(x) = -6.000000 → Maksimum Lokal
           f(x) = 5.000000
   Titik 2: x = 3.000000
           f''(x) = 6.000000 → Minimum Lokal
           f(x) = 1.000000
```

### 🚀 Cara Menjalankan Kasus A

```bash
# Jalankan analisis lengkap
python CaseA_ExtremumAnalysis.py
```

Atau jalankan fungsi spesifik dalam Python:
```python
from CaseA_ExtremumAnalysis import case_a_extremum_analysis
numeric_results, exact_results = case_a_extremum_analysis()
```

### 🧪 Fungsi Demo Lain

File ini juga menyediakan `demo_other_functions()` yang menunjukkan analisis titik ekstrim untuk:
- **Fungsi trigonometri**: `f(x) = sin(x) + 0.5*cos(2x)`
- **Interval**: `[0, 2π]`
- **Implementasi otomatis** pencarian titik stasioner dalam beberapa sub-interval

### 📈 Keunggulan Implementasi

✅ **Akurasi Tinggi**: Error < 1e-8 dibandingkan solusi eksak  
✅ **Robust**: Dapat menangani berbagai jenis fungsi  
✅ **Modular**: Setiap komponen dapat digunakan secara terpisah  
✅ **Validasi Lengkap**: Perbandingan dengan solusi analitik  
✅ **Analisis Mendalam**: Klasifikasi jenis ekstrim menggunakan turunan kedua  

### ⚙️ Dependencies Tambahan

Untuk menjalankan Kasus A, install dependency berikut:
```bash
pip install sympy
```

**SymPy** digunakan untuk:
- Menghitung turunan simbolik (eksak)
- Membandingkan hasil numerik dengan solusi analitik
- Melakukan diferensiasi otomatis untuk validasi

---

## 📐 Kasus B - Integral Tentu

### 📋 Deskripsi Kasus

Kasus B bertujuan untuk menghitung nilai integral tentu dari suatu fungsi  pada interval  menggunakan dua metode numerik:

1. Metode Trapezoidal
2. Metode Simpson 1/3

Kasus ini digunakan untuk mengaproksimasi luas daerah di bawah kurva, terutama ketika integrasi simbolik tidak memungkinkan. Hasil dihitung berdasarkan jumlah partisi yang diberikan oleh pengguna, dan dibandingkan dengan hasil eksak bila tersedia.

### 🔬 Implementasi

🔷 1. TrapezoidalNOrder.py
```
def trapezoidal_rule(f, a, b, n)
```
Menghitung nilai integral tentu dengan pendekatan metode trapesium.

### 📘 Rumus:

![image](https://github.com/user-attachments/assets/421768a2-3548-4f51-b13e-c37691da4ead)

dengan ![image](https://github.com/user-attachments/assets/4f620bf3-c9ea-4b4c-8ff8-6120478459fc)

### 📌 Parameter:

- f: fungsi Python satu variabel

- a: batas bawah integrasi

- b: batas atas integrasi

- n: jumlah partisi (semakin besar, semakin akurat)

### ✅ Return:

Nilai pendekatan integral tentu dari f(x) pada interval [a, b].

### 📎 Contoh penggunaan:
```
from math import sin, pi
hasil = trapezoidal_rule(sin, 0, pi, 10)
print(hasil)  # Output: mendekati 2.0
```
🔷 2. simpson.py
```
def simpson_one_third(f, a, b, n)
```
Menggunakan Simpson's 1/3 Rule, dengan jumlah partisi n yang harus genap, metode ini memberikan akurasi lebih tinggi dibanding trapesium untuk fungsi halus.

### 📘 Rumus:

![image](https://github.com/user-attachments/assets/ad3875f5-dc9d-48dc-a15d-d5f5702eaafc)

### 📌 Parameter:

- f: fungsi Python satu variabel

- a: batas bawah integrasi

- b: batas atas integrasi

- n: jumlah partisi (genap)

### ✅ Return:

Hasil pendekatan integral tentu pada interval [a, b].

### 📎 Contoh penggunaan:
```
from math import exp
simpson_one_third(lambda x: exp(-x**2), 0, 1, 10)
```
🛑 Jika n ganjil, fungsi akan memunculkan error:
```
ValueError: n harus genap untuk Simpson's 1/3 rule.
```
### 🧪 Studi Kasus

Misalkan ingin menghitung:

![image](https://github.com/user-attachments/assets/05d82960-34f2-4bc2-a725-6d8ca23c59a7)

Secara analitik:

![image](https://github.com/user-attachments/assets/1c678699-a798-4e5e-a882-8a41cfb81fd9)

📎 Dengan Trapezoidal (n = 10):
```bash
Hasil pendekatan: 9.135
```
📎 Dengan Simpson 1/3 (n = 10):
```bash
Hasil pendekatan: 9.0000
```
✅ Akurasi tinggi tercapai dengan jumlah partisi yang sesuai dan metode Simpson.

### 🚀 Cara Menjalankan Kasus B

Jalankan MainCalculus.py dan pilih:
```
3. Integral - Trapezoidal Rule
4. Integral - Simpson 1/3 Rule
```
Masukkan fungsi, batas bawah a, batas atas b, dan jumlah partisi n.

### 🧠 Tujuan Analisis

- Menunjukkan efektivitas pendekatan numerik terhadap integrasi.

- Membandingkan hasil numerik dengan solusi analitik.

- Mengilustrasikan pengaruh jumlah partisi terhadap akurasi hasil.

### ✅ Keunggulan Implementasi

- Modular: Fungsi dapat digunakan terpisah untuk analisis lanjutan.

- Aman: Validasi input partisi (Simpson) mencegah kesalahan logika.

- Realis: Dapat diterapkan pada fungsi kompleks yang tidak memiliki solusi integral eksak.

- Akurat: Performa tinggi untuk fungsi kontinyu dan halus.
