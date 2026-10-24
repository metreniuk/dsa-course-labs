# Lab 3: Recursion, Merge, and Merge Sort

Use the account and submission steps from [Lab 1](01-arrays.md).
Review the [Lecture 3 slides](../slides/03-sorting-and-merge-sort-student.md)
when needed.

Complete all three exercises in the order below.

## 1. Recursion: Reduce a number to zero

[1342. Number of Steps to Reduce a Number to Zero](https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/) - Easy

Write a **recursive** solution that counts the steps:

- Stop when the number is zero.
- For an even number, divide it by two.
- For an odd number, subtract one.

Trace this input before you write code:

```text
14 -> 7 -> 6 -> 3 -> 2 -> 1 -> 0
6 steps
```

Explain:

- What is the base case? What does it return?
- What smaller problem does each recursive call solve?
- Why does the returned answer gain one step?
- Why will the calls reach the base case?

Test `0`, `1`, an even number, and an odd number. State the time and
extra-space costs. Include the active recursive calls in the space cost.

## 2. Guided warm-up: Merge two sorted arrays

[88. Merge Sorted Array](https://leetcode.com/problems/merge-sorted-array/) - Easy

Both input parts are already sorted. Write the result into **`nums1`**.
This exercise practices merging, not the full merge-sort algorithm.

- The first `m` positions in `nums1` contain input values.
- Its last `n` positions provide space for the result.
- `nums2` contains `n` input values.
- Use `m` and `n` to find the input values. A zero can be a real input value.

Trace this example:

```text
nums1 = [2, 5, 6, 0, 0, 0]   m = 3
nums2 = [1, 2, 4]            n = 3

result: [1, 2, 2, 4, 5, 6]
```

**Merge from the back:**

1. Track the last unused input value in each array and the last free output
   position in `nums1`.
2. Compare the two input values. Write the larger value at the output position.
3. Move the output position and the selected input position backward.
4. Repeat while both input parts have unused values.
5. Copy any remaining values from `nums2`. Remaining values from `nums1`
   can stay where they are.

Show each write in your trace. Explain why this direction avoids overwriting
unread values in `nums1`.

Test `m = 0`, `n = 0`, equal values, and input values that are zero.
Aim for `O(m + n)` time and `O(1)` extra space. Explain both costs.

## 3. Merge sort: Sort an array

[912. Sort an Array](https://leetcode.com/problems/sort-an-array/) - Medium

Implement **merge sort**. Do not use built-in sorting. The problem requires
`O(n log n)` time.

- Define the base case.
- Split the input into two smaller parts.
- Recursively sort both parts.
- Merge the sorted parts.

Unlike Exercise 2, the input is not already sorted. Use a temporary buffer
for merging; do not assume the input has unused positions at the end.
You can allocate one buffer and reuse it across recursive calls.

Trace the splits and merges for the lecture input:

```text
[6, 2, 5, 2, 1] -> [1, 2, 2, 5, 6]
```

Test one value, negative values, duplicates, an already sorted array,
a reverse-sorted array, and an odd-length array.
Check that the result is sorted and keeps every original value and its count.

Explain:

- Why must both parts be sorted before you merge them?
- Why does each recursive call reach the base case?
- Why is the time cost `O(n log n)`?
- With one shared buffer, why is the total extra space `O(n)`?
  Account for both the buffer and the active call stack.

## Completion check

- Show an **Accepted** submission for each of the three problems.
- Keep your code, traces, and explanations in your student repository.

## Recommendations

1. Give each problem at least 3-5 submission attempts before you seek help,
   unless your solution is accepted sooner. Do not look at solutions or use AI
   during these attempts.
2. Open the **Solutions** tab only **after** you have a working, accepted
   solution. Compare other approaches with your code.
3. **Optional:** After your solution works, ask AI to review your code and
   suggest improvements.
