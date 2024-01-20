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

 
    '''A doubly-linked ordered list of items, from lowest (head of list) to highest (tail of list)''' 
    def is_empty(self):
        if self.head is None:
            return True
        else:
            print("List is not empty")
            return False

        '''Returns True if OrderedList is empty MUST have O(1) performance''' 
    pass 
 
    def add(self, item): 
        '''Adds an item to OrderedList, in the proper location based on ordering of items 
        from lowest (at head of list) to highest (at tail of list) and returns True. 
        If the item is already in the list, do not add it again and return False. 
        MUST have O(n) average-case performance''' 
        new_node = Node(item)
        # condition to check if the list is empty
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return True
        else:
            current_node = self.head
            while current_node is not None:
                # check if current node is the item
                if current_node.value == item:
                    return False
            

    pass 
    
    def remove(self, item): 
        '''Removes the first occurrence of an item from OrderedList. If item is removed (was in the list) 
        returns True.  If item was not removed (was not in the list) returns False 
        MUST have O(n) average-case performance''' 
    pass 
    
    def index(self, item): 
        '''Returns index of the first occurrence of an item in OrderedList (assuming head of 
        list is index 0). If item is not in list, return None MUST have O(n) average-case performance''' 
    pass 
    
    def pop(self, index): 
        '''Removes and returns item at index (assuming head of list is index 0). If index is 
        negative or >= size of list, raises IndexError MUST have O(n) average-case performance''' 
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