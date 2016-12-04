class DLLNode:

    def __init__(self, item, prevnode, nextnode):
        self.element = item
        self.next = nextnode
        self.prev = prevnode

    def __str__(self):
        output = ""
        output += str(self.element)
        return output

class DLinkedList:
    
    def __init__(self):
        self.head = DLLNode(None, None, None)
        self.tail = DLLNode(None, self.head, None)
        self.head.next = self.tail
        self.size = 0
        self.cursor = None
        
    def add_at_end(self, item):
        n1 = self.tail.prev
        newnode = DLLNode(item, None, None)
        n1.next.prev = newnode
        newnode.next = n1.next
        newnode.prev = n1
        n1.next = newnode
        self.size += 1
        
    def next(self):
        if self.cursor == None or self.cursor.next == None:
            self.cursor = self.head.next
        else:
            self.cursor = self.cursor.next       

    def prev(self):
        if self.cursor == None or self.cursor.prev == None:
            self.cursor = self.tail.prev

        else:
            self.cursor = self.cursor.prev
            
    def getCursor(self):
        return self.cursor.element
    
    def move_to_front(self):
        self.cursor = self.head
        
    def swap_adjacent(self, n1, n2):
        n1.prev.next = n2
        n2.next.prev = n1
        n2.prev = n1.prev
        n1.next = n2.next
        n1.prev = n2
        n2.next = n1
        
    def get_pos(self, n1):
        pos = 1
        node = self.head.next
        while node.element != n1:
            node = node.next
            pos += 1
        return(pos)

    def clear(self):
        counter = 0
        node = self.head
        while counter > self.size:
            node.prev = None
            node.element = None
            temp = node.next
            node.next = None
            node = temp
            counter += 1
        self.tail.prev = self.head
        self.head.next = self.tail
        self.size = 0

    def __str__(self):
        outstr = "-"
        node = self.head
        while node:
            outstr = outstr + str(node.element) + "-"
            node = node.next
        return outstr

class Board(DLinkedList):

    def __init__(self):
        DLinkedList.__init__()
        self.corner1 = (1, go_method)
        self.corner2 = (11, jail_method)
        #self.corner3 = (21, parking_method)
        #self.corner4 = (31, go_to_jail_method)

    def fill_board(self, lst):
        for i in lst:
            self.add_to_end(i)

    def move(self, player, dice_res):
        self.cursor = player.cursor
        for i in range(dice_res):
            self.cursor = self.cursor.next
            self.check(player) 

        player.cursor = self.cursor

    def check(self, player):
        pos = self.get_pos(player.cursor)
        if pos == self.corner1[0]:
            self.corner1[1](player)
        elif pos == self.corner2[0]:
            self.corner2[1](player)

    def go_method(self, player):
        player.funds += 200

    def jail_method(self, player):
        self.cursor = player.cursor


lst=[]
crumlin = Property("Crumlin", 60, "brown", 50, 2)
kimmage = Property("Kimmage", 60, "brown", 50, 4)
"""........................................................."""
lst+=[crumlin,kimmage.......]
board = Board()
board.fill_board(lst)