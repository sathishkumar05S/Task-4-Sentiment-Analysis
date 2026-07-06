import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt

# Reviews list
reviews = [
    "This product is amazing and works perfectly.",
    "I love this phone. Excellent quality.",
    "Very bad experience. Waste of money.",
    "The product is okay, nothing special.",
    "Terrible customer service.",
    "Fantastic product. Highly recommended.",
    "Average quality.",
    "I am very happy with my purchase.",
    "Not worth the price.",
    "Excellent and awesome."
]

# Create DataFrame
data = pd.DataFrame({"Review": reviews})

# Sentiment function
def get_sentiment(text):
    polarity = TextBlob(text).sentiment.polarity

    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"

# Apply sentiment analysis
data["Sentiment"] = data["Review"].apply(get_sentiment)

# Print output
print(data)

# Save CSV
data.to_csv("sentiment_output.csv", index=False)

# Bar Chart
counts = data["Sentiment"].value_counts()

plt.bar(counts.index, counts.values)
plt.title("Sentiment Analysis")
plt.xlabel("Sentiment")
plt.ylabel("Count")

plt.savefig("sentiment_chart.png")
plt.show()

print("Sentiment Analysis Completed!")
