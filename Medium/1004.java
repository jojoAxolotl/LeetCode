// 1004. Max Consecutive Ones III
package Medium;

class Solution {
    public int longestOnes(int[] nums, int k) {
        int left = 0;
        for(int i=0;i<nums.length;i++) {
            if(nums[i] == 0)  
                k--;
            // 在用完 k 之後，才開始移動 left
            // 如果左邊界有遇到 0 時，把 k + 1
            if(k < 0 && nums[left++] == 0)
                k++;   
        }
        return nums.length-left;
    }
}