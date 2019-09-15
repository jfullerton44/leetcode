class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        output = []
        intervals = sorted(intervals, key=lambda i:i[0])
        for i in intervals:
            if len(output) == 0:
                output.append(i)
            elif i[0] <= output[-1][1]:
                output[-1][1] = max(i[1], output[-1][1])
            else:
                output.append(i)
        return output