class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {'(':')','[':']','{':'}'}
        stack = []
        for i in s:
            if i in brackets.keys():
                stack.append(i)
            elif stack and i==brackets[stack[-1]]:
                stack.pop(-1)
            else:
                return False
        return len(stack)==0
