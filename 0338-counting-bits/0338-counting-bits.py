class Solution:
    def countBits(self, n: int) -> List[int]:
        def cnt(n):
            count = 0 
            while n > 0:
                n = n &(n-1)
                count +=1 
            return count

        return [cnt(i) for i in range(n+1)]
