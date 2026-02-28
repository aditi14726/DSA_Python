class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        ans=float('inf')
        for i in range(len(landStartTime)):
            for j in range(len(waterStartTime)):
                finishLand= landStartTime[i] + landDuration[i]
                total1= max(finishLand,waterStartTime[j]) +waterDuration[j]

                finishWater= waterStartTime[j] + waterDuration[j]
                total2= max(finishWater, landStartTime[i]) +landDuration[i]

                ans= min(ans, total1, total2)
        return ans 