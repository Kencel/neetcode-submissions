class Solution {
public:
    long long compute_hash(vector<int> s) {
        const int p = 31;
        const int m = 1e9 + 9;
        long long hash_value = 0;
        long long p_pow = 1;
        for (int c : s) {
            hash_value = (hash_value + c * p_pow) % m;
            p_pow = (p_pow * p) % m;
        }
        return hash_value;
    }

    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        map<long long, int> idx;
        vector<vector<string>> ans;
        int curr = 1;
        for(string s : strs){
            vector<int> count(26);
            for(char c : s){
                count[c - 'a']++;
            }
            long long hash = compute_hash(count);
            if(idx[hash] == 0){
                idx[hash] = curr;
                curr++;
                ans.push_back({s});
            } else {
                ans[idx[hash] - 1].push_back(s);
            }
        }
        return ans;
    }
};
