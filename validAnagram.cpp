#include <iostream>
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
            cout<<"S[s[i]]: "<<S[s[i]]<<endl;
            T[t[i]]++; 
            cout<< " T[t[i]]: "<<T[t[i]]<<endl;
        }
        for (const auto& pair : S) {
        cout << "Key: " << pair.first << ", Value: " << pair.second << endl;
        }
        cout<<endl;
        for (const auto& pair : T) {
        cout << "Key: " << pair.first << ", Value: " << pair.second << endl;
        }


        return S==T;



    }
};

