class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> m;
        for (int i = 0; i < nums.size(); i++){
            int dif = target - nums[i];
            if (m.count(dif)) return {m[dif], i};
            else m[nums[i]] = i;
        }
    
    }
};
