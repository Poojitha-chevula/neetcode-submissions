class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> ans;
        vector<pair<int,int>> a;
        for(int i=0;i<nums.size();i++){
            a.push_back({nums[i],i});
        }
        sort(a.begin(),a.end());
        int i=0;
        int j=nums.size()-1;
        while(i<j){
            int s=a[i].first+a[j].first;
            if(s==target){
                ans.push_back(a[i].second);
                ans.push_back(a[j].second);
                break;
            }else if(s<target){
                i++;
            }else{
                j--;
            }
        }
        sort(ans.begin(),ans.end());
        return ans;
    }
};
