# Trees
Relationships in a tree are **hierarchical**
A tree is an ADT that stores elements hierarchical.
With the exception of the top

## Formal definition
A **tree** T is a set of **nodes** storing elements such that the nodes have a parend-child relationship that satisfies the following properties.

**siblings** - 2 nodes of the same parent
**external** - a child that has no children
External nodes are also known as **leaves**
**internal** - a node that has one or more children

## Edges and Paths in Trees
An edte of tree T is a parif of nodes(u,v) such taht u is the parent of v or vice versa.


# Ordered Trees
A tree is ordered if there is a meaningful linear order among the children of each node.

# The Tree Abstract Data Type
I define an tree ADT using the concept of **position** as an abstraction for a node of a tree.

p.element() - return the element stored at position p

The tree ADT supports the following accessor methods

T.root()
T.is_root(p)
T.parent(p)
T.num_children(p)
T.children(p)
T.is_leaf(p)
len(T)
T.is_empty()
T.positions()
iter(T)


Computing Depth and Height

Depth - number of ancestors of a *p*(Position) node excluding itself.


## Binary Trees
Properties
1. Every node has at most two children
2. Each child node is labeled as being either left child or right child
3. A left child preceed a right child in the order of children of a node

The subtree that emerges at a left or right child of an inernal node v is called left subtree or right subtree, respectively of v.

A binary tree is **proper** (full binary tree) if each node has either zero or two children.
Thus in a proper binary tree every internal node has exactly 2 children