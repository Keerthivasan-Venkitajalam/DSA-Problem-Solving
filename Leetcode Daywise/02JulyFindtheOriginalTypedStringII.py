class Solution:
    def possibleStringCount(self, word: str, k: int) -> int:
        mod = 10**9 + 7  # define the modulo value for large number handling
        n, cnt = len(word), 1  # n: length of word, cnt: to count frequency of repeated characters
        freq = []  # list to store length of each block of consecutive same characters

        # loop through the word to find runs of repeated characters
        for i in range(1, n):
            if word[i] == word[i - 1]:
                cnt += 1  # increase count for current run
            else:
                freq.append(cnt)  # store the length of the current group
                cnt = 1  # reset count for the next group
        freq.append(cnt)  # don't forget to append the last group

        ans = 1  # total ways = product of ways for each block
        for o in freq:
            ans = ans * o % mod  # multiply each block's contribution (each char can be deleted once except one)

        # if the number of blocks is at least k, then all deletions are fine
        if len(freq) >= k:
            return ans

        # dynamic programming: count invalid ways to remove from at most k groups
        f = [1] + [0] * (k - 1)  # f[i]: number of ways to delete i chars using current prefix of blocks
        g = [1] * k  # prefix sum array to speed up range sum queries on f

        for i in range(len(freq)):
            f_new = [0] * k  # new state for f after considering freq[i]-th group
            for j in range(1, k):
                f_new[j] = g[j - 1]  # add number of ways to use j deletions
                if j - freq[i] - 1 >= 0:
                    # subtract the number of invalid ways that exceed block size
                    f_new[j] = (f_new[j] - g[j - freq[i] - 1]) % mod
            # update prefix sum g for new f
            g_new = [f_new[0]] + [0] * (k - 1)
            for j in range(1, k):
                g_new[j] = (g_new[j - 1] + f_new[j]) % mod
            f, g = f_new, g_new  # move to next state

        # subtract the number of invalid deletions from total possible answers
        return (ans - g[k - 1]) % mod
