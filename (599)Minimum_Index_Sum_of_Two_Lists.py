'''********************************************************************************** 
Suppose Andy and Doris want to choose a restaurant for dinner, and they both have a list of favorite restaurants represented by strings.

You need to help them find out their common interest with the least list index sum. If there is a choice tie between answers, output all of them with no order requirement. You could assume there always exists an answer.


Input: list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]
Output: ["Shogun"]
Explanation: The only restaurant they both like is "Shogun".
**********************************************************************************'''

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        res=[]
        d=dict()
        inter = [value for value in list1 if value in list2]
        #temp = max(len(list1),len(list2))
        print(inter)
        if len(inter)==1:
            return inter
        else:
            for i in inter:
                index_sum = list1.index(i)+list2.index(i)
                d[i]=index_sum
            #print(d)
            m = min(d.values())
            #print(m)
            for j in d:
                if d[j]==m:
                    res.append(j)
        return res
