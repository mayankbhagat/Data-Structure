class Solution:
    def countDigits(self, num: int) -> int:
        og=num
        count=0
        while num>0:
            r=num%10
            
            if og%r==0 and r!=0:
                count+=1
            num//=10
        return count