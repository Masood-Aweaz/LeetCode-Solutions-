class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights)
        #print(expected)
        x = zip(heights,expected)
        count = 0
        for i in x:
            print(i)
            if i[0]!=i[1]:
                count+=1
        return count
