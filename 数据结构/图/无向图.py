# author:





class BaseGraph:
    """
    基本图的类，具有最简单的图的基本属性
    有 种实现方式：
    1、adjacency_list： 邻接列表
        每个节点后面跟着具备路径的列表
    2、adjacency_matrix:  邻接矩阵
        用二维数组存放顶点间的关系

    """

    # 3、orthogonal_list：  十字链表
    # 用邻接表和逆邻接表储存：无向图不需要
    def __init__(self, method='adjacency_list'):
        self.method = method
        self.nodes = []
        if self.method == 'adjacency_matrix':
            self.adjacency_matrix = [[], ]
        elif self.method == 'adjacency_list':
            self.list_dict = {}

    def add_node(self, obj, neighbor_objs=None):
        if not neighbor_objs:
            neighbor_objs = []
        # 从neighbor_objs 里面去除要增加的节点
        if obj in neighbor_objs:
            neighbor_objs.remove(obj)
        if obj in self.nodes:
            raise ValueError('图节点已存在，无法插入。')
        else:
            self.nodes.append(obj)  # 加入图节点
            if self.method == 'adjacency_list':
                self.list_dict[obj] = neighbor_objs
                for i in neighbor_objs:     # 加入每个不存在的节点 调用自身，递归
                    if i not in self.nodes:
                        self.add_node(i)
                    if obj not in self.list_dict[i]:    # 因为是无向图互相加入节点
                        self.list_dict[i].append(obj)
            elif self.method == 'adjacency_matrix':
                obj_index = self.nodes.index(obj)  # 插入节点的index
                # 判断是否是第一个加入的，如果是第一个加入的，只是一个0的矩阵
                if not obj_index:
                    self.adjacency_matrix[0].append(0)
                else:
                    for i in self.adjacency_matrix:
                        i.append(0)
                    else:
                        self.adjacency_matrix.append([0 for x in range(obj_index + 1)])
                    # 加入 neighbor_objs
                    if neighbor_objs:
                        for i in neighbor_objs:
                            if i not in self.nodes:
                                self.add_node(i)
                        index_list = [self.nodes.index(i) for i in neighbor_objs]
                        for i in index_list:
                            self.adjacency_matrix[i][obj_index], self.adjacency_matrix[obj_index][i] = 1, 1

    def add_links(self, all_links=None, links_list=None):
        """
        添加弧，或者叫添加链接关系的方法
        :param all_links: 具有相连关系的节点, 会两两都会建立节点，相互完全关系
        :param links_list: 具有节点的list，列表里的每个列表或tuple 为两两具有关系
        """

        def __add_links_inner(all_links=None):
            # 判断对象是否存在, 不在就加入，在就加入弧
            if all_links:
                for i in all_links:
                    if i not in self.nodes:
                        self.nodes.append(i)
                    if self.method == 'adjacency_list':
                        # 更新节点的邻接列表
                        if i not in self.list_dict.keys():
                            self.list_dict[i] = list(all_links).pop(all_links.index(i))
                        else:
                            temp_list = list(set(list(all_links) + self.list_dict[i]))
                            temp_list.remove(i)
                            self.list_dict[i] = temp_list
                    elif self.method == 'adjacency_matrix':
                        # TODO 有bug  无法添加上
                        i_index = all_links.index(i)
                        index_list = [j for j in all_links[(i_index + 1):]]   # 获取当前节点后面的 节点列表
                        for j in index_list:
                            if j != i:    # 相等的不更新成1
                                self.adjacency_matrix[self.nodes.index(j)][self.nodes.index(i)], self.adjacency_matrix[self.nodes.index(i)][self.nodes.index(j)] = 1, 1

        __add_links_inner(all_links=all_links)
        if links_list:
            for i in links_list:
                __add_links_inner(all_links=i)

    def describe(self, matrix=False):
        """
        描述图的函数，形式为节点：连接的节点列表
        :type matrix: boolean 是否输出矩阵
        :return:
        """
        print(''.center(40, '='))
        print(f'图类型：{self.method}')
        # TODO 图的大小
        print(f'图大小：还没弄，哈哈')
        if matrix:
            if self.method == 'adjacency_matrix':
                # print(self.adjacency_matrix)
                print()
                for i in self.adjacency_matrix:
                    # print(i)
                    for j in i:
                        print(j, end=' ')
                    print('')
                print('')
            else:
                print('图的类型不是邻接矩阵类型( adjacency_matrix )，无法输出矩阵。')
        else:
            if self.method == 'adjacency_list':
                for i, k in self.list_dict.items():
                    print(f'{i}: {k}')
            elif self.method == 'adjacency_matrix':
                for i in range(len(self.nodes)):
                    print(f'{self.nodes[i]}: [', end='')
                    for j in range(len(self.adjacency_matrix[i])):
                        if self.adjacency_matrix[i][j]:
                            print(f'{self.nodes[j]}, ', end='')
                    else:
                        print(']')

    def transform_method(self, to_method='adjacency_list'):
        ...

    def del_nodes(self, *args):
        ...
        def del_node(node):
            ...

    def del_links(self, *args):
        # 参数可能是list fill with tuple
        ...

    def get_ways(self, a, b, time_id=False, type='all'):
        # type min, max
        ...





if __name__ == '__main__':
    # n = BaseGraph(method='adjacency_list')
    n = BaseGraph(method='adjacency_matrix')
    n.add_node(3)
    n.add_node(2, [3, ])
    n.add_node(5)
    n.add_node(7, neighbor_objs=[5, 6, 8, 10])
    n.add_links(all_links=[5, 3])
    n.add_links(links_list=[[6, 8], [2, 10]])
    n.describe(matrix=True)
    n.describe()
