from random import shuffle, choice

import pandas as pd


class WordGame:
    def __init__(self):
        self.word_list = self.getWordList()
        self.vowels = []
        self.consonants = []
        self.flatten()
        shuffle(self.vowels)
        shuffle(self.consonants)
        self.letters = []

    def anagram_check(self, word, check_word):
        for letter in word:
            if letter in check_word:
                check_word = check_word.replace(letter, '', 1)
            else:
                return False
        return True

    def word_solve(self):
        top_score = 0
        solution = []
        letters = ''.join(self.letters).lower()
        for words in self.word_list:
            words.lower()
            words = words.strip()
            if self.anagram_check(words, letters):
                if len(words) < top_score:
                    break
                solution.append(words)
                top_score = len(words)
        return solution

    def getVowel(self):
        vowel = choice(self.vowels)
        self.vowels.remove(vowel)
        self.checkStackLength(vowel)
        return vowel

    def getConsonant(self):
        consonant = choice(self.consonants)
        self.consonants.remove(consonant)
        self.checkStackLength(consonant)
        return consonant

    def checkStackLength(self, letter):
        if len(self.letters) <= 9:
            self.letters.append(letter)
        else:
            print('9 letters chosen; start solving')
            self.word_solve()

    def flatten(self):
        vowels, consonants = self.loadAlphabet()
        for i in vowels.index:
            for j in range(vowels.loc[i, 1]):
                self.vowels.append(vowels.loc[i, 0])

        for i in consonants.index:
            for j in range(consonants.loc[i, 1]):
                self.consonants.append(consonants.loc[i, 0])

    def loadAlphabet(self):
        alphabet_pd = pd.read_csv('letter-distribution.csv', header=None)
        return alphabet_pd[:5], alphabet_pd[5:]

    def getWordList(self):
        word_list = []
        with open('words/SortedWords') as sorted_words:
            for lines in sorted_words:
                word_list.append(lines.strip())
        return word_list



