import pandas as pd

def preprocess(df):
    # Dropping any duplicates
    df.drop_duplicates(inplace=True)
    df['Year']=df['Year'].astype(str)
    return df
