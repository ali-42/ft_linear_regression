from utils import getData, getNormalizeData, getTheta, normalizeValue, getDenormalizedTheta
import matplotlib.pyplot as plt

def plot(ax1, ax2, kilometrages, prices, normMileages, normPrices):
    theta0, theta1 = getTheta()
    deNormTheta0, deNormTheta1 = getDenormalizedTheta(theta0, theta1)

    ax1.scatter(normMileages, normPrices, label="data")
    x = [normalizeValue(-deNormTheta0 / deNormTheta1, min(kilometrages), max(kilometrages)), normalizeValue(0, min(kilometrages), max(kilometrages))]
    y = [normalizeValue(0, min(prices), max(prices)), normalizeValue(deNormTheta0, min(prices), max(prices))]
    ax1.plot(x, y, 'r', label="linear regression")
    ax1.set_title("Normalized values")
    ax1.legend()

    ax2.scatter(kilometrages, prices, label="data")
    x = [-deNormTheta0 / deNormTheta1, 0]
    y = [0, deNormTheta0]
    ax2.plot(x, y, 'r', label="linear regression")
    ax2.set_title("Denormalized values")
    ax2.legend()

def vizualize():
    theta0, theta1 = getTheta()
    if theta1 == 0 and theta0 == 0:
        print("You have to run the training first")
        return
    try:
        kilometrages, prices = getData()
        normMileages, normPrices = getNormalizeData()
    except Exception as error:
        print("Exception:", error)
        return
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 7))
    if plot(ax1, ax2, kilometrages, prices, normMileages, normPrices) == -1:
        return
    plt.show()

if __name__ == '__main__':
    vizualize()
