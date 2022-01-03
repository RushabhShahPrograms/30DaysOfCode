class Solution:
   def solve(self, num):
      if(num == 0):
         return 0
      length = 1
      while(num != 1):
         num = (num / 2) if num % 2 == 0 else (3 * num + 1)
         length += 1
      return length
ob = Solution()
a = int(input())
print(ob.solve(a))
