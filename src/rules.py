def detect_duplicate_payments(df):
    duplicates = df[df.duplicated(subset=['vendor', 'amount'], keep=False)]
    return duplicates

def detect_ghost_vendors(df):
    ghost_vendors = df[df['vendor'].str.contains("Ghost", case=False)]
    return ghost_vendors

def detect_round_figures(df):
    round_payments = df[df['amount'] % 10000 == 0]
    return round_payments
