class Solution(object):
    def isPerfectSquare(self, num):
         x = int(num ** 0.5)
         return x * x == num 
