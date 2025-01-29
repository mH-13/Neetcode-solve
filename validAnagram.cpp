#include <unordered_map>
#include <vector>
#include <string>

using namespace std;
class Solution {
public:
    bool isAnagram(string s, string t) {
        if(s.length() != t.length()){
            return false;
        }
        unordered_map <char, int> S;
        unordered_map <char, int> T;

        for(int i =0; i<s.length(); i++){
            S[s[i]]++;
            T[t[i]]++; 
        }
        return S==T;



    }
};
