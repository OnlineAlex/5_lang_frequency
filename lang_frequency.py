import sys
import string
import re
import collections


def load_data(filepath):
    with open(filepath, 'r') as work_file:
        return work_file.read()


def remove_punctuation(work_text):
    work_text = re.sub("\s*\n|\xa0|—\s*", ' ', work_text)
    table = work_text.maketrans("", "", string.punctuation)
    clean_text = work_text.translate(table)
    return clean_text


def get_most_frequent_words(text):
    text = text.lower()
    clean_text = remove_punctuation(text)
    list_all_words = clean_text.split()
    words_stat = collections.Counter()
    for word in list_all_words:
        words_stat[word] += 1

    return words_stat.most_common(10)


def print_frequent_words(top_freq_words):
    place = 1
    for word, frequent in top_freq_words:
        print('{0:>2}: "{1}" — {2}'.format(place, word, frequent))
        place += 1


if __name__ == '__main__':
    try:
        link_file = sys.argv[1]
        text_file = load_data(link_file)
    except IndexError:
        print('Ошибка! Вы не указали путь к файлу.')
        print('Сработает, если написать "python lang_frequency.py <путь к файлу>"')
    except FileNotFoundError:
        print('Ошибка! Система не нашла такой файл.')
    except ValueError:
        print('Ошибка. Файл должен быть в формате .txt')
    else:
        frequent_stat = get_most_frequent_words(text_file)
        print_frequent_words(frequent_stat)
