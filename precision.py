import pandas as pd
from sys import argv
from math import sqrt
from predictPrice import estimatePrice

def calc_the_mse(t0, t1, mileage, price_value):
    mse = 0
    for i in range(0, len(mileage)):
        mse += (price_value[i] - estimatePrice(mileage[i], t0, t1)) ** 2
    mse = mse / len(mileage - 1)
    return mse

def calc_the_r2(t0, t1, mileage, price_value):
    mean = sum(price_value) / len(price_value - 1)
    print(mean)
    sst = 0 #sum of squares total
    ssr = 0 #sum of squares due to regression
    for i in range(0, len(mileage)):
        ssr += (estimatePrice(mileage[i], t0, t1) - mean) ** 2
        sst += (price_value[i] - mean) ** 2
    r2 = ssr / sst
    return r2


def main():
    try:
        assert len(argv) == 2, "You need to pass the path of the training file"
        df_true = pd.read_csv(argv[1])
        params = pd.read_csv("params.csv")
        #Average squared error
        mse = calc_the_mse(params.loc[:,"Theta0"].values[0], params.loc[:,"Theta1"].values[0], df_true.loc[:, "km"].values, df_true.loc[:, "price"].values)
        #average error
        rmse = sqrt(mse)
        r2 = calc_the_r2(params.loc[:,"Theta0"].values[0], params.loc[:,"Theta1"].values[0], df_true.loc[:, "km"].values, df_true.loc[:, "price"].values)
        print(f"Average squared error = {mse} \nRoot Average squared error = {rmse}\n Coefficient of determination = {r2}")


    except Exception as e:
        print(f'Error: {e}')


if __name__ == "__main__":
	main()
