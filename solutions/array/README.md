
# Problems and Different Approaches

## 1. Contains Duplicate II - Multiple Solution Patterns

**Problem**: Given an array and integer `k`, return `true` if there are two distinct indices `i` and `j` such that `nums[i] == nums[j]` and `abs(i - j) <= k`.

### Approach Comparison

#### Brute Force O(n²)

- Nested loops to check all pairs
- Simple but inefficient for large inputs

#### Hashmap O(n)

- Track last seen index of each element
- Flexible for variable distance checks
- Best when you need to compare exact indices

#### Sliding Window O(n)

- Maintain a set of at most `k` recent elements
- Clean pattern for fixed-distance problems
- Best when window size is constant

**Key Insight**: Same problem, different data structures - hashmap for index tracking vs set for membership testing.

### 2. Maximum Average Subarray I - Fixed-Size Sliding Window

**Problem**: Find contiguous subarray of length `k` with maximum average.

#### Core Technique

- **Sum-based sliding window**: Work with sums, convert to average once
- **Window update formula**: `new_sum = old_sum - nums[left] + nums[right]`
- **Why sums?** Avoids floating-point precision issues during sliding

**Key Insight**: For arithmetic operations (sum, average, product), maintain the calculation incrementally rather than recalculating each window.

## Pattern Recognition

### When to Use Each Approach

**Fixed-Size Sliding Window**:

- Window size is constant (`k`)
- Need to process every possible window of size `k`
- Examples: max sum of k elements, average of k elements

**Hashmap/Dictionary**:

- Need to track positions or counts
- Variable distance or time-based lookups
- Examples: two sum, last occurrence tracking

**Set-Based Sliding Window**:

- Membership testing within a window
- Duplicate detection in recent elements
- Examples: contains duplicate, unique characters in window

### Implementation Templates

**Sum-Based Fixed Window**:

```python
# Initialize first window
current_sum = sum(nums[:k])
result = current_sum

# Slide window
for i in range(k, len(nums)):
    current_sum = current_sum - nums[i-k] + nums[i]
    result = max(result, current_sum)  # or min, etc.
```

**Set-Based Fixed Window**:

```python
window = set()
for i, val in enumerate(nums):
    if val in window:  # Check condition
        return True
    window.add(val)
    if len(window) > k:  # Maintain window size
        window.remove(nums[i-k])
```

## Learning Progression

1. **Master brute force first** - understand the problem completely
2. **Identify the pattern** - what are you tracking? (sum, duplicates, count)
3. **Choose data structure** - set for membership, dict for mapping, variables for arithmetic
4. **Apply sliding window** - maintain window size, update incrementally
5. **Handle edge cases** - empty arrays, k=0, k > array length
