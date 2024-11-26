import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

def train_model():
    df = pd.read_csv('data/processed/processed_data.csv')

    # Features and target
    X = df[['market_cap', 'total_volume']]
    y = df['current_price']

    # Train model
    model = LinearRegression()
    model.fit(X, y)

    # Save the model
    with open('models/model.pkl', 'wb') as model_file:
        pickle.dump(model, model_file)
    print("Model saved as model.pkl")

if __name__ == "__main__":
    train_model()
