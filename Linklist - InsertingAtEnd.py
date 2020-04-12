class Node:
    def __init__(self, data_value = None):
        self.data_value = data_value
        self.next_value = None


class Listt:
    def __init__(self, head_value = None):
        self.head_value = head_value

    def PrintList(self):
        print_value = self.head_value
        while(print_value != None):
            print(print_value.data_value)
            print_value = print_value.next_value

    def InsertAtEnd(self, new_value):
        new_node = Node(new_value)
        if self.head_value == None: # if there is no node the head will be the first and last
            self.head_value = new_node
            return
        print_value = self.head_value
        while(print_value.next_value): #print_value.next_value and not print_value != None, because it will assign None value to itseld by which new_node will not be assigned to it further
            print_value = print_value.next_value
        print_value.next_value = new_node


list1 = Listt()
list1.head_value = Node('Mon')
e2 = Node('Tues')
e3 = Node('Wed')

list1.head_value.next_value = e2
e2.next_value = e3

list1.InsertAtEnd('Thru')
list1.PrintList()