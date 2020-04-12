class Node:
    def __init__(self,data_value = None):
        self.data_value = data_value
        self.next_value = None

class Listt:
    def __init__(self):
        self.head_value = None

    def printList(self):
        printvalue = self.head_value
        while(printvalue != None):
            print(printvalue.data_value)
            printvalue = printvalue.next_value

list1 = Listt()
list1.head_value = Node(1)
e2 = Node(2)
e3 = Node(3)

list1.head_value.next_value = e2
e2.next_value = e3

list1.printList()
