import pandas as pd
import gensim
from gensim import corpora
import re
import pyLDAvis.gensim_models as gensimvis
import os
import pyLDAvis

# Обновляем путь к CSS-файлу
css_path = os.path.join(os.getcwd(), 'static', 'ldavis.v1.0.0.css')
pyLDAvis.urls.LDAVIS_CSS_URL = f'file://{os.path.abspath(css_path)}'

# Загрузка данных из CSV файла
df = pd.read_csv('data/tweets_climate_change.csv')

# Функция для очистки и подготовки текста
def preprocess(text):
    text = re.sub(r'@\w+', '', text)
    text = re.sub(r'http\S+', '', text)
    text = re.sub(r'[^A-Za-z\s]', '', text)
    result = [token for token in gensim.utils.simple_preprocess(text) if token not in gensim.parsing.preprocessing.STOPWORDS and len(token) > 3]
    return result

df['cleaned_tweet'] = df['Tweet'].apply(preprocess)

# Создание словаря и корпуса
dictionary = corpora.Dictionary(df['cleaned_tweet'])
corpus = [dictionary.doc2bow(text) for text in df['cleaned_tweet']]

# Обучение модели LDA с 3 темами
lda_model = gensim.models.ldamodel.LdaModel(corpus, num_topics=3, id2word=dictionary, passes=15)

# Визуализация тем
lda_display = gensimvis.prepare(lda_model, corpus, dictionary, sort_topics=False)
pyLDAvis.save_html(lda_display, 'results/lda.html')


