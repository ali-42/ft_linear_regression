from data import getData, getTheta, getNormalizeData
import matplotlib.pyplot as plt

def vizualize():
    try:
        # mileages, prices = getData()
        mileages, prices = getNormalizeData()
    except Exception as error:
        print("Exception: ", error)
        return;
    theta0, theta1 = getTheta()
    # theta0 = theta0 * max(prices)
    # theta1 = theta1 * (max(prices) / max(mileages))
    plt.plot([theta0, theta1 + theta0])
    plt.scatter(mileages, prices)
    plt.show()

if __name__ == '__main__':
    vizualize()
