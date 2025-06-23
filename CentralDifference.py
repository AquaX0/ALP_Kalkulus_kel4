def central_difference(f, x, h=1e-5):
    """
    Menghitung turunan numerik f'(x) menggunakan metode Central Difference.
    
    Parameter:
    - f: fungsi yang akan diturunkan (callable)
    - x: titik di mana turunan dihitung (float)
    - h: langkah (step size) untuk pendekatan (default: 1e-5)

    Return:
    - Nilai pendekatan dari turunan pertama f'(x)

    Contoh penggunaan:
    >>> def f(x):
    ...     return x**2
    >>> central_difference(f, 2)
    4.000000000026205
    """
    return (f(x + h) - f(x - h)) / (2 * h)
