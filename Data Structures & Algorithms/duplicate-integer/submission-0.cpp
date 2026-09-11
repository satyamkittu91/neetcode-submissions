class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_map<int, int> m1;
        for (int i = 0; i < nums.size(); i++){
            if (m1.count(nums[i])) return true;
            else m1[nums[i]] = i;
        }
    return false;
    }
};