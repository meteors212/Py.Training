
#-*- coding: UTF-8 -*-
import matplotlib.pyplot as plt

def scatter_test():
    #define points list
    points = [(10, 20), (25, 40), (80, 60), (60, 90), (10, 20), (80, 90), (50, 60), (30, 80)]
    x, y = zip(*points)

    plt.figure()
    plt.scatter(x, y)
    plt.show()

    return

def main():
    scatter_test()
    return

if __name__ == "__main__":
    main()