# 二分查找数
# 递归法


def find_a_num(num, l, start=-1, end=-1):
    if -1 <= start - end <= 1 and start > 0:
        print('找不到这个数。')
        return
    if not l:
        print('列表为空。')
        return
    if len(l) == 1:
        print(f'{num} is at {0}') if l[0] == num else print('找不到这个数。')
        return
    if end == start == -1:
        start = 0
        end = len(l)  # 结束的坐标
    index = (start + end) // 2  # 比较的index
    m = l[index]  # 找到比较值
    if num == m:
        print(f'{num} is at {index}')
    elif num < m:
        print(f'{num} < {m}，查找{start}--{index}')
        find_a_num(num, l, start=start, end=index)
    elif num > m:
        print(f'{num} > {m}，查找{index}--{end}')
        find_a_num(num, l, start=index, end=end)


# 循环法


if __name__ == '__main__':
    import random

    l1 = sorted(list(set([random.randint(1, 9999) for x in range(3000)])))
    l1 = [1, 3, 5]
    find_a_num(5, l1)
