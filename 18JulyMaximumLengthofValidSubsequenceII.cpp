class Solution {
public:
    int maximumLength(vector<int>& nums, int k) {
        int n=nums.size();
        vector<unordered_map<int, int>> dp(n);
        int maxLen=1;

        for (int i=0;i<n;++i){
            //for each previous index j
            for (int j=0;j<i;++j){
                int mod=(nums[i]+nums[j])%k;
                int preLen=dp[j].count(mod)?dp[j][mod]:1; //default pair len is 2
                dp[i][mod]=max(dp[i][mod], preLen+1);
                maxLen=max(maxLen, dp[i][mod]);
            }
        }
        return maxLen;
    }
};
