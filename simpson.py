def simpson_one_third(f, a, b, n):
    """
    Menghitung integral tentu dari fungsi f(x) di interval [a, b]
    menggunakan metode Simpson's 1/3 Rule dengan jumlah segmen genap n.

    Parameter:
    - f : fungsi satu variabel (lambdify sympy atau lambda)
    - a : batas bawah integrasi
    - b : batas atas integrasi
    - n : jumlah segmen (harus genap)

    Return:
    - Hasil pendekatan integral tentu dari f(x) di [a, b]

    Contoh penggunaan:
    >>> from math import sin, pi
    >>> simpson_one_third(sin, 0, pi, 10)
    2.0001095173150043
    """
    if n % 2 != 0:
        raise ValueError("n harus genap untuk Simpson's 1/3 rule.")

    h = (b - a) / n
    result = f(a) + f(b)

    for i in range(1, n):
        x = a + i * h
        if i % 2 == 0:
            result += 2 * f(x)
        else:
            result += 4 * f(x)

    return (h / 3) * result
