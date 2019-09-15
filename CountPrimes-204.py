class Solution:
    def countPrimes(self, n: int) -> int:
        prime = [True] * n
        count = 0
        for i in range(2, n):
            if prime[i]:
                count +=1
                print(i)
                j = 2*i
                while j<n:
                    prime[j]=False
                    j+=i
        return count
        