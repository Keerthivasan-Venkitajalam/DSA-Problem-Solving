class Solution {
public:
    int possibleStringCount(string word) {
        //base case: if word is empty, there's only 1 possible original (the empty string itself)
        if (word.empty()) return 1;

        int count = 1; //start with 1 for the case where no characters are deleted
        int n = word.length();
        int groupStart = 0; //pointer to the start of a group of repeated characters

        //iterate through the string to find groups of repeated characters
        for (int i = 1; i < n; ++i) {
            //if current character is different from previous, we reached end of a repeated group
            if (word[i] != word[i - 1]) {
                int len = i - groupStart; //length of the repeated group
                if (len > 1) {
                    count += len - 1; //you can remove one of the repeated characters in len - 1 ways
                }
                groupStart = i; //update group start to the new character
            }
        }

        //handle the last group (in case the string ends with repeated characters)
        int len = n - groupStart;
        if (len > 1) {
            count += len - 1;
        }

        return count; //return total possible original strings Alice might have typed
    }
};
