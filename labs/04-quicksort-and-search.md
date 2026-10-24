# Lab 4: Quicksort and Binary Search

Use the account and submission steps from [Lab 1](01-arrays.md).
Review the [Lecture 4 slides](../slides/04-quicksort-and-binary-search-student.md)
when needed.

Complete the local task and both required LeetCode problems in order.
Use Python or C. Keep reusable functions in `algorithms/` in your student
repository.

## 1. Local task: Implement quicksort

How can you sort an array without the merge buffer from Lab 3?

Implement **partition** and **recursive quicksort**. Do this task locally,
without LeetCode. Do not use built-in sorting in your implementation.
The lecture has complete examples in
[Python](../slides/examples/04-quicksort.py) and
[C](../slides/examples/04-quicksort.c).

Use the same rules as the slides:

- Work on `[lo, hi)`: include `lo`, exclude `hi`.
- Choose the **first value**, `values[lo]`, as the pivot.
- Start `boundary = lo`. Scan from `lo + 1` to `hi - 1`.
- If a value is `< pivot`, increase `boundary`, then swap the values at
  `boundary` and `scan`.
- After the scan, swap the pivot with `values[boundary]`. Return its index `p`.
- Recursively sort `[lo, p)` and `[p + 1, hi)`. Exclude the fixed pivot.
- Stop before partitioning a range with zero or one value.

Trace the lecture input before you write code:

```text
Input:                  [6, 2, 5, 2, 1]
After first partition:  [1, 2, 5, 2, 6]   p = 4
Final sorted result:    [1, 2, 2, 5, 6]
```

Record each pivot, swap, and recursive range. After each partition, check:

- All values left of the pivot in this range are `< pivot`.
- All values right of it in this range are `>= pivot`.
- Neither side needs to be sorted yet.

Test an empty array, one value, negative values, duplicates, sorted input,
reverse-sorted input, and all-equal input.
Check that the result is sorted and keeps every original value and its count.
You may use built-in sorting to check the expected result in tests.

Compare your result with your merge sort from [Lab 3](03-sorting.md).
Give each sort a separate copy of the same input.

Explain:

- Why does each recursive call reach the base case?
- Why must both calls exclude the pivot?
- Why do balanced partitions give `O(n log n)` time and `O(log n)` stack space?
- Why can this version take `O(n^2)` time and `O(n)` stack space?

Count pivot comparisons on `[1, 2, 3, 4, 5]` and `[2, 2, 2, 2, 2]`.
Keep these traces small. In-place partitioning removes the merge buffer,
but recursive calls still use memory. Random pivots alone do not fix the
all-equal case with this strict `<` rule.

## 2. Binary search: Find a target

[704. Binary Search](https://leetcode.com/problems/binary-search/) - Easy

How can sorted order help you skip values that you have not read?

Implement **iterative binary search** with index bounds. Do not use a built-in
search function or copy array slices. The input is already sorted; do not sort
it again. Return the target's index, or `-1` if it is absent.

Let `n` be the array length. Use `[lo, hi)`, with `lo = 0` and `hi = n`
at the start:

- Continue while `lo < hi`.
- Calculate `mid = lo + (hi - lo) // 2`. In C, use `/` for integer division.
- If the middle value matches, return `mid`.
- If it is smaller than the target, set `lo = mid + 1`.
- If it is larger, set `hi = mid`.
- If the range becomes empty, return `-1`.

Trace both cases. Record `lo`, `hi`, `mid`, the middle value, and the next range.

```text
values = [-1, 0, 3, 5, 9, 12]
target = 9     result: 4
target = 2     result: -1
```

Test a match at the first and last index, one value, and a missing target
below, above, and between stored values. Also test an empty array locally.
LeetCode supplies nonempty arrays with distinct values.

Explain why a possible match stays in `[lo, hi)` and why each unsuccessful
check makes the range smaller. Why can `lo = mid` cause an infinite loop?
Aim for `O(log n)` worst-case time and `O(1)` extra space.

## 3. Guided task: Find an insertion position

[35. Search Insert Position](https://leetcode.com/problems/search-insert-position/) - Easy

If a target is absent, can the final search boundary still give a useful answer?

Adapt binary search to return the first position whose value is **not less
than the target**. Return `n` if no such value exists.
The input is already sorted and has distinct values.

- Keep `[lo, hi)` and the same middle-index calculation.
- If `values[mid] < target`, move `lo` past `mid`.
- Otherwise, move `hi` to `mid`. Keep searching for an earlier position.
- Return `lo` when the boundaries meet.

Trace these cases:

```text
values = [1, 3, 5, 6]
target = 5     result: 2
target = 2     result: 1
target = 0     result: 0
target = 7     result: 4
```

Return an index only. Do not insert a value or shift the array.
Test one value and an empty array locally; the empty array gives position `0`.
Explain why every value before the returned position is smaller than the
target, and every value from that position onward is at least the target.
Aim for `O(log n)` worst-case time and `O(1)` extra space.

## Optional: Partition by parity

[905. Sort Array By Parity](https://leetcode.com/problems/sort-array-by-parity/) - Easy

Place all even values before all odd values. Use swaps and a boundary,
as in partitioning. Do not fully sort the array.
Any order within each group is valid. Aim for `O(n)` time and `O(1)` extra space.

## Completion check

- Keep your locally tested partition and quicksort in your student repository.
- Show **Accepted** submissions for **704** and **35**. Problem **905** is optional.
- Keep your tests, traces, correctness explanations, and time/space analysis.
- Include the recursive stack in quicksort's space cost. Accepted search
  submissions do not test your local quicksort.

## Recommendations

1. Give each problem at least 3-5 submission attempts before you seek help,
   unless your solution is accepted sooner. Do not look at solutions or use AI
   during these attempts.
2. Open the **Solutions** tab only **after** you have a working, accepted
   solution. Compare other approaches with your code.
3. **Optional:** After your solution works, ask AI to review your code and
   suggest improvements.
