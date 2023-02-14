import statistics
from prog1 import get_params
from prog2 import load_data, estimate
from matplotlib import pyplot as plt

def prog3():
    (x,y) = load_data()
    (t0, t1) = get_params()
    tx = [i / 10 for i in range (1, max(x) * 10)]
    ty = [estimate((t0, t1), i) for i in tx]
    plt.figure()
    plt.title("data")
    plt.xlabel("mileage")
    plt.ylabel("price")
    plt.scatter(statistics.mean(x),statistics.mean(y))
    plt.scatter(x,y)
    plt.plot(tx, ty)
    plt.show()
prog3()  
