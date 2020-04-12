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

    def AtAnyPoint(self, loc = None , value = None):
        new_node = Node(value)
        print_value = self.head_value

        if print_value.next_value == None:
            print_value.next_value = new_node
            return
        for i in range(loc - 2 ):
            print_value = print_value.next_value

        new_node.next_value = print_value.next_value # we are assigning the remaining list, to the next of node here
        print_value.next_value = new_node # here we are assigning the next value of print equal to new_node means None



list1 = Listt()
list1.head_value = Node('Mon')
e2 = Node('Sat')
# e3 = Node('Sat')
# e4 = Node('Thru')
# e5 = Node('Sat')

list1.head_value.next_value = e2
# e2.next_value = e3
# e3.next_value = e4
# e4.next_value = e5

list1.AtAnyPoint(2 ,'Tues')
list1.AtAnyPoint(3 ,'Wed')
list1.AtAnyPoint(4, 'Thru')
list1.AtAnyPoint(5, 'Fri')

list1.PrintList()