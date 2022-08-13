# y = b0 + b1*x1 + b2*x2 + b3*x3 + ... + bn*xn

from sklearn.linear_model import LinearRegression
from sklearn import metrics
import matplotlib.pyplot as plt
import numpy as np
import scipy as sp


def regression_model(x_train, y_train, x_test, y_test):

    # Create a model and fit it
    model = LinearRegression().fit(x_train, y_train)

    # Get results
    r_sq = model.score(x_train, y_train)
    intercept = model.intercept_
    slopes = model.coef_
    print("[INFORMATION ABOUT THE PERFORMANCE OF MODEL]")
    print(
        f"coefficient of determination (model accuracy where 1 is best): {r_sq}")  # How much variance can be explained through model (0 nothing - 1 all)?
    print(f"intercept (value when x is zero): {intercept}")  # What is value of y, when x is zero?
    print(
        f"slopes (increase of y when x is increasing by one unit): {slopes}")  # How much is y increasing (decreasing) when unit of x is increasing (decreasing) by one?

    # 5: Test the model
    predictions = model.predict(x_test)

    # SHOW VARIANCE OF ACTUAL REGRESSAND AND PREDICTED REGRESSAND
    plt.scatter(y_test, predictions)
    plt.title("Variance of actual and predicted price")
    plt.xlabel("actual closing price")
    plt.ylabel("predicted closing price")
    plt.show()

    # CHECK CONDITION: SHOW NORMAL DISTRIBUTION OF RESIDUALS
    plt.hist(y_test - predictions)  # showing residuals: must be normally distributed
    plt.title("Difference between observed and predicted price (Residuals)")
    plt.xlabel("Price Data")
    plt.ylabel("Frequencies")
    plt.show()

    # CHECK METRICS
    MAE = metrics.mean_absolute_error(y_test, predictions)  # Mean Absolute Error (MAE)
    print(f"Mean Absolute Error (arithmetic average of errors): {MAE}")

    # DRAW ACTUAL AND PREDICTED POINTS IN PLOT
    plt.plot(predictions, y_test, '.', label='actual vs. predicted')
    plt.plot(predictions, predictions, '.', label='predicted  vs. predicted')
    plt.legend(loc='best')
    plt.show()

    # CHECK VARIANCE INFLATION FACTORS FOR EACH FEAUTURE
    ck = np.column_stack([x_train])
    cc = sp.corrcoef(ck, rowvar=False)
    VIF = np.linalg.inv(cc).diagonal()
    print(f"VIF for each feautures (Open, Low and High):{VIF}")


def make_prediction(x_train, y_train):
    model = LinearRegression().fit(x_train.values, y_train.values)
    while True:
        # 6: Make a closing price prediction

        try:
            x1 = input("type in the value for first regressor (Open Price in USD or Points): ")
            x2 = input("type in the value for second regressor (Lowest Price in USD or Points): ")
            x3 = input("type in the value for third regressor (Highest Price in USD or Points): ")
            x_new = [[int(x1), int(x2), int(x3)]]
            y_pred = model.predict(x_new)
            print()
            print(f"predicted closing price in USD is:\n{y_pred}")
            print()
            ask = input("Do you want to make another prediction? type 'yes' or 'no' (!case sensitive!)")
            if ask == "yes":
                continue
            elif ask == "no":
                break

        except ValueError:
            print("Please only type in integers i.e. 20, 150; not floats i.e. 20.30, 200.52")
