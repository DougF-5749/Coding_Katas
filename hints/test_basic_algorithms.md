# 1. Factorial
1. Definition: ( n! = n times (n-1) times (n-2) times dots times 1 ).  
2. Edge Case: By definition, ( 0! = 1 ).  
3. Approaches:  
   - Recursive: Base case is when ( n = 0 ) or ( n = 1 ). Then multiply down.  
   - Iterative: Start at 1 and multiply up to ( n ).  

# 2. Fibonacci
1. Definition:  
   - ( F(0) = 0 ), ( F(1) = 1 ).  
   - ( F(n) = F(n-1) + F(n-2) ) for ( n ge 2 ).  
2. Edge Cases: Check how you handle `fibonacci(0)` and `fibonacci(1)`.  
3. Approaches:  
   - Naive recursion: Straightforward but exponential time.  
   - Memoization: Cache results in a dictionary to avoid repeated calculation.  
   - Iterative: Keep track of the last two Fibonacci numbers in a loop.

Hint: If you just need the *nth* Fibonacci number without storing all previous values, the iterative approach with two variables is efficient (O(n) time, O(1) space).

# 3. Permutations
1. Permutation Definition: All possible *distinct* orderings of a list’s elements.  
2. Approaches:  
   - Recursive (backtracking): At each step, choose an element to place first, then recursively permute the remainder.  
   - Itertools: Python has a built-in method `itertools.permutations`, if allowed.  
3. Edge Case: A single-element list has only one permutation—[ that element ].

Hint: In a backtracking approach, you can swap elements in-place: pick an index, swap with each possible element, and recurse on the subarray.

# 4. Binary Search
1. Algorithm: Given a sorted list, you can repeatedly compare the target with the middle element:
   - If `target` == `mid_value`, return the index.  
   - If `target` < `mid_value`, search the left half.  
   - If `target` > `mid_value`, search the right half.  
2. Iterative vs Recursive: Both have the same O(log n) complexity.  
3. Edge Case: Return `-1` if the target is not found.

Hint: Keep track of the left and right pointers; repeatedly compute `mid = (left + right) // 2` until `left` > `right`.

# 5. Merge Sort
1. Divide and Conquer:
   - Divide the list into two halves recursively until you reach lists of size 1 or 0.  
   - Merge the two sorted halves into a single sorted list.  
2. Merging Step:
   - Have two pointers, one for each sub-list, compare elements, and pick the smaller to build the sorted result.  
3. Base Case: A list of length 0 or 1 is already sorted.

Hint: Carefully handle indexing when you split the list. The typical split is `mid = len(lst) // 2`; the left half is `[0:mid]` and the right half is `[mid:]`.

# General Tips
1. Plan First: Outline your approach before coding.  
2. Test Edge Cases: Small inputs (like n=0, an empty list, etc.) or large inputs if you want to check performance.  
3. Time Complexity:  
   - Factorial: O(n) (iterative) or O(n) (recursive).  
   - Fibonacci: O(n) with iterative/memoization, O(2^n) with naive recursion.  
   - Permutations: O(n!) (that’s the number of permutations).  
   - Binary Search: O(log n).  
   - Merge Sort: O(n log n).  