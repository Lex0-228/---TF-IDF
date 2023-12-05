"""Модуль для укладання таблицю зі значеннями TF-IDF до двох текстах"""

# Використано засоби бібліотеки scikit-learn
from sklearn.feature_extraction.text import TfidfVectorizer
# Та датафрейми pandas задля додаткової зручності
import pandas as pd
# sqlalchemy для конвертації датафреймів в SQL БД
from sqlalchemy import create_engine
from LABA import preprocess, get_tokens, subsampling, text_1, text_2

# Зв'язок із файлом БД
engine = create_engine('sqlite:///tfidf_text.db')

# TF-IDF дані побудовано для наступних списків словоформ з двох текстів
sample_tokens1 = get_tokens(preprocess(text_1))[:20000]
sample_tokens2 = get_tokens(preprocess(text_2))[:20000]

# Функція визначення TF-IDF, бере на вхід список словоформ та повертає pd-датафрейм, що легко перевести в SQL таблицю
def tfidf(sample):
    strings = []
    for s in subsampling(sample, 1000):
        string = ' '.join(s)
        strings.append(string)
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(strings[:20])
    tokens = vectorizer.get_feature_names_out()
    df_tfidfvect = pd.DataFrame(data = X.toarray().transpose(), index = tokens, columns = [f"sub{i}" for i in range(1,21)])
    df_tfidfvect.insert(0,"word",tokens,True)
    return df_tfidfvect

# Конвертація pd-датафреймів до таблиць у БД
tfidf(sample_tokens1).to_sql('TF-IDF per subsets for text 1', con=engine, if_exists='replace', index=False)
tfidf(sample_tokens2).to_sql('TF-IDF per subsets for text 2', con=engine, if_exists='replace', index=False)
