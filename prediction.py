import sys
from utils import getNormalizeData, getTheta, estimateRealPrice, getData

def getInput():
    while (1):
        try:
            kilometrage = input("Input the kilometrage of the car:\n")
            kilometrage = float(kilometrage)
            if kilometrage < 0:
                print("You must input a positive number")
                continue
            return kilometrage
        except EOFError:
            print("Exit")
            sys.exit()
        except ValueError:
            print("You must input a number")


def predict():
    try:
        getNormalizeData()
    except Exception as error:
        print("Exception:", error)
        return

    theta0, theta1 = getTheta()
    if theta0 == 0 and theta1 == 0:
        print("You have to run the training first")
        return 
    kilometrage = getInput()
    kilometrages, prices = getData()
    realPrice = int(estimateRealPrice(kilometrage, kilometrages, prices, theta0, theta1))
    if realPrice <= 0:
        print("This car is not worth selling")
    else:
        print("The estimate price is", realPrice, "euros")

if __name__ == "__main__":
    predict()
