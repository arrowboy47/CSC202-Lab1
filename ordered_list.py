from dataclasses import dataclass 
@dataclass 
class Node:
    value: int     
    prev_node: None     
    next_node: None    
         
@dataclass 
class doubly_Ordered_List: 
    head: 'Node' = None
    tail: 'Node' = None
    # average of all the values in the list
    average: int = None

    # going to be used to determine wither the starting node is the head or tail
    def get_avg(self):
        current_node = self.head
        sum = 0
        count = 0
        while current_node is not None:
            sum += current_node.value
            count += 1
            current_node = current_node.next_node
        self.average = sum/count
        return self.average

    def det_start_pos(self, value):
        if self.average > value:
            return self.head
        elif self.average < value:
            return self.tail
        else:
            return self.head
 
    '''A doubly-linked ordered list of items, from lowest (head of list) to highest (tail of list)''' 
    '''Returns True if OrderedList is empty MUST have O(1) performance''' 
    def is_empty(self):
        if self.head is None:
            return True
        else:
            print("List is not empty")
            return False
 
    def add(self, item): 
        '''Adds an item to OrderedList, in the proper location based on ordering of items 
        from lowest (at head of list) to highest (at tail of list) and returns True. 
        If the item is already in the list, do not add it again and return False. 
        MUST have O(n) average-case performance''' 
        new_node = Node(item)

        # determine the starting position
        # check if there is an average value and list isnt empty
        if self.average is None and self.is_empty() is False:
            self.get_avg()
            startpos = self.det_start_pos(item)
        elif self.is_empty() is True:
            # condition to check if the list is empty
            self.head = new_node
            self.tail = new_node
            return True
        else:
            # condition where avg is already calculated
            startpos = self.det_start_pos(item)

        current_node = startpos
        while current_node is not None:
            # check if current node is the item
            if current_node.value == item:
                return False
            # check if value is greater than the current node
            if current_node.value < item:
                # add it after current node
                new_node.next_node = current_node.next_node
                new_node.prev_node = current_node
                current_node.next_node = new_node
                return True
            else:
                # determine derection to go
                if startpos == self.head:
                    current_node = current_node.next_node
                else:
                    current_node = current_node.prev_node


    def remove(self, item): 
        '''Removes the first occurrence of an item from OrderedList. If item is removed (was in the list) 
        returns True.  If item was not removed (was not in the list) returns False 
        MUST have O(n) average-case performance'''

        # determine the starting position
        # check if there is an average value and list isnt empty
        if self.average is None and self.is_empty() is False:
            self.get_avg()
            startpos = self.det_start_pos(item)
        elif self.is_empty() is True:
            # condition to check if the list is empty
            return False
        else:
            # condition where avg is already calculated
            startpos = self.det_start_pos(item)

        current_node = startpos
        while current_node is not None:
            # check if current node is the item
            if current_node.value == item:
                # check if the current node is the head
                if current_node == self.head:
                    self.head = current_node.next_node
                    return True
                # check if the current node is the tail
                elif current_node == self.tail:
                    self.tail = current_node.prev_node
                    return True
                else:
                    current_node.prev_node.next_node = current_node.next_node
                    current_node.next_node.prev_node = current_node.prev_node
                    return True
            else:
                # determine derection to go
                if startpos == self.head:
                    current_node = current_node.next_node
                else:
                    current_node = current_node.prev_node

        # item was not in list
        return False
    
    def index(self, item): 
        '''Returns index of the first occurrence of an item in OrderedList (assuming head of 
        list is index 0). If item is not in list, return None MUST have O(n) average-case performance''' 
        #check if list is empty
        if self.is_empty():
            return None
        else:
            index = 0
            current_node = self.head
            while current_node is not None:
                # check if current node is the item
                if current_node.value == item:
                    return index
                else:
                    current_node = current_node.next_node
                    index += 1
            # item was not in list
            return None
    
    def pop(self, index): 
        '''Removes and returns item at index (assuming head of list is index 0). If index is 
        negative or >= size of list, raises IndexError MUST have O(n) average-case performance''' 
        if self.is_empty():
            raise IndexError("List is empty") 
        else:
            current_node = self.head
            current_index = 0
            while current_node is not None:
                if current_index == index:
                    '''rewriting remove code rather than calling remove method, 
                    so it doesnt have to traverse the list again'''
                    # check if the current node is the head
                    if current_node == self.head:
                        self.head = current_node.next_node
                        return current_node.value
                    # check if the current node is the tail
                    elif current_node == self.tail:
                        self.tail = current_node.prev_node
                        return current_node.value
                    else:
                        current_node.prev_node.next_node = current_node.next_node
                        current_node.next_node.prev_node = current_node.prev_node
                        return current_node.value
                else:
                    current_node = current_node.next_node
                    current_index += 1
            raise IndexError("Index out of range")

    pass 
    
    def search(self, item): 

        '''Searches OrderedList for item, returns True if item is in list, False otherwise" 
        To practice recursion, this method must call a RECURSIVE method that will search the list 
        MUST have O(n) average-case performance''' 
    pass 
    
    def python_list(self): 
        '''Return a Python list representation of OrderedList, from head to tail 
        For example, list with integers 1, 2, and 3 would return [1, 2, 3] 
        MUST have O(n) performance''' 
    pass 
    
    def python_list_reversed(self): 
        '''Return a Python list representation of OrderedList, from tail to head, using 
        recursion For example, list with integers 1, 2, and 3 would return [3, 2, 1] 
        To practice recursion, this method must call a RECURSIVE method that 
        will return a reversed list MUST have O(n) performance''' 
    pass 
    
    def size(self): 
        '''Returns number of items in the OrderedList To practice recursion, this method must call a RECURSIVE 
        method that will count and return the number of items in the list MUST have O(n) performance''' 
    pass