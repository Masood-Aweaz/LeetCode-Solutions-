class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        arr.sort(reverse=False)
        print(arr)
        for i in range(len(arr)):
            temp = arr[i] 
            double = temp*2
            half = temp/2
            print(arr[i+1:])
            if double in arr[i+1:]:
                return True
            if half in arr[i+1:]:
                return True
        return False
