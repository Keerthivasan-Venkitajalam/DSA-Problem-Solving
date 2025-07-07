class Solution {
public:
    vector<string> letterCombinations(string digits) {
        // result vector to store combinations
        vector<string> result;

        // if digits is empty, return empty result
        if (digits.empty()) return result;

        // map digits to corresponding characters
        vector<string> mapping = {
            "",     // 0
            "",     // 1
            "abc",  // 2
            "def",  // 3
            "ghi",  // 4
            "jkl",  // 5
            "mno",  // 6
            "pqrs", // 7
            "tuv",  // 8
            "wxyz"  // 9
        };

        // Temporary string to hold the current combination
        string current;

        // Start backtracking
        backtrack(digits, 0, current, result, mapping);

        return result;
    }

private:
    void backtrack(const string &digits, int index, string &current, vector<string> &result, const vector<string> &mapping) {
        // Base case: if the current combination is the same length as digits, store it
        if (index == digits.length()) {
            result.push_back(current);
            return;
        }

        // Get the digit at current index
        int digit = digits[index] - '0';

        // Loop through all characters that digit can represent
        for (char c : mapping[digit]) {
            current.push_back(c);                   // Choose
            backtrack(digits, index + 1, current, result, mapping);  // Explore
            current.pop_back();                     // Un-choose (backtrack)
        }
    }
};
