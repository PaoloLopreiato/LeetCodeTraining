class MinStack(object):

    def __init__(self):
        self.minStack = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.minStack.append(val)
        

    def pop(self):
        """
        :rtype: None
        """
        self.minStack[:-1]
        

    def top(self):
        """
        :rtype: int
        """
        return self.minStack[len(self.minStack)]
        

    def getMin(self):
        """
        :rtype: int
        """
        return min(sorted(self.minStack))
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()