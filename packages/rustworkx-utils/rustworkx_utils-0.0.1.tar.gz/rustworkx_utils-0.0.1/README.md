# RustworkX Utils

A repository for utils for graphs constructed with rustworkx.


## Installation

```bash
pip install rustworkx_utils
```

## Example Usage

```python
from rustworkx_utils import RWXNode, ColorLegend

# Build a small DAG using RWXNode
root = RWXNode("Root", enclosed=True)
a = RWXNode("A", color=ColorLegend(name="A", color="red"))
b = RWXNode("B", color=ColorLegend(name="B", color="green"))
c = RWXNode("C", color=ColorLegend(name="C", color="blue"))

# Establish primary parent relationships
a.parent = root
b.parent = root
c.parent = a

# Add an additional non-primary edge for multi-parent showcase
c.add_parent(b)

# Visualize (should save a pdf called pdf_graph.pdf in CWD)
fig, ax = root.visualize(figsize=(10, 10), node_size=1500, font_size=15,
                          spacing_x=2.0, spacing_y=2.0,
                          layout='tidy', edge_style='orthogonal')
```

