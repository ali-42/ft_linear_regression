import csv

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
    data = [[],[]]
    with open('data.csv', newline='', mode='r') as csvfile:
        dataRaw = csv.reader(csvfile, delimiter=' ')
        next(dataRaw)
        for row in dataRaw:
            values = row[0].split(',')
            mileage = int(values[0])
            price = int(values[1])
            data[0].append(mileage)
            data[1].append(price)
    return data

if __name__ == "__main__":
    theta0 = 0
    theta1 = 0
    data = getData()
    minMileage = min(data[0])
    maxMileage = max(data[0])
    minPrice = min(data[1])
    maxPrice = max(data[1])
    mileages = normalizeData(data[0], minMileage, maxMileage)
    prices = normalizeData(data[1], minPrice, maxPrice)
    print(deNormalizeData(mileages, minMileage, maxMileage))
    print(deNormalizeData(prices, minPrice, maxPrice))
