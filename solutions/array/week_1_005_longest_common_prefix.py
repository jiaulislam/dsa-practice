from typing import List

"""
At first I was unable to get the solution within 45 minutes. I had one brute-force solution
but that is too complex to implement also the time-complexity was O(n)^3. So I dropped the
idea to solve it on my own. And tried to learn the solusion.

here in this solution the main idea was to sort the array of strings.
then we don't need to iterate over each word rather take first one and
last one. then compare with them. I made also one mistake i didn't break
earlier as If character don't match on first, we don't need to care about later also.

So now the solution time complexity is:
O(m . n log n + p^2) as in python string are immutable
and we're copying building new array everytime.
but if we make a list of chars then use .join()
then it would be `O(m . n log n)`
"""


def longest_common_prefix(strs: List[str]) -> str:
    n = len(strs)  # O(1)
    strs.sort()  # O(m.n log n) here m is the longes string length
    first_str = strs[0]  # O(1)
    last_str = strs[n - 1]  # O(1)
    # longest_prefix = ""
    longest_prefix_chars = []
    for i in range(len(first_str)):  # O(p) here p is the final length of the prefix
        if first_str[i] == last_str[i]:
            # longest_prefix += first_str[i] # O(p)^2
            longest_prefix_chars.append(first_str[i])
            continue
        break
    return "".join(longest_prefix_chars)
