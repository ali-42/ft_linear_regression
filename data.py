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

def getDenormalizedTheta():
    mileages, prices = getData()
    maxMileage = max(mileages)
    minMileage = min(mileages)
    maxPrice = max(prices)
    minPrice = min(prices)
    theta0, theta1 = getTheta()

    deNormTheta0 = deNormalizeValue(theta0, minPrice, maxPrice)
    y0 = deNormTheta0
    x0 = deNormalizeValue(0, minMileage, maxMileage)
    y1 = deNormalizeValue(theta0 + theta1, minPrice, maxPrice)
    x1 = deNormalizeValue(1, minMileage, maxMileage)
    deNormTheta1 = (y1 - y0) / (x1 - x0)

    return deNormTheta0, deNormTheta1

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

if __name__ == "__main__":
    mileages, prices = getData()
    normMileages, normPrices = getNormalizeData()
    print("data = ", mileages, prices)
    print()
    print("normalized data = ", normMileages, normPrices)
    print()
    print("denormalized mileages = ", deNormalizeData(normMileages, min(mileages), max(mileages)))
    print()
    print("denormalized prices = ", deNormalizeData(normPrices, min(prices), max(prices)))
