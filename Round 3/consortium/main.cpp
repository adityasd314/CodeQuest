#include <iostream>
#include <vector>
#include <unordered_set>
#include <algorithm>
using namespace std;


bool canDivideConsortium(int M, const vector<pair<string, string>>& troublesomePairs) {
        unordered_set<string> group1;
        unordered_set<string> group2;

        for (const auto& pair : troublesomePairs) {
            const string& member1 = pair.first;
            const string& member2 = pair.second;

            if (group1.count(member1) && group1.count(member2)) {
                return false;
            } else if (group2.count(member1) && group2.count(member2)) {
                return false;
            } else {
                group1.insert(member1);
                group1.insert(member2);
            }
        }

        return true;
    }
int main() {

    int M;
    cin >> M;

    vector<pair<string, string>> troublesomePairs;
    for (int i = 0; i < M; ++i) {
        string member1, member2;
        cin >> member1 >> member2;
        troublesomePairs.emplace_back(member1, member2);
    }

    if (canDivideConsortium(M, troublesomePairs)) {
        cout << "Yes" << endl;
    } else {
        cout << "No" << endl;
    }

    return 0;
}