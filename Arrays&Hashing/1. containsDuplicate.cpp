
#include <unordered_set>
#include <vector>

using namespace std;

class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_set<int> checkCounts;
        for (int num: nums){
            if(checkCounts.count(num)){
                return true;
            }
            checkCounts.insert(num);
        }
        return false;

    }
};




/*
#include <iostream>
#include <unordered_set>
#include <vector>

using namespace std;

class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_set<int> checkCounts;
        for (int num : nums) {
            if (checkCounts.count(num)) {
                return true;
            }
            checkCounts.insert(num);
        }
        return false;
    }
};

int main() {
    Solution solution;
    vector<int> nums;

    cout << "Enter numbers (separated by spaces, end with -1): ";
    int num;
    while (cin >> num && num != -1) {
        nums.push_back(num);
    }

    if (solution.hasDuplicate(nums)) {
        cout << "Duplicates found!" << endl;
    } else {
        cout << "No duplicates." << endl;
    }

    return 0;
}
*/