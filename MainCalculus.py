from ForwardDifference import forward_difference
from sympy import symbols, lambdify, sympify
import math

x_sym = symbols('x')

print("Masukkan fungsi f(x) dalam format Python. Contoh: x**2 + 3*x + 2 atau sin(x)")
print("Untuk fungsi matematika seperti sin, cos, exp, gunakan nama fungsi Python (sin, cos, exp, log, dll).")

fungsi_input = input("Masukkan fungsi f(x): ")
if not fungsi_input.strip():
    print("Input fungsi tidak boleh kosong.")
    exit()

try:
    fungsi_expr = sympify(fungsi_input)
    fungsi = lambdify(x_sym, fungsi_expr, modules=["math"])
except Exception as e:
    print("Fungsi tidak valid:", e)
    exit()

try:
    x = float(input("Masukkan nilai x: "))
    h = float(input("Masukkan nilai h: "))
    if h == 0:
        print("Nilai h tidak boleh nol.")
        exit()
except Exception as e:
    print("Input angka tidak valid:", e)
    exit()

try:
    hasil = forward_difference(fungsi, x, h)
    print(f"f({x}) = {fungsi(x)}")
    print(f"f({x}+{h}) = {fungsi(x+h)}")
    print(f"Forward Difference dari f(x) = {fungsi_input} di x={x} dengan h={h} adalah {hasil}")
except Exception as e:
    print("Terjadi kesalahan saat menghitung:", e)