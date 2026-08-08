class Solution:
    def isPalindrome(self, x: int) -> bool:
        temp=x
        num=0
        while x>0:
            r=x%10
            x//=10
            num=(num*10+r)
        if temp==num:
            return True
        else:
            return False
        