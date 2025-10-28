from typing import List

"""
MAXIMUM AVERAGE SUBARRAY I - SLIDING WINDOW TECHNIQUE

PROBLEM UNDERSTANDING:
- Find contiguous subarray of length k with maximum average
- Return the maximum average value
- All subarrays must have exactly k elements

KEY INSIGHT:
Instead of calculating average for each window, work with SUMS throughout
the algorithm and convert to average only at the end.
Why? Because max sum ÷ k = max average (since k is constant)

SLIDING WINDOW APPROACH:
1. Calculate sum of first k elements (initial window)
2. Slide window: remove leftmost element, add new rightmost element
3. Track maximum sum encountered
4. Return max_sum / k

SLIDING WINDOW FORMULA:
new_sum = old_sum - nums[left] + nums[right]
where left = i - k, right = i

TIME COMPLEXITY: O(n) - single pass after initial sum calculation
SPACE COMPLEXITY: O(1) - only using a few variables

COMMON MISTAKES TO AVOID:
❌ Working with averages in the loop (causes precision issues)
❌ Recalculating sum for each window O(n*k)
❌ Dividing by k multiple times

✅ Work with sums, convert to average once at the end
✅ Use sliding window to update sum in O(1)
✅ Only divide by k once

TRACE EXAMPLE: nums = [1,12,-5,-6,50,3], k = 4
Initial window [1,12,-5,-6]: sum = 2
Slide to [12,-5,-6,50]: sum = 2 - 1 + 50 = 51 ← maximum
Slide to [-5,-6,50,3]: sum = 51 - 12 + 3 = 42
Maximum average = 51/4 = 12.75
"""


def find_maximum_average(nums: List[int], k: int) -> float:
    n = len(nums)

    if k <= 0:
        raise ValueError("k cannot be negative")

    # Step 1: Calculate sum of first k elements (initial window)
    current_sum = sum(nums[0:k])
    max_sum = current_sum

    # Step 2: Slide the window from position k to n-1
    for i in range(k, n):
        # Sliding window formula: remove left, add right
        current_sum += nums[i] - nums[i - k]

        # Track maximum sum
        if current_sum > max_sum:
            max_sum = current_sum

    # Step 3: Convert maximum sum to average
    return max_sum / k


"""
PATTERN RECOGNITION:
This is a FIXED-SIZE SLIDING WINDOW problem.

Template for fixed-size sliding window:
1. Initialize window of size k
2. Calculate initial result
3. Slide window: remove left, add right
4. Update result
5. Return final result

SIMILAR PROBLEMS:
- Maximum sum subarray of size k
- Minimum average subarray
- First negative number in every window
- Count distinct elements in every window

DEBUGGING TIPS:
- Print current_sum at each step to verify sliding
- Check boundary conditions (k=1, k=n)
- Verify that you're not dividing by k in the loop
"""
