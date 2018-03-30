def discrete_search(root_obj, expansion_fn, goal_fn, heuristic_fn=None):
    """
    Performs a search for a goal state using the A* algorithm.

    :param root_obj: The initial state object
    :param expansion_fn: Takes a state and returns an iterable of child states, along with an iterable of the transition costs of moving from parent state to child state
    :param goal_fn: Takes a state object and returns whether the state is a goal state
    :param heuristic_fn: Takes a state and returns a value <= to the actual remaining path cost to a goal state
    :return: An iterable of state objects starting from the initial state and ending with the goal state. TODO: Also return a list of the transition functions used between each state
    """
    def create_node(obj, parent, path_cost, heuristic_cost):
        class Node:
            #def __gt__(self, other):
            #    return self.path_cost > other.path_cost

            def __lt__(self, other):
                return self.path_cost + self.heuristic_cost < other.path_cost + other.heuristic_cost

        node = Node()
        node.obj = obj
        node.parent = parent
        node.path_cost = path_cost
        node.heuristic_cost = heuristic_cost

        return node

    from sortedcontainers import SortedList
    nodes = SortedList([ create_node(root_obj, None, 0, 0 if heuristic_fn is None else heuristic_fn(root_obj)) ])
    closed_set = set()

    def node_generator(node):
        while True:
            yield node

    while True:
        try:
            best_node = nodes.pop(0)
        except IndexError:
            raise ValueError('Goal state unreachable')

        if goal_fn(best_node.obj):
            break

        try:
            if best_node in closed_set:
                continue

            closed_set.add(best_node.obj)

        except TypeError:# Unhashable obj; expand anyway
            pass

        child_objs, step_costs = expansion_fn(best_node.obj)

        path_costs = [best_node.path_cost+sc for sc in step_costs]

        heuristic_costs = map((lambda obj:0) if heuristic_fn is None else heuristic_fn, child_objs)

        leaf_nodes = map(create_node, child_objs, node_generator(best_node), step_costs, heuristic_costs)

        nodes.update(leaf_nodes)

    solution = [best_node]
    while solution[-1].parent is not None:
        solution.append(solution[-1].parent)

    return [node.obj for node in solution[::-1]]