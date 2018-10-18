import random


def sorted_word_list(file_name):
    with open(file_name, 'r') as fileopen:
        words = [line.strip() for line in fileopen]
    sorted_list = sorted(words, key=len)
    rev_list = reversed(sorted_list)
    with open('words/SortedWords', 'w') as sort_write:
        for word in rev_list:
            if len(word) < 10:
                sort_write.write(word)
                sort_write.write('\n')


def anagram_check(word, check_word):
    for letter in word:
        if letter in check_word:
            check_word = check_word.replace(letter, '', 1)
        else:
            return False
    return True


def scramble_generator():
    alphabet = list('qwertyuiopasdfghjklzxcvbnm')
    vowels = list('aeiou')
    consonants = []
    for letter in alphabet:
        if letter not in vowels:
            consonants.append(letter)

    scramble = random.sample(vowels, 3) + random.sample(consonants, 4) + random.sample(alphabet, 2)
    return scramble


def word_solve(letters):
    top_score = 0
    solution = []
    with open('words/sortedWords', 'r') as dict_file:
        for dict_item in dict_file:
            dict_item = dict_item.strip()
            if anagram_check(dict_item, letters):
                if len(dict_item) < top_score:
                    break
                print(dict_item)
                solution.append(dict_item)
                top_score = len(dict_item)
    dict_file.close()
    return solution


board = scramble_generator()
print(board)
let = ''.join(board)
answer = word_solve(let)
