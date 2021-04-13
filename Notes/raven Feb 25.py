import string

def process_text(raven_text):
    letter_count = {}
    for ch in string.ascii_lowercase:
        letter_count[ch] = 0
    for ch in raven_text:
        letter_count[ch] += 1
    return letter_count


def print_dictionary(raven_dictionary):
    for ch in string.ascii_lowercase:
        print(ch, raven_dictionary[ch])
# ---------------------------

def keep_letters(filename):
    file = open(filename, "r")
    modified_text = ""

    for line in file:
        line = line.lower()
        for letter in line:
            if letter in string.ascii_letters:
                modified_text += letter.lower()

    file.close()
    return modified_text

# ---------------------------

text = keep_letters("raven.txt")
dictionary = process_text(text)
print_dictionary(dictionary)
        
