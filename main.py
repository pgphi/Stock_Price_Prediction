from preprocessing import extract_data, create_scatter_plot
from multipleRegression import regression_model, make_prediction

if __name__ == '__main__':
    # Create training and testing regressors and predictor arrays from columns
    df = extract_data("DataSets/NASDQ_Price_Data.csv")[0]
    X = df[["Volume", "Low", "High"]]
    x1 = df["Volume"]
    x2 = df["Low"]
    x3 = df["High"]
    y = df["Close"]

    df_train = extract_data("DataSets/NASDQ_Price_Data.csv")[1]
    X_train = df_train[["Volume", "Low", "High"]]
    print(X_train)
    y_train = df_train[["Close"]]
    print(y_train)

    df_test = extract_data("DataSets/NASDQ_Price_Data.csv")[2]
    X_test = df_test[["Volume", "Low", "High"]]
    print(X_test)
    y_test = df_test[["Close"]]
    print(y_test)

    # Create and evaluate regression Model
    regression_model(X_train, y_train, X_test, y_test)

    # Create 3D scatter plot
    create_scatter_plot("Predicting NASDAQ Closing Price",
                        "Volume",
                        "Lowest Price",
                        "Highest Price",
                        "Closing Price",
                        x1, x2, x3, y)

    # Make predictions
    print()
    print("[REGRESSOR VALUES FOR MAKING A PREDICTION]")

    make_prediction(X, y)  # Using all data available not just training data
