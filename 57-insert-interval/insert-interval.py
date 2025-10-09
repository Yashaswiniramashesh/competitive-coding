class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        res = []

        i = 0
        n = len(intervals)
        start = 0
        end = 1

        while i < n and( newInterval[start] > intervals[i][end]):
            res.append(intervals[i])
            i += 1

        while i < n and intervals[i][start] <= newInterval[end]:
            newInterval[start] = min(intervals[i][start], newInterval[start])
            newInterval[end] = max(intervals[i][end], newInterval[end])
            i += 1

        res.append(newInterval)

        while i < n:
            res.append(intervals[i])
            i += 1

        return res