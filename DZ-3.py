
###############_Доп. задание_##########

ls5 = "lorem ipsum amet dolor amet consectetur adipiscing elit sed do emus elit. "
censur = ["amet", "elit"]
def censure(text, censured_words):
    for word in censured_words:
        while word in text:
            start_index = text.find(word)
            end_index = start_index + len(word)
            firs_section = text[:start_index]
            second_section = text[end_index:]
            text = firs_section + second_section

    return text

print(censure(ls5, censur))


###############_Задание_1_##########

# Пользователь вводит с клавиатуры некоторый текст,
# после чего пользователь вводит список зарезервированных слов.
# Необходимо найти в тексте все зарезервированные слова и изменить их регистр на верхний.
# Вывести на экран измененный текст.

text_dz_1 = "Lorem ipsum dolor sit amet consectetur adipisicing elit. Laborum perspiciatis quasi earum eius molestiae! Ab accusantium placeat at ipsa earum."
rezerv = ["amet", "elit", "quasi", "Ab", "ipsa"]

def censure(text, rez_words):
    words = text.split()
    result = []
    for word in words:
            stripped_word = word.strip('.,!?;:')
            if stripped_word in rez_words:
                word = word.upper()
                result.append(word)
            elif word not in rez_words:
                result.append(word)

    new_text = " ".join(result)
    print(new_text)

censure(text_dz_1, rezerv)

###############_Задание_2_##########

# Есть некоторый текст. Посчитайте в этом тексте количество предложений и
# выведите на экран полученный результат.
#
text_dz_2 = "Lorem ipsum dolor sit amet consectetur adipisicing elit... Laborum perspiciatis quasi earum eius molestiae! Ab accusantium placeat at ipsa earum."


def count_sentences(text):
    sentences = text.split()
    i = 0
    for word in sentences:
        if word[-1] == "." or word[-1] == "!" or word[-1] == "?":
            i = i + 1
    return i

print( "В тексте", count_sentences(text_dz_2), "предложения")



