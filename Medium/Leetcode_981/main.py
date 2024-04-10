"""
Input
["TimeMap", "set", "get", "get", "set", "get", "get"]
[[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 5]]
Output
[null, null, "bar", "bar", null, "bar2", "bar2"]
"""

def main():
    ...

class TimeMap():
    def __init__(self):
        self.dict = {} 

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        if key not in self.dict:
            self.dict[key] = []
        self.dict[key].append((timestamp, value))

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        if key not in self.dict:
            return ""
        
        timestamps = self.data[key]
        left, right = 0, len(timestamps) - 1
        
        while left <= right:
            mid = (left + right) // 2
            if timestamps[mid][0] == timestamp:
                return timestamps[mid][1] #Value
            elif timestamps[mid][0] < timestamp:
                left = mid + 1
            else:
                right = mid - 1
        
        if right >= 0:
            return timestamps[right][1]
        else:
            return ""