import math

# Pakai try except untuk hindari inputan acak dari user. Kalau inputan acak, eval akan bermasalah

def trapezoidal_n_order(f, a, b, n):
        """
        Menghitung integral numerik dengan metode Trapezoidal untuk n subinterval.
        Args:
            f (function): fungsi yang akan diintegralkan
            a (float): batas bawah
            b (float): batas atas
            n (int): jumlah subinterval (harus > 0)
        Returns:
            float: hasil integral numerik
        """
        if n <= 0:
            raise ValueError("Jumlah subinterval harus lebih dari 0")
        h = (b - a) / n
        total = f(a) + f(b)
        for i in range(1, n):
            x = a + i * h
            total += 2 * f(x)
        return (h / 2) * total
