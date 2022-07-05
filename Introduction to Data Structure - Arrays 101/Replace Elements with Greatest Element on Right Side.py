class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(0,len(arr)-1):
            max1=max(arr[i+1:])
            arr[i]=max1
        arr[-1]=-1
        return arr
