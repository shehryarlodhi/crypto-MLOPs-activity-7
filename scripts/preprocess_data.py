import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def preprocess_data():
    df = pd.read_csv('data/raw/raw_data.csv')

    # Handle missing values
    df.fillna(0, inplace=True)

    # Normalize numerical fields
    scaler = MinMaxScaler()
    df[['current_price', 'market_cap', 'total_volume']] = scaler.fit_transform(
        df[['current_price', 'market_cap', 'total_volume']]
    )

    # Save processed data
    df.to_csv('data/processed/processed_data.csv', index=False)
    print("Preprocessed data saved as processed_data.csv")

if __name__ == "__main__":
    preprocess_data()
