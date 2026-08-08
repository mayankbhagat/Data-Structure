class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        temp=n
        sum=0
        prd=1
        while n>0:
            r=n%10
            n//=10

            sum+=r
            prd*=r
        return prd-sum

        