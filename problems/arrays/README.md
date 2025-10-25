# Arrays

Arrays are a fundamental data structure in programming that allows you to store and manipulate collections of elements of the same data type. All though python
list are totally different from arrays. Arrays are fixed in size and can only store elements of the same data type, while lists are dynamic and can store elements of different data types. Arrays are also more efficient for accessing elements by index, while lists are more efficient for adding and removing elements.

## Arrays in Python

Python does not have a built-in array data type like some other programming languages. Instead, it uses lists to represent arrays. However, there are several libraries available that provide array-like functionality, such as NumPy.

## DSA with Arrays

DSA with Arrays is a collection of problems that focus on the use of arrays in data structures and algorithms. These problems are designed to help you develop your skills in working with arrays and to improve your understanding of how arrays can be used to solve complex problems.
There are many techniques that can be used to solve problems involving arrays, such as sorting, searching, and dynamic programming. These techniques can be applied to a wide range of problems, from simple array manipulation to complex data analysis.

### Sliding Window Technique

At high level: you maintain a "window" (a contiguous segment) defined by two indices (say `left` and `right`) over your data. And you slide(move) the window through your data, incrementally updating your answer rather than recomputing from scratch each time.

There are tow main flavours in sliding window technique:

- **Fixed-size window**: window size (lets say `k`) which is a constant. You slide the window at a time through your data computing something at a time (sum, average, max) each window.
- **Variable-size window**: window size can grow or shrink. You constantly grow or shrink the window size until a condition is met (e.g, longest substring with at most k distinct chars)
