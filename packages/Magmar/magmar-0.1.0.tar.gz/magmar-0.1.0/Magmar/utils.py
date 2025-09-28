def MegaImputer(df, target_col=None):
    import lightgbm as lgb
    from tqdm import tqdm 
    import numpy as np
    import pandas as pd
    from sklearn.impute import SimpleImputer
   
    imputer = SimpleImputer(strategy = "mean")
    
    df.isnull().sum()
    if target_col:
        dt = df.drop(columns = [target_col])

    else:
        dt = df

    data = dt
    dtype_lst = []
    for i in range(len(data.dtypes)):
        if (data.dtypes[i]== "object"):
            dtype_lst.append("o")
        else:
            dtype_lst.append("n")

    data_imp = imputer.fit_transform(data)
    data_imp = pd.DataFrame(data_imp)
    data = data.to_numpy()
    data = pd.DataFrame(data)
    
    data_cl = data.dropna()
    
    data_imp

    for i in tqdm(range(len(dtype_lst))):
        if data.iloc[:,i].isnull().sum() > 0:
                
            X1 = data_cl.iloc[: , :i]
            X2 = data_cl.iloc[: , i+1:]
            Y = data_cl.iloc[:,i]
            X = pd.concat([X1,X2], axis = 1)

            if (dtype_lst[i]=="n"):
                model = lgb.LGBMRegressor()
            else:
                model = lgb.LGBMClassifier()

            X = X.astype(int)
            Y = Y.astype(int)
            model.fit(X,Y)
            missing_index = []
            for j in range(len(data)):
                
                if (data.iloc[:,i].isnull()[j] == True):
                    missing_index.append(j)

            
            furry1 = data_imp.iloc[missing_index,:i]
            furry2 = data_imp.iloc[missing_index,i+1:]
            furry = pd.concat([furry1,furry2], axis = 1)
            prediction = model.predict(furry)
            
            for f in tqdm(range(len(missing_index))):
                index = missing_index[f]
                data.iloc[:,i][index] = prediction[f]
                
        else:
            continue

    
    if target_col:
        data.columns = dt.columns
        return pd.concat([data,df[target_col]],axis =1)

    else:
        data.columns = dt.columns
        return data
    
