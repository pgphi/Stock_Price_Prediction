## About the Project

    This project aims to predict the closing stock market price of the 
    US NASDAQ Stock Index based on the Open, Highest and Lowest Price in 
    one trading day. Furthermore, for convenience reasons it shows the 3 
    independent and 1 dependent variable(s) in a 3D Scatter Plot. In order 
    to visualize the 4th dimension (Highest Price) a heatmap was used:

<p align="center">
  <img src="https://github.com/pgphi/Stock_Price_Prediction/blob/main/Scatter%20Open%20Price.png" width="350" title="hover text">
  <img src="https://github.com/pgphi/Stock_Price_Prediction/blob/main/Scatter%20Open%20Price.png" width="350" alt="accessibility text">
</p>

###### Here is the Logic (Output) for making a closing price prediction:
    
    [REGRESSOR VALUES FOR MAKING A PREDICTION]
    type in the value for first regressor (Open Price in USD): 13344
    type in the value for second regressor (Lowest Price in USD): 13312    
    type in the value for third regressor (Highest Price in USD): 13583

    predicted closing price in USD is:
    [[13529.62372264]]

    Do you want to make another prediction? type 'yes' or 'no' (!case sensitive!)
    no

###### Try it out and compare it to recent closing prices of the NASDAQ Stock Index:

    For example:
    Price Data from 12-08-2022 (day-month-year):

    Actual Open Price    = 12.866,31
    Actual Highest Price = 13.047,19
    Actual Lowest Price  = 12.821,22
    Actual Closing Price = 13.047,19
    
    Predicted Closing Price = 12.992,43 (variance of 0.42%).
    
<b>Source:</b> https://www.finanzen.net/index/nasdaq_composite

###### The dataset used in this project can be found here:

https://www.kaggle.com/datasets/mattiuzc/stock-exchange-data?resource=download

    The data was collected from yahoo finance during 1971-02-05 till 2021-05-28

##### The independend variables used in this project were:
    Open = Opening Price
    (Volume) = Shares traded per day
    High = Highest price during trading day
    Low = Lowest price during trading day
    

##### The dependend variable used in this project was:
    Close = Close price adjusted for splits

### About the Model
    For predicting the closing price a multiple regression model with 3 regressors and one predictor
    was used. In order to evaluate the performance of the model training/test split of 80/20 was 
    used with a random seed of 25.

### Conditions which must be satisfied for validation and reliability for forecast model:

1. There must be a linear relationship between the outcome variable and the independent variables.
<b>Scatterplots</b> can show whether there is a linear or curvilinear relationship.

![](../../../Desktop/Bildschirmfoto 2022-08-13 um 15.18.24.png)


2. Multivariate Normality–Multiple regression assumes that the <b>residuals are normally distributed</b>.

![](../../../Desktop/Bildschirmfoto 2022-08-13 um 15.28.48.png)

3. Multiple Regression assumes that the <b>independent variables are not highly correlated</b> with each 
other. This assumption is tested using Variance Inflation Factor (VIF) values.

    
        Here the independent variables are highly correlated:
        VIF for each feautures (Open, Low and High):[18268.37360056  7584.67313824 13624.71922208]

        However Multicollinearity can be optimized by changing feautures (Open --> to Volume):
        New VIFs for each feautures (Volume, Low and High): [3.60976473e+00 6.17859750e+03 6.26088737e+03]

        Model Performance stays pretty much the same:
        coefficient of determination (model accuracy where 1 is best): 0.9999322950352939
        intercept (value when x is zero): [-0.45500212]
        slopes (increase of y when x is increasing by one unit): [[4.51323174e-10 5.62005458e-01 4.39271244e-01]]
        Mean Absolute Error (arithmetic average of errors): 9.543825927960192

        For example:
        Price Data from 12-08-2022 (day-month-year):

        Actual Volume        = 4310579000
        Actual Highest Price = 13.047,19
        Actual Lowest Price  = 12.821,22
        Actual Closing Price = 13.047,19

        Predicted Closing Price = 12.938,36 (variance of 0.84%).

![](../../../Desktop/Bildschirmfoto 2022-08-13 um 17.36.42.png)



4. Homoscedasticity–This assumption states that the variance of error terms are similar across the values of the 
independent variables.  A <b>plot of standardized residuals versus predicted values can show whether points are equally 
distributed across all values of the independent variables</b>.

![](../../../Desktop/Bildschirmfoto 2022-08-13 um 15.19.30.png)


5. Multiple linear regression requires <b>at least two independent variables</b>, which can be nominal, ordinal, 
or interval/ratio level variables.  A rule of thumb for the sample size is that regression analysis requires at least 
20 cases per independent variable in the analysis. 

    Also Check no. of feautures >= 2 (3 independent variables: Open, Lowest, Highest Price)

##### Model Performance
    
    coefficient of determination (model accuracy where 1 is best): 0.9999550474481538
    intercept (value when x is zero): [-0.28454242]
    slopes (increase of y when x is increasing by one unit): [[-0.64493405  0.77681206  0.86836385]]
    Mean Absolute Error (arithmetic average of errors): 7.041656288084994

##### General Remarks regard re-use
    
    This project can be used for other forecasting models with 3 regressors
    and one predictor as well. Just make sure to rename the scatter plot
    (and other potential variables) and preprocess the csv dataset in a proper way.

##### Outlook and further idea
    
    Collect text data of every day between 1971-02-05 till 2021-05-28 and evaluate
    sentiments with NLP (i.e. 1 - bad news | 2 - neutral news | 3 - good news) and 
    incorporate categorical data into the model for better predictions.

