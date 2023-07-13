from training import estimatePrice
import sys
from data import deNormalizeValue, getData, getDenormalizedTheta, getTheta, normalizeValue

def getInput():
    while (1):
        try:
            mileage = input("what's the mileage of the car?\n")
            mileage = float(mileage)
            if mileage < 0:
                print("You must input a positive number")
                continue
            return mileage
        except EOFError:
            print("Exit")
            sys.exit()
        except ValueError:
            print("You must input a number")

def predict():
    theta0, theta1 = getTheta()
    mileage = getInput()
    mileages, prices = getData()
    mileage = normalizeValue(mileage, min(mileages), max(mileages))
    print(mileage)
    price = estimatePrice(mileage, theta0, theta1)
    print(price)
    if price <= 0:
        print("This car is not worth selling")
    else:
        print("The estimate price is", int(deNormalizeValue(price, min(prices), max(prices))), " euros")

if __name__ == "__main__":
    predict()
