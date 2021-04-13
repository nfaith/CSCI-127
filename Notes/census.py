census_file = open("census.txt", "r")


total_population = 0
for one_line in census_file:
    values = one_line.split()
    # print("State: " + values[0] + ", Population: " +  values[1])
    total_population += int(values[1])

print("The total population = ", total_population)

census_file.close()


"""
sentence = "I am looking forward to the long weekend"

sentence.split(" ")

sentence.split("forward")

sentence.split() # this splits the empty space.


if in a sub-directory pyhton will not find it... so you have to specify where to find
it... EX: open("file/census.txt") - relative adressing

if on desktop - ../files/censis.txt

""" 
