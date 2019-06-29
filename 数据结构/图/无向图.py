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
            self.adjacency_matrix = [[]]
        elif self.method == 'adjacency_list':
            self.list_dict = {}

    def add_node(self, obj, neighbor_objs=[]):
        if obj in self.nodes:
            raise ValueError('图节点已存在，无法插入。')
        else:
            self.nodes.append(obj)  # 加入图节点
            if self.method == 'adjacency_list':
                self.list_dict[obj] = neighbor_objs
            # TODO 加入adjacency_matrix 的 add node方法
            elif self.method == 'adjacency_matrix':
                self.adjacency_matrix.append()

    def add_links(self, *args):
        # 判断对象是否存在, 不在就加入，在就加入弧
        for i in args:
            if i not in self.nodes:
                self.nodes.append(i)
            if self.method == 'adjacency_list':
                if i not in self.list_dict.keys():
                    self.list_dict[i] = list(args).pop(i)
                self.list_dict[i] = list(set(list(args) + self.list_dict[i])).pop(i)
            elif self.method == 'adjacency_matrix':
                # TODO 加入adjacency_matrix 的 add node方法
                ...