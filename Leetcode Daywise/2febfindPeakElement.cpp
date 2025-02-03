class Solution {
public:
    int findPeakElement(vector<int>& nums) {
        int n=nums.size();
        if(n==1) return 0;
        if(nums[0]>nums[1]) return 0;
        if(nums[n-1]>nums[n-2]) return n-1;

        int lo=1,hi=n-2;
        while(lo<=hi){
            int m=(lo+hi)/2;
            if (nums[m]>nums[m-1] && nums[m]>nums[m+1]){
                return m;
            }
            else if(nums[m]>nums[m-1]) lo=m+1;
            else hi=m-1;
        }
        return -1;
    }
};

// public:  
//     int findPeakElement(vector<int>& nums) {  // function to find a peak element index
//         int n=nums.size();  // get the size of the input vector
//         if(n==1) return 0;  // if only one element, return index 0
//         if(nums[0]>nums[1]) return 0;  // if first element is greater than second, return index 0
//         if(nums[n-1]>nums[n-2]) return n-1;  // if last element is greater than second last, return last index

//         int lo=1,hi=n-2;  // set search range from second to second-last element
//         while(lo<=hi){  // loop while low index is less than or equal to high index
//             int m=(lo+hi)/2;  // find the middle index
//             if (nums[m]>nums[m-1] && nums[m]>nums[m+1]){  // check if middle element is greater than neighbors
//                 return m;  // return middle index if it's a peak
//             }
//             else if(nums[m]>nums[m-1]) lo=m+1;  // if increasing, move right
//             else hi=m-1;  // if decreasing, move left
//         }
//         return -1;  // return -1 if no peak is found (shouldn't reach here)
//     }
// };
