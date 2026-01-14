import joblib
from sklearn.ensemble import RandomForestClassifier
from preprocess import preprocess

def train():
    X = preprocess()
    y = [0 if i % 10 else 1 for i in range(len(X))]  # sample labels

    model = RandomForestClassifier()
    model.fit(X, y)

    joblib.dump(model, "models/random_forest.pkl")

if __name__ == "__main__":
    train()
