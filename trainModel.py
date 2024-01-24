import sys
import csv
import matplotlib.pyplot as plt
import pandas as pd
import numpy
import statistics

def parseCsv(file_obj):
    km_list = []
    price_value = []
    reader = csv.DictReader(file_obj)
    for row in reader:
        km_list.append(int(row['km']))
        price_value.append(int(row['price']))
    return (km_list, price_value)


def change_value(data, std_dev, mean):
    for i in range(len(data)):
        data[i] = (data[i] - mean) / std_dev


def denormalise_value(data, std_dev, mean):
    for i in range(len(data)):
        data[i] = (data[i] * std_dev) + mean


def normalise_value(data):
    meanVal = statistics.mean(data)
    std_dev = numpy.std(data)
    #Formula to normalize value for a linear regression
    change_value(data, std_dev, meanVal)
    return (meanVal, std_dev)


def estimatePrice(t0, t1, mileage):
    return t0 + (t1 * mileage)


def plot_value(mileage, price, theta0, theta1):
    x = numpy.linspace(min(mileage), max(mileage), 2)
    plt.plot(mileage, price, 'o', label="Dataset")
    plt.plot(x, theta1 * x + theta0, 'r', label="Linear Regression")
    plt.xlabel('Mileage (km)')
    plt.ylabel('Price')
    plt.title('Scatter Plot of Mileage vs. Price')
    plt.legend()


def calc_the_mse(t0, t1, mileage, price_value):
    mse = 0
    for i in range(1, len(mileage)):
        mse += (price_value - estimatePrice(mileage[i], t0, t1)) ** 2
    mse = mse / len(mileage)
    return mse


def find_theta(km_list, price_value):
    """
    Function to find theta0 and t1, thanks to the model trainer
    called gradient descend
    """
    learningRate = 0.1 #also called alpha a number between 0 and 1
    totalT0 = 0
    totalT1 = 0
    tmpT0 = 0
    tmpT1 = 0
    listOfTmpT0 = []
    listOfTmpT1 = []
    for _ in range(100): #500 was too high, 100 was the the one doing less iteration and being the closestt to the final result
        totalT0 = 0
        totalT1 = 0
        for i in range(len(km_list) - 1):
            totalT0 += estimatePrice(tmpT0, tmpT1, km_list[i]) - price_value[i]
            totalT1 += (estimatePrice(tmpT0, tmpT1, km_list[i]) - price_value[i]) * km_list[i]
        tmpT0 -= totalT0 * (1 / len(km_list)) * learningRate
        tmpT1 -= totalT1 * (1 / len(km_list)) * learningRate
        listOfTmpT0.append(tmpT0)
        listOfTmpT1.append(tmpT1)
    return tmpT0, tmpT1


def create_file(t0, t1):
    data = {
        'Theta0': [t0],
        'Theta1': [t1],
        # Add more columns as needed
    }
    df = pd.DataFrame(data)
    df.to_csv("params.csv", index=False)

def main():
    try:
        f = open(sys.argv[1])
        km_list = []
        price_value = []
        km_list, price_value= parseCsv(f)
        meanVal, std= normalise_value(km_list)
        t0, t1 = find_theta(km_list, price_value)
        t0 = t0 - (t1 * meanVal / std) #denornalize thetas
        t1 = t1 / std
        print("theta 0 found = ", t0," \ntheta 1 found =", t1)
        denormalise_value(km_list, std, meanVal) # denornalize km_list
        create_file(t0, t1)
        plot_value(km_list, price_value, t0, t1)
        plt.show()
    except:
        print("Couldn't open file")

if (__name__ == "__main__"):
    main()
