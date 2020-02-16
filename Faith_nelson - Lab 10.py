# -----------------------------------------------------
# CSCI 127, Lab 10                                    |
# March 28, 2019                                      |
# Faith Nelson                                        |
# -----------------------------------------------------

class Queue():

    def __init__(self, name):

        self.name = name
        self.list = []

    def __str__(self):
        numbers = ""
        for item in self.list:
            numbers += str(item)+ " "
         
        line = "Contents: " + numbers
        return line

    def __add__(self, item):

        self.list.append(item)
        return self

    def enqueue(self, given_list):

        self.list.append(given_list)


    
    def dequeue(self):

        return self.list.pop(0)

    def is_empty(self):
        if self.list == []:
            return True
        else:
            return False
        

# -----------------------------------------------------

def main():
    numbers = Queue("Numbers")

    print("Enqueue 1, 2, 3, 4, 5")
    print("---------------------")
    for number in range(1, 6):
        numbers.enqueue(number)
        print(numbers)

    print("\nDequeue one item")
    print("----------------")
    numbers.dequeue()
    print(numbers)

    print("\nDeque all items")
    print("---------------")
    while not numbers.is_empty():
        print("Item dequeued:", numbers.dequeue())
        print(numbers)

    # Enqueue 10, 11, 12, 13, 14
    for number in range(10, 15):
        numbers.enqueue(number)

    # Enqueue 15
    numbers += 15

    print("\n10, 11, 12, 13, 14, 15 enqueued")
    print("-------------------------------")
    print(numbers)

# -----------------------------------------------------

main()
