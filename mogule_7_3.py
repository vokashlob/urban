# импорты

import re
from collections import Counter

# определение классов


class WordsFinder:
    def __init__(self, *files):
        self.file_names = []
        for file in files:
            self.file_names.append(file)

    def get_all_words(self):
        all_words = {}
        for i in self.file_names:
            words = ''
            with open(i, encoding='utf-8') as file:
                for line in file:
                    words += re.sub(r'[^\w\s\']', '', line).lower()
            all_words[i] = words.split()
        return all_words

    def find(self, word):
        d = {}
        for name, words in self.get_all_words().items():
            if word.lower() in words:
                d[name] = words.index(word.lower()) + 1
            else:
                print(f"Слова {word} нет в файле {name}")
        return d

    def count(self, word):
        d = {}
        for name, words in self.get_all_words().items():
            counter = Counter(words)
            d[name] = counter[word.lower()]
        return d


# проверки

# finder = WordsFinder('test_file.txt', 'Walt Whitman - O Captain! My Captain!.txt', 'Rudyard Kipling - If.txt', 'Mother Goose - Monday’s Child.txt')
# print(finder.file_names)
# print(finder.get_all_words())
# print(finder.find('TEXT'))
# print(finder.count('TEXT'))

finder2 = WordsFinder('test_file.txt')
# print(finder2.file_names)
print(finder2.get_all_words())
print(finder2.find('TEXT'))
print(finder2.count('TEXT'))