"""
This module contains utility functions for grapes.
These are the main functions that an user (not designer) should use to interact with a grapes graph.
"""

import copy
import json
import sys
import warnings

# Since tomllib is only standard in 3.11, we import tomli in prior versions
if sys.version_info.major >= 3 and sys.version_info.minor >= 11:
    import tomllib
else:
    import tomli as tomllib

from .context import (
    clear_values,
    get_internal_context,
    get_dict_of_values,
    get_list_of_values,
    set_internal_context,
    update_internal_context,
)
from .evaluate import execute_to_targets, progress_towards_targets
from .features import (
    freeze,
    get_all_sinks,
    get_args,
    get_kwargs,
    get_recipe,
    get_topological_generation_index,
    unfreeze,
)
from .merge import get_subgraph
from .path import get_path_to_target
from .reachability import (
    clear_reachabilities,
    compute_reachability_targets,
    get_has_reachability,
    get_reachability,
    get_worst_reachability,
)
from .simplify import (
    convert_all_conditionals_to_trivial_steps,
    simplify_all_dependencies,
)


def execute_graph_from_context(
    graph, context, *targets, inplace=False, check_feasibility=True
):
    """
    Execute a graph up to the desired targets given a context.

    Parameters
    ----------
    graph : grapes Graph
        Graph of the computation.
    context : dict
        Dictionary of the initial context of the computation (input).
    targets : hashables (typically strings)
        Indicator of what to compute (desired output).
    inplace : bool
        Whether to modify graph and context inplace (default: False).
    check_feasibility : bool
        Whether to check the feasibility of the computation, which slows performance (default: True).

    Returns
    -------
    grapes Graph
        Graph with context updated after computation.
    """
    # No target is interpreted as compute everything
    if len(targets) == 0:
        targets = get_all_sinks(graph, exclude_recipes=True)

    if check_feasibility:
        feasibility, missing_dependencies = check_feasibility_of_execution(
            graph, context, *targets, inplace=inplace
        )
        if feasibility == "unreachable":
            raise ValueError(
                "The requested computation is unfeasible because of the following missing dependencies: "
                + ", ".join(missing_dependencies)
            )
        elif feasibility == "uncertain":
            warnings.warn(
                "The feasibility of the requested computation is uncertain because of the following missing dependencies: "
                + ", ".join(missing_dependencies)
            )

    if not inplace:
        graph = copy.deepcopy(graph)
        context = copy.deepcopy(context)

    set_internal_context(graph, context)
    execute_to_targets(graph, *targets)

    return graph


def json_from_graph(graph):
    """
    Get a JSON string representing the context of a graph.

    Parameters
    ----------
    graph : grapes Graph
        Graph containing the context to convert to JSON.

    Returns
    -------
    str
        JSON string that prettily represents the context of the graph.
    """

    context = get_internal_context(graph, exclude_recipes=True)
    non_serializable_items = {}
    for key, value in context.items():
        try:
            json.dumps(value)
        except:
            non_serializable_items.update({key: str(value)})
    if (
        len(non_serializable_items) > 0
    ):  # We must copy the context, to preserve it, and dump a modified version of it
        res = copy.deepcopy(context)
        res.update(non_serializable_items)
    else:
        res = context
    return json.dumps(res, sort_keys=True, indent=4, separators=(",", ": "))


def context_from_json_file(file_name):
    """
    Load a json file into a dictionary.

    Parameters
    ----------
    file_name : str
        Path to the json file.

    Returns
    -------
    dict
        Content of the file as dictionary.
    """
    with open(file_name, encoding="utf-8") as json_file:
        data = json.load(json_file)
    return data


def context_from_toml_file(file_name):
    """
    Load a toml file into a dictionary.

    Parameters
    ----------
    file_name : str
        Path to the toml file.

    Returns
    -------
    dict
        Content of the file as dictionary.
    """
    with open(file_name, "rb") as toml_file:
        data = tomllib.load(toml_file)
    return data


def context_from_file(file_name):
    """
    Load a file (any of the supported formats) into a dictionary.

    Parameters
    ----------
    file_name : str
        Path to the file.

    Returns
    -------
    dict
        Content of the file as dictionary.
    """
    supported_formats = ["JSON", "TOML"]
    reading_functions = [context_from_json_file, context_from_toml_file]
    for func in reading_functions:
        try:
            data = func(file_name)
            return data
        except (json.decoder.JSONDecodeError, tomllib.TOMLDecodeError):
            pass
    # If we arrive here, there has been an issue in all reading functions
    raise ValueError(
        "File "
        + file_name
        + " is not valid in any of the supported formats ("
        + ",".join(supported_formats)
        + ")"
    )


def wrap_graph_with_function(
    graph, input_keys, *targets, constants={}, input_as_kwargs=True, output_as_dict=True
):
    """
    Wrap a the execution of a graph into a function that can be called with the desired inputs and returns the desired outputs.

    Parameters
    ----------
    graph : grapes Graph
        Graph of the computation.
    input_keys : hashables (typically strings)
        Keys in the graph that will be treated as inputs of the function.
    targets : hashables (typically strings)
        Keys in the graph that will be treated as outputs of the function.
    constants : dict
        Keys and values that are assigned to the graph before the function creation and are present when the function is called, default is empty set. If a key is both in constants and input_keys, it is treated as input (i.e., the value in constants is ignored).
    input_as_kwargs : bool
        Whether the input of the function is a set of keyword arguments (True) or a list (False), default: True.
    output_as_dict : bool
        Whether the output of the function is a dictionary (True) or a list (False), default: True.

    Returns
    -------
    function
        A function that can be called with the desired inputs and returns the desired outputs.
    """
    # Copy graph so as not to pollute the original
    operational_graph = copy.deepcopy(graph)
    # Pass all constants to the graph
    update_internal_context(operational_graph, constants)
    # Freeze so that the constants are fixed
    freeze(operational_graph)
    # Unfreeze the input.
    # Note that this has precedence over constants (i.e., if a key is both input and constant, it is treated as input)
    if len(input_keys) > 0:
        unfreeze(operational_graph, *input_keys)
        clear_values(operational_graph, *input_keys)
    # No target is interpreted as compute everything
    if len(targets) == 0:
        targets = get_all_sinks(operational_graph, exclude_recipes=True)
    # Move as much as possible towards targets
    progress_towards_targets(operational_graph, *targets)
    # Check feasibility
    placeholder_value = 0
    context = {key: placeholder_value for key in input_keys}
    feasibility, missing_dependencies = check_feasibility_of_execution(
        operational_graph, context, *targets
    )
    if feasibility == "unreachable":
        raise ValueError(
            "The requested computation is unfeasible because of the following missing dependencies: "
            + ", ".join(missing_dependencies)
        )
    elif feasibility == "uncertain":
        warnings.warn(
            "The feasibility of the requested computation is uncertain because of the following missing dependencies: "
            + ", ".join(missing_dependencies)
        )

    if input_as_kwargs and output_as_dict:

        def specific_function_input_as_kwargs_output_as_dict(**kwargs):
            # Use for loop rather than dict comprehension because it is a more basic operation
            for key in input_keys:
                operational_graph[key] = kwargs[key]
            execute_to_targets(operational_graph, *targets)
            dict_of_values = get_dict_of_values(operational_graph, targets)
            # Clear values so that the function can be called again
            clear_values(operational_graph)
            if len(dict_of_values.keys()) == 1:
                return dict_of_values[list(dict_of_values.keys())[0]]
            else:
                return dict_of_values

        return specific_function_input_as_kwargs_output_as_dict

    elif input_as_kwargs and not output_as_dict:

        def specific_function_input_as_kwargs_output_as_list(**kwargs):
            # Use for loop rather than dict comprehension because it is a more basic operation
            for key in input_keys:
                operational_graph[key] = kwargs[key]
            execute_to_targets(operational_graph, *targets)
            list_of_values = get_list_of_values(operational_graph, targets)
            # Clear values so that the function can be called again
            clear_values(operational_graph)
            if len(list_of_values) == 1:
                return list_of_values[0]
            else:
                return list_of_values

        return specific_function_input_as_kwargs_output_as_list

    elif not input_as_kwargs and output_as_dict:
        input_keys = list(input_keys)

        def specific_function_input_as_args_output_as_dict(*args):
            # Use for loop rather than dict comprehension because it is a more basic operation
            for i in range(len(input_keys)):
                operational_graph[input_keys[i]] = args[i]
            execute_to_targets(operational_graph, *targets)
            dict_of_values = get_dict_of_values(operational_graph, targets)
            # Clear values so that the function can be called again
            clear_values(operational_graph)
            if len(dict_of_values.keys()) == 1:
                return dict_of_values[list(dict_of_values.keys())[0]]
            else:
                return dict_of_values

        return specific_function_input_as_args_output_as_dict

    else:  # not input_as_kwargs and not output_as_dict
        input_keys = list(input_keys)

        def specific_function_input_as_args_output_as_list(*args):
            # Use for loop rather than dict comprehension because it is a more basic operation
            for i in range(len(input_keys)):
                operational_graph[input_keys[i]] = args[i]
            execute_to_targets(operational_graph, *targets)
            list_of_values = get_list_of_values(operational_graph, targets)
            # Clear values so that the function can be called again
            clear_values(operational_graph)
            if len(list_of_values) == 1:
                return list_of_values[0]
            else:
                return list_of_values

        return specific_function_input_as_args_output_as_list


def lambdify_graph(graph, input_keys, target, constants={}):
    """
    Convert a graph into a function that can be called with the desired inputs and returns the desired output.
    This function is independent from the rest of grapes, and does not require any other grapes function to work.

    Parameters
    ----------
    graph : grapes Graph
        Graph of the computation.
    input_keys : list or set of strings
        Keys in the graph that will be treated as inputs of the function.
    target : string (or name of a node in the graph)
        Key in the graph that will be treated as output of the function.
    constants : dict
        Keys and values that are assigned to the graph before the function creation and are present when the function is called, default: {}. If a key is both in constants and input_keys, it is treated as input (i.e., the value in constants is ignored).

    Returns
    -------
    function
        A function that can be called with the desired inputs and returns the desired output.
    """
    # Copy graph so as not to pollute the original
    operational_graph = copy.deepcopy(graph)
    # Pass all constants to the graph
    update_internal_context(operational_graph, constants)
    # Freeze so that the constants are fixed
    freeze(operational_graph)
    # Unfreeze the input.
    # Note that this has precedence over constants (i.e., if a key is both input and constant, it is treated as input)
    if len(input_keys) > 0:
        unfreeze(operational_graph, *input_keys)
        clear_values(operational_graph, *input_keys)
    # Convert all conditional, progressing to the conditions
    convert_all_conditionals_to_trivial_steps(
        operational_graph, execute_towards_conditions=True
    )
    # Progress as much as possible
    progress_towards_targets(operational_graph, target)
    # The starting point of the computation will include the constants
    initial_keys = set(input_keys) | set(constants.keys())
    # Simplify until the graph is a single function
    while not set(
        get_args(operational_graph, target)
        + tuple(get_kwargs(operational_graph, target).values())
    ).issubset(initial_keys):
        simplify_all_dependencies(operational_graph, target, exclude=initial_keys)
    # Get the function representing the graph
    function = operational_graph[get_recipe(operational_graph, target)]
    # If needed, get a function only of the input keys
    if len(constants) > 0:

        def function_only_input_keys(**kwargs):
            kwargs.update(constants)
            return function(**kwargs)

        return function_only_input_keys
    else:
        return function


def check_feasibility_of_execution(graph, context, *targets, inplace=False):
    """
    Check the feasibility of executing a graph up to the desired targets given a context.

    Parameters
    ----------
    graph : grapes Graph
        Graph of the computation.
    context : dict
        Dictionary of the initial context of the computation (input).
    targets : hashables (typically strings)
        Indicator of what to compute (desired output).
    inplace : bool
        Whether to modify graph and context inplace (default: False).

    Returns
    -------
    feasibility : str
        One of "reachable", "unreachable", "uncertain".
    missing_dependencies : set
        Set of nodes that are missing in the context and prevent the computation from being feasible.
    """
    # No target is interpreted as compute everything
    if len(targets) == 0:
        targets = graph.get_all_sinks(exclude_recipes=True)

    if not inplace:
        graph = copy.deepcopy(graph)
        context = copy.deepcopy(context)

    clear_reachabilities(graph)
    set_internal_context(graph, context)
    compute_reachability_targets(graph, *targets)
    feasibility = get_worst_reachability(graph, *targets)
    missing_dependencies = set()
    if feasibility in {"unreachable", "uncertain"}:
        for node in graph.nodes:
            if (
                get_topological_generation_index(graph, node) == 0
                and get_has_reachability(graph, node)
                and get_reachability(graph, node) != "reachable"
            ):
                missing_dependencies.add(node)
    return feasibility, missing_dependencies


def get_execution_subgraph(graph, context, *targets):
    """
    Get the subgraph that would be executed to compute the desired targets given a context.

    Parameters
    ----------
    graph : grapes Graph
        Graph of the computation.
    context : dict
        Dictionary of the initial context of the computation (input).
    targets : hashables (typically strings)
        Indicator of what to compute (desired output).

    Returns
    -------
    grapes Graph
        Subgraph that would be executed to compute the desired targets given the context.
    """
    graph = copy.deepcopy(graph)
    context = copy.deepcopy(context)
    update_internal_context(graph, context)
    path = set()
    for target in targets:
        path = path | get_path_to_target(graph, target)
    return get_subgraph(graph, path)
