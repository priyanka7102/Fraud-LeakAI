import pandas as pd

def assign_risk_score(df):
    """Assign a risk score 1-100 based on anomalies"""
    df = df.copy()
    df['risk_score'] = 0
    df.loc[df['duplicate'] == True, 'risk_score'] += 40
    df.loc[df['ghost_vendor'] == True, 'risk_score'] += 50
    df.loc[df['round_figure'] == True, 'risk_score'] += 20
    df['risk_score'] = df['risk_score'].clip(0, 100)
    return df

def generate_report(df, filename="fraud_report.csv"):
    df.to_csv(filename, index=False)
    print(f"[INFO] Report saved as {filename}")
