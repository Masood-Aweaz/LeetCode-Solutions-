class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        min_len = min([len(x) for x in strs])
       
        for i in range(min_len):
            co = [x[:min_len] for x in strs]
            if((len(set(co)))==1):
                return strs[0][:min_len]
            min_len-=1
        return ""
