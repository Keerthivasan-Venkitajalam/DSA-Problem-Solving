#include <unordered_map>
#include <vector>
#include <algorithm>

class Solution {
public:
    int findLHS(std::vector<int>& nums) {
        std::unordered_map<int, int> freq;  // map to store frequency of each number
        int longest = 0;  // variable to keep track of the longest harmonious subsequence

        // count the frequency of each number in the array
        for (int num : nums) {
            freq[num]++;
        }

        // iterate through all keys in the map
        for (auto& [key, value] : freq) {
            // check if there exists an adjacent number (key + 1)
            if (freq.count(key + 1)) {
                // update the longest length by comparing with current potential harmonious subsequence
                longest = std::max(longest, value + freq[key + 1]);
            }
        }

        return longest;  // return the length of the longest harmonious subsequence
    }
};
