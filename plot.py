from data import deNormalizeValue, getData, getNormalizeData, getTheta
import matplotlib.pyplot as plt

def plot(mileages, theta0, theta1):
    mil, pri = getData()
    x = [deNormalizeValue(0, min(mil), max(mil)), deNormalizeValue(max(mileages), min(mil), max(mil))]
    y = [deNormalizeValue(theta0, min(pri), max(pri)), deNormalizeValue(theta1 * max(mileages) + theta0, min(pri), max(pri))]
    plt.plot(x, y, 'r')
    plt.scatter(mil, pri)
    plt.show()

def normPlot(mileages, prices, theta0, theta1):
    x = [0, max(mileages)]
    y = [theta0, theta1 * max(mileages) + theta0]
    plt.plot(x, y, 'r')
    plt.scatter(mileages, prices)
    plt.show()

def vizualize():
    try:
        mileages, prices = getNormalizeData()
    except Exception as error:
        print("Exception: ", error)
        return
    theta0, theta1 = getTheta()
    plot(mileages, theta0, theta1)
    normPlot(mileages, prices, theta0, theta1)

if __name__ == '__main__':
    vizualize()
