""" linked_list.py

Student: Mohamed Habidu
Mail: mohamed.habidu.3061@student.uu.se
Reviewed by: Anton 
Date reviewed: 25 April 2025
"""
class Person: ####################################################for Ex7
    def __init__(self, name, pnr):
        self.name = name
        self.pnr = pnr

    def __str__(self):
        return f"{self.name}:{self.pnr}"
    
    def __lt__(self, other):
        return self.pnr < other.pnr

    def __le__(self, other):
        return self.pnr <= other.pnr

    def __eq__(self, other):
        return self.pnr == other.pnr


class LinkedList:

    class Node:
        def __init__(self, data, succ):
            self.data = data
            self.succ = succ

    def __init__(self):
        self.first = None

    def __iter__(self):            # Discussed in the section on iterators and generators
        current = self.first
        while current:
            yield current.data
            current = current.succ

    def __in__(self, x):           # Discussed in the section on operator overloading
        for d in self:
            if d == x:
                return True
            elif x < d:
                return False
        return False

    def insert(self, x):
        if self.first is None or x <= self.first.data:
            self.first = self.Node(x, self.first)
        else:
            f = self.first
            while f.succ and x > f.succ.data:
                f = f.succ
            f.succ = self.Node(x, f.succ)

    def print(self):
        print('(', end='')
        f = self.first
        while f:
            print(f.data, end='')
            f = f.succ
            if f:
                print(', ', end='')
        print(')')

    # To be implemented

    def length(self):          ###################################   Ex1
        f= self.first
        len= 0
        while f:
            len +=1
            f= f.succ
        return len

  




    def remove_last(self):       ################################### Ex2
        if self.first == None: 
            raise ValueError("The list is empty")           #list is empty
        
        if self.first.succ == None:             #the list contains only one item
            removed = self.first.data
            self.first= None
            return removed 
        

        f= self.first                         # the list contains several items
        while f.succ.succ: 
            f= f.succ
        removed = f.succ.data
        f.succ= None
        return removed    

    def remove(self, x):         ################################### Ex3

        f= self.first     
        if f is None:               
            return False            #list is empty
        if f.data== x:              
            self.first = f.succ
            return True             # x is in first element
        while f.succ:               # x is in other elements 
            if f.succ.data == x: 
                f.succ= f.succ.succ
                return True
            f= f.succ 
        return False
        
        


    def to_list(self):  # Ex4
        def _to_list(f):
            if f is None:
                return []
            return [f.data] + _to_list(f.succ)

        return _to_list(self.first)
    




    def __str__(self):                  ################################### Ex5
        return f"({', '.join(str(x) for x in self)})"

    def copy(self):
        result = LinkedList()
        for x in self:
            result.insert(x)
        return result
    
    ''' Complexity for this implementation = O(n²)
    '''

    def copy(self):               ################################## Ex6, Should be more efficient
        result = LinkedList()
        f= self.first
        latest= None
        while f: 
            copied_element = LinkedList.Node(f.data, None) 
            if latest is None:
                result.first = copied_element   # inserting the first node
                latest = copied_element  # updating the latest node in result list
            else:
                latest.succ = copied_element
                latest = copied_element
            f = f.succ  # Move next in orignal
        return result    
    
    ''' Complexity for this implementation = O(n)
    '''


def main():
    lst = LinkedList()
    for x in [1, 1, 1, 2, 3, 3, 2, 1, 9, 7]:
        lst.insert(x)
    lst.print()

    # Test code:

    plst = LinkedList()
    p= Person("Alex","20250101-0000")
    plst.insert(p)
    q= Person("Oscar","20000101-0000")
    plst.insert(q)

    print(plst)



if __name__ == '__main__':
    main()
