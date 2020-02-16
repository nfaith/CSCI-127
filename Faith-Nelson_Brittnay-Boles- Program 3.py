# -----------------------------------------+
# CSCI 127, Joy and Beauty of Data         |
# Program 3: Weather CSV Library           |
# Faith Nelson, Brittany Boles             |
# Last Modified: March 1, 2019             |
# -----------------------------------------+
# This program allows for a user to        |
# interact and manipulate the information  |
# that can be found in a csv file.         |
# -----------------------------------------+

import csv


def all_stations_by_state(input_file, state):
    file = open(input_file)
    file.readline()
    
    csvfile = csv.reader(file)
    stations = []
    counter = 0

    for line in file:
        information = line.split(",")
        if information[12] == state:
            if (information[1] in stations) == False:
                stations.append(information[1])
                counter += 1
                stations.sort()
                print(str(counter) + ". "+ str(information[1]))
        


def coldest_temp_by_state(input_file, state):
    file = open(input_file)
    file.readline()
    
    csvfile = csv.reader(file)
    min_temp = []
    coldest = ""

    for line in file:
        information = line.split(",")
        if information[12] == state:
            if (information[8] in min_temp) == False :
                min_temp.append(information[8])
        min_temp.sort()
    coldest = min_temp[0]
    print("The coldest temperature in", state,"is", coldest)
    



def coldest_temperature(input_file):
    
    infile = open(input_file)
    infile.readline()
    
    csvfile = csv.reader(infile)
    rows=next(csvfile)
    
    min=float(rows[7])
    
    location=""
    date=""
    
    for row in csvfile:
        if min>=float(row[7]):
            min=float(row[7])
            location=row[5]
            date=row[4]
    
    print("Coldest Fahrenheit temperature reading:",min)
    print("Location:",location)
    print("Date:",date)
#-----------------------------------------------------------------
    
    
def average_temperature(input_file, location):
    infile = open(input_file)
    infile.readline()
    
    csvfile = csv.reader(infile)
    rows=next(csvfile)
    average=0
    total_average=0
    count=0
    location=location.lower()
    
    for row in csvfile:
        
        if location==row[5].lower():
            average+=float(row[0])
            count+=1
    if count>=1:
        total_average=str(round((average/count),2))
    else:
        total_average="Not applicable"       
               
    print("Number of readings:",count)
    print("Average temperature:",total_average)


# -----------------------------------------+
# Do not change anything below this line   |
# with the exception of code related to    |
# option 4.                                |
# -----------------------------------------+

# -----------------------------------------+
# menu                                     |
# -----------------------------------------+
# Prints a menu of options for the user.   |
# -----------------------------------------+           
                

def menu():
    
    print()
    print("1. Identify coldest temperature.")
    print("2. Identify average temperature for a given location.")
    print("3. Identify all recording station locations by state.")
    print("4. Identify the coldest tempuratures of a given state.")
    print("5. Quit.")
    print()

# -----------------------------------------+
# main                                     |
# -----------------------------------------+
# Repeatedly query the user for options.   |
# -----------------------------------------+

def main():
    input_file = "weather.csv"
    choice = 0
    while (choice != 5):
        menu()
        choice = int(input("Enter your choice: "))
        print()
        if (choice == 1):
            coldest_temperature(input_file)
        elif (choice == 2):
            location = input("Enter desired location (e.g. Miles City, MT): ")
            average_temperature(input_file, location)
        elif (choice == 3):
            state = input("Enter name of state (e.g. Montana): ")
            all_stations_by_state(input_file, state)
        elif (choice == 4):
            state = input("Enter name of state (e.g. Montana): ")
            coldest_temp_by_state(input_file, state)
        elif (choice != 5):
            print("That is not a valid option.  Please try again.")
    print("Goodbye!")

# -----------------------------------------+

main()
