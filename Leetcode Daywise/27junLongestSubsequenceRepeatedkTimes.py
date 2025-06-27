from collections import deque

class Solution:
    def countSubsequences(self, s: str, next_str: str) -> int:
        i = 0  # pointer for the main string s
        j = 0  # pointer for the target subsequence next_str
        m = len(next_str)  # length of the subsequence to match
        subsequence_count = 0  # to count how many times next_str occurs in s as a subsequence

        while i < len(s):  # iterate through string s
            if s[i] == next_str[j]:  # if characters match, move to the next character in next_str
                j += 1
                if j == m:  # full match found
                    j = 0  # reset pointer to start looking for another occurrence
                    subsequence_count += 1
            i += 1  # move to next character in s

        return subsequence_count  # return total occurrences of next_str in s

    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        n = len(s)  # total length of the input string
        freq = [0] * 26  # frequency array for characters a to z

        for c in s:
            freq[ord(c) - ord('a')] += 1  # count how many times each character appears in s

        curr = ""  # current candidate string (starts empty)
        queue = deque()  # initialize a queue for BFS
        queue.append(curr)  # start BFS with an empty string
        res = ""  # to store the best valid result found so far

        while queue:  # BFS loop
            curr = queue.popleft()  # get the next string to explore

            # try extending current string by adding one character at the end
            for c in range(ord('a'), ord('z') + 1):
                char = chr(c)  # convert ASCII code to character

                # skip if the character does not appear at least k times in s
                if freq[c - ord('a')] < k:
                    continue

                next_str = curr + char  # form new string by appending the current character

                # check how many times next_str occurs in s as a subsequence
                if self.countSubsequences(s, next_str) >= k:
                    res = next_str  # update result if it's a valid subsequence
                    queue.append(next_str)  # explore further extensions of next_str

        return res  # return the longest valid subsequence found
