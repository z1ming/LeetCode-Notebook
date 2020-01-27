class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
      int filpPos=-1;
      int maxCount =0;
      int curCount =0;
      for(int i=0;i<nums.length;i++){
          if(nums[i]==1){
              curCount++;
          }else{
              curCount=i-filpPos;
              filpPos=i;
          }
          maxCount=Math.max(maxCount,curCount);
      }
      return maxCount;
    }
}