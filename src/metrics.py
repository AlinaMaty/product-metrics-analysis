import pandas as pd


def calculate_dau(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calculate Daily Active Users (DAU).
    """
    return (
        df[df['event'].isin(['registration', 'purchase'])]
        .groupby('event_date')['user_id']
        .nunique()
        .reset_index(name='DAU')
    )


def calculate_conversion(df: pd.DataFrame) -> float:
    """
    Conversion from install to purchase (%).
    """
    installs = df[df['event'] == 'install']['user_id'].nunique()
    purchases = df[df['event'] == 'purchase']['user_id'].nunique()
    return round(purchases / installs * 100, 2)


def calculate_arpu(df: pd.DataFrame) -> float:
    """
    Average Revenue Per User (ARPU).
    """
    revenue = df['revenue'].sum()
    users = df['user_id'].nunique()
    return round(revenue / users, 2)
