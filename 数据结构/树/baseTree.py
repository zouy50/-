

class Node:
    """
    树的结点类
    """

    def __init__(self, parent, data, children: list = None):
        """
        :param parent: 父结点
        :param data: 结点数据
        :param children: 子结点列表
        """
        self.parent = parent
        self.data = data
        if children is None:
            self.children = []
        else:
            self.children = children

    def __del__(self):
        self.parent, self.data, self.children = None, None, None

    def __str__(self):
        return self.data


class Tree:
    def __init__(self, root_value=None, ):
        """构造树的空头结点，任何树都有个空结点"""
        self.root_node = Node(None, root_value, [])

    @property
    def leaves(self):
        """
        返回树的所有叶子
        :return:
        """
        ...

    def add_node(self, node: Node, parent: Node = None):
        """
        增加结点的方法，node为结点， parent为父结点，默认为根结点
        :param node: 结点对象
        :type parent: Node
        """
        if parent is None:
            parent = self.root_node
        Node.parent = parent
        parent.children.append(node)

    def del_node(self, node: Node, del_all: bool = True):
        """
        删除某个结点的方法，如果del all 是 True，then it will 递归 delete all that 子孙
        if del all is False, then just delete node self and then 使这个结点的儿子们升级为这个结点的层级
        :rtype: object
        """
        if del_all:
            node.parent.children.remove(node)
        else:
            for x in node.children:  # 将所有子结点给到这个结点的父结点
                x.parent = node.parent
        del node

    @staticmethod
    def print_nodes(node, level):
        if not node.children:
            return
        else:
            for i in node.children:
                print(f"\t"*level, i, end='')
            else:
                print('')
                level += 1
            for i in node.children:
                Tree.print_nodes(i, level)

    def __repr__(self):
        print(self.root_node)
        for i in self.root_node.children:
            print(f"\t{i}", end='')

