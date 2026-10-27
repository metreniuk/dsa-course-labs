# Lab 6: Binary Search Trees, DFS, and BFS

Use the account and submission steps from [Lab 1](01-arrays.md).
Review the [Lecture 6 slides](../slides/06-trees-and-binary-search-trees-student.md)
when needed.

Complete all three problems in order. Choose any programming language.
Reuse the tree from Problem 1 for your local traversal tests.

## Before you start

- A node stores a value, a left child, and a right child.
- Use your language's null value for an empty child.
- The lecture uses `node.value`. Use the node definition and field names
  supplied by LeetCode for your chosen language.
- Return the required result. Printing values is not enough for the judge.
- Use valid trees: no cycles and no child shared by two parents.

## 1. Build a binary search tree

[701. Insert into a Binary Search Tree](https://leetcode.com/problems/insert-into-a-binary-search-tree/) - Medium

Where should a new value go so that the tree keeps its BST order?

Implement **insertion**. Return the updated root.

- All values in a node's left subtree must be smaller than its value.
- All values in its right subtree must be larger.
- Follow left or right links until you find an empty position.
- Add a new leaf there. Keep the existing nodes in their positions.
- Handle an empty tree. Its new node becomes the root.
- If you use recursion, save the returned subtree root in the correct
  child link.

LeetCode guarantees that the new value is absent. For your local version,
use the lecture's rule: inserting a duplicate leaves the tree unchanged.

**Local build task:** Start with an empty root. Insert these values in order.
After each insertion, save the returned root.

```text
Input: [4, 2, 7, 1, 3, 6, 9]

Expected tree:

        4
       / \
      2   7
     / \ / \
    1  3 6  9
```

Before you write code:

1. Draw the tree after each insertion.
2. Record the comparison path for each new value.
3. Predict where `5` would go. Build a fresh tree before you test this insertion.

Test an empty input, one value, negative values, duplicates, and sorted
input. Inserting `[1, 2, 3, 4]` must make a right-only chain with this method.
Do not sort the input first or build a balanced tree instead.

Explain:

- Why does the new leaf preserve the rule for the whole subtree?
- Why must the caller save the returned root?
- Why does one insertion take `O(h + 1)` time for height `h`?
- Why can building a tree with `n` distinct values take `O(n^2)` time?
- If the tree stays balanced during construction, why is the total time
  `O(n log n)`?

Height counts edges. The final tree needs `O(n)` node storage.
Recursive insertion also needs `O(h + 1)` call-stack space for one insertion;
iterative insertion can use `O(1)` extra working space.
An ordinary BST does not guarantee balance.
If your language limits recursion depth, use iterative insertion for long chains.

## 2. DFS: Return the inorder traversal

[94. Binary Tree Inorder Traversal](https://leetcode.com/problems/binary-tree-inorder-traversal/) - Easy

How can you visit every value in the BST in sorted order?

Implement **recursive inorder DFS**. Return one list of values.

- Visit the left subtree.
- Add the current node's value to the result.
- Visit the right subtree.
- Stop at an empty child. An empty tree returns `[]`.
- Use one shared result list or an output buffer with a write index.
  Avoid copying a new list of subtree results at each recursive return.

Trace the tree from Problem 1 before you write code:

```text
Input insertion order: [4, 2, 7, 1, 3, 6, 9]
Inorder result:        [1, 2, 3, 4, 6, 7, 9]
```

Record when each call starts, when it adds a value, and when it returns.
Does the first call add its value first?

LeetCode supplies a **binary tree**, which need not be a BST. Your traversal
must follow its links. Do not sort the values.

Test the lecture's binary tree that is not a BST:

```text
    2
   / \
  1   3
 /
4

Inorder result: [4, 1, 2, 3]
```

Also test an empty tree, one node, a left-only chain, and a right-only chain.
Confirm that traversal leaves every node and child link unchanged.

Explain:

- Why is every node added exactly once?
- Why does recursion finish on a valid finite tree?
- Why is inorder sorted for a BST, but not for every binary tree?
- Why is the time `O(n)`, even for a balanced BST?

The call stack needs `O(h + 1)` extra working space. The result list needs
another `O(n)` space. A deep chain can exceed your language's stack limit;
keep recursive local tests small.

## 3. BFS: Return one list per level

[102. Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/) - Medium

How can you keep nodes from the same depth together?

Implement **BFS with a FIFO queue**. Return a list of levels, with values
from left to right within each level.

- An empty tree returns `[]`.
- Start the queue with the root.
- At the start of each level, save the number of nodes in the queue.
- Remove exactly that many nodes. Add their values to one level list.
- For each removed node, add its left child, then its right child, if present.
- Add the completed level list to the result. Continue with the next level.

Use a queue of node references or pointers with `O(1)` enqueue and dequeue
operations. You may use a suitable queue from your language's standard library.
Do not shift every remaining element when you remove the front.

Trace the tree from Problem 1:

```text
Queue at level start    Nodes to remove    Level result
--------------------    ---------------    ------------
[4]                     1                  [4]
[2, 7]                  2                  [2, 7]
[1, 3, 6, 9]            4                  [1, 3, 6, 9]

Final result: [[4], [2, 7], [1, 3, 6, 9]]
```

The trace shows values; the queue stores node references or pointers.
Also record the queue after each node is removed and its children are added.

Test an empty tree, one node, a chain, and the binary tree from Problem 2.
That tree must return `[[2], [1, 3], [4]]`.
Confirm that traversal leaves the tree unchanged.

Explain:

- Why must you save the level size before adding children?
- Why does adding the left child first give the required order?
- Why does each node enter and leave the queue exactly once?
- Why is the time `O(n)`?

Let `w` be the largest number of nodes on one level. A queue that stores only
waiting nodes needs `O(w)` extra working space. It can contain parts of two
adjacent levels. The returned lists need another `O(n)` space.
If your queue allocates an array for all `n` nodes, report its `O(n)` space.

## Completion check

- Show **Accepted** submissions for **701**, **94**, and **102**.
- Keep your local BST builder and both traversals in your student repository.
- Keep the tree drawings, DFS call trace, BFS queue trace, and test results.
- State the time, working-space, and output-storage costs separately.
- Accepted insertion tests do not replace tests of your local build task.
- If your language requires manual memory management, release locally
  allocated nodes, queue storage, and result buffers after your tests.
  Keep judge output allocated for the judge to read.

## Recommendations

1. Give each problem at least 3-5 submission attempts before you seek help,
   unless your solution is accepted sooner. Do not look at solutions or use AI
   during these attempts.
2. Open the **Solutions** tab only **after** you have a working, accepted
   solution. Compare other approaches with your code.
3. **Optional:** After your solution works, ask AI to review your code and
   suggest improvements.
