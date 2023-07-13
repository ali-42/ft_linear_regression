import csv

def estimatePrice(kilometrage, theta0, theta1):
    return theta0 + theta1 * kilometrage

def estimateRealPrice(kilometrage, kilometrages, prices, theta0, theta1):
    kilometrage = normalizeValue(kilometrage, min(kilometrages), max(kilometrages))
    price = estimatePrice(kilometrage, theta0, theta1)
    return deNormalizeValue(price, min(prices), max(prices))


def getTheta():
    with open('theta.csv', mode='r', newline='') as csvfile:
        theta0 = theta1 = 0
        reader = csv.reader(csvfile, delimiter=' ')
        for row in reader:
            thetas = row[0].split(',')
            try:
                theta0 = float(thetas[0])
                theta1 = float(thetas[1])
            except ValueError:
                raise Exception("values are not float")
    return theta0, theta1

def getDenormalizedTheta(theta0, theta1):
    kilometrages, prices = getData()
    maxMileage = max(kilometrages)

    deNormtheta0 = estimateRealPrice(0, kilometrages, prices, theta0, theta1)
    y1 = estimateRealPrice(maxMileage, kilometrages, prices, theta0, theta1)
    deNormtheta1 = (y1 - deNormtheta0) / maxMileage

    return deNormtheta0, deNormtheta1

def deNormalizeValue(value, minValue, maxValue):
    return value * (maxValue - minValue) + minValue

def normalizeValue(value, minValue, maxValue):
    return (value - minValue) / (maxValue - minValue)

def normalizeData(dataSet, minValue, maxValue):
    normData = []
    if maxValue == minValue:
        for data in dataSet:
            normData.append(0.5)
    else:
        for data in dataSet:
            normData.append(normalizeValue(data, minValue, maxValue))
    return normData

def deNormalizeData(dataSet, minValue, maxValue):
    denormData = []
    if maxValue == minValue:
        for data in dataSet:
            denormData.append(minValue)
    else:
        for data in dataSet:
            denormData.append(deNormalizeValue(data, minValue, maxValue))
    return denormData

def getData():
    kilometrages = []
    prices = []
    with open('data.csv', newline='', mode='r') as csvfile:
        reader = csv.reader(csvfile, delimiter=' ')
        next(reader)
        for row in reader:
            values = row[0].split(',')
            try:
                kilometrages.append(int(values[0]))
                prices.append(int(values[1]))
            except ValueError:
                raise Exception("csv file not valid")
    return kilometrages, prices

def isUniform(dataSet):
    data0 = dataSet[0]
    for data in dataSet:
        if data != data0:
            return False
    return True

def getNormalizeData():
    kilometrages, prices = getData()
    if len(kilometrages) != len(prices):
        raise Exception("csv file not valid")
    if len(kilometrages) <= 1 or isUniform(kilometrages):
        raise Exception("not enough data, there must be at least data for two different kilometrages in the dataset")
    if isUniform(prices):
        raise Exception("constant price in dataset, case is trivial")
    minMileage = min(kilometrages)
    maxMileage = max(kilometrages)
    minPrice = min(prices)
    maxPrice = max(prices)
    kilometrages = normalizeData(kilometrages, minMileage, maxMileage)
    prices = normalizeData(prices, minPrice, maxPrice)
    return kilometrages, prices
