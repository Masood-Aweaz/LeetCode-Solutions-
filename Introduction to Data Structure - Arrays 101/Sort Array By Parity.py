class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        odd = []
        even =[]
        for i in nums:
            if i%2==1:
                odd.append(i)
            else:
                even.append(i)
        #print(odd,even)
        even.extend(odd)
        print(even)
        return even
