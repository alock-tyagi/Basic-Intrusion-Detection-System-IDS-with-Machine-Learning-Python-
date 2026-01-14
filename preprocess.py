import pandas as pd
from sklearn.preprocessing import StandardScaler

def preprocess():
    df = pd.read_csv("data/processed/dataset.csv")
    df = df.drop(["src_ip", "dst_ip"], axis=1)

    scaler = StandardScaler()
    X = scaler.fit_transform(df)

    return X

