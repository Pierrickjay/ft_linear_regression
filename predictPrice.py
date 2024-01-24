import pandas as pd
import sys

def estimatePrice(mileage, t0, t1):
    return (t0 + (t1 * mileage))

def main():
    try:
        df = pd.read_csv("params.csv")
        if ('Theta0' in df.columns and 'Theta1' in df.columns and (
            not pd.isna(df['Theta0'].iloc[0]) and not pd.isna(df['Theta1'].iloc[0]))):
            theta0 = float(df['Theta0'].iloc[0])
            theta1 = float(df['Theta1'].iloc[0])
            print("theta0 and theta 1", theta0, theta1)
        else:
            print("Missing values for Theta0 or Theta1 in params.csv. Using default values.")
            theta0 = 0  # Default value for theta0
            theta1 = 0  # Default value for theta1
    except:
        theta0 = 0
        theta1 = 0
        print("linear not train, using the value 0 for theta0 and 0 for theta1")

    try:
        data1 = input("Write the mileage of the car you want to estimate the price >")
        mileage = float(data1)
        print("Estimated price for your car =", estimatePrice(mileage, theta0, theta1))

    except ValueError:
        print("Invalid input")
        sys.exit(1)

if (__name__ == "__main__"):
    main()
