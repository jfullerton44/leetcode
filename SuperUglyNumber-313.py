import math

class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        positions = [0] * len(primes)
        ret = []
        ret.append(1)
        while len(ret) < n:
            low = 10 ** 100
            for i in range(len(primes)):
                low = min(primes[i]*ret[positions[i]], low)
            for i in range(len(primes)):
                if low == primes[i]*ret[positions[i]]:
                    positions[i] = positions[i] + 1
            ret.append(low)
        return ret.pop()