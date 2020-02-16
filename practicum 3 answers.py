"""
# 1.)

word_count = {"apple":10, "banana":15, "coconut":6}

for key, value in word_count.items():
    print(key, value)

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
    count = 1

    for line in file_1:
        if count % 2 == 1:
            file_2.write(line)
        count += 1


    file_1.close()
    file_2.close()
    


retain_every_other_line("input.txt", "output.txt")


