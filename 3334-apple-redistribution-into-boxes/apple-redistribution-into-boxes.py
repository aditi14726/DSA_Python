class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        s=0
        curr_capacity=0 
        box=0
        capacity.sort(reverse=True)
        s=sum(apple)
        for cap in capacity:
            curr_capacity+=cap
            box+=1
            if(curr_capacity>=s):
                return box

        