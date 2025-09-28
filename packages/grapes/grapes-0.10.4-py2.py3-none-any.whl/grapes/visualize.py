"""
This module contains tools that allow the visualization of a graph using graphviz and pygraphviz.
"""

import io
import matplotlib
import matplotlib.pyplot as plt
import networkx as nx
from PIL import Image

from .features import (
    get_all_sinks,
    get_all_sources,
    get_topological_generation_index,
    get_topological_generations,
)


def get_graphviz_digraph(
    graph,
    hide_recipes=False,
    pretty_names=False,
    include_values=False,
    color_mode="none",
    colormap="viridis",
    **attrs,
):
    """
    Create a pygraphviz AGraph from a grapes graph.

    Parameters
    ----------
    graph : grapes Graph
        The graph to visualize.
    hide_recipes : bool, optional
        If True, recipe nodes are hidden. Default is False.
    pretty_names : bool, optional
        If True, node labels are prettified. Default is False.
    include_values : bool, optional
        If True, node values are included in labels. Default is False.
    color_mode : str, optional
        Coloring mode for nodes ("none", "by_generation", "sources_and_sinks", default is "none").
    colormap : str, optional
        Name of matplotlib colormap to use. Default is "viridis".
    **attrs
        Additional attributes for the AGraph.

    Returns
    -------
    pygraphviz.AGraph
        The constructed pygraphviz AGraph.
    """
    # Get a graphviz AGraph
    g = nx.drawing.nx_agraph.to_agraph(graph._nxdg)
    # Add attributes to the AGraph
    g.graph_attr.update(**attrs)
    # Save some values that will be useful later
    max_topological_generation_index = len(get_topological_generations(graph)) - 1
    sources = get_all_sources(graph)
    sinks = get_all_sinks(graph)
    cmap = matplotlib.colormaps[colormap]

    for node_name in g.nodes():
        new_attrs = {}
        node = graph._nxdg.nodes[node_name]

        # Remove recipes if needed, or eliminate attribute of function
        if node["is_recipe"] and hide_recipes:
            g.remove_node(node_name)
            continue
        elif node["is_recipe"] and node["has_value"]:
            new_attrs.update(value="function")

        # Prettify label if required
        label = prettify_label(node_name) if pretty_names else node_name

        # Add values to the label if required
        if include_values and node.attr["has_value"]:
            if isinstance(node.attr["value"], float):
                value_in_label = "{:.2e}".format(node.attr["value"])
            else:
                value_in_label = str(node.attr["value"])
            label += "\n" + value_in_label.partition("\n")[0]
            if value_in_label.find("\n") != -1:
                label += "\n..."
        new_attrs.update(label=label)

        # Manipulate shapes
        if node["is_recipe"]:
            shape = "ellipse"
        elif node["type"] == "conditional":
            shape = "diamond"
        else:
            shape = "box"
        new_attrs.update(shape=shape)

        # Manipulate colors
        must_be_colored = False
        color_rgba = (1, 1, 1, 1)  # Default to white
        if color_mode.lower() == "by_generation":
            topological_generation_index = get_topological_generation_index(
                graph, node_name
            )
            # The __call__ method of the colormap returns a tuple of rgba values in [0, 1]
            # We call it passing the ratio between the topological_generation_index of this node and the max of the graph
            color_rgba = cmap(
                topological_generation_index / max_topological_generation_index
            )
            must_be_colored = True
        elif color_mode.lower() == "sources_and_sinks":
            if node_name in sources:
                color_rgba = cmap(0.0)
                must_be_colored = True
            elif node_name in sinks:
                color_rgba = cmap(1.0)
                must_be_colored = True
        if must_be_colored:
            # Note that graphviz wants colors in hex form
            new_attrs.update(
                style="filled",
                fillcolor=hex_string_from_rgba(*color_rgba),
                fontcolor=hex_string_from_rgba(
                    *best_text_from_background_color(*color_rgba)
                ),
            )
        # Pass these attributes to the actual AGraph
        g.get_node(node_name).attr.update(new_attrs)

        # Handle edge shapes
        if node["type"] == "standard" and "recipe" in node:
            # This condition might be false for example because of hide_recipes
            if node["recipe"] in g.nodes():
                g.get_edge(node["recipe"], node_name).attr.update(arrowhead="dot")
        elif node["type"] == "conditional":
            for condition in node["conditions"]:
                if condition in g.nodes():
                    g.get_edge(condition, node_name).attr.update(arrowhead="diamond")

    # Return the AGraph (no layout is computed yet)
    return g


def write_string(graphviz_graph):
    """
    Get the string representation of a pygraphviz AGraph.

    Parameters
    ----------
    graphviz_graph : pygraphviz.AGraph
        The graph to be converted to string.

    Returns
    -------
    str
        The string representation of the graph in dot format.
    """
    return graphviz_graph.string()


def write_dotfile(graphviz_graph, filename):
    """
    Write a pygraphviz AGraph to a dot file.

    Parameters
    ----------
    graphviz_graph : pygraphviz.AGraph
        The graph to be written.
    filename : str
        The name of the file where to save the dot file.
    """
    graphviz_graph.write(filename)


def draw_to_screen(graphviz_graph, format="png", prog="dot"):
    """
    Draw a pygraphviz AGraph to an image and display it using matplotlib.

    Parameters
    ----------
    graphviz_graph : pygraphviz.AGraph
        The graph to be drawn.
    format : str, optional
        The format of the output image (default: "png"). See graphviz documentation for supported formats.
    prog : str, optional
        The layout program to use (default: "dot"). See graphviz documentation for supported programs.
    """
    graphviz_graph.layout(prog=prog)
    buffer = io.BytesIO()
    graphviz_graph.draw(buffer, format=format)
    buffer.seek(0)
    img = Image.open(buffer)
    plt.imshow(img)
    plt.axis("off")  # Hide axes
    plt.show()


def draw_to_file(graphviz_graph, filename, format="pdf", prog="dot"):
    """
    Draw a pygraphviz AGraph to a file.

    Parameters
    ----------
    graphviz_graph : pygraphviz.AGraph
        The graph to be drawn.
    filename : str
        The name of the file where to save the drawing.
    format : str, optional
        The format of the output file (default: "pdf"). See graphviz documentation for supported formats.
    prog : str, optional
        The layout program to use (default: "dot"). See graphviz documentation for supported programs.
    """
    # Process filename
    if ("." + format) not in filename:
        filename += "." + format
    graphviz_graph.layout(prog=prog)
    graphviz_graph.draw(filename, format=format)


# Utility functions
def prettify_label(name):
    """
    Prettify a node label by capitalizing and replacing underscores with spaces.

    Parameters
    ----------
    name : str
        The original node name.

    Returns
    -------
    str
        The prettified label.
    """
    return "".join(
        c.upper() if ((i > 0 and name[i - 1] == "_") or i == 0) else c
        for i, c in enumerate(name)
    ).replace("_", " ")


def hex_string_from_rgba(r, g, b, a):
    """
    Get a formatted hex string from RGBA values.

    Parameters
    ----------
    r : float
        Red color channel in [0, 1].
    g : float
        Green color channel in [0, 1].
    b : float
        Blue color channel in [0, 1].
    a : float
        Alpha color channel in [0, 1].

    Returns
    -------
    str
        Formatted hex string starting with # and then 8 hex characters (4 bytes).
    """
    # Convert float values in [0, 1] to hex strings of two characters, e.g. 1->ff
    r_hex = f"{int(r*255):02x}"
    g_hex = f"{int(g*255):02x}"
    b_hex = f"{int(b*255):02x}"
    a_hex = f"{int(a*255):02x}"
    return "#" + r_hex + g_hex + b_hex + a_hex


def best_text_from_background_color(r, g, b, a=1.0):
    """
    Get the best text color (white or black) for a given background color.

    Parameters
    ----------
    r : float
        Red color channel in [0, 1].
    g : float
        Green color channel in [0, 1].
    b : float
        Blue color channel in [0, 1].
    a : float, optional
        Alpha color channel in [0, 1]. Default is 1.0. This value is ignored.

    Returns
    -------
    tuple
        Tuple of RGBA values representing pure white (1, 1, 1, 1) or pure black (0, 0, 0, 1) depending on luminance of input color.
    """
    luminance = 0.212 * r + 0.701 * g + 0.087 * b
    return (1, 1, 1, 1) if luminance < 0.5 else (0, 0, 0, 1)
