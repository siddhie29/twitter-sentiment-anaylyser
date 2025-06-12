from textblob import TextBlob
import matplotlib.pyplot as plt

# Mock tweet data
tweets = [
    "I love how the government handled the pandemic!",
    "This election is the worst I have ever seen.",
    "I have no strong opinions about this party.",
    "The rally today gave me hope for a better future.",
    "What a disaster! The policies are totally useless.",
    "The minister’s speech was okay, nothing new.",
    "Finally some real change happening in the system!",
    "Nothing ever changes no matter who wins.",
    "Impressed by the youth participation this year!",
    "Totally disappointed by the way things turned out."
]

# Counters for sentiment categories
positive = 0
negative = 0
neutral = 0

# Analyze sentiment of each tweet
for tweet in tweets:
    analysis = TextBlob(tweet)
    polarity = analysis.sentiment.polarity
    
    print(f"Tweet: {tweet}")
    print(f"Sentiment polarity: {polarity}")

    if polarity > 0:
        positive += 1
    elif polarity < 0:
        negative += 1
    else:
        neutral += 1

# Print summary counts
print("\nSummary:")
print(f"Positive tweets: {positive}")
print(f"Negative tweets: {negative}")
print(f"Neutral tweets: {neutral}")

# Plotting pie chart
labels = ['Positive', 'Negative', 'Neutral']
sizes = [positive, negative, neutral]
colors = ['green', 'red', 'gray']

plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
plt.title("Mood of the Nation on Twitter (Mock Data)")
plt.axis('equal')  # Equal aspect ratio ensures pie chart is circular.
plt.show()
