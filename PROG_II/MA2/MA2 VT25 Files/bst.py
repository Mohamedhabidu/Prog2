""" bst.py

Student: Mohamed Habidu
Mail: mohamed.habidu.3061@student.uu.se
Reviewed by: Anton
Date reviewed: 25 April 2025
"""


from linked_list import LinkedList


class BST:

    class Node:
        def __init__(self, key, left=None, right=None):
            self.key = key
            self.left = left
            self.right = right

        def __iter__(self):     # Discussed in the text on generators
            if self.left:
                yield from self.left
            yield self.key
            if self.right:
                yield from self.right

    def __init__(self, root=None):
        self.root = root

    def __iter__(self):         # Dicussed in the text on generators
        if self.root:
            yield from self.root

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, r, key):
        if r is None:
            return self.Node(key)
        elif key < r.key:
            r.left = self._insert(r.left, key)
        elif key > r.key:
            r.right = self._insert(r.right, key)
        else:
            pass  # Already there
        return r

    def print(self):
        self._print(self.root)

    def _print(self, r):
        if r:
            self._print(r.left)
            print(r.key, end=' ')
            self._print(r.right)

    '''def contains(self, k): # given function(iteration)
        n = self.root
        while n and n.key != k:
            if k < n.key:
                n = n.left
            else:
                n = n.right
        return n is not None'''

   

    def contains(self, k):  # ##########################  Ex8 - recursive contains
        return self._contains(self.root, k)

    def _contains(self, node, k):
            if node is None:
                return False
            if node.key == k:
                return True
            elif k < node.key:
                return self._contains(node.left, k)
            else:
                return self._contains(node.right, k)




    def size(self):
        return self._size(self.root)

    def _size(self, r):
        if r is None:
            return 0
        else:
            return 1 + self._size(r.left) + self._size(r.right)

#
#   Methods to be completed
#

    def height(self):       ###########################Ex9     
    
        return self._height(self.root)

    def _height(self, r):
        if r is None:
            return 0
        else:
            return 1 + max(self._height(r.left), self._height(r.right))


    def __str__(self):                ###########################Ex10       
      
        return f"<{', '.join(str(k) for k in self)}>"


    def to_list(self):                             ###########################Ex11 
        result = []
        self._to_list(self.root, result)
        return result

    def _to_list(self, r, result):
        if r is None:
            return
        self._to_list(r.left, result)
        result.append(r.key)
        self._to_list(r.right, result)
    """
Complexity of to_list: O(n), every node visited once.
"""

    def to_LinkedList(self):               ##########################Ex12
   
        ll = LinkedList()                    
        latest = None
        for key in self:
            new_node = LinkedList.Node(key, None)
            if ll.first is None:
                ll.first = new_node
                latest = new_node
            else:
                latest.succ = new_node
                latest = new_node
        return ll
    '''Complexity of _LinkedList: O(n)'''


                           
    def remove(self, key): #
        self.root = self._remove(self.root, key)

    def _remove(self, r, k):                    ########################## Ex13
        if r is None:
            return None
        elif k < r.key:
            r.left = self._remove(r.left, k)
            # r.left = left subtree with k removed
        elif k > r.key:
            r.right = self._remove(r.right, k)
            # r.right =  right subtree with k removed
        else:  # This is the key to be removed
            if r.left is None:     # Easy case(no children)
                return r.right
            elif r.right is None:  # Also easy case
                return r.left
            else:  # This is the tricky case.
                min_key = self._min(r.right)
                r.key = min_key
                r.right = self._remove(r.right, min_key)
                


                # Find the smallest key in the right subtree
                # Put that key in this node
                # Remove that key from the right subtree
        return r  # Remember this! It applies to some of the cases above

    def _min(self, r):
        while r.left:
          r = r.left
        return r.key

def main():
    t = BST()
    for x in [4, 1, 3, 6, 7, 1, 1, 5, 8]:
        t.insert(x)
    t.print()
    print()

    print('size  : ', t.size())
    for k in [0, 1, 2, 5, 9]:
        print(f"contains({k}): {t.contains(k)}")


if __name__ == "__main__":
    main()


"""
Ex####################################################14: What is the generator good for?
==============================

1. computing size? yes
2. computing height? no
3. contains? yes
4. insert? no 
5. remove? no

"""
