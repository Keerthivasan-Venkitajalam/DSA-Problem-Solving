class Solution:
    def myPow(self, x: float, n: int) -> float:
        # handle negative exponent by inverting x and making n positive
        if n < 0:
            x = 1 / x
            n = -n

        result = 1.0  # initialize result

        while n > 0:
            if n % 2 == 1:
                result *= x  # if current bit is set, multiply result by x
            x *= x  # square the base
            n //= 2  # shift exponent right by 1 (i.e., divide by 2)

        return result  # return final result after processing all bits
