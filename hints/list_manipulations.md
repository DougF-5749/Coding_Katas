# 1. Reverse a List
You can use **list slicing**: `my_list[::-1]` to quickly reverse.  
If you need to **reverse in-place**, consider a **two-pointer approach** where one pointer starts at the beginning and another at the end, and you **swap** elements until they meet in the middle.  
Be careful with the edge case of an **empty list**—decide what you should return in that scenario.

# 2. Rotate a List
Rotating by `k` positions is similar to performing **two** or **three** reversals:
  - Reverse the **entire list**.
  - Reverse the **first k** elements.
  - Reverse the **remaining** elements.
Alternatively, you can use **slicing**:
  - Convert `k` to something within the range of the list length (i.e., `k = k % len_list`).  
  - Concatenate two slices: the **last k elements** + the **first (len - k) elements**.
Remember that **negative k** means rotate in the **opposite** direction.

# 3. Remove Duplicates (Non-Sorted List)
Use a **set** to keep track of seen elements.
As you iterate over the list, check if an element is **in** the seen set.  
  - If **not**, add it to the resulting list.
You can do it **in place** (by overwriting at a correct index) or build a **new list** to collect unique items.

# 4. Merge Two Sorted Lists
Use **two pointers**, one for each list.  
  - Compare the elements at both pointers and add the **smaller** one to the new merged list.
If one pointer reaches the end of its list, **append** all remaining elements from the other list.
Watch out for **edge cases** where one or both lists are **empty**.

# 5. Move Zeros to the End
Think of it like a **partition**: non-zero elements should remain in the front, zeroes go to the back.
You can maintain a **write pointer** (index) that moves only when you write a non-zero, and a **read pointer** that scans the list.
After processing all non-zero elements, fill the **remaining** indices of the list with **0**.

# 6. Partition List Around a Pivot
A simple approach is to create **two new lists**:
  - One for elements **less than** the pivot.
  - One for elements **greater than or equal to** the pivot.  
  Then **concatenate** them.
If you want to do it **in place**, consider a **two-pointer** strategy or a method similar to the **partition** step in QuickSort.

# 7. Find All Pairs That Sum to a Target
To avoid duplicates, you can keep track in a **set** of seen numbers or of seen pairs.
For each element `x`, check if `target - x` has been seen before.
Make sure to handle the **case** where the target might be **2x** (e.g., looking for `(x, x)` if it appears more than once in the list).

# 8. Flatten a Nested List
A **recursive** function can handle arbitrary nesting:
  - If an element is a **list**, recursively flatten it.
  - Otherwise, add it to the **result** list.
You could also use an **iterative** approach with a stack while there are still lists to expand.

# 9. Reverse Sub-List In Place
You can do a **mini two-pointer** approach **between `start` and `end`** indices:
  - Swap `list[start]` and `list[end]`, then move each pointer inward.
Pay attention to **boundary conditions**. If `start` >= `end`, no change is needed.
Confirm if `start` and `end` are always **valid** or if you need to **validate** them.
