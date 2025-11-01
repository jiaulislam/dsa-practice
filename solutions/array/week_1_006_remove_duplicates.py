from typing import List


"""
first I tried to solve it with brute-force approach i thought. it was easy for me still
it took me around 30 minutes to come up with an algorithm.
"""
# def remove_duplicates(nums: List[int]) -> int:
#     n = len(nums)
#     unique_elements = sorted(set(nums))
#     for i, num in enumerate(unique_elements):
#         nums[i] = num

#     for i in range(len(unique_elements), n-1):
#         nums[i] = -1
#     return len(unique_elements)


"""
later I learned about two pointer technique. this technique works in perfectly for this problem.
as the arrays are sorted the algorithm gets pretty easy
"""


def remove_duplicates(nums: List[int]) -> int:
    if not nums:
        return 0

    right_pointer = 1  # this is what we call slow pointer. we only increase it when we seen an unique item

    # here the left_pointer is the slow pointer means we iterate over each item of the array.
    # and notice how we start from index 1 that is because we always assume index 0 is unique
    for left_pointer in range(1, len(nums)):
        if nums[left_pointer] != nums[left_pointer - 1]:
            nums[right_pointer] = nums[left_pointer]
            right_pointer += 1
    return right_pointer
