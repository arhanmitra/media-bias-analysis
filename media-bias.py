import pandas as pd
import matplotlib.pyplot as plt
import nltk
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# --- 1. Load data ---
# Replace with your file path
df = pd.read_csv("allsides_balanced_news_headlines-texts.csv")


# Ensure columns exist
assert "headline" in df.columns and "bias" in df.columns, "CSV must have 'headline' and 'bias' columns"

# --- 2. Preprocessing ---
# Download stopwords if not already
nltk.download("stopwords")
nltk.download("punkt")

# Fill missing headlines just in case
df["headline"] = df["headline"].fillna("")

# --- 3. Sentiment Analysis ---
analyzer = SentimentIntensityAnalyzer()

def get_sentiment(text):
    score = analyzer.polarity_scores(text)
    return score["compound"]

df["sentiment"] = df["headline"].apply(get_sentiment)

# --- 4. Aggregate by bias ---
results = df.groupby("bias")["sentiment"].mean().reset_index()

print("=== Average Sentiment by Bias ===")
print(results)

# --- 5. Plot ---
plt.bar(results["bias"], results["sentiment"])
plt.xlabel("Media Bias")
plt.ylabel("Average Sentiment (compound score)")
plt.title("Political Polarization in News Headlines")
plt.show()

# --- 6. Print counts of articles ---
print("\n=== Number of Articles by Bias ===")
counts = df["bias"].value_counts()
print(counts.to_string())
