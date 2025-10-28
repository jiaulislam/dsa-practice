from typing import List

# version 1
# Brute-force approach to check for duplicates within k distance
# Time Complexity: O(n^2)
# Space Complexity: O(1)
# But can be optimized to O(n) time using sliding window
# def contains_duplicate(arr: List[int], k: int):
#     if len(arr) == 1:
#         return False
#     for i, v in enumerate(arr):
#         for j, v2 in enumerate(arr[i+1:], start=i+1):
#             if v == v2 and abs(i-j) <= k:
#                 return True
#     return False


# version 2
# using hashmap
def contains_duplicate(nums: List[int], k: int):
    seen = {}

    for index, num in enumerate(nums):
        if num not in seen:
            seen[num] = index
            continue
        if abs(index - seen[num]) <= k:
            return True
        seen[num] = index  # keep the latest index
    return False


# version 3
# using sliding window technique
# def contains_duplicate(nums: List[int], k: int):
#     window = set()
#     left = 0

#     for right in nums:
#         if right in window:
#             return True
#         window.add(right)
#         if len(window) > k:
#             window.remove(nums[left])
#             left += 1
#     return False
