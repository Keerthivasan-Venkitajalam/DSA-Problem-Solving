class Solution:
    def minSteps(self, n: int) -> int:
        #initialize result to store total number of operations
        res = 0
        #start checking from the smallest prime factor
        i = 2
        #loop until i*i exceeds n
        while i * i <= n:
            #check if i is a factor of n
            while n % i == 0:
                #if i divides n, add i to result
                #this represents one copy and (i - 1) paste operations
                res += i
                #divide n by i and continue with the reduced value
                n //= i
            #move to the next possible factor
            i += 1
        #if n is greater than 1, it must be a prime number
        #add it to the result as one last set of operations
        if n > 1:
            res += n
        
        #return the total number of operations
        return res
