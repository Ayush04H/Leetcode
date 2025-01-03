class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        def josp(n,k):
            if n == 1:
                return 1
            return ((josp(n-1,k)+ (k-1)) %n+1)

        return josp(n,k)
        