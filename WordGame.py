import re


class WordGame:
    def __init__(self, letters):
        self.letters = [i for i in letters]
        self.word_list = self.create_word_list()
        self.short_list = self.create_short_list()

    def word_finder(self):
        matched_words = []
        word_length = 0
        for i in self.short_list:
            i = i.strip()
            word_break = [j for j in i]
            match_criteria = sorted(word_break)
            if match_criteria == sorted(self.letters) and len(i) >= word_length:
                    word_length = len(i)
                    matched_words.append(i)
                    if len(matched_words) > 20:
                        matched_words = matched_words[1:]
        matched_words = matched_words[::-1]
        return matched_words

    @staticmethod
    def create_word_list():
        word_list = []
        with open('words/en') as words:
            for line in words:
                word_list.append(line)
        return word_list

    def create_short_list(self):
        shortened_list = []
        usable_words = re.compile('^[a-z]{1,9}')
        for i in self.word_list:
            try:
                if re.match(usable_words, i.rstrip()).group() == i.rstrip():
                    shortened_list.append(i)
            except AttributeError:
                count = 0
        return shortened_list


game = WordGame('fdofieasg')
lst = game.word_finder()
print(lst)