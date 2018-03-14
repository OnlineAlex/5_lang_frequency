import string
import re

def load_data(filepath):
    with open(filepath, 'r') as file:
        file = re.sub("\s*\n\s*", ' ', file.read())
        return file


def remove_punctuation(work_text):
    table = work_text.maketrans("", "", string.punctuation)
    clean_text = work_text.translate(table)
    return clean_text


def get_unique_words(words_text):
    set_words = set(word for word in words_text.split(' '))
    if '' in set_words:
        set_words.remove('')
    tuple_words = tuple(set_words)
    return tuple_words


def get_most_frequent_words(text):
    text = text.lower()
    clean_text = remove_punctuation(text)
    unique_words = get_unique_words(clean_text)
    list_all_words = clean_text.split(' ')

    words_stat = {}
    for word in unique_words:
        word_repeat = list_all_words.count(word)
        words_stat[word] = word_repeat

    words_stat = sorted(words_stat.items(), key=lambda value: value[1])
    return words_stat


if __name__ == '__main__':
    while True:
        try:
            filepath = input('Напишите путь к файлу в формате .txt \n')
            text_file = load_data(filepath)
        except FileNotFoundError:
            print('Ошибка! Система не нашла такой файл.')
            print('Пробуйте указать полный путь к файлу.\n')
        else:
            print('Файл принял, начинаю анализ...')
            break
    frequent_stat = get_most_frequent_words(text_file)
    for place in range(1, 11):
        print('{0}: "{1}" — {2}'.format(place, frequent_stat[-place][0], frequent_stat[-place][1]))
