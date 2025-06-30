#include <vector>
#include <algorithm>

class Solution {
public:
    const int MOD = 1e9 + 7;  // large prime for modulo to prevent overflow
    
    int numSubseq(std::vector<int>& nums, int target) {
        std::sort(nums.begin(), nums.end());  // sort the array to allow two-pointer scanning

        int n = nums.size();
        std::vector<int> pow2(n, 1);  // precompute powers of 2 modulo MOD

        // fill pow2[i] = 2^i % MOD
        for (int i = 1; i < n; ++i) {
            pow2[i] = (pow2[i - 1] * 2LL) % MOD;
        }

        int left = 0;         // pointer to the smallest element in subsequence
        int right = n - 1;    // pointer to the largest element in subsequence
        int result = 0;       // to store total number of valid subsequences

        while (left <= right) {
            // if sum of current smallest and largest is within target
            if (nums[left] + nums[right] <= target) {
                // count of subsequences is 2^(right - left)
                result = (result + pow2[right - left]) % MOD;
                ++left;  // move left to consider larger minimums
            } else {
                --right;  // move right to consider smaller maximums
            }
        }

        return result;  // return total valid subsequences modulo MOD
    }
};
