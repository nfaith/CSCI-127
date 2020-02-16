# --------------------------------------
# CSCI 127, Lab 7                      |
# February 28, 2019                    |
# Faith Nelson                         |



def create_dictionary(file_name):
    file = open(file_name, "r")
    dictionary = {}
    
    for item in file:
        item = item.split(",")

        if item[1][:-1] == "space":
           dictionary[" "] = item[0]
        elif item[1][:-1] == "comma":
            dictionary[","] = item[0]
        else:
            dictionary[item[1][:-1]] = item[0]
    file.close()
    return dictionary

# Explaination 

def translate(sentence, dictionary, file_name):
    file = open(file_name, "w")
    for ch in sentence:
        if ch in dictionary:
            output = (ch, dictionary[ch])
            file.write(str(output) + "\n")
        else:
            output =(ch, "UNKNOWN")
            file.write(str(output) + "\n")
            
            
    file.close()
# --------------------------------------

def main():
    dictionary = create_dictionary("ascii-codes.csv")
    sentence = "Buck lived at a big house in the sun-kissed Santa Clara Valley. Judge Miller's place, it was called!"
    translate(sentence, dictionary, "output-1.txt")
    sentence = "Bozeman, MT  59717"
    translate(sentence, dictionary, "output-2.txt")
    sentence = "The value is ~$25.00"
    translate(sentence, dictionary, "output-3.txt")

# --------------------------------------

main()
