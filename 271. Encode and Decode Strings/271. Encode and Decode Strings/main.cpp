#include <iostream>
#include <string>
#include <vector>

using namespace std;

string encode(vector<string>& strs) {
	string str = "";
	if (strs.size() == 0)
		return str;
	for (int i = 0; i < strs.size(); i++) {
		str += to_string(strs[i].size()) + "#" + strs[i];
	}
	return str;
}

vector<string> decode(string s) {
	vector<string> result;
	if (s == "")
		return result;
	int pos = 0;
	while (pos < s.size() - 1) {
		string ssize;
		string tmp;
		while (s[pos] != '#') {
			ssize += s[pos];
			pos++;
		}
		int size = stoi(ssize);
		pos ++;
		if (pos >= s.size()) {
			result.push_back(tmp);
			break;
		}

		for (int i = 0; i < size; i++) {
			tmp += (s[pos]);
			pos++;
		}
		result.push_back(tmp);
	}
	return result;
}


int main() {
	vector<string> strings = { "neet", "code", "love", "kd@#%$Y&#@"};
	string str = encode(strings);
	cout << (strings == decode(str));
}