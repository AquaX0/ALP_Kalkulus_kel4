def forward_difference(f, x, h=1e-5):
    """
    Menghitung Forward Difference dari fungsi f di titik x dengan step size h.
    
    Args:
        f (function): Fungsi yang akan dihitung turunan numeriknya.
        x (float): Titik di mana turunan dihitung.
        h (float, optional): Step size. Default 1e-5.
    
    Returns:
        float: Nilai Forward Difference di titik x.
    """
    return (f(x + h) - f(x)) / h