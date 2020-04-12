class Node:
    def __init__(self, data_value = None):
        self.data_value = data_value
        self.next_value = None


class Listt:
    def __init__(self):
        self.head_value = None

    def PrintList(self):
        printvalue = self.head_value
        while(printvalue != None):
            print(printvalue.data_value)
            printvalue  = printvalue.next_value

    def InsertAtBeg(self, new_value = None):
        new_node = Node(new_value)
        new_node.next_value = self.head_value
        self.head_value = new_node

list1 = Listt()
list1.head_value = Node('Mon')
e2 = Node('Tue')
e3 = Node('Wed')

list1.head_value.next_value = e2
e2.next_value = e3

list1.InsertAtBeg('Sun')
list1.PrintList()
