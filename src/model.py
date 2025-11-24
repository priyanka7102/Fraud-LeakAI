from sklearn.ensemble import IsolationForest

def detect_anomalies(df):
    model = IsolationForest(contamination=0.1, random_state=42)
    df_model = df[['amount']]  # Use amount as a simple feature
    df['anomaly'] = model.fit_predict(df_model)
    df['anomaly'] = df['anomaly'].apply(lambda x: True if x == -1 else False)
    return df[df['anomaly'] == True]
