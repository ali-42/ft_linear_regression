import csv

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

def deNormalizeValue(value, dataSet):
    maxValue = max(dataSet)
    minValue = min(dataSet)
    return (maxValue - minValue) * value + minValue

def normalizeData(dataSet, minValue, maxValue):
    normData = []
    if maxValue == minValue:
        for data in dataSet:
            normData.append(0.5)
    else:
        for data in dataSet:
            normData.append((data - minValue) / (maxValue - minValue))
    return normData

def deNormalizeData(dataSet, minValue, maxValue):
    denormData = []
    if maxValue == minValue:
        for data in dataSet:
            denormData.append(minValue)
    else:
        for data in dataSet:
            denormData.append((maxValue - minValue) * data + minValue)
    return denormData

def getData():
    mileages = []
    prices = []
    with open('data.csv', newline='', mode='r') as csvfile:
        reader = csv.reader(csvfile, delimiter=' ')
        next(reader)
        for row in reader:
            values = row[0].split(',')
            try:
                mileages.append(int(values[0]))
                prices.append(int(values[1]))
            except ValueError:
                raise Exception("some values are not numbers")
    return mileages, prices

def getNormalizeData():
    mileages, prices = getData()
    if len(mileages) != len(prices):
        raise Exception("csv file not valid")
    if len(mileages) == 0:
        raise Exception("no data")
    minMileage = min(mileages)
    maxMileage = max(mileages)
    minPrice = min(prices)
    maxPrice = max(prices)
    mileages = normalizeData(mileages, minMileage, maxMileage)
    prices = normalizeData(prices, minPrice, maxPrice)
    return mileages, prices
