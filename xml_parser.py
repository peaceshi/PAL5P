import xmltodict
from file_paths import *


def load_xml_document_files(files):
    for file_index, file_name in enumerate(files):
        file_path = sys.path[0] + "/Data/" + file_name
        # print(file_path)
        if os.access(file_path, os.R_OK):
            with open(file_path) as xml_document:
                traverse_dict(xmltodict.parse(xml_document.read()))
        else:
            print("failed to access file.", file_path)
            sys.exit(1)
# load_xml_document_files(files)


def traverse_dict(dictionary):  # 遍历生成的字典
    if isinstance(dictionary, dict):
        for node_index in range(len(dictionary)):
            node_name = list(dictionary.keys())[node_index]
            node_value = dictionary[node_name]
            traverse_dict(node_value)
    else:
        leaf(dictionary)
# traverse_dict(dictionary)


def leaf(leaf_value):
    item_used_number_sets = []  # 本类型中已使用的编号
    for tree_index, tree_node in enumerate(leaf_value):  # 叶节点是list
        dict_key_number = len(tree_node)
        item_value = []  # 项目值
        item_attribute = []  # 项目属性/名称
        for leaf_index in range(dict_key_number):
            leaf_node_name = list(tree_node.keys())[leaf_index]  # 这个list包含若干个dict
            leaf_node_value = tree_node[leaf_node_name]
            if tree_index == 0:
                item_attribute.append(leaf_node_name)
            if leaf_index == 0:  # 只要编号项
                item_used_number_sets.append(leaf_node_value)
            item_value.append(leaf_node_value)
            if dict_key_number <= leaf_index + 1:  # 是否遍历了所有叶子节点
                for item_attribute_index, attribute_value in enumerate(item_attribute):
                    print(attribute_value[1:], end=';', flush=True)
                print('')
                for item_value_index, value_value in enumerate(item_value):
                    print(value_value, end=';', flush=True)
                print('')
    for item_used_number_sets_index, value in enumerate(item_used_number_sets):
        print(value, item_used_number_sets_index)
# leaf()

