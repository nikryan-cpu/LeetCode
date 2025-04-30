#include <iostream>
#include <vector>
#include <algorithm>
#include <unordered_map>

using namespace std;


vector<int> topKFrequent(vector<int>& nums, int k) {
	unordered_map<int, int> counter;
	vector<vector<int>> freq(nums.size() + 1);
	for (int i = 0; i < nums.size(); i++) {
		counter[nums[i]]++;
	}

	for (auto& i : counter) {
		freq[i.second].push_back(i.first);
	}
	vector<int> result(k);
	
	for (int i = freq.size() - 1; i >= 0; i--) {
		for (int num : freq[i]) {
			result.push_back(num);
			if (result.size() == k) {
				return result;
			}
		}
	}
}

int main() {
	int k = 2;
	vector<int> vec = { 1,2,7,3,4,5,67,2,3,5 };
	topKFrequent(vec, k);
}