class Node: #Creating each node
    def __init__(self,data_value = None):
        self.data_value = data_value
        self.next_value = None


class Train: #creating list (train) {Universal list creater, can create multiple list(train)}
    def __init__(self):
        self.head_value = None

List1 = Train()
List1.head_value = Node('Mon') # initiating head value with Mon (value)
e2 = Node('Tue') # giving value Tue (value) to second node
e3 = Node('Wed') # giving value Wed (value) to third node

List1.head_value.next_value = e2 # connecting head with e2 (first node with second) or storing address of next node
e2.next_value = e3 # connecting second node with third node

print(e2.next_value.data_value)


