a = 0.0
b = 1.0
n = 3
v = 4

def get_x():
    x = []
    i = a
    while i <= b:
        x.append(i)
        i += 0.1
    return x

def get_f(x):
    fx = []
    for xi in x:
        fx.append(v * (4.0 / 3.0 * xi + 0.25 * xi * xi + 0.2 * xi * xi * xi))
    return fx

def y_exact(x):
    y = []
    for xi in x:
        y.append(v * xi)
    return y