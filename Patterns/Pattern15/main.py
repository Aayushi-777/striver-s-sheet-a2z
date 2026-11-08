class Solution:
    def pattern(self, n):
        for i in range(n-1, -1, -1):
            for j in range(i+1):
                print(chr(65+j), end=" ")
            print()
if __name__=="__main__":
    sol=Solution()
    n=5
    sol.pattern(n)

"""
Pattern is:        
A B C D E 
A B C D 
A B C 
A B 
A 
"""