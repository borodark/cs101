class Tree:
    """Abstract base class representing a tree structure."""
    #------------------------------- nested Position class -------------------------------
    class Position:
        """An abstraction representing the location of a single element."""
        def element(self):
            """Return the element stored at this Position."""
            raise NotImplementedError( must be implemented by subclass )
        def     eq     (self, other):
            """Return True if other Position represents the same location."""
            raise NotImplementedError( must be implemented  by subclass )
        def     ne     (self, other):
            """Return True if other does not represent the same location."""
            return not (self == other) # opposite of     eq
    # ---------- abstract methods that concrete subclass must support ----------
    def root(self):
        """Return Position representing the tree s root (or None if empty)."""
        raise NotImplementedError( must be implemented by subclass )
    def parent(self, p):
        """Return Position representing p s parent (or None if p is root)."""
        raise NotImplementedError( must be implemented by subclass )
    def num children(self, p):
        """Return the number of children that Position p has."""
        raise NotImplementedError( must be implemented by subclass )
    def children(self, p):
        """Generate an iteration of Positions representing p s children."""
        raise NotImplementedError( must be implemented by subclass )
    def len (self):
        """Return the total number of elements in the tree."""
        raise NotImplementedError( must be implemented by subclass )

    # ---------- concrete methods implemented in this class ----------
    def is root(self, p):
        """Return True if Position p represents the root of the tree."""
        return self.root( ) == p
    def is leaf(self, p):
        """Return True if Position p does not have any children."""
        return self.num children(p) == 0
    def is empty(self):
        """Return True if the tree is empty."""
        return len(self) == 0

    """Return the number of levels separating Position p from the root."""
    def depth(self, p):
        if self.is root(p):
            return 0
        else:
            return 1 + self.depth(self.parent(p))

    def height(self, p=None):
        """Return the height of the subtree rooted at Position p.
        If p is None, return the height of the entire tree. """
        if p is None:
            p = self.root()
        return self.height2(p) # start height2 recursion

    def height1(self): # works, but O(nˆ2) worst-case time Return the height of the tree.
        return max(self.depth(p) for p in self.positions( ) if self.is leaf(p))

    def height2(self, p): # time is linear in size of subtree
        """Return the height of the subtree rooted at Position p"""
        if self.is leaf(p):
            return 0
        else:
            return 1 + max(self. height2(c) for c in self.children(p))
