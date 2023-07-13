from data import getNormalizeData
import csv

def estimatePrice(mileage, theta0, theta1):
    return theta0 + theta1 * mileage

def trainOnce(LEARNING_RATE, mileages, prices, oldTheta0, oldTheta1):
    size = len(mileages)
    sum0 = sum1 = 0
    for mileage, price in zip(mileages, prices):
        sum0 += estimatePrice(mileage, oldTheta0, oldTheta1) - price
        sum1 += (estimatePrice(mileage, oldTheta0, oldTheta1) - price) * mileage
    delta0 = sum0 * LEARNING_RATE / size 
    delta1 = sum1 * LEARNING_RATE / size
    return oldTheta0 - delta0, oldTheta1 - delta1

def training(LEARNING_RATE, GENERATIONS):
    try:
        mileages, prices = getNormalizeData()
    except Exception as error:
        print("Exception: ", error)
        return;
    theta0 = 0.0
    theta1 = 0.0
    for i in range(GENERATIONS):
        newTheta0, newTheta1 = trainOnce(LEARNING_RATE, mileages, prices, theta0, theta1)
        theta0 = newTheta0
        theta1 = newTheta1
    with open('theta.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([theta0, theta1])

if __name__ == "__main__":
    training(0.9, 439)
