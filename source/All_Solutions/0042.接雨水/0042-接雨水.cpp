class Solution {
public:
    int trap(vector<int>& height) {
        int ans = 0;
        int n = height.size();
        int maxleft;
        int maxright;
        for (int i = 0;i < n;i++){
            maxleft = maxright = 0;
            for (int j = 0;j < i;j++){
                maxleft = max(maxleft,height[j]);
            }
            for (int k = i;k<n;k++){
                maxright = max(maxright,height[k]);
            }
            if (min(maxleft,maxright) > height[i]){
                ans += min(maxleft,maxright) - height[i];
            }
            
        }
        return ans;
    }
};