class Solution {
public:
    // Helper function to shift character 'c' forward by 'step' positions with wrap around
    char shiftChar(char c, int step) {
        return (c - 'a' + step) % 26 + 'a';
    }

    char kthCharacter(int k) {
        int len = 1, level = 0;

        // Step 1: Find the minimum level such that the total length ≥ k
        while (len < k) {
            len *= 2;
            level++;
        }

        // Step 2: Simulate the process in reverse to find original character
        // Start from 'a', which is at position 1
        char ch = 'a';
        while (level > 0) {
            int half = len / 2;
            if (k > half) {
                // If k is in the second half, it's a shifted version of a character in the first half
                k -= half;          // Map to original index in the first half
                ch = shiftChar(ch, 1);  // Shift character once for this level
            }
            level--;
            len /= 2; // Go to the previous level
        }

        return ch;
    }
};
