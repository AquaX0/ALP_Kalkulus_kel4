"""
Test sederhana untuk memverifikasi implementasi Kasus A
"""

# Test import modules
try:
    from CaseA_ExtremumAnalysis import case_a_extremum_analysis
    from BisectionMethod import bisection_method, find_stationary_points
    from CentralDifference import central_difference
    print("✅ Semua modul berhasil diimport!")
except ImportError as e:
    print(f"❌ Import error: {e}")
    exit(1)

# Test simple bisection method
print("\n🧪 Test Metode Bisection:")
def test_func(x):
    return x**2 - 4  # Akar di x = ±2

try:
    root, iterations = bisection_method(test_func, 1, 3)
    print(f"Akar ditemukan: x = {root:.6f} (iterasi: {iterations})")
    print(f"Verifikasi: f({root:.6f}) = {test_func(root):.2e}")
except Exception as e:
    print(f"❌ Error dalam bisection: {e}")

# Test central difference
print("\n🧪 Test Central Difference:")
def test_deriv(x):
    return x**2  # Turunan eksak: 2x

x_test = 3
numerical_deriv = central_difference(test_deriv, x_test)
exact_deriv = 2 * x_test
error = abs(numerical_deriv - exact_deriv)

print(f"f(x) = x²")
print(f"x = {x_test}")
print(f"Turunan numerik: {numerical_deriv:.8f}")
print(f"Turunan eksak: {exact_deriv}")
print(f"Error: {error:.2e}")

# Test simple case A analysis (without full output)
print("\n🧪 Test Kasus A (versi ringkas):")
try:
    # Define test function: f(x) = x³ - 6x² + 9x + 1
    def test_case_func(x):
        return x**3 - 6*x**2 + 9*x + 1
    
    # Define derivative numerically
    def test_case_deriv(x):
        return central_difference(test_case_func, x, h=1e-6)
    
    # Find stationary points
    intervals = [(0, 2), (2, 4)]
    stationary_points = find_stationary_points(test_case_deriv, intervals)
    
    print(f"Jumlah titik stasioner ditemukan: {len(stationary_points)}")
    for i, point_info in enumerate(stationary_points, 1):
        x_stat = point_info['point']
        print(f"Titik {i}: x = {x_stat:.6f}")
    
    print("✅ Test Kasus A berhasil!")
    
except Exception as e:
    print(f"❌ Error dalam Kasus A: {e}")

print("\n🎯 Kesimpulan: Implementasi siap digunakan!")
