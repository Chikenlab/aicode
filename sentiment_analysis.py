import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt
import os

# Создаем директорию 'results', если она не существует
os.makedirs('results', exist_ok=True)

# Загрузка данных из CSV
df = pd.read_csv('data/tweets_climate_change.csv')

# Функция для определения тональности
def get_sentiment(text):
    analysis = TextBlob(text)
    if analysis.sentiment.polarity > 0:
        return 'Positive'
    elif analysis.sentiment.polarity < 0:
        return 'Negative'
    else:
        return 'Neutral'

# Применяем функцию ко всем твитам
df['Sentiment'] = df['Tweet'].apply(get_sentiment)
print("Sentiment analysis completed")

# Сохраняем результаты в новый CSV-файл
df.to_csv('results/tweets_sentiment_analysis.csv', index=False)
print("CSV file saved sucessfully")

# Визуализация распределения тональностей
sentiment_counts = df['Sentiment'].value_counts()
sentiment_counts.plot(kind='bar', color=['green', 'red', 'blue'])
plt.title('Sentiment Analysis of Tweets')
plt.xlabel('Sentiment')
plt.ylabel('Number of Tweets')
plt.show()

print(df.head())  # Печатает первые 5 строк DataFrame
print(df['Sentiment'].value_counts())  # Показывает распределение тональностей
try:
    df.to_csv('results/tweets_sentiment_analysis.csv', index=False)
    print("CSV file saved successfully")
except Exception as e:
    print("Failed to save CSV file:", e)
