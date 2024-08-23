import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt
import spacy

# Загрузка модели английского языка SpaCy
nlp = spacy.load("en_core_web_sm")

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

# Функция для очистки текста
def clean_text(text):
    doc = nlp(text.lower())  # Приводим текст к нижнему регистру и токенизируем
    words = [token.lemma_ for token in doc if not token.is_stop and token.is_alpha]  # Лемматизация и удаление стоп-слов
    return ' '.join(words)

# Применяем очистку текста ко всем твитам
df['Cleaned_Tweet'] = df['Tweet'].apply(clean_text)

# Функция для подсчета и визуализации частоты слов
def plot_word_frequency(sentiment, color):
    sentiment_df = df[df['Sentiment'] == sentiment]
    all_words = ' '.join(sentiment_df['Cleaned_Tweet'].tolist())
    word_freq = pd.Series(all_words.split()).value_counts().head(10)

    plt.bar(word_freq.index, word_freq.values, color=color)
    plt.xlabel('Words')
    plt.ylabel('Frequency')
    plt.title(f'Top 10 Words in {sentiment} Tweets')

# Визуализация для каждого типа настроения
plt.figure(figsize=(10, 15))

plt.subplot(3, 1, 1)
plot_word_frequency('Positive', 'green')

plt.subplot(3, 1, 2)
plot_word_frequency('Negative', 'red')

plt.subplot(3, 1, 3)
plot_word_frequency('Neutral', 'blue')

plt.tight_layout()
plt.show()


