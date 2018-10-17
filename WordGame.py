with open('words/en', 'r') as fileopen:
    words = [line.strip() for line in fileopen]

# Sort dictionary by lenght
sortedList = sorted(words, key=len)

# Reverses list, longest lenght to the top
resverseDic = reversed(sortedList)
f = open("sortedDic.txt","w")

# Write word to text file with 9 letters or lower
for item in resverseDic:
    if len(item) < 10:
        f.write("%s\n" % item)
f.close()

def anagram_check(word, check_word):
    for letter in word:
        if letter in check_word:
            check_word=check_word.replace(letter, '', 1)
        else:
            return 0
    return 1


a = 'jasdiusdf'
i = 0
f = open('sortedDic.txt','r')
for line in f:
    line=line.strip()
    if len(line)>=3:
        if anagram_check(line,a):
            print (i , ":", line)
            i += 1
            break
f.close()