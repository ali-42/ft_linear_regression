from data import getData, getDenormalizedTheta, getNormalizeData, getTheta
import matplotlib.pyplot as plt

def vizualize():
    try:
        mileages, prices = getData()
    except Exception as error:
        print("Exception: ", error)
        return;
    theta0, theta1 = getDenormalizedTheta()
    x = [0, max(mileages)]
    y = [theta0, theta1 * max(mileages) + theta0]
    plt.plot(x, y)
    plt.scatter(mileages, prices)
    plt.show()

def normVizualize():
    try:
        mileages, prices = getNormalizeData()
    except Exception as error:
        print("Exception: ", error)
        return
    theta0, theta1 = getTheta()
    x = [0, max(mileages)]
    y = [theta0, theta1 * max(mileages) + theta0]
    plt.plot(x, y)
    plt.scatter(mileages, prices)
    plt.show()

if __name__ == '__main__':
    # vizualize()
    normVizualize()
