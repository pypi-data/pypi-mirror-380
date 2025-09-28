"""
This module contains functions to evaluate the graph, i.e. call the recipes or assign conditionals to compute values of nodes.
Usually, it is unnecessary to call these functions directly, as the more convenient interface is in the `util` module.
"""

from .context import get_kwargs_values, get_list_of_values
from .features import (
    get_args,
    get_conditions,
    get_has_value,
    get_kwargs,
    get_possibilities,
    get_recipe,
    get_type,
    get_value,
    set_value,
)


def evaluate_target(graph, target, continue_on_fail=False):
    """
    Evaluate a target node in the graph (any type of node).

    Parameters
    ----------
    graph : grapes Graph
        The graph containing the node to evaluate.
    target : hashable (typically string)
        The name of the node to evaluate.
    continue_on_fail : bool, optional
        If True, continue evaluation even if an error occurs. Default is False.

    Raises
    ------
    ValueError
        If the node type is not supported.

    Notes
    -----
    If continue_on_fail is False, any error during evaluation will raise an exception.
    """
    if get_type(graph, target) == "standard":
        return evaluate_standard(graph, target, continue_on_fail)
    elif get_type(graph, target) == "conditional":
        return evaluate_conditional(graph, target, continue_on_fail)
    else:
        raise ValueError(
            "Evaluation of nodes of type "
            + get_type(graph, target)
            + " is not supported"
        )


def evaluate_standard(graph, node, continue_on_fail=False):
    """
    Evaluate a standard node in the graph.

    Parameters
    ----------
    graph : grapes Graph
        The graph containing the node to evaluate.
    node : hashable (typically string)
        The name of the standard node to evaluate.
    continue_on_fail : bool, optional
        If True, continue evaluation even if an error occurs. Default is False.

    Raises
    ------
    Exception
        If evaluation fails and continue_on_fail is False.
    """
    # Check if it already has a value
    if get_has_value(graph, node):
        get_value(graph, node)
        return
    # If not, evaluate all arguments
    for dependency_name in graph._nxdg.predecessors(node):
        evaluate_target(graph, dependency_name, continue_on_fail)

    # Actual computation happens here
    try:
        recipe = get_recipe(graph, node)
        func = get_value(graph, recipe)
        res = func(
            *get_list_of_values(graph, get_args(graph, node)),
            **get_kwargs_values(graph, get_kwargs(graph, node))
        )
    except Exception as e:
        if continue_on_fail:
            # Do nothing, we want to keep going
            return
        else:
            if len(e.args) > 0:
                e.args = ("While evaluating " + node + ": " + str(e.args[0]),) + e.args[
                    1:
                ]
            raise
    # Save results
    set_value(graph, node, res)


def evaluate_conditional(graph, conditional, continue_on_fail=False):
    """
    Evaluate a conditional node in the graph.

    Parameters
    ----------
    graph : grapes Graph
        The graph containing the conditional node.
    conditional : hashable (typically string)
        The name of the conditional node to evaluate.
    continue_on_fail : bool, optional
        If True, continue evaluation even if an error occurs. Default is False.

    Raises
    ------
    ValueError
        If no condition is true or evaluation fails and continue_on_fail is False.
    """
    # Check if it already has a value
    if get_has_value(graph, conditional):
        get_value(graph, conditional)
        return
    # If not, check if one of the conditions already has a true value
    for index, condition in enumerate(get_conditions(graph, conditional)):
        if get_has_value(graph, condition) and get_value(graph, condition):
            break
    else:
        # Happens only if loop is never broken
        # In this case, evaluate the conditions until one is found true
        for index, condition in enumerate(get_conditions(graph, conditional)):
            evaluate_target(graph, condition, continue_on_fail)
            if get_has_value(graph, condition) and get_value(graph, condition):
                break
            elif not get_has_value(graph, condition):
                # Computing failed
                if continue_on_fail:
                    # Do nothing, we want to keep going
                    return
                else:
                    raise ValueError("Node " + condition + " could not be computed")
        else:  # Happens if loop is never broken, i.e. when no conditions are true
            index = -1

    # Actual computation happens here
    possibility = get_possibilities(graph, conditional)[index]
    try:
        evaluate_target(graph, possibility, continue_on_fail)
        res = get_value(graph, possibility)
    except:
        if continue_on_fail:
            # Do nothing, we want to keep going
            return
        else:
            raise ValueError("Node " + possibility + " could not be computed")
    # Save results and release
    set_value(graph, conditional, res)


def execute_to_targets(graph, *targets):
    """
    Evaluate all nodes in the graph required to reach the specified targets.

    Parameters
    ----------
    graph : grapes Graph
        The graph containing the nodes to evaluate.
    *targets : hashables (typically strings)
        Names of one or more target nodes to evaluate.
    """
    for target in targets:
        evaluate_target(graph, target, False)


def progress_towards_targets(graph, *targets):
    """
    Progress towards the specified targets by evaluating nodes, continuing on failure.

    Parameters
    ----------
    graph : grapes Graph
        The graph containing the nodes to evaluate.
    *targets : hashables (typically strings)
        Names of one or more target nodes to evaluate.
    """
    for target in targets:
        evaluate_target(graph, target, True)


def execute_towards_conditions(graph, *conditions):
    """
    Progress towards the specified conditions, stopping if one is found true.

    Parameters
    ----------
    graph : grapes Graph
        The graph containing the conditions.
    *conditions : hashables (typically strings)
        Names of one or more (condition) nodes to evaluate.
    """
    for condition in conditions:
        evaluate_target(graph, condition, True)
        if get_has_value(graph, condition) and graph[condition]:
            break


def execute_towards_all_conditions_of_conditional(graph, conditional):
    """
    Progress towards all conditions of a specific conditional node, stopping if one is found true.

    Parameters
    ----------
    graph : grapes Graph
        The graph containing the conditional node.
    conditional : hashable (typically string)
        The name of the conditional node whose conditions are to be evaluated.
    """
    execute_towards_conditions(graph, *get_conditions(graph, conditional))
