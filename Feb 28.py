
##
##dictionary = {"computer":"a device"}
##
##dictionary.get["computer"]
##dictionary.get["pc", "unknown definition"]

import string


def print_dictionary(dictionary):
    for word, count in dictionary.items():
        print(word,count)

def most_frequent_word(dictionary):
    pass


def process(word):
    result = ""
    for ch in string.ascii_lowercase:
        result += ch
    return result

def create_dictionary(words):
    dictionary = {}
    for word in words:
        dictionary[word] = dictionary.get(word,0) + 1

    return dictionary
    
def keep_words(file_name):
    file = open(file_name, "r")
    words = []
    final_words = []
    for line in file:
        line = line.lower()
        words = line.split()
        for word in words:
            final_words += [process(word)]
    print(final_words[:50])
    file.close()
    return words



words = keep_words("raven.txt")
dictionary = create_dictionary(words)
print_dictionary(dictionary)
