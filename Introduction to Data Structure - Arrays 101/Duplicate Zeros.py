class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        i=0
        count=0
        n=len(arr)
        while(i<n):
            if arr[i]==0:
                j=i+1
                arr.insert(j,0)
                count+=1
                i=i+2
            else:
                i=i+1
        #print(arr[:n])
        for i in range(count):
            del arr[-1]
    
