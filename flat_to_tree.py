from collections import defaultdict
from pprint import pprint
data = [
    {"menu": "menu 1", "id": 1, "parent_id": None},
    {"menu": "menu 1.1", "id": 2, "parent_id": 1},
    {"menu": "menu 1.2", "id": 3, "parent_id": 1},
    {"menu": "menu 1.3", "id": 4, "parent_id": 1},
    {"menu": "menu 1.1.1", "id": 5, "parent_id": 2},
    {"menu": "menu 1.1.2", "id": 6, "parent_id": 2},
    {"menu": "menu 1.1.3", "id": 7, "parent_id": 2},
    {"menu": "menu 2", "id": 8, "parent_id": None},
    {"menu": "menu 2.1", "id": 9, "parent_id": 8},
    {"menu": "menu 2.2", "id": 10, "parent_id": 8},
    {"menu": "menu 2.3", "id": 11, "parent_id": 8},
    {"menu": "menu 2.4", "id": 12, "parent_id": 8},
    {"menu": "menu 2.1.1", "id": 13, "parent_id": 9},
    {"menu": "menu 2.1.2", "id": 14, "parent_id": 9},
    {"menu": "menu 2.1.3", "id": 15, "parent_id": 9},
    {"menu": "menu 2.1.4", "id": 16, "parent_id": 9},
    {"menu": "menu 2.3.1", "id": 17, "parent_id": 11},
    {"menu": "menu 2.3.2", "id": 18, "parent_id": 11},
    {"menu": "menu 2.4.2", "id": 19, "parent_id": 25},
    {"menu": "menu 2.4.1", "id": 20, "parent_id": 25},
]


def convert_flat_to_hierachy_tree(list_of_dict, parent_name, ref_name):
    """ Root có superior id là null hoặc không có parent trong mảng
        :parameter:

            - list_of_dict: list các dictionary cần chuyển đổi
            - parent_name: tên của tham số gốc:     vd: user_id
            - ref_name: tên của tham số liên kết:   vd: superior_id

        :result:
            - tree of dict: các node cha là None
    """
    if list_of_dict in (None, []):
        return []

    def build_hierarchy(parent, child_lookup):
        childs = child_lookup.get(parent[parent_name], list())
        for c in childs:
            build_hierarchy(c, child_lookup)
        if childs:
            parent['childs'] = childs
        return parent

    list_childs = defaultdict(list)
    list_id = {item.get(parent_name) for item in list_of_dict}
    list_parent_id = {item.get(ref_name) for item in list_of_dict}

    list_parent_id_want_to_get = []
    for item in list_parent_id:
        if item not in list_id:
            list_parent_id_want_to_get.append(item)
    for e in list_of_dict:
        list_childs[e[ref_name]].append(e)

    list_parent = list()
    for item in list_parent_id_want_to_get:
        data = list_childs.get(item)
        if data not in ([], None):
            list_parent += data

    child_lookup = list_childs
    result = []

    for parent in list_parent:
        hierarchy = build_hierarchy(parent=parent, child_lookup=child_lookup)
        result.append(hierarchy)
    return result


tree = convert_flat_to_hierachy_tree(data, "id", "parent_id")
pprint(tree)
