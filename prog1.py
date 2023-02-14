from sys import exit
from prog2 import prog2, estimate 

def get_params():
    try:
        f = open("params.txt", "r")
        return (float(f.readline()), float(f.readline()))
    except:
        print ("Params not found !\nLunch: python3 prog2.py")
        exit (1)

def prog1():
    val = input ("Get a mileage : ")
    if (val.isnumeric() == False) :
        print ("It is not a number !")
    (t0, t1) = get_params()
    print("Estimation price : ", round(estimate((t0, t1), float(val)), 4))
if __name__ == "__main__":
    prog1()
