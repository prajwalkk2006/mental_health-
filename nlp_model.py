import pandas as pd
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
import joblib

nltk.download('punkt', quiet=True)

DATA_PATH = "data/emotions.csv"
MODEL_PATH = "emotion_model.pkl"

def train_model():
    df = pd.read_csv(DATA_PATH)
    X = df["text"]
    y = df["label"]

    model = make_pipeline(TfidfVectorizer(), MultinomialNB())
    model.fit(X, y)

    joblib.dump(model, MODEL_PATH)
    print("✅ Model trained and saved to", MODEL_PATH)

def load_model():
    return joblib.load(MODEL_PATH)

if __name__ == "__main__":
    train_model()
