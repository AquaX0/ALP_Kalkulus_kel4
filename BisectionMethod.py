"""
Implementasi Metode Bisection untuk Mencari Akar Fungsi
Digunakan untuk mencari titik stasioner (akar dari turunan)
"""

def bisection_method(f, a, b, tolerance=1e-6, max_iterations=100):
    """
    Mencari akar fungsi menggunakan metode bisection
    
    Parameters:
    f: fungsi yang akan dicari akarnya
    a: batas kiri interval
    b: batas kanan interval  
    tolerance: toleransi error (default 1e-6)
    max_iterations: maksimum iterasi (default 100)
    
    Returns:
    root: nilai akar fungsi
    iterations: jumlah iterasi yang digunakan
    """
    
    # Validasi bahwa f(a) dan f(b) memiliki tanda berbeda
    if f(a) * f(b) >= 0:
        raise ValueError("f(a) dan f(b) harus memiliki tanda yang berbeda")
    
    iteration = 0
    
    while iteration < max_iterations:
        # Hitung titik tengah
        c = (a + b) / 2
        
        # Cek apakah sudah mencapai toleransi
        if abs(f(c)) < tolerance or abs(b - a) / 2 < tolerance:
            return c, iteration + 1
        
        # Tentukan interval baru
        if f(c) * f(a) < 0:
            b = c
        else:
            a = c
            
        iteration += 1
    
    # Jika tidak konvergen dalam max_iterations
    return (a + b) / 2, iteration


def find_stationary_points(derivative_func, intervals, tolerance=1e-6):
    """
    Mencari titik-titik stasioner (akar dari turunan) dalam beberapa interval
    
    Parameters:
    derivative_func: fungsi turunan
    intervals: list of tuples (a, b) yang merepresentasikan interval pencarian
    tolerance: toleransi error
    
    Returns:
    stationary_points: list titik-titik stasioner yang ditemukan
    """
    stationary_points = []
    
    for a, b in intervals:
        try:
            # Cek apakah ada perubahan tanda dalam interval
            if derivative_func(a) * derivative_func(b) < 0:
                root, iterations = bisection_method(derivative_func, a, b, tolerance)
                stationary_points.append({
                    'point': root,
                    'iterations': iterations,
                    'interval': (a, b)
                })
        except ValueError:
            # Tidak ada akar dalam interval ini
            continue
    
    return stationary_points
