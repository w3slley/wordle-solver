import sys
import collections


num_letters = 5
word_pattern = sys.argv[1]
word_pattern_wrong_positions = sys.argv[2]
letters_not_present = sys.argv[3]
letters_present = '' if sys.argv[4] == '0' else sys.argv[4]
filename = sys.argv[5]
print(num_letters,word_pattern, letters_not_present, letters_present, filename)

f = open(filename,'r')
words = []
count = 0
while True:
    count += 1
    word = f.readline().strip('\n')
    if len(word) == int(num_letters):
        words.append(word)
    if not word:
        break
#word_pattern = 's...p'
def get_input_letters_num(word_pattern):
    count = 0
    for i in word_pattern:
        if i != '.': count += 1
    return count

def does_word_contain_letter_not_present(word, letters_not_present):
    contains = 0
    for letter in letters_not_present:
        if word.lower().find(letter.lower()) != -1: contains += 1
    return contains > 0

def strip(word,pattern):
    ans = ''
    for w in word:
        if w != pattern: ans+=w
    return ans

def has_equal_word_count(word_pattern,letters_present,word):
    #e: 2, r:1

    
    #return collections.Counter(word) == collections.Counter(word_pattern.strip('.') + letters_present)
    valid = True
    word_counter = collections.Counter(word)
    counter_present = collections.Counter(strip(word_pattern,'.') + letters_present)
    #print(word_counter, strip(word_pattern,'.'))
    for key in counter_present.keys():
        if word_counter[key] != counter_present[key]: valid = False
    return valid

    
def get_possible_words_from_pattern(word_pattern, word_pattern_wrong_positions, letters_not_present, letters_present, words):
    results = []
    for word in words:
        if does_word_contain_letter_not_present(word, letters_not_present): continue
        if not has_equal_word_count(word_pattern, letters_present, word): continue
        
        valid = 0
        input_letters_num = get_input_letters_num(word_pattern)
        for i,v in enumerate(word_pattern):
            if v == '.': continue
            if v.lower() == word[i].lower() and word_pattern_wrong_positions[i].lower() != word[i]:
                valid+=1
                
        if valid == input_letters_num:
            results.append(word)


    return results

print(get_possible_words_from_pattern(word_pattern, word_pattern_wrong_positions, letters_not_present, letters_present, words))
