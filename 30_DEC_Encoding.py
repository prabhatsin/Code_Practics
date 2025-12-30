import numpy as np
import pandas as pd

def encodin_departments():
    departments=['Sales', 'HR', 'IT', 'Sales', 'IT', 'HR', 'Sales','Accounts'] # List defined inside the function
    array=np.array(departments*2) # Converted to numpy array
    df=pd.DataFrame(array,columns=['Department']) # Converted to dataframe 
    encoding={'Sales':0,
            'HR':1,
            'IT':2
        
            }
    # Fill unknown departments with -1 to handle unseen categories safely
    df['Department_encoded']=df['Department'].map(encoding).fillna(-1)
    return df

print(encodin_departments())





# -----------------------------------------------------------------------------------------------------------------------------------------

# Verify using sklearn

# import sklearn
# from sklearn.preprocessing import LabelEncoder
# encoder=LabelEncoder()
# # df["Department_Encoded"]=encoder.fit_transform(df['Department'])
# print(df)




'''
When to use each encoder:


Encoder	           Use case
LabelEncoder	  Target variable (y)
OrdinalEncoder	  Ordered categorical features
OneHotEncoder	  Nominal categorical features
map()	          Full control, small datasets

'''