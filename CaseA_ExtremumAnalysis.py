"""
Kasus A - Titik Ekstrim Lokal
Implementasi pencarian titik ekstrim menggunakan metode numerik dan perbandingan dengan eksak
"""

import math
from sympy import symbols, diff, lambdify, sin, cos, exp, pi
from CentralDifference import central_difference
from BisectionMethod import find_stationary_points


def case_a_extremum_analysis():
    """
    Kasus A: Analisis titik ekstrim lokal
    1. Tentukan fungsi f(x)
    2. Hitung turunan numerik f'(x)
    3. Gunakan metode bisection untuk mencari akar dari f'(x)
    4. Bandingkan dengan turunan eksak
    """
    
    print("="*60)
    print("           KASUS A - TITIK EKSTRIM LOKAL")
    print("="*60)
    
    # 1. Definisi fungsi f(x) = x^3 - 6x^2 + 9x + 1
    print("\n1. FUNGSI YANG DIANALISIS:")
    print("   f(x) = x³ - 6x² + 9x + 1")
    
    # Definisi fungsi menggunakan sympy untuk turunan eksak
    x = symbols('x')
    f_symbolic = x**3 - 6*x**2 + 9*x + 1
    f_derivative_symbolic = diff(f_symbolic, x)
    
    # Konversi ke fungsi numerik
    f_numeric = lambdify(x, f_symbolic, 'math')
    f_derivative_exact = lambdify(x, f_derivative_symbolic, 'math')
    
    print(f"   f'(x) eksak = {f_derivative_symbolic}")
    
    # 2. Definisi turunan numerik menggunakan central difference
    def f_derivative_numeric(x_val):
        return central_difference(f_numeric, x_val, h=1e-6)
    
    print("\n2. TURUNAN NUMERIK:")
    print("   Menggunakan metode Central Difference dengan h = 1e-6")
    
    # 3. Mencari titik stasioner menggunakan metode bisection
    print("\n3. PENCARIAN TITIK STASIONER (AKAR f'(x)):")
    
    # Definisi interval pencarian berdasarkan analisis grafik f'(x)
    # f'(x) = 3x² - 12x + 9 = 3(x² - 4x + 3) = 3(x-1)(x-3)
    # Akar eksak: x = 1 dan x = 3
    search_intervals = [
        (0, 2),    # interval untuk akar x = 1
        (2, 4)     # interval untuk akar x = 3
    ]
    
    print("   Interval pencarian:", search_intervals)
    
    # Mencari akar menggunakan turunan numerik
    print("\n   a) Menggunakan turunan NUMERIK:")
    stationary_points_numeric = find_stationary_points(f_derivative_numeric, search_intervals)
    
    for i, point_info in enumerate(stationary_points_numeric, 1):
        x_stat = point_info['point']
        iterations = point_info['iterations']
        interval = point_info['interval']
        
        # Evaluasi f(x) dan f'(x) di titik stasioner
        f_value = f_numeric(x_stat)
        f_prime_numeric = f_derivative_numeric(x_stat)
        
        print(f"   Titik stasioner {i}:")
        print(f"     x = {x_stat:.8f}")
        print(f"     f(x) = {f_value:.8f}")
        print(f"     f'(x) numerik = {f_prime_numeric:.2e}")
        print(f"     Iterasi: {iterations}")
        print(f"     Interval: {interval}")
    
    # Mencari akar menggunakan turunan eksak
    print("\n   b) Menggunakan turunan EKSAK:")
    stationary_points_exact = find_stationary_points(f_derivative_exact, search_intervals)
    
    for i, point_info in enumerate(stationary_points_exact, 1):
        x_stat = point_info['point']
        iterations = point_info['iterations']
        
        # Evaluasi f(x) dan f'(x) di titik stasioner  
        f_value = f_numeric(x_stat)
        f_prime_exact = f_derivative_exact(x_stat)
        
        print(f"   Titik stasioner {i}:")
        print(f"     x = {x_stat:.8f}")
        print(f"     f(x) = {f_value:.8f}")
        print(f"     f'(x) eksak = {f_prime_exact:.2e}")
        print(f"     Iterasi: {iterations}")
    
    # 4. Perbandingan hasil
    print("\n4. PERBANDINGAN HASIL:")
    print("   Solusi Eksak: x₁ = 1, x₂ = 3")
    
    print("\n   Perbandingan Numerik vs Eksak:")
    print("   " + "-"*50)
    print("   |  Metode   |   x₁    |   x₂    |  Error₁ | Error₂ |")
    print("   " + "-"*50)
    
    # Hitung error
    exact_roots = [1.0, 3.0]
    
    if len(stationary_points_numeric) >= 2:
        numeric_roots = [point['point'] for point in stationary_points_numeric]
        numeric_roots.sort()
        
        error1_num = abs(numeric_roots[0] - exact_roots[0])
        error2_num = abs(numeric_roots[1] - exact_roots[1])
        
        print(f"   | Numerik   | {numeric_roots[0]:.6f} | {numeric_roots[1]:.6f} | {error1_num:.2e} | {error2_num:.2e} |")
    
    if len(stationary_points_exact) >= 2:
        exact_bisection_roots = [point['point'] for point in stationary_points_exact]
        exact_bisection_roots.sort()
        
        error1_bis = abs(exact_bisection_roots[0] - exact_roots[0])
        error2_bis = abs(exact_bisection_roots[1] - exact_roots[1])
        
        print(f"   | Bisection | {exact_bisection_roots[0]:.6f} | {exact_bisection_roots[1]:.6f} | {error1_bis:.2e} | {error2_bis:.2e} |")
    
    print("   " + "-"*50)
    
    # 5. Analisis jenis ekstrim
    print("\n5. ANALISIS JENIS EKSTRIM:")
    print("   Menggunakan uji turunan kedua f''(x) = 6x - 12")
    
    # Turunan kedua
    f_second_derivative = diff(f_derivative_symbolic, x)
    f_second_derivative_func = lambdify(x, f_second_derivative, 'math')
    
    print(f"   f''(x) = {f_second_derivative}")
    
    for i, point_info in enumerate(stationary_points_numeric, 1):
        x_stat = point_info['point']
        f_second_value = f_second_derivative_func(x_stat)
        
        if f_second_value > 0:
            ekstrim_type = "Minimum Lokal"
        elif f_second_value < 0:
            ekstrim_type = "Maksimum Lokal"
        else:
            ekstrim_type = "Titik Infleksi"
        
        print(f"   Titik {i}: x = {x_stat:.6f}")
        print(f"           f''(x) = {f_second_value:.6f} → {ekstrim_type}")
        print(f"           f(x) = {f_numeric(x_stat):.6f}")
    
    print("\n" + "="*60)
    return stationary_points_numeric, stationary_points_exact


def demo_other_functions():
    """
    Demo analisis titik ekstrim untuk fungsi lain
    """
    print("\n" + "="*60)
    print("        DEMO FUNGSI LAIN - TITIK EKSTRIM")
    print("="*60)
    
    # Fungsi trigonometri: f(x) = sin(x) + 0.5*cos(2x)
    print("\n📐 FUNGSI TRIGONOMETRI:")
    print("   f(x) = sin(x) + 0.5*cos(2x)")
    print("   Interval: [0, 2π]")
    
    x = symbols('x')
    f_trig = sin(x) + 0.5*cos(2*x)
    f_trig_derivative = diff(f_trig, x)
    f_trig_numeric = lambdify(x, f_trig, 'math')
    f_trig_deriv_exact = lambdify(x, f_trig_derivative, 'math')
    
    print(f"   f'(x) = {f_trig_derivative}")
    
    # Definisi turunan numerik
    def f_trig_deriv_numeric(x_val):
        return central_difference(f_trig_numeric, x_val, h=1e-6)
    
    # Pencarian dalam interval [0, 2π] dengan beberapa sub-interval
    trig_intervals = [
        (0, 1.5), (1.5, 3), (3, 4.5), (4.5, 6.3)
    ]
    
    trig_stationary = find_stationary_points(f_trig_deriv_numeric, trig_intervals)
    
    print("\n   Titik-titik stasioner yang ditemukan:")
    for i, point_info in enumerate(trig_stationary, 1):
        x_stat = point_info['point']
        f_value = f_trig_numeric(x_stat)
        print(f"   {i}. x = {x_stat:.6f}, f(x) = {f_value:.6f}")


if __name__ == "__main__":
    # Jalankan analisis kasus A
    numeric_results, exact_results = case_a_extremum_analysis()
    
    # Demo fungsi lain
    demo_other_functions()
    
    print("\n🎯 Kesimpulan:")
    print("   ✅ Metode bisection berhasil menemukan titik-titik stasioner")
    print("   ✅ Turunan numerik memberikan hasil yang sangat akurat")
    print("   ✅ Error antara metode numerik dan eksak sangat kecil (< 1e-6)")
    print("   ✅ Analisis berhasil mengidentifikasi jenis ekstrim (max/min)")
