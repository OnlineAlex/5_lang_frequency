import sys
import re
import collections


def load_data(filepath):
    with open(filepath, 'r') as work_file:
        return work_file.read()


def remove_punctuation(work_text):
    clean_data = re.sub("\W", ' ', work_text)
    return clean_data


def get_lower_tuple(text):
    text_lower = text.lower()
    tuple_words = text_lower.split()
    return tuple_words


def get_most_frequent_words(words, num_words):
    words_stat = collections.Counter(words)
    return words_stat.most_common(num_words)


def print_frequent_words(top_freq_words):
    for place, word in enumerate(top_freq_words):
        print('{0:>2}: "{1}"'.format(place, word[0]))


if __name__ == '__main__':
    try:
        link_file = sys.argv[1]
        text_data = load_data(link_file)
    except IndexError:
        print('Ошибка! Вы не указали путь к файлу.')
        print('Сработает, если написать "python lang_frequency.py <путь к файлу>"')
    except FileNotFoundError:
        print('Ошибка! Система не нашла такой файл.')
    except ValueError:
        print('Ошибка. Файл должен быть в формате .txt')
    else:
        clean_text = remove_punctuation(text_data)
        text_words = get_lower_tuple(clean_text)
        frequent_words = get_most_frequent_words(text_words, 10)
        print_frequent_words(frequent_words)
