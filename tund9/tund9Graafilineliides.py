import numpy as np  #������ �������� �������� x=[min,max]
import matplotlib.pyplot as plt

def vaal(color:str):
    x1 = np.arange(0,10,1) # 0,1,2,3,4,5,6,7,8,9
    y1 = (2/27)*x1**2 - 3

    x2 = np.arange(-10, 0.5, 0.5) # min, max + step, step
    y2 = 0.04*x2**2 - 3

    x3 = np.arange(-9, -2.5, 0.5)
    y3 = (2/9)*(x3+6)**2 + 1

    x4 = np.arange(-3, 9.5, 0.5) # min max step
    y4 = (-1/12)*(x4-3)**2 + 6

    x5 = np.arange(5, 9, 0.5) # min max step
    y5 = (1/9)*(x5-5)**2 + 2

    x6 = np.arange(5, 8.5, 0.5) # min max step
    y6 = (1/8)*(x6-7)**2 + 1.5

    x7 = np.arange(-13, -8.5, 0.5) # min max step
    y7 = (-0.75)*(x7+11)**2 + 6

    x8 = np.arange(-15, -12.5, 0.5) # min max step
    y8 = (-0.5)*(x8+13)**2 + 3

    x9 = np.arange(-15, -10, 0.5) # min max step
    y9 = [1]*len(x9)

    x10 = np.arange(3, 4, 0.5) # min max step
    y10 = [3]*len(x10)

    plt.figure(facecolor="lightgreen")
    plt.title("Vaal")
    plt.ylabel("Y")
    plt.xlabel("X")
    plt.grid(True)
    ax=plt.axes()
    ax.set_facecolor("Lightblue")
    colors=["c" , "m" , "y" , "r" , "g" , "b", "w", "k", "k", "k"]
    for i in range(1, 11): 
        plt.plot(eval(f"x{i}"), eval(f"y{i}"),color[0]+"-*")  #b-* ���� ����� ����� � ������ colors[i-1]+"-*"
    plt.show()  


# vaal()

def Liblikas(color:str):
    x1=np.arange(-9,-0.5,0.5)    # min, max+step, step
    y1=(-1/8)*(x1+9)**2+8

    x2=np.arange(1,9.5,0.5)
    y2=(-1/8)*(x2-9)**2+8

    x3=np.arange(-9,-7.5,0.5)
    y3=7*(x3+8)**2+1

    x4=np.arange(8,9.5,0.5)
    y4=7*(x4-8)**2+1

    x5=np.arange(-8,-0.5,0.5)
    y5=(1/49)*(x5+1)**2

    x6=np.arange(1,8.5,0.5)
    y6=(1/49)*(x6-1)**2

    x7=np.arange(-8,-0.5,0.5)
    y7=(-4/49)*(x7+1)**2

    x8=np.arange(1,8.5,0.5)
    y8=(-4/49)*(x8-1)**2

    x9=np.arange(-8,-1.5,0.5)
    y9=(1/3)*(x9+5)**2-7

    x10=np.arange(2,8.5,0.5)
    y10=(1/3)*(x10-5)**2-7

    x11=np.arange(-2,-0.5,0.5)
    y11=-2*(x11+1)**2-2

    x12=np.arange(1,2.5,0.5)
    y12=-2*(x12-1)**2-2

    x13=np.arange(-1,1.5,0.5)
    y13=-4*x13**2+2

    x14=np.arange(-1,1.5,0.5)
    y14=4*x14**2-6

    x15=np.arange(-2,0.5,0.5)
    y15=-1.5*x15+2

    x16=np.arange(0,2.5,0.5)
    y16=1.5*x16+2

    plt.figure(facecolor="cyan")
    plt.title("Liblikas")
    plt.ylabel("Y")
    plt.xlabel("X")
    plt.grid(True)
    ax=plt.axes()
    ax.set_facecolor("lightyellow")
    #colors=["c","m","y","r","g","b","k","k","c","m","y","r","g","b","k","k"]
    for i in range(1,17):
        plt.plot(eval(f"x{i}"),eval(f"y{i}"),color[0]+"-*")
    plt.show()


def Vihmavari():
    pass