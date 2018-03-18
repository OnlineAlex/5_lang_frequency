import sys
import re
import collections


def load_data(filepath):
    with open(filepath, 'r') as work_file:
        return work_file.read()


def get_words_from_text(work_text):
    clean_text = re.sub('\W', ' ', work_text)
    text_lower = clean_text.lower()
    words_list = text_lower.split()
    return words_list


def get_most_frequent_words(words):
    words_stat = collections.Counter(words)
    num_words = 10
    return words_stat.most_common(num_words)


def print_frequent_words(top_freq_words):
    for index, (word, count) in enumerate(top_freq_words, start=1):
        print('{0:>2}: "{1}" — {2}'.format(
            index,
            word,
            count
        ))


if __name__ == '__main__':
    try:
        file_path = sys.argv[1]
        text_data = load_data(file_path)
    except IndexError:
        print('Ошибка! Вы не указали путь к файлу.')
        print('Сработает, если написать "python lang_frequency.py <путь к файлу>"')
    except FileNotFoundError:
        print('Ошибка! Система не нашла такой файл.')
    except ValueError:
        print('Ошибка. Файл должен быть в формате .txt')
    else:
        words_text_list = get_words_from_text(text_data)
        frequent_words = get_most_frequent_words(words_text_list)
        print_frequent_words(frequent_words)
