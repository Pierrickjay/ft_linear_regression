import matplotlib.pyplot as plt
from sys import argv
import pandas as pd
import numpy as np

def plot_only_point(km_list, price_value):
    plt.scatter(km_list, price_value, color='blue', marker='o', label='Data Points')
    plt.xlabel('Mileage (km)')
    plt.ylabel('Price')
    plt.title('Scatter Plot of Mileage vs. Price')
    plt.legend()
    # ax.plot([1, 2, 3, 4], [1, 4, 2, 3])
    plt.show()

def plot_value(mileage, price, theta0, theta1):
    x = np.linspace(min(mileage), max(mileage), 2)
    plt.plot(mileage, price, 'o', label="Dataset")
    plt.plot(x, theta1 * x + theta0, 'r', label="Linear Regression")
    plt.xlabel('Mileage (km)')
    plt.ylabel('Price')
    plt.title('Scatter Plot of Mileage vs. Price')
    plt.legend()
    plt.show()

def main():
    try:
        assert len(argv) == 2, "You need to pass the path of the training file"
        df_true = pd.read_csv(argv[1])
        plot_only_point(df_true.loc[:, "km"].values, df_true.loc[:, "price"].values)
        params = pd.read_csv("params.csv")
        #Average squared error
        plot_value(df_true.loc[:, "km"].values, df_true.loc[:, "price"].values,params.loc[:,"Theta0"].values[0], params.loc[:,"Theta1"].values[0])
    except Exception as e:
        print(f'Error: {e}')

if (__name__ == "__main__"):
    main()


