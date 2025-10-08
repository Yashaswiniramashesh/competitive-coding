class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        print(intervals)
        intervals = sorted(intervals)
        print(intervals)
        res = []

        for curr_interval in intervals:
            if not res :
                res.append(curr_interval)
            else:
                start = 0
                end = 1
                top_interval = res[-1]
                if top_interval[end] >= curr_interval[start]:
                    new_interval = [min(top_interval[start],curr_interval[start]), max(top_interval[end], curr_interval[end])]
                    res[-1] = new_interval
                else:
                    res.append(curr_interval)

        return res
