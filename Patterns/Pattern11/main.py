class Solution:
    def pattern(self, n):
        for i in range(1, n+1):
            if i%2==0:
                start=0
            else:
                start=1
            for j in range(1, i+1):
                print(start, end=" ")
                start=1-start
            print()
if __name__=="__main__":
    sol=Solution()
    n=5
    sol.pattern(n)

"""
Pattern is:        
1 
0 1
1 0 1
0 1 0 1
1 0 1 0 1
"""