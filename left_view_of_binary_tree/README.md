# Left View of A Binary Tree
This python program gives the left view of a given binary tree.

### Pre-requisites:
python3 or higher version should be installed

### Usage
function **__get_left_view__** can be simply imported and called by passing a binary tree to get it's left view.
```
from binary_tree_left_view import Node, get_left_view
# Create your binary tree by creating Node class instances
left_view = get_left_view(<root_node_of_your_tree>, [])
```

### Running the unittests
**1. Using python**
```
python -m unittest discover
```

**2. Using [Coverage](https://coverage.readthedocs.io/) tool**<br/>
a. Install coverage library
```
pip install coverage
```
b. run tests - 
```
coverage run --omit=test_*.py -m unittest discover
coverage report
```
