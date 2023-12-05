"""Модуль для роботи з SQL командами та експортом результатів у файл-базу даних"""
import sqlite3
# Отримані результати обчислень імпортуємо та маємо вставити в базу даних
from variables import slovoformy_freq1, lemm_freq1, pos_freq1, slovoformy_freq2, lemm_freq2, pos_freq2

# Визначаємо зв'язок та курсор для взаємодії зі створеною БД
conn = sqlite3.connect('frequency_dict.db')
cursor = conn.cursor()

# 1. Створюємо 6 таблиць: частота по 20 підвибірках словоформ, лем, частин мови (для 2 текстів)

cursor.execute("""CREATE TABLE IF NOT EXISTS vol5_words_frequency (word TEXT PRIMARY KEY NOT NULL,
                  subs_1 INTEGER,subs_2 INTEGER,subs_3 INTEGER,subs_4 INTEGER,subs_5 INTEGER,subs_6 INTEGER,
                  subs_7 INTEGER,subs_8 INTEGER,subs_9 INTEGER,subs_10 INTEGER,subs_11 INTEGER,subs_12 INTEGER,
                  subs_13 INTEGER,subs_14 INTEGER,subs_15 INTEGER,subs_16 INTEGER,subs_17 INTEGER,subs_18 INTEGER,
                  subs_19 INTEGER,subs_20 INTEGER)
""")
cursor.execute("""CREATE TABLE IF NOT EXISTS vol5_lemmas_frequency (lemma TEXT PRIMARY KEY NOT NULL,
                  subs_1 INTEGER,subs_2 INTEGER,subs_3 INTEGER,subs_4 INTEGER,subs_5 INTEGER,subs_6 INTEGER,
                  subs_7 INTEGER,subs_8 INTEGER,subs_9 INTEGER,subs_10 INTEGER,subs_11 INTEGER,subs_12 INTEGER,
                  subs_13 INTEGER,subs_14 INTEGER,subs_15 INTEGER,subs_16 INTEGER,subs_17 INTEGER,subs_18 INTEGER,
                  subs_19 INTEGER,subs_20 INTEGER)
""")
cursor.execute("""CREATE TABLE IF NOT EXISTS vol5_POS_frequency (POS TEXT PRIMARY KEY,
                  subs_1 INTEGER,subs_2 INTEGER,subs_3 INTEGER,subs_4 INTEGER,subs_5 INTEGER,subs_6 INTEGER,
                  subs_7 INTEGER,subs_8 INTEGER,subs_9 INTEGER,subs_10 INTEGER,subs_11 INTEGER,subs_12 INTEGER,
                  subs_13 INTEGER,subs_14 INTEGER,subs_15 INTEGER,subs_16 INTEGER,subs_17 INTEGER,subs_18 INTEGER,
                  subs_19 INTEGER,subs_20 INTEGER)
""")

cursor.execute("""CREATE TABLE IF NOT EXISTS vol11_words_frequency (word TEXT PRIMARY KEY NOT NULL,
                  subs_1 INTEGER,subs_2 INTEGER,subs_3 INTEGER,subs_4 INTEGER,subs_5 INTEGER,subs_6 INTEGER,
                  subs_7 INTEGER,subs_8 INTEGER,subs_9 INTEGER,subs_10 INTEGER,subs_11 INTEGER,subs_12 INTEGER,
                  subs_13 INTEGER,subs_14 INTEGER,subs_15 INTEGER,subs_16 INTEGER,subs_17 INTEGER,subs_18 INTEGER,
                  subs_19 INTEGER,subs_20 INTEGER)
""")
cursor.execute("""CREATE TABLE IF NOT EXISTS vol11_lemmas_frequency (lemma TEXT PRIMARY KEY NOT NULL,
                  subs_1 INTEGER,subs_2 INTEGER,subs_3 INTEGER,subs_4 INTEGER,subs_5 INTEGER,subs_6 INTEGER,
                  subs_7 INTEGER,subs_8 INTEGER,subs_9 INTEGER,subs_10 INTEGER,subs_11 INTEGER,subs_12 INTEGER,
                  subs_13 INTEGER,subs_14 INTEGER,subs_15 INTEGER,subs_16 INTEGER,subs_17 INTEGER,subs_18 INTEGER,
                  subs_19 INTEGER,subs_20 INTEGER)
""")
cursor.execute("""CREATE TABLE IF NOT EXISTS vol11_POS_frequency (POS TEXT PRIMARY KEY,
                  subs_1 INTEGER,subs_2 INTEGER,subs_3 INTEGER,subs_4 INTEGER,subs_5 INTEGER,subs_6 INTEGER,
                  subs_7 INTEGER,subs_8 INTEGER,subs_9 INTEGER,subs_10 INTEGER,subs_11 INTEGER,subs_12 INTEGER,
                  subs_13 INTEGER,subs_14 INTEGER,subs_15 INTEGER,subs_16 INTEGER,subs_17 INTEGER,subs_18 INTEGER,
                  subs_19 INTEGER,subs_20 INTEGER)
""")
conn.commit()

# 3. Зміст утворених раніше списків імпортуємо у визначені таблиці
cursor.executemany("INSERT INTO vol5_words_frequency VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", slovoformy_freq1)
conn.commit()
cursor.executemany("INSERT INTO vol5_lemmas_frequency VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", lemm_freq1)
conn.commit()
cursor.executemany("INSERT INTO vol5_POS_frequency VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", pos_freq1)
conn.commit()

cursor.executemany("INSERT INTO vol11_words_frequency VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", slovoformy_freq2)
conn.commit()
cursor.executemany("INSERT INTO vol11_lemmas_frequency VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", lemm_freq2)
conn.commit()
cursor.executemany("INSERT INTO vol11_POS_frequency VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", pos_freq2)
conn.commit()

# 4. Для підрахунку абсолютних частот (сума по всіх підвибірках) визначаємо по новому додатковому стовпцю
cursor.execute("""ALTER TABLE vol5_words_frequency ADD abs_frequency AFTER word""")
cursor.execute("""UPDATE vol5_words_frequency SET abs_frequency = subs_1+subs_2+subs_3+subs_4+subs_5+subs_6+subs_7+subs_8+subs_9+subs_10+subs_11+subs_12+subs_13+subs_14+subs_15+subs_16+subs_17+subs_18+subs_19+subs_20""")

cursor.execute("""ALTER TABLE vol5_lemmas_frequency ADD abs_frequency AFTER lemma""")
cursor.execute("""UPDATE vol5_lemmas_frequency SET abs_frequency = subs_1+subs_2+subs_3+subs_4+subs_5+subs_6+subs_7+subs_8+subs_9+subs_10+subs_11+subs_12+subs_13+subs_14+subs_15+subs_16+subs_17+subs_18+subs_19+subs_20""")

cursor.execute("""ALTER TABLE vol5_POS_frequency ADD abs_frequency AFTER POS""")
cursor.execute("""UPDATE vol5_POS_frequency SET abs_frequency = subs_1+subs_2+subs_3+subs_4+subs_5+subs_6+subs_7+subs_8+subs_9+subs_10+subs_11+subs_12+subs_13+subs_14+subs_15+subs_16+subs_17+subs_18+subs_19+subs_20""")
conn.commit()

cursor.execute("""ALTER TABLE vol11_words_frequency ADD abs_frequency AFTER word""")
cursor.execute("""UPDATE vol11_words_frequency SET abs_frequency = subs_1+subs_2+subs_3+subs_4+subs_5+subs_6+subs_7+subs_8+subs_9+subs_10+subs_11+subs_12+subs_13+subs_14+subs_15+subs_16+subs_17+subs_18+subs_19+subs_20""")

cursor.execute("""ALTER TABLE vol11_lemmas_frequency ADD abs_frequency AFTER lemma""")
cursor.execute("""UPDATE vol11_lemmas_frequency SET abs_frequency = subs_1+subs_2+subs_3+subs_4+subs_5+subs_6+subs_7+subs_8+subs_9+subs_10+subs_11+subs_12+subs_13+subs_14+subs_15+subs_16+subs_17+subs_18+subs_19+subs_20""")

cursor.execute("""ALTER TABLE vol11_POS_frequency ADD abs_frequency AFTER POS""")
cursor.execute("""UPDATE vol11_POS_frequency SET abs_frequency = subs_1+subs_2+subs_3+subs_4+subs_5+subs_6+subs_7+subs_8+subs_9+subs_10+subs_11+subs_12+subs_13+subs_14+subs_15+subs_16+subs_17+subs_18+subs_19+subs_20""")
conn.commit()

# 5. Закриваємо зв'язок з БД по закінченню алгоритма
conn.close()


# import cProfile, pstats
# profiler = cProfile.Profile()
# profiler.enable()
#
#
# profiler.disable()
#
# stats = pstats.Stats(profiler).sort_stats('ncalls')
# stats.print_stats()