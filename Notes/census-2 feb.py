census_file = open("census.txt", "r")
summary_file = open("summary.txt", "w")

## input_line = census_file.readline()
cumulative_population = 0

for input_line in census_file:
    print(input_line)
    values = input_line.split()
    cumulative_population = cumulative_population + int(values[1])
    summary_file.write(str(cumulative_population) + "\n")



'''
while input_line:
    values = input_line.split()
    cumulative_population = cumulative_population + int(values[1])
    summary_file.write(str(cumulative_population) + "\n")
    input_line = census_file.readline()
    print("line = ", input_line)

census_file.close()
summary_file.close()

'''


## sentence = "a" + "/n" + "b" + "/n" + "c" + "/n"  # /n = new line when printing a string. 
