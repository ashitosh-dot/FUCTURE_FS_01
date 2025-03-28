import matplotlib.pyplot as plt
sentiment_labels = ['Positive', 'Neutral', 'Negative']
sentiment_values = [65, 20, 15]
color_scheme = ['#4CAF50', '#FFC107', '#F44336']
plt.figure(figsize=(7, 7))
plt.pie(sentiment_values, labels
sentiment_labels, autopct='%1.1f%%', colors=color_scheme,
startangle=140, shadow=True)
plt.title('Customer Sentiment Distribution for Amazon Cotton Cloth')
plt.show()