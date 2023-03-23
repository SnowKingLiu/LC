# by:Snowkingliu
# 2023/3/22 16:53


def get_least_cost(nodes, node_dict):
    least_cost = 0
    least_node = None
    old_node = None
    for node in nodes:
        for new_node, cost in node_dict[node].items():
            if new_node in nodes:
                continue
            if least_cost == 0 or cost < least_cost:
                least_node = new_node
                least_cost = cost
                old_node = node

    del node_dict[old_node][least_node]
    if not node_dict[old_node]:
        del node_dict[old_node]
        nodes.remove(old_node)

    del node_dict[least_node][old_node]
    if not node_dict[least_node]:
        del node_dict[least_node]
        nodes.remove(least_node)

    return least_node, least_cost


def main():
    n, m = [int(x) for x in input().split(" ")]
    node_dict = {}

    for _ in range(m):
        node1, node2, cost = [int(x) for x in input().split(" ")]
        node_dict[node1] = {**node_dict.get(node1, {}), node2: cost}
        node_dict[node2] = {**node_dict.get(node2, {}), node1: cost}
    nodes = []
    count = 0
    total_cost = 0
    while count < n:
        if count == 0:
            node = list(node_dict.keys())[0]
        else:
            node, cost = get_least_cost(nodes, node_dict)
            total_cost += cost
        nodes.append(node)
        count += 1
    print(total_cost)


if __name__ == "__main__":
    main()
