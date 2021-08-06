#!/usr/bin/env python

"""
Toytree: A minimalist Python package for tree drawing and manipulation.
...
"""

__version__ = "2.1.0-dev"
__author__ = "Deren Eaton"


# expose types: ToyTree, MultiTree
# expose constructors: .tree, .rtree, .mtree, .rawtree
from toytree.core.tree import tree, ToyTree
from toytree.core.rawtree import RawTree as rawtree
from toytree.core.treenode import TreeNode
from toytree.core import rtree
from toytree.core.multitree import mtree, MultiTree
from toytree.core.drawing.colors import COLORS1 as colors
from toytree.core.drawing.colors import ICOLORS1 as icolors

# expose submodules
# import toytree.pcm

# start the logger in INFO
from toytree.utils.logger import set_loglevel
set_loglevel("WARNING")
