# -*- coding:utf-8 -*-

# Given a string, find the length of the longest substring without repeating characters.
"""
独创方法
个人思路：
1. 维护一个i，j。i只增不减，从头开始遍历索引j，
2. 当遇到之前的元素时，找到之前相同元素位置（hash）j',令i为j'+1，此时最长子序列长度(max_len)为j-i
3. 之后放弃i前面的所有，每次当遇到（2）时的情况时，比较此时j-i和max_len的长度
4. 注意：当j一直到结束都没遇到之前的元素，此时得到的最长长度只是i前面的元素得到的，由于i之后没有存在过的元素，所以比较max_len 和len(s)-i的大小
"""
def lengthOfLongestSubstring(s):
    if len(s) <= 1:
        return len(s)
    i = 0
    max_len = 0
    dic = {}
    temp = 0
    for j in range(len(s)):
        if s[j] in dic:
            max_len = max(j - i, max_len)
            i = max(dic[s[j]] + 1, i)
            temp = j
        dic[s[j]] = j
        if j == len(s) - 1:
            max_len = max(len(s) - i, max_len)

    max_len = max(max_len, len(s) - temp)

    return max_len

if __name__ == '__main__':
    print(lengthOfLongestSubstring('abba'))
