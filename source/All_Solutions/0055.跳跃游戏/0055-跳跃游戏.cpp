class Solution {
public:
    bool canJump(vector<int>& nums) {
        int max_i = 0;
        for(int i = 0; i<nums.size();i++){
            if(max_i >= i && i + nums[i] > max_i){
                max_i = i + nums[i];
            }
        }
        return max_i >= nums.size() - 1;
    }
};