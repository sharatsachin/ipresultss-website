// Created by Sharat Sachin
#include <bits/stdc++.h>
using namespace std;
using ll = long long;
int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    string s, nm1, nm2;
    vector<string> vs;
    map<string, string> mp;
    while (cin >> s) {
        bool f = false;
        if (s.length() == 11 && all_of(s.begin(), s.end(), [](char c) { return c >= '0' && c <= '9'; })) {
            f = true;
            cin >> nm1 >> nm2;
            nm1 += " ";
            if (nm2 != "SID:")
                nm1 += nm2;
            mp[s] = nm1;
        }
        else if ((s.length() == 5 || s.length() == 6) && find(s.begin(), s.end(), '(') != s.end())
            f = true;
        if (!f)
            continue;
        vs.push_back(s);
    }
    vector<pair<float, string> > vp;
    float f = 0;
    for (int i = 0; i < vs.size(); i++) {
        if (vs[i].length() == 11)
            s = vs[i];
        else
            f += ((vs[i][0] - '0') * 10 + (vs[i][1] - '0'));
        if (vs[i + 1].length() == 11) {
            vp.push_back({ f, s });
            f = 0.0;
        }
    }
    sort(vp.rbegin(), vp.rend());
    for (int i = 0; i < vp.size(); i++) {
        cout << i + 1 << "\t: " << mp[vp[i].second] << "\n\t% = " << vp[i].first / 12 << "\n";
    }
    return 0;
}
