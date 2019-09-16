class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        start = []
        end = []
        for lst in intervals:
            start.append(lst[0])
            end.append(lst[1])
        start.sort()
        end.sort()
        rooms, available = 0,0
        s , e = 0,0 
        while s < len(start):
            if start[s] < end[e]:
                if available == 0:
                    rooms += 1
                else:
                    available -= 1
                s += 1  
            else:
                available += 1 
                e += 1
        return rooms
        