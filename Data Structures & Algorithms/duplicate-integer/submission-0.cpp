class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        vector<int> arr;
        for(int i = 0 ; i < nums.size() ; i++){
            bool flag = false;
            for(int j = 0 ; j < arr.size() ; j++){
                if(nums[i] == arr[j]){
                    flag = true;
                }
            }
            if(flag){
                return true;
            }
            else{
                arr.push_back(nums[i]);
            }
        }
        return false;
    }
};