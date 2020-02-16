# -----------------------------------------------------
# CSCI 127, Lab 8
# March 7, 2019
# Faith Nelson
# ----------------------------------------------------

class Contact:
    """A contancts class for creating new contacts"""

    def __init__(self,first_name, last_name, cell_number):
        """A contructor method that sets the the first name, last name and cell number."""
        self.title = ""
        self.first_name = first_name
        self.last_name = last_name
        self.cell_number = cell_number
        self.area_code = ""

    def get_first_name(self):
        """A reader method that returns the first name"""
        return self.first_name

    def get_last_name(self):
        """A reader method that returns the last name."""
        return self.last_name

    def get_cell_number(self):
        """A reader method that returns cell number. """
        return self.cell_number

    def get_area_code(self):
        """A reader method that returns the area code."""
        self.area_code = self.cell_number[:3]
        return self.area_code

    def set_title(self, title):
        """A writer method that sets the title. """
        self.title = title

    def set_first_name(self, first_name):
        """A writer method that sets the first name."""
        self.first_name = first_name
        
    def print_entry(self):
        if self.title == "":
            name = self.first_name + " " + self.last_name
        else:
            name = self.title +" "+ self.first_name+ " "+ self.last_name
        print(name + " " + self.cell_number.rjust(35 - len(name)))

# -----------------------------------------------------
# Do not change anything below this line
# -----------------------------------------------------

def print_directory(contacts):
    print("My Contacts")
    print("-----------")
    for person in contacts:
        person.print_entry()
    print("-----------\n")

# -----------------------------------------------------

def main():
    champ = Contact("???", "Bobcat", "406-994-0000")
    president = Contact("Waded", "Cruzado", "406-994-CATS")
    professor = Contact("John", "Paxton", "406-994-4780")

    contacts = [champ, president, professor]

    print_directory(contacts)

    champ.set_first_name("Champ")
    president.set_title("President")
    professor.set_title("Professor")

    print_directory(contacts)

    print("The area code for cell number", champ.get_cell_number(), "is", \
           champ.get_area_code())

# -----------------------------------------------------

main()
