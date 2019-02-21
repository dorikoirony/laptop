# -*- coding:utf-8 -*-
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        a=list(numbers)
        b=[1]*len(a)
        for i in range(len(a)):
            for j in range(i+1,len(a)) :
                if a[i]==a[j]:
                    b[i]+=1
        c=0
        for k in range(len(b)):
            if b[k]>(len(a)/2):
                c=2
        print(b)
        return c


ass=[1,2,2,2,3,3,3,4,4,4,4,4,4,4,4]
Solution().MoreThanHalfNum_Solution(ass)
