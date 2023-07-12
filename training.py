from data import getNormalizeData
import csv

LEARNING_RATE = 0.5
GENERATIONS = 300

def estimatePrice(mileage, theta0, theta1):
    return theta0 + theta1 * mileage

def trainOnce(mileages, prices, oldTheta0, oldTheta1):
    size = len(mileages)
    sum0 = sum1 = 0
    for mileage, price in zip(mileages, prices):
        sum0 += estimatePrice(mileage, oldTheta0, oldTheta1) - price
        sum1 += (estimatePrice(mileage, oldTheta0, oldTheta1) - price) * mileage
    newTheta0 = sum0 * LEARNING_RATE / size 
    newTheta1 = sum1 * LEARNING_RATE / size
    return newTheta0, newTheta1

def training():
    try:
        mileages, prices = getNormalizeData()
    except Exception as error:
        print("Exception: ", error)
        return;
    theta0 = 0;
    theta1 = 0;
    for i in range(GENERATIONS):
        newTheta0, newTheta1 = trainOnce(mileages, prices, theta0, theta1)
        print(theta0, theta1)
        theta0 = newTheta0
        theta1 = newTheta1
    with open('theta.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([theta0, theta1])

if __name__ == "__main__":
    training()
