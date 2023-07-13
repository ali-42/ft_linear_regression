from data import getData, getDenormalizedTheta, getNormalizeData, getTheta
import matplotlib.pyplot as plt

def plot(mileages, prices, theta0, theta1):
    x = [0, max(mileages)]
    y = [theta0, theta1 * max(mileages) + theta0]
    plt.plot(x, y, 'r')
    plt.scatter(mileages, prices)
    plt.show()


def vizualize():
    try:
        mileages, prices = getData()
    except Exception as error:
        print("Exception: ", error)
        return;
    theta0, theta1 = getDenormalizedTheta()
    plot(mileages, prices, theta0, theta1)

def normVizualize():
    try:
        mileages, prices = getNormalizeData()
    except Exception as error:
        print("Exception: ", error)
        return
    theta0, theta1 = getTheta()
    plot(mileages, prices, theta0, theta1)

if __name__ == '__main__':
    vizualize()
    normVizualize()
