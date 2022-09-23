
class Node(object):
    def __init__(self, x = 0):
        self.value = x
        self.next = None 
 
class Solution (object):
    def addingTwoLinklist(self, list1, list2):
        dummyNode = Node(0)
        curr = dummyNode
        carry = 0
        
        while list1 != None or list2 != None or carry != 0:
            value1 = list1.value if list1 else 0
            value2 = list2.value if list2 else 0
            tempSum = value1 + value2 + carry
            carry = tempSum // 10
            extra = tempSum % 10
            newNode = Node(extra)
            curr.next = newNode
            curr = newNode
            list1 = list1.next if list1 else None
            list2 = list2.next if list2 else None
        return dummyNode.next    
            
    

        
        
node1 = Node(1)

node1.next = Node(2)
node1.next.next = Node(3)

node2 = Node(4)
node2.next = Node(5)
node2.next.next = Node(9)

answer = (Solution().addingTwoLinklist(node1, node2))
while answer:
    print(answer.value, end=' ')
    answer = answer.next




