### Binary Search Tree

A Binary Search Tree (BST) is a tree data structure in which each node has at most two children, referred to as the left child and the right child. It is a binary tree with the property that the key in each node must be greater than or equal to any key stored in the left sub-tree, and less than or equal to any key stored in the right sub-tree.

Here are some key characteristics of a Binary Search Tree:

1. **Ordered or Sorted Binary Tree**: The left sub-tree of a node contains only nodes with keys less than the node’s key. The right sub-tree of a node contains only nodes with keys greater than the node’s key. Both the left and right sub-trees must also be binary search trees.

2. **Unique Entries**: No two nodes in the tree can have the same key or data value. This property makes binary search trees suitable for dictionary problems where the tree structure is used to provide quick search, insert and delete operations.

3. **Flexible Size**: The number of nodes in a binary search tree can dynamically increase or decrease as entries are added or removed.

4. **Efficient Operations**: Binary search trees are designed to enable efficient searching, insertion, and deletion operations. These operations can usually be performed in O(log n) time, where n is the number of nodes in the tree.

Here are the basic operations that can be performed on a Binary Search Tree:

- **Search**: Starting from the root, we traverse the tree. If the current node is null, the key we are searching for does not exist in the tree. Otherwise, if the current node's key equals the key we are searching for, we return the node. If the current node's key is less than our key, we search the right subtree. Otherwise, we search the left subtree.

- **Insertion**: Starting from the root, we traverse the tree. If the tree is empty, the new node becomes the root. Otherwise, we search the tree. If the key we are inserting is less than the current node's key, we go to the left child. If it is greater, we go to the right child. When we reach a null node, we insert the new node.

- **Deletion**: There are three cases to consider when deleting a node:
  - The node to be deleted is a leaf (has no children). In this case, we just remove the node from the tree.
  - The node to be deleted has one child. In this case, we elevate the child to the position of the parent.
  - The node to be deleted has two children. This is the most complex case. We need to find the in-order predecessor or the in-order successor of the node and replace the node with it. Then, we delete the in-order predecessor or successor, which will now be a node with at most one child.

- **Traversal**: There are three common ways to traverse a BST:
  - In-order traversal: Traverse the left subtree, visit the root, then traverse the right subtree.
  - Pre-order traversal: Visit the root, traverse the left subtree, then traverse the right subtree.
  - Post-order traversal: Traverse the left subtree, traverse the right subtree, then visit the root.

These operations make the Binary Search Tree an effective data structure for many problems where the data needs to be stored in a sorted manner and the data is constantly being inserted or deleted.

Here's a simple visual representation of a Binary Search Tree (BST):

```
        8
       / \
      3   10
     / \    \
    1   6    14
       / \   /
      4   7 13
```

In this Binary Search Tree:

- `8` is the root of the tree.
- `3` and `10` are the children of `8`. `3` is the left child (because `3 < 8`), and `10` is the right child (because `10 > 8`).
- Similarly, for node `3`, `1` is the left child and `6` is the right child.
- Node `10` has `14` as its right child.
- Node `6` has `4` and `7` as its left and right child respectively.
- Node `14` has `13` as its left child.

This tree satisfies the property of a Binary Search Tree: for any given node, all elements in its left subtree are less than the node, and all elements in its right subtree are greater than the node.
