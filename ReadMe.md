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
 ┣ 📜 Trapezoidal.py              ← Implementasi metode Trapezoidal
 ┣ 📜 SimpsonOneThird.py          ← Implementasi metode Simpson's 1/3
 ┣ 📜 main.py                     ← Menu utama CLI interaktif
 ┣ 📜 README.md                   ← Dokumentasi proyek
 ┗ 📜 requirements.txt            ← (Opsional) Daftar dependensi
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
python main.py
```

Program akan menampilkan menu:

```
=== MENU METODE NUMERIK ===
1. Turunan - Forward Difference
2. Turunan - Central Difference
3. Integral - Trapezoidal Rule
4. Integral - Simpson 1/3 Rule
5. Keluar
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
