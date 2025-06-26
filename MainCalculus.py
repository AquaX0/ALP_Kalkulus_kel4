from sympy import symbols, lambdify, sympify
from ForwardDifference import forward_difference
from CentralDifference import central_difference
from TrapezoidalNOrder import trapezoidal_n_order
from simpson import simpson_one_third
from CaseA_ExtremumAnalysis import case_a_extremum_analysis
import math

x_sym = symbols('x')

def input_function():
    print("\nMasukkan fungsi f(x) (contoh: x**2 + 3*x + 2 atau sin(x))")
    print("Gunakan fungsi Python standar seperti sin, cos, exp, log, dll.")
    fungsi_input = input("f(x) = ")
    if not fungsi_input.strip():
        raise ValueError("Fungsi tidak boleh kosong.")
    
    # Parse and lambdify
    fungsi_expr = sympify(fungsi_input)
    fungsi_raw = lambdify(x_sym, fungsi_expr, modules=["math"])

    # Unit choice
    print("\nApakah Anda ingin menggunakan satuan:")
    print("1. Derajat (Degrees)")
    print("2. Radian")
    mode = input("Pilih (1/2): ")

    if mode == "1":
        print("Anda memilih DERAJAT. Semua input x, h, a, dan b akan dikonversi ke radian di dalam fungsi.")
        return lambda x: fungsi_raw(math.radians(x)), fungsi_expr, "degrees"
    elif mode == "2":
        print("Anda memilih RADIAN.")
        return fungsi_raw, fungsi_expr, "radians"
    else:
        raise ValueError("Pilihan satuan tidak valid.")

def menu():
    print("\n=== MENU METODE NUMERIK ===")
    print("1. Turunan - Forward Difference")
    print("2. Turunan - Central Difference")
    print("3. Integral - Trapezoidal Rule")
    print("4. Integral - Simpson 1/3 Rule")
    print("5. Kasus A - Titik Ekstrim Lokal")
    print("6. Keluar")
    return input("Pilih opsi (1-6): ")

while True:
    pilihan = menu()

    if pilihan == "6":
        print("Keluar dari program.")
        break

    if pilihan == "5":
        # Kasus A - Titik Ekstrim Lokal
        print("\n=== KASUS A - TITIK EKSTRIM LOKAL ===")
        print("Analisis titik ekstrim menggunakan metode bisection dan turunan numerik")
        print("Fungsi yang akan dianalisis: f(x) = x³ - 6x² + 9x + 1")
        
        konfirmasi = input("\nJalankan analisis? (y/n): ")
        if konfirmasi.lower() == 'y':
            try:
                numeric_results, exact_results = case_a_extremum_analysis()
                print("\n✅ Analisis Kasus A selesai!")
            except Exception as e:
                print(f"❌ Error saat menjalankan Kasus A: {e}")
        continue

    try:
        f, expr, unit_mode = input_function()

        if pilihan in ["1", "2"]:
            x = float(input("Masukkan nilai x: "))
            h = float(input("Masukkan nilai h: "))
            if h == 0:
                raise ValueError("h tidak boleh nol.")

            if pilihan == "1":
                result = forward_difference(f, x, h)
                method = "Forward Difference"
            else:
                result = central_difference(f, x, h)
                method = "Central Difference"

            print(f"\n=== HASIL TURUNAN ({method}) ===")
            print(f"f(x) = {expr}")
            print(f"x = {x} ({unit_mode}), h = {h}")
            print(f"Hasil turunan numerik: {result}")

        elif pilihan in ["3", "4"]:
            a = float(input("Masukkan batas bawah a: "))
            b = float(input("Masukkan batas atas b: "))
            n = int(input("Masukkan jumlah subinterval n: "))
            if n <= 0:
                raise ValueError("n harus lebih dari nol.")

            if pilihan == "3":
                result = trapezoidal_n_order(f, a, b, n)
                method = "Trapezoidal Rule"
            else:
                if n % 2 != 0:
                    raise ValueError("n harus genap untuk Simpson 1/3.")
                result = simpson_one_third(f, a, b, n)
                method = "Simpson 1/3 Rule"

            print(f"\n=== HASIL INTEGRAL ({method}) ===")
            print(f"f(x) = {expr}")
            print(f"Interval: [{a}, {b}] ({unit_mode}), n = {n}")
            print(f"Hasil integral numerik: {result}")

        else:
            print("Opsi tidak valid. Silakan pilih 1-6.")

    except Exception as e:
        print("Terjadi kesalahan:", e)
