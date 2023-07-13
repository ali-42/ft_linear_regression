from training import training
from utils import getTheta, getNormalizeData, estimatePrice
import numpy as np

def squareResiduals(kilometrages, prices, theta0, theta1):
    sumSquares = 0
    for kilometrage, price in zip(kilometrages, prices):
        sumSquares += (estimatePrice(kilometrage, theta0, theta1) - price) ** 2
    return sumSquares

def accuracy(kilometrages, prices, theta0, theta1):
    mean = np.array(prices).mean()
    sumError = 0
    sumDist = 0
    for kilometrage, price in zip(kilometrages, prices):
        sumError += (estimatePrice(kilometrage, theta0, theta1) - price) ** 2
        sumDist += (price - mean) ** 2
    return 1 - sumError / sumDist

def checkAccuracy():
    theta0, theta1 = getTheta()
    if theta0 == 0 and theta1 == 0:
        print("You have to run the training first")
        return
    try:
        kilometrages, prices = getNormalizeData()
    except Exception as error:
        print("Exception:", error)
        return;

    R2 = accuracy(kilometrages, prices, theta0, theta1)
    print("accuracy of this model: " + str(int(accuracy(kilometrages, prices, theta0, theta1) * 100)) + "%")

    return R2

def minimizeError():
    try:
        kilometrages, prices = getNormalizeData()
    except Exception as error:
        print("Exception:", error)
        return;

    errors = []
    lrs = []
    gens = []
    for learning_rate in range(9):
        for i in range(1000):
            training((learning_rate + 1) / 10, i)
            theta0, theta1 = getTheta()
            errors.append(squareResiduals(kilometrages, prices, theta0, theta1))
            lrs.append((learning_rate + 1) / 10)
            gens.append(i)
    index = errors.index(min(errors))
    print("minimizing errors at learning rate of", lrs[index], " and with", gens[index], " generations")

if __name__ == "__main__":
    # use this to get appropriate training parameters :
    # minimizeError()
    checkAccuracy()
