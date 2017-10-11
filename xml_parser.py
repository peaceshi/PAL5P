import xmltodict
import os,sys

file_path = sys.path[0] + "/Data/weapon.xml"

print(file_path)

with open(file_path) as xml_document:
    doc = xmltodict.parse(xml_document.read())
'''
def list_all_dict(dict_a):
    if isinstance(dict_a, dict) : #使用isinstance检测数据类型
        for x in range(len(dict_a)):
            temp_key = list(dict_a.keys())[x]
            temp_value = dict_a[temp_key]
            print("%s : %s", temp_key, temp_value)
            list_all_dict(temp_value) #自我调用实现无限遍历


list_all_dict(doc)
'''

# 遍历生成的字典
for root_index in range(len(doc)):
    node_name = list(doc.keys())[root_index]
    node_value = doc[node_name]
    leaf_value = []
    item_used_number_sets = []  # 已使用的编号
    if root_index == 0:
        root_node_name = node_name
        root_node_value = node_value
        print("根节点名称: ", root_node_name)

    while True:   # 不是叶子节点全是dict
        if isinstance(node_value, dict):
            tree_node_name = list(node_value.keys())[0]
            tree_node_value = node_value[tree_node_name]
            print("子节点名称: ", tree_node_name)
            if isinstance(tree_node_value, dict):
                node_value = tree_node_value
            else:
                leaf_value = tree_node_value
                break
        else:
            leaf_value = node_value
            break

    for tree_index, tree_node in enumerate(leaf_value):  # 叶节点是list
        dict_key_number = len(tree_node)
        item_value = []  # 项目值
        item_attribute = []  # 项目属性/名称

        for leaf_index in range(dict_key_number):
            leaf_node_name = list(tree_node.keys())[leaf_index]  # 这个list包含若干个dict
            leaf_node_value = tree_node[leaf_node_name]
            if tree_index == 0:
                item_attribute.append(leaf_node_name)
            if leaf_index == 0:  # 只要编号
                item_used_number_sets.append(int(leaf_node_value))
            item_value.append(leaf_node_value)
            if dict_key_number <= leaf_index + 1:  # 是否遍历了所有叶子节点
                for item_attribute_index, attribute_value in enumerate(item_attribute):
                    print(attribute_value[1:], end=';', flush=True)
                print('')
                for item_value_index, value_value in enumerate(item_value):
                    print(value_value, end=';', flush=True)
                print('')
for index, value in enumerate(item_used_number_sets):
    print(value, index)

print("process shutdown")

