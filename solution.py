from collections import Counter
import functools
class Solution(object):
    def common(self,str1,str2):
        dict1=Counter(str1)
        dict2=Counter(str2)
        common_dict=dict1 & dict2
        if len(common_dict)==0:
            return
        common_char=list(common_dict.elements())
        if len(common_char)==len(str1):
            return str2
    def mergedict(self,dict1,dict2):
        dict3={**dict1,**dict2}
        for key,value in dict3.items():
            if key in dict1 and key in dict2:
                list2=[value,dict1[key]]
                list2.sort(reverse=True)
                dict3[key]=list2[0]
        return dict3
    def makestr(self,list1):
        count=0
        dict4={}
        for i in range(0,len(list1)-1):
            count=count+1
            if not dict4:
                dict2=Counter(list1[i])
            else:
                dict2=dict4
            dict3= Counter(list1[count])
            dict4=self.mergedict(dict2,dict3)
        final_str=""
        for key,value in dict4.items():
            final_str=final_str+key*value
        return final_str   
    def wordSubsets(self, A, B):
        """
        :type A: List[str]
        :type B: List[str]
        :rtype: List[str]
        """
        res=[]
        i=self.makestr(B)
        for j in A:
            if len(j)>=len(i):
                res.append(self.common(i,j))
        results=list(filter(None,res))
        return results
listA=["amazon","apple","facebook","google","leetcode"]
listb=["e","o"]

result=Solution().wordSubsets(listA,listb)      
print(result)
               
                
            
        
        