# Problem: 001_containts_duplicate

`https://leetcode.com/problems/contains-duplicate-ii/description/?envType=problem-list-v2&envId=sliding-window
`

Given an integer array nums and an integer k,
return true if there are two distinct indices i and j
in the array such that nums[i] == nums[j] and abs(i - j) <= k

## Approach

At first I tried to solve with sliding window technique. But unable to do it
I tried for brute-force first.
My solution time complexity is O(n)^2. I'm iterating over the array on given array
and then taking a 2nd loop and again iterating over the array but starting with index first loop.
then inside the second loop I'm checking i.value == j.value and abs(i-j) <= k. If found return True
else False.

Learned the solution for sliding window and it's variant

- Sliding window with 2 pointer
- Simple hashmap solution
