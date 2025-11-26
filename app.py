from src.demo_data import get_demo_transactions
from src.rules import detect_duplicate_payments, detect_ghost_vendors, detect_round_figures
from src.utils import assign_risk_score, generate_report
from src.model import detect_anomalies

def main():
    print("[INFO] Loading demo transactions...")
    df = get_demo_transactions()
    
    # Apply rules
    df['duplicate'] = df.index.isin(detect_duplicate_payments(df).index)
    df['ghost_vendor'] = df.index.isin(detect_ghost_vendors(df).index)
    df['round_figure'] = df.index.isin(detect_round_figures(df).index)

    # Assign risk scores
    df = assign_risk_score(df)

    # ML anomaly detection
    anomalies = detect_anomalies(df)
    print("\n[INFO] ML Anomalies Detected:")
    print(anomalies)

    # Generate final report
    generate_report(df)

if __name__ == "__main__":
    main()
