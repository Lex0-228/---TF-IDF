"""Проєкт LABA - частотний словник 5-го (лірика) та 11-го (листи) томів Повного академічного видання творів Лесі Українки.
У цьому файлі визначені функції опрацювання тексту, що безпосередньо використанні для укладання списків частот
за словоформами, лемами та частинами мови."""

# Для токенізації текстів використано бібліотеку tokenize_uk
from tokenize_uk import tokenize_words
# Для автоматичного морфологічного аналізу використано модуль SpaCy (лематизація словоформ та визначення частин мови)
import spacy
# Для попередньої обробки (очистки) текстів використано регулярні вирази
import re

# 1. Функція попередньої обробки тексту (очистки) від елементів, які не потрібні для подальшого аналізу (напр. числа, дати, редакторські примітки)
def preprocess(text):
	clean_text = re.sub(r'(^.*Том 5.*$)|(^.*Збірка «.*$)|(^.*18\]?\[?[0-9]{2}.*$)|(^.*(нім\.|італ\.|англ\.|франц\.).*$)|(^.*19\]?\[?[0-9]{2}.*$)|(^.*Поезія поза збірками.*$)|(^.*(До )?[А-ЯІЇҐЄ]\..?[А-ЯІЇҐЄ]\..*$)||(^.*[0-9]{2} .+ 1[89][0-9]{2} р\..*$)|[\[\]]', '', text)
	return clean_text

# 2. Функція токенізації тексту. До списку токенів входять виділені модулем tokenize_uk елементи лише в нижньому регістрі та такі, що починаються з літери
def get_tokens(text):
	tok_text = [s.lower() for s in tokenize_words(text) if s[0].isalpha()]		
	return tok_text

# 3. Функція лематизації словоформ. Функція бере на вхід список токенів, а повертає список лем (методами бібліотеки SpaCy)
def get_lemm(tokens):
	nlp = spacy.load('uk_core_news_sm')
	doc = [nlp(token) for token in tokens]
	lemmas_list = []
	for t in doc:
		for x in t:
			lemma = x.lemma_
			lemmas_list.append(lemma)
	return lemmas_list

# 4. Функція визначення частиномовної приналежності. Імплементація аналогічна до лематизації методами SpaCy
def get_pos(tokens):
	nlp = spacy.load('uk_core_news_sm')
	doc = [nlp(token) for token in tokens]
	pos_list = []
	for t in doc:
		for x in t:
			pos = x.pos_
			pos_list.append(pos)
	return pos_list

# 5. Функція поділу списку токенів на підвибірки. Функція бере на вхід список токенів та параметр обсягу кожної вибірки (поділ порівну).
def subsampling(token, chunk_size):
	chunked_list = [token[i:i+chunk_size] for i in range(0,len(token),chunk_size)]
	return chunked_list

# 6. Функція підрахунку частоти кожної словоформи в кожній підвибірці. Бере на вхід список токенів,
# використовує поділ на підвибірки, та шляхом циклічного підрахунку повертає список кортежів з 1+кількість підвибірок елементів (слово та частоти)
def gen_freq(token):
	subs = subsampling(token, 1000)
	subDist = [[] for item in range(0,len(subs))]
	for t in token:
		for s in subDist:
			s = subDist.index(s)
			subDist[s].append(subs[s].count(t))
	dictf = list(set(zip(token,*subDist)))
	return dictf




