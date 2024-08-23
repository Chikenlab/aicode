import tweepy
import pandas as pd

# Bearer Token для API v2
bearer_token = ''

# Создаем клиент Tweepy для API v2
client = tweepy.Client(bearer_token=bearer_token)

# Пример запроса поиска твитов
try:
    response = client.search_recent_tweets(query="climate change", max_results=100, tweet_fields=['created_at', 'text', 'author_id', 'geo'])

    # Создаем список для хранения твитов
    tweets_data = []

    for tweet in response.data:
        tweets_data.append({
            'Datetime': tweet.created_at,
            'Tweet': tweet.text,
            'Author ID': tweet.author_id,
            'Geo': tweet.geo
        })

    # Создаем DataFrame из списка
    df = pd.DataFrame(tweets_data)

    # Сохраняем DataFrame в CSV файл
    df.to_csv('tweets_climate_change.csv', index=False)

    print("Tweets have been saved to 'tweets_climate_change.csv'")

except tweepy.TweepyException as e:
    print(f"An error occurred: {e}")










