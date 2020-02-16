
"""
# 1.)

word_count = {"apple":10, "banana":15, "coconut":6}

for item in word_count:
    print(item, word_count.get(item))

"""
"""
# 2.)

class Movie:

    def __init__(self, title, director):
        
        self.title = title
        self.director = director

    def __str__(self):
        
        line = 'The movie "' + self.title + '" was directed by ' + self.director 
        return line
        




movie_1 = Movie("Bao", "Domee Shi")
print(movie_1)

movie_2 = Movie("Between the Lines", "Maria Koneva")
print(movie_2)
"""

# 3.)

def retain_every_other_line(input_file, output_file):
    file_1 = open(input_file, "r")
    file_2 = open(output_file, "w")
    count = 0

    for line in file_1:
        count += 1
        print(line)
        for i in range(count):
            if i % 2 != 0:
                file_2.write(line)


    file_1.close()
    return file_2
    


retain_every_other_line("input.txt", "output.txt")
