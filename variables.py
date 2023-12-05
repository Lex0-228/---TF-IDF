"""ПРоміжний модуль визначення змінних імплементації функцій"""

# Визначені функції відокремлено від їхньої імплементації задля більш швидкого доступу та повторного викорстання
from LABA import preprocess, get_tokens, get_lemm, get_pos, gen_freq

# Необхідні для аналізу тексти знаходяться у відповідниз текстових файлах, зміст яких тут переноситься у змінні
with open("lesya_vol.5.txt", "r", encoding = "utf-8") as data_1:
    text_1 = data_1.read()
with open("lesya_vol.11.txt", "r", encoding = "utf-8") as data_2:
    text_2 = data_2.read()

# text 1
# В окремі змінні зберігаємо: список перших 20к токенів (значення кастомізується), список частот словоформ, список частот лем, список частот за частинами мови
sample_tokens1 = get_tokens(preprocess(text_1))[:20000]
slovoformy_freq1 = gen_freq(sample_tokens1)
lemm_freq1 = gen_freq(get_lemm(sample_tokens1))
pos_freq1 = gen_freq(get_pos(sample_tokens1))

# text 2
# В окремі змінні зберігаємо: список перших 20к токенів (значення кастомізується), список частот словоформ, список частот лем, список частот за частинами мови
sample_tokens2 = get_tokens(preprocess(text_2))[:20000]
slovoformy_freq2 = gen_freq(sample_tokens2)
lemm_freq2 = gen_freq(get_lemm(sample_tokens2))
pos_freq2 = gen_freq(get_pos(sample_tokens2))