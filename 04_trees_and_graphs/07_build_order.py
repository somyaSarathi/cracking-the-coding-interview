'''
    (a) → (c) → (f)
     ↓     ↓     ↑
    (b) → (d) → (e)
'''

def isSatisfied(depends: set, order: set) -> bool:
    # O(M)
    for depend in depends:
        if depend not in order:
            return False
    
    return True


def independent(depends) -> list[str]:
    order: list = list()

    for project in depends.keys():
        if len(depends[project]) == 0:
            order.append(project)

    return order


def buildOrder(graph: dict, depends: dict, order: list):
    orderSet = set(order)
    if len(order) == 0:
        return -1

    idx: int = 0

    while idx < len(order):
        for vtx in graph[order[idx]]:
            if isSatisfied(depends[vtx], orderSet) and vtx not in orderSet:
                order.append(vtx)
                orderSet.add(vtx)

        idx += 1
    
    return order


if __name__ == '__main__':
    graph: dict = {
        'a': set(['b', 'c']),
        'b': set(['d']),
        'c': set(['d', 'f']),
        'd': set(['e']),
        'e': set(['f']),
        'f': set()
    }

    depends: dict = {
        'a': set(),
        'b': set(['a']),
        'c': set(['a']),
        'd': set(['b', 'c']),
        'e': set(['d']),
        'f': set(['c', 'e'])
    }

    print(buildOrder(graph, depends, independent(depends)))
