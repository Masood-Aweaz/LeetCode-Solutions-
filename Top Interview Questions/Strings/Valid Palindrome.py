class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        temp=""
        for i in s:
            if i.isalnum()==True:
                temp = temp+i
        rev = temp[::-1]
        if(temp==rev):
            return True
        else:
            return False
