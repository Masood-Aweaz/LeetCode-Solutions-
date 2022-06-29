class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ans=[]
        i=1
        while(i<=n):
            #print(i)
            if i%3==0 and i%5==0:
                ans.append("FizzBuzz")
            elif i%3==0:
                ans.append("Fizz")
            elif i%5==0:
                ans.append("Buzz")
            else:
                ans.append(str(i))
            i=i+1
        print(ans)
        return ans
                
            
