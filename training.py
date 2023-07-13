from utils import getDenormalizedTheta, getNormalizeData, estimatePrice
import csv

def trainOnce(LEARNING_RATE, kilometrages, prices, oldTheta0, oldTheta1):
    size = len(kilometrages)
    sum0 = sum1 = 0
    for kilometrage, price in zip(kilometrages, prices):
        sum0 += estimatePrice(kilometrage, oldTheta0, oldTheta1) - price
        sum1 += (estimatePrice(kilometrage, oldTheta0, oldTheta1) - price) * kilometrage
    step0 = sum0 * LEARNING_RATE / size 
    step1 = sum1 * LEARNING_RATE / size
    return step0, step1

def training(LEARNING_RATE, GENERATIONS):
    try:
        kilometrages, prices = getNormalizeData()
    except Exception as error:
        print("Exception:", error)
        return;
    theta0 = 0.0
    theta1 = 0.0
    for i in range(GENERATIONS):
        step0, step1 = trainOnce(LEARNING_RATE, kilometrages, prices, theta0, theta1)
        theta0 = theta0 - step0
        theta1 = theta1 - step1
    with open('theta.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([theta0, theta1])

    print("Training results:")
    print("-------------------------------------------------")
    print("Normalized values: theta0 =", theta0, ", theta1 =", theta1)
    deNormTheta0, deNormTheta1 = getDenormalizedTheta(theta0, theta1)
    print("Denormalized values: theta0 =", deNormTheta0, ", theta1 =", deNormTheta1)

if __name__ == "__main__":
    # Run minimizeError in module accuracy to get the best parameters
    training(0.5, 963)
