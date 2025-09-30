from __future__ import annotations

from dataclasses import dataclass

"""
Utilities for hashing, rendering, and general helpers used by the
symbolic query engine.
"""
import codecs
import itertools
import os
import re
from subprocess import check_call
from tempfile import NamedTemporaryFile

try:
    import six
except ImportError:
    six = None

try:
    from graphviz import Source
except ImportError:
    Source = None

from anytree import Node, RenderTree, PreOrderIter
from typing_extensions import Callable, Set, Any, Optional, List

from . import logger


class IDGenerator:
    """
    A class that generates incrementing, unique IDs and caches them for every object this is called on.
    """

    _counter = 0
    """
    The counter of the unique IDs.
    """

    # @lru_cache(maxsize=None)
    def __call__(self, obj: Any) -> int:
        """
        Creates a unique ID and caches it for every object this is called on.

        :param obj: The object to generate a unique ID for, must be hashable.
        :return: The unique ID.
        """
        self._counter += 1
        return self._counter


def lazy_iterate_dicts(dict_of_iterables):
    """Generator that yields dicts with one value from each iterable"""
    for values in zip(*dict_of_iterables.values()):
        yield dict(zip(dict_of_iterables.keys(), values))


def generate_combinations(generators_dict):
    """Yield all combinations of generator values as keyword arguments"""
    for combination in itertools.product(*generators_dict.values()):
        yield dict(zip(generators_dict.keys(), combination))


def filter_data(data, selected_indices):
    data = iter(data)
    prev = -1
    encountered_indices = set()
    for idx in selected_indices:
        if idx in encountered_indices:
            continue
        encountered_indices.add(idx)
        skip = idx - prev - 1
        data = itertools.islice(data, skip, None)
        try:
            yield next(data)
        except StopIteration:
            break
        prev = idx


def make_list(value: Any) -> List:
    """
    Make a list from a value.

    :param value: The value to make a list from.
    """
    return list(value) if is_iterable(value) else [value]


def is_iterable(obj: Any) -> bool:
    """
    Check if an object is iterable.

    :param obj: The object to check.
    """
    return hasattr(obj, "__iter__") and not isinstance(obj, (str, type, bytes, bytearray))


def make_tuple(value: Any) -> Any:
    """
    Make a tuple from a value.
    """
    return tuple(value) if is_iterable(value) else (value,)


def make_set(value: Any) -> Set:
    """
    Make a set from a value.

    :param value: The value to make a set from.
    """
    return set(value) if is_iterable(value) else {value}


def get_unique_node_names_func(root_node) -> Callable[[Node], str]:
    nodes = [root_node]

    def get_all_nodes(node):
        for c in node.children:
            nodes.append(c)
            get_all_nodes(c)

    get_all_nodes(root_node)

    def nodenamefunc(node: Node):
        """
        Set the node name for the dot exporter.
        """
        similar_nodes = [n for n in nodes if n.name == node.name]
        node_idx = similar_nodes.index(node)
        return node.name if node_idx == 0 else f"{node.name}_{node_idx}"

    return nodenamefunc


def edge_attr_setter(parent, child):
    """
    Set the edge attributes for the dot exporter.
    """
    if child and hasattr(child, "weight") and child.weight is not None:
        return f'style="bold", label=" {child.weight}"'
    return ""


_RE_ESC = re.compile(r'["\\]')


class FilteredDotExporter(object):

    def __init__(self, node, include_nodes=None, graph="digraph", name="tree", options=None,
                 indent=4, nodenamefunc=None, nodeattrfunc=None,
                 edgeattrfunc=None, edgetypefunc=None, maxlevel=None):
        """
        Dot Language Exporter.

        Args:
            node (Node): start node.

        Keyword Args:
            graph: DOT graph type.

            name: DOT graph name.

            options: list of options added to the graph.

            indent (int): number of spaces for indent.

            nodenamefunc: Function to extract node name from `node` object.
                          The function shall accept one `node` object as
                          argument and return the name of it.

            nodeattrfunc: Function to decorate a node with attributes.
                          The function shall accept one `node` object as
                          argument and return the attributes.

            edgeattrfunc: Function to decorate a edge with attributes.
                          The function shall accept two `node` objects as
                          argument. The first the node and the second the child
                          and return the attributes.

            edgetypefunc: Function to which gives the edge type.
                          The function shall accept two `node` objects as
                          argument. The first the node and the second the child
                          and return the edge (i.e. '->').

            maxlevel (int): Limit export to this number of levels.

        >>> from anytree import Node
        >>> root = Node("root")
        >>> s0 = Node("sub0", parent=root, edge=2)
        >>> s0b = Node("sub0B", parent=s0, foo=4, edge=109)
        >>> s0a = Node("sub0A", parent=s0, edge="")
        >>> s1 = Node("sub1", parent=root, edge="")
        >>> s1a = Node("sub1A", parent=s1, edge=7)
        >>> s1b = Node("sub1B", parent=s1, edge=8)
        >>> s1c = Node("sub1C", parent=s1, edge=22)
        >>> s1ca = Node("sub1Ca", parent=s1c, edge=42)

        .. note:: If the node names are not unqiue, see :any:`UniqueDotExporter`.

        A directed graph:

        >>> from anytree.exporter import DotExporter
        >>> for line in DotExporter(root):
        ...     print(line)
        digraph tree {
            "root";
            "sub0";
            "sub0B";
            "sub0A";
            "sub1";
            "sub1A";
            "sub1B";
            "sub1C";
            "sub1Ca";
            "root" -> "sub0";
            "root" -> "sub1";
            "sub0" -> "sub0B";
            "sub0" -> "sub0A";
            "sub1" -> "sub1A";
            "sub1" -> "sub1B";
            "sub1" -> "sub1C";
            "sub1C" -> "sub1Ca";
        }

        The resulting graph:

        .. image:: ../static/dotexporter0.png

        An undirected graph:

        >>> def nodenamefunc(node):
        ...     return '%s:%s' % (node.name, node.depth)
        >>> def edgeattrfunc(node, child):
        ...     return 'label="%s:%s"' % (node.name, child.name)
        >>> def edgetypefunc(node, child):
        ...     return '--'
                >>> from anytree.exporter import DotExporter
        >>> for line in DotExporter(root, graph="graph",
        ...                             nodenamefunc=nodenamefunc,
        ...                             nodeattrfunc=lambda node: "shape=box",
        ...                             edgeattrfunc=edgeattrfunc,
        ...                             edgetypefunc=edgetypefunc):
        ...     print(line)
        graph tree {
            "root:0" [shape=box];
            "sub0:1" [shape=box];
            "sub0B:2" [shape=box];
            "sub0A:2" [shape=box];
            "sub1:1" [shape=box];
            "sub1A:2" [shape=box];
            "sub1B:2" [shape=box];
            "sub1C:2" [shape=box];
            "sub1Ca:3" [shape=box];
            "root:0" -- "sub0:1" [label="root:sub0"];
            "root:0" -- "sub1:1" [label="root:sub1"];
            "sub0:1" -- "sub0B:2" [label="sub0:sub0B"];
            "sub0:1" -- "sub0A:2" [label="sub0:sub0A"];
            "sub1:1" -- "sub1A:2" [label="sub1:sub1A"];
            "sub1:1" -- "sub1B:2" [label="sub1:sub1B"];
            "sub1:1" -- "sub1C:2" [label="sub1:sub1C"];
            "sub1C:2" -- "sub1Ca:3" [label="sub1C:sub1Ca"];
        }

        The resulting graph:

        .. image:: ../static/dotexporter1.png

        To export custom node implementations or :any:`AnyNode`, please provide a proper `nodenamefunc`:

        >>> from anytree import AnyNode
        >>> root = AnyNode(id="root")
        >>> s0 = AnyNode(id="sub0", parent=root)
        >>> s0b = AnyNode(id="s0b", parent=s0)
        >>> s0a = AnyNode(id="s0a", parent=s0)

        >>> from anytree.exporter import DotExporter
        >>> for line in DotExporter(root, nodenamefunc=lambda n: n.id):
        ...     print(line)
        digraph tree {
            "root";
            "sub0";
            "s0b";
            "s0a";
            "root" -> "sub0";
            "sub0" -> "s0b";
            "sub0" -> "s0a";
        }
        """
        self.node = node
        self.graph = graph
        self.name = name
        self.options = options
        self.indent = indent
        self.nodenamefunc = nodenamefunc
        self.nodeattrfunc = nodeattrfunc
        self.edgeattrfunc = edgeattrfunc
        self.edgetypefunc = edgetypefunc
        self.maxlevel = maxlevel
        self.include_nodes = include_nodes
        node_name_func = get_unique_node_names_func(node)
        self.include_node_names = [node_name_func(n) for n in self.include_nodes] if include_nodes else None

    def __iter__(self):
        # prepare
        indent = " " * self.indent
        nodenamefunc = self.nodenamefunc or self._default_nodenamefunc
        nodeattrfunc = self.nodeattrfunc or self._default_nodeattrfunc
        edgeattrfunc = self.edgeattrfunc or self._default_edgeattrfunc
        edgetypefunc = self.edgetypefunc or self._default_edgetypefunc
        return self.__iter(indent, nodenamefunc, nodeattrfunc, edgeattrfunc,
                           edgetypefunc)

    @staticmethod
    def _default_nodenamefunc(node):
        return node.name

    @staticmethod
    def _default_nodeattrfunc(node):
        return None

    @staticmethod
    def _default_edgeattrfunc(node, child):
        return None

    @staticmethod
    def _default_edgetypefunc(node, child):
        return "->"

    def __iter(self, indent, nodenamefunc, nodeattrfunc, edgeattrfunc, edgetypefunc):
        yield "{self.graph} {self.name} {{".format(self=self)
        for option in self.__iter_options(indent):
            yield option
        for node in self.__iter_nodes(indent, nodenamefunc, nodeattrfunc):
            yield node
        for edge in self.__iter_edges(indent, nodenamefunc, edgeattrfunc, edgetypefunc):
            yield edge
        yield "}"

    def __iter_options(self, indent):
        options = self.options
        if options:
            for option in options:
                yield "%s%s" % (indent, option)

    def __iter_nodes(self, indent, nodenamefunc, nodeattrfunc):
        emitted_nodes = set()
        for node in PreOrderIter(self.node, maxlevel=self.maxlevel):
            nodename = nodenamefunc(node)
            if self.include_nodes is not None and nodename not in self.include_node_names:
                continue
            if nodename in emitted_nodes:
                continue
            emitted_nodes.add(nodename)
            nodeattr = nodeattrfunc(node)
            nodeattr = " [%s]" % nodeattr if nodeattr is not None else ""
            yield '%s"%s"%s;' % (indent, FilteredDotExporter.esc(nodename), nodeattr)

    def __iter_edges(self, indent, nodenamefunc, edgeattrfunc, edgetypefunc):
        maxlevel = self.maxlevel - 1 if self.maxlevel else None
        emitted_edges = set()
        for node in PreOrderIter(self.node, maxlevel=maxlevel):
            nodename = nodenamefunc(node)
            if self.include_nodes is not None and nodename not in self.include_node_names:
                continue
            for child in node.children:
                childname = nodenamefunc(child)
                if self.include_nodes is not None and childname not in self.include_node_names:
                    continue
                edge_key = (nodename, childname)
                if edge_key in emitted_edges:
                    continue
                emitted_edges.add(edge_key)
                edgeattr = edgeattrfunc(node, child)
                edgetype = edgetypefunc(node, child)
                edgeattr = " [%s]" % edgeattr if edgeattr is not None else ""
                yield '%s"%s" %s "%s"%s;' % (indent, FilteredDotExporter.esc(nodename), edgetype,
                                             FilteredDotExporter.esc(childname), edgeattr)

    def to_dotfile(self, filename):
        """
        Write graph to `filename`.

        >>> from anytree import Node
        >>> root = Node("root")
        >>> s0 = Node("sub0", parent=root)
        >>> s0b = Node("sub0B", parent=s0)
        >>> s0a = Node("sub0A", parent=s0)
        >>> s1 = Node("sub1", parent=root)
        >>> s1a = Node("sub1A", parent=s1)
        >>> s1b = Node("sub1B", parent=s1)
        >>> s1c = Node("sub1C", parent=s1)
        >>> s1ca = Node("sub1Ca", parent=s1c)

        >>> from anytree.exporter import DotExporter
        >>> DotExporter(root).to_dotfile("tree.dot")

        The generated file should be handed over to the `dot` tool from the
        http://www.graphviz.org/ package::

            $ dot tree.dot -T png -o tree.png
        """
        with codecs.open(filename, "w", "utf-8") as file:
            for line in self:
                file.write("%s\n" % line)

    def to_picture(self, filename):
        """
        Write graph to a temporary file and invoke `dot`.

        The output file type is automatically detected from the file suffix.

        *`graphviz` needs to be installed, before usage of this method.*
        """
        fileformat = os.path.splitext(filename)[1][1:]
        with NamedTemporaryFile("wb", delete=False) as dotfile:
            dotfilename = dotfile.name
            for line in self:
                dotfile.write(("%s\n" % line).encode("utf-8"))
            dotfile.flush()
            cmd = ["dot", dotfilename, "-T", fileformat, "-o", filename]
            check_call(cmd)
        try:
            os.remove(dotfilename)
        except Exception:  # pragma: no cover
            msg = 'Could not remove temporary file %s' % dotfilename
            logger.warning(msg)

    def to_source(self) -> Source:
        """
        Return the source code of the graph as a Source object.
        """
        return Source("\n".join(self), filename=self.name)

    @staticmethod
    def esc(value):
        """Escape Strings."""
        return _RE_ESC.sub(lambda m: r"\%s" % m.group(0), six.text_type(value))


def render_tree(root: Node, use_dot_exporter: bool = False,
                filename: str = "query_tree", only_nodes: List[Node] = None, show_in_console: bool = False,
                color_map: Optional[Callable[[Node], str]] = None,
                view: bool = False, layout_engine: str = "dot", render_backend: str = "graphviz") -> None:
    """
    Render the tree/graph using console and optionally export it to an image file.

    :param root: The root node of the tree/graph.
    :param use_dot_exporter: Whether to export using Graphviz/DOT (kept for backward-compat with anytree).
    :param filename: The base file name for output files (without extension).
    :param only_nodes: Limit export to these nodes (anytree only).
    :param show_in_console: Whether to print a textual representation.
    :param color_map: Function mapping a node to a color string.
    :param view: Whether to open a viewer after generating (graphviz backend only).
    :param layout_engine: Layout name. For graphviz: "dot", "neato", etc. For igraph: "tree", "kk", "fr", "sugiyama".
    :param render_backend: "graphviz" (default) or "igraph" for python-igraph.
    """
    if not root:
        logger.warning("No nodes to render")
        return

    # Detect anytree.Node vs RWX-like node (duck-typing on children attr but not anytree.Node)
    is_anytree = isinstance(root, Node)

    if show_in_console:
        if is_anytree:
            for pre, _, node in RenderTree(root):
                if only_nodes is not None and node not in only_nodes:
                    continue
                print(f"{pre}{getattr(node, 'weight', '') or ''} {node.__str__()}")
        else:
            # Simple DFS console render for RWX-like nodes
            def dfs(n, depth=0, seen=None):
                seen = seen or set()
                if id(n) in seen:
                    return
                seen.add(id(n))
                indent = ' ' * (depth * 2)
                print(f"{indent}{getattr(n, 'weight', '') or ''} {n}")
                for c in getattr(n, 'children', []):
                    dfs(c, depth + 1, seen)
            dfs(root)

    # Graphviz path for anytree
    if is_anytree and (render_backend == "graphviz" or use_dot_exporter):
        unique_node_names = get_unique_node_names_func(root)
        de = FilteredDotExporter(root,
                                 include_nodes=only_nodes,
                                 nodenamefunc=unique_node_names,
                                 edgeattrfunc=edge_attr_setter,
                                 nodeattrfunc=lambda node: \
                                     f'style=filled,'
                                     f' fillcolor={color_map(node) if color_map else getattr(node, "color", "white")}',
                                 )
        if view:
            de.to_source().view()
        else:
            filename = filename or "query_tree"
            de.to_dotfile(f"{filename}{'.dot'}")
            try:
                de.to_picture(f"{filename}{'.svg'}")
            except FileNotFoundError as e:
                logger.warning(f"{e}")
        return

    # For RWX-like graphs we support either igraph or graphviz
    # Collect nodes and unique edges first
    if not is_anytree:
        nodes = []
        edges = set()
        seen = set()

        def collect(n):
            if id(n) in seen:
                return
            seen.add(id(n))
            nodes.append(n)
            for c in getattr(n, 'children', []):
                # avoid duplicate edges
                edge_key = (id(n), id(c))
                if edge_key not in edges:
                    edges.add(edge_key)
                collect(c)

        collect(root)

        # Fallback or explicit graphviz backend for RWX
        # Build DOT string
        lines = ["digraph tree {"]
        for n in nodes:
            fill = getattr(n, 'color', 'white')
            raw_label = getattr(n, 'name', str(n))
            label = FilteredDotExporter.esc(raw_label)
            lines.append(f'    "{id(n)}" [label="{label}", style=filled, fillcolor={fill}];')
        for (a, b) in edges:
            child_obj = next((x for x in nodes if id(x) == b), None)
            edge_attrs = ''
            wt = getattr(child_obj, 'weight', None)
            if wt is not None:
                wt_str = FilteredDotExporter.esc(str(wt))
                edge_attrs = f' [style="bold", label=" {wt_str}"]'
            lines.append(f'    "{a}" -> "{b}"{edge_attrs};')
        lines.append("}")
        dot_src = "\n".join(lines)

        if Source is not None:
            try:
                src = Source(dot_src, filename=filename or "query_tree", engine=layout_engine)
                if view:
                    src.view()
                else:
                    # write .dot and .svg
                    dot_path = f"{filename or 'query_tree'}.dot"
                    with codecs.open(dot_path, 'w', 'utf-8') as f:
                        f.write(dot_src)
                    try:
                        svg = src.pipe(format='svg')
                        svg_path = f"{filename or 'query_tree'}.svg"
                        with codecs.open(svg_path, 'w', 'utf-8') as f:
                            f.write(svg.decode('utf-8') if isinstance(svg, (bytes, bytearray)) else svg)
                    except Exception as e:
                        logger.warning(f"graphviz render failed: {e}")
            except Exception as e:
                logger.warning(f"graphviz Source failed: {e}")
        else:
            # Fallback: write dot and try CLI engine
            dot_path = f"{filename or 'query_tree'}.dot"
            with codecs.open(dot_path, 'w', 'utf-8') as f:
                f.write(dot_src)
            try:
                cmd = [layout_engine, dot_path, '-T', 'svg', '-o', f"{filename or 'query_tree'}.svg"]
                check_call(cmd)
            except Exception as e:
                logger.warning(f"Failed external graphviz call: {e}")


@dataclass(eq=False)
class ALL:
    """
    Sentinel that compares equal to any other value.

    This is used to signal wildcard matches in hashing/containment logic.
    """
    def __eq__(self, other):
        """Always return True."""
        return True

    def __hash__(self):
        """Hash based on object identity to remain unique as a sentinel."""
        return hash(id(self))


All = ALL()
