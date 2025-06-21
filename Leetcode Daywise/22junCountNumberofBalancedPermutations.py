import math

class Solution:
    MOD = 10**9 + 7  # modulus for preventing integer overflow

    def modMul(self, a, b):
        return (a % self.MOD) * (b % self.MOD) % self.MOD  # modular multiplication

    def computeFactorial(self, n):
        self.fact = [1] * (n + 1)  # list to store factorial values up to n
        for i in range(1, n + 1):
            self.fact[i] = self.modMul(self.fact[i - 1], i)  # compute i! = (i-1)! * i

    def binaryExponentiation(self, a, b):
        res = 1  # initialize result
        while b > 0:
            if b & 1:
                res = self.modMul(res, a)  # multiply when current bit of b is set
            a = self.modMul(a, a)  # square the base
            b >>= 1  # move to the next bit
        return res  # return a^b % MOD

    def computeInverseFactorial(self, n):
        self.inverse_fact = [1] * (n + 1)  # list to store inverse factorials
        for i in range(n + 1):
            self.inverse_fact[i] = self.binaryExponentiation(self.fact[i], self.MOD - 2)  # use fermat's little theorem

    def countPermutation(self, digit, leftover, target):
        if digit == 10:
            # all digits tried, return 1 only if exact match on digit count and sum
            return self.tot_ways_to_permute if (leftover == 0 and target == 0) else 0
        if self.mem[digit][leftover][target] != -1:
            return self.mem[digit][leftover][target]  # return memoized result if already computed

        include_count = min(leftover, self.freq[digit])  # max count of current digit we can include
        if digit > 0:
            include_count = min(include_count, target // digit)  # bound by digit sum limit

        ans = 0  # initialize answer for current state

        for i in range(include_count + 1):
            # compute number of ways to pick i digits of this digit (multinomial part)
            ways_for_current_digit = self.modMul(self.inverse_fact[i], self.inverse_fact[self.freq[digit] - i])
            # recursively count valid permutations using remaining digits
            ans += ways_for_current_digit * self.countPermutation(digit + 1, leftover - i, target - digit * i)
            ans %= self.MOD  # apply modulo

        self.mem[digit][leftover][target] = ans  # memoize the result
        return ans  # return number of valid permutations

    def countBalancedPermutations(self, num: str) -> int:
        n = len(num)  # total number of digits
        sum_digits = 0  # initialize total sum of digits
        self.freq = [0] * 10  # frequency array to count each digit

        for ch in num:
            digit = int(ch)
            sum_digits += digit  # compute total digit sum
            self.freq[digit] += 1  # update digit frequency

        if sum_digits % 2 == 1:
            return 0  # cannot split odd sum into two equal halves

        target = sum_digits // 2  # target sum for both even and odd indexed digits

        self.computeFactorial(n)  # compute factorials up to n
        self.computeInverseFactorial(n)  # compute inverse factorials up to n

        half_len = n // 2  # number of digits on one side (even or odd positions)

        # total permutations = half_len! * (n - half_len)!
        self.tot_ways_to_permute = self.modMul(self.fact[half_len], self.fact[n - half_len])

        max_sum = 42 * 9  # upper bound on possible digit sum (for safety)
        # initialize memoization dp table: digit x leftover x target
        self.mem = [[[-1] * (max_sum + 1) for _ in range(half_len + 1)] for _ in range(10)]

        return self.countPermutation(0, half_len, target)  # start from digit 0
