from data import getData, getTheta, deNormalizeValue
import matplotlib.pyplot as plt

def vizualize():
    try:
        mileages, prices = getData()
    except Exception as error:
        print("Exception: ", error)
        return;
    theta0, theta1 = getTheta()
    theta0 = deNormalizeValue(theta0, prices)
    theta1 = deNormalizeValue(theta1, prices)
    print(theta0)
    plt.plot([theta0, theta1 + theta0])
    plt.scatter(mileages, prices)
    plt.show()

if __name__ == '__main__':
    vizualize()
