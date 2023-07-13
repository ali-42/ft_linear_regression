from training import training, estimatePrice
from data import getTheta, getNormalizeData
import numpy as np

def accuracy(mileages, prices, theta0, theta1):
    size = len(mileages)
    mean = np.array(prices).mean()
    sumError = 0
    sumDist = 0
    for mileage, price in zip(mileages, prices):
        sumError += (estimatePrice(mileage, theta0, theta1) - price) ** 2
        sumDist += (price - mean) ** 2
    return 1 - sumError / sumDist

def checkAccuracy():
    mileages, prices = getNormalizeData()
    theta0, theta1 = getTheta()

    R2 = accuracy(mileages, prices, theta0, theta1)
    print(str(int(accuracy(mileages, prices, theta0, theta1) * 100)) + "%")

    return R2

def getBestAccuracy():
    accuracies = []
    lrs = []
    gens = []
    for generations in range(1000):
        for learning_rate in range(9):
            training((learning_rate + 1) / 10, generations)
            accuracies.append(checkAccuracy())
            lrs.append((learning_rate + 1) / 10)
            gens.append(generations)
    index = accuracies.index(max(accuracies))
    print("max accuracy is ", accuracies[index], " at learning rate of ", lrs[index], " and with ", gens[index], " generations")

if __name__ == "__main__":
    checkAccuracy()

