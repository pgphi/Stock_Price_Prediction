#### ValueError: Found array with dim 3. LinearRegression expected <= 2.
    Solution: 
    x = np.array([x1, x2, x3]) # use np.array for shaping
    d2_x = x_test.reshape(-1, 2)  # reduce 3D to 2D

    First dimension is maintained and the other two dimensions are flattened (so 28x28 becomes 784). 
    The fit algorithm will next consider the first 784 features part of sample number one and the next 
    784 features part of sample two and so on.

#### AttributeError: 'list' object has no attribute 'shape'
    Solution:
    change "x = [[x1, x2, x3]]"
    to "x = np.array([[x1, x2, x3]])"

### Main Solution for errors above:
    Just integrate all feautures (High, Low, Open) into one dataframe by using pandas
   
    i.e.:       
    df_train = extract_data("DataSets/NASDQ_Price_Data.csv")[1]
    X_train = df_train[["Open", "Low", "High"]]