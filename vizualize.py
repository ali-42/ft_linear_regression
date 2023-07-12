from data import getNormalizeData, getTheta
import matplotlib.pyplot as plt

def vizualize():
    try:
        mileages, prices = getNormalizeData()
    except Exception as error:
        print("Exception: ", error)
        return;
    theta0, theta1 = getTheta()
    plt.plot([theta0, theta1 + theta0])
    plt.scatter(mileages, prices)
    plt.show()

if __name__ == '__main__':
    vizualize()
