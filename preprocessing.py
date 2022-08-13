# Preprocess csv file with n columns and n rows
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


# Extract regressors and predictor from csv file

def extract_data(csv_dataset):
    """
    :param csv_dataset: csv_dataset (relative path)
    :return: list of arrays [dataset-, training- and test-array].
    """

    df = pd.read_csv(csv_dataset)  # "DataSets/NASDQ_Price_Data.csv"
    # print(df)

    training_data = df.sample(frac=0.8, random_state=25)
    testing_data = df.drop(training_data.index)

    # print(f"No. of training examples: {training_data.shape[0]}")
    # print(f"No. of testing examples: {testing_data.shape[0]}")

    return [df, training_data, testing_data]


# Visualize Data
def create_scatter_plot(title, x1label, x2label, x3label, ylabel,
                        x1, x2, x3, y):
    fig = plt.figure(figsize=(9, 9))
    ax = fig.add_subplot(111, projection="3d")

    ax.set_title(title)
    ax.set_xlabel(x1label + " (x1)")
    ax.set_zlabel(x2label + " (z or x2)")
    ax.set_ylabel(ylabel + " (y)")

    img = ax.scatter(x1, y, x2, c=x3, cmap=plt.hot())  # takes x, y, z and c
    clb = fig.colorbar(img)
    clb.ax.set_title(x3label + " (x3)")
    plt.show()
    scatter_plot = fig.savefig(title + ".png", dpi=1000)

    return scatter_plot


"""
[OUTPUT]
      Index        Date          Open  ...         Close     Adj Close      Volume
0      IXIC  1971-02-05    100.000000  ...    100.000000    100.000000           0
1      IXIC  1971-02-08    100.839996  ...    100.839996    100.839996           0
2      IXIC  1971-02-09    100.760002  ...    100.760002    100.760002           0
3      IXIC  1971-02-10    100.690002  ...    100.690002    100.690002           0
4      IXIC  1971-02-11    101.449997  ...    101.449997    101.449997           0
...     ...         ...           ...  ...           ...           ...         ...
12685  IXIC  2021-05-24  13557.209960  ...  13661.169920  13661.169920  3490650000
12686  IXIC  2021-05-25  13721.540040  ...  13657.169920  13657.169920  4084480000
12687  IXIC  2021-05-26  13693.940430  ...  13738.000000  13738.000000  4231140000
12688  IXIC  2021-05-27  13742.589840  ...  13736.280270  13736.280270  5057550000
12689  IXIC  2021-05-28  13792.049810  ...  13748.740230  13748.740230  4435220000

[12690 rows x 8 columns]
No. of training examples: 10152
No. of testing examples: 2538
"""
