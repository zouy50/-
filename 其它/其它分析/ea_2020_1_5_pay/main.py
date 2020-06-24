"""
分析 ea 的出单 和 课频 以及 完课率的相关性
目前北京给出的结论是， 完课率越高 出单 占比越高，因此要追完课率
"""
import datetime

from scipy.optimize import leastsq
import numpy as np
import pandas as pd


def cal_k(x_list, y_list):
    """
    根据给定的 x列表的数 和 y 列表的数  计算斜率， 来代表成绩的变化
    :param x_list:
    :param y_list:
    :return:
    """

    # 拟合函数
    def func(a, x):
        k, b = a
        return k * x + b

    # 残差
    def dist(a, x, y):
        return func(a, x) - y

    param = np.array([0, 0])
    for i in [x_list, y_list]:
        if not isinstance(i, list):
            i = list(i)
    x = np.array(x_list)
    y = np.array(y_list)

    var = leastsq(dist, param, args=(x, y))
    return var[0][0]


def get_pay_num_student_df():
    _df = pd.read_csv("ea_pay.csv").rename(columns={'学生ID': 'student_id'})
    df = pd.pivot_table(_df[['student_id', 'ea_id']], index='student_id', aggfunc=np.count_nonzero)
    return df.rename(columns={'ea_id': '出单数'})


def get_ea_student():
    def cal_learning_month(date):
        return round((datetime.datetime(2020, 6, 21) - date).days / 30)

    def cal_need_course_num(date):
        if date < datetime.datetime(2020, 1, 7):
            return (datetime.datetime(2020, 6, 21) - datetime.datetime(2020, 1, 6)).days / 7 * 2
        else:
            return (datetime.datetime(2020, 6, 21) - date).days / 7 * 2

    df = pd.read_csv('ea_student.csv', encoding='gbk').set_index('student_id')
    df['first_course_date'] = df['first_course_date'].astype('datetime64')
    df['学龄月'] = df['first_course_date'].apply(cal_learning_month)
    df['应完课数'] = df['first_course_date'].apply(cal_need_course_num)
    return df[['ea_id', 'first_course_date', '学龄月', '应完课数']]


def get_ea_ua():
    df = pd.read_csv("ea_ua.csv").dropna()
    df['oc.scheduled_date_time'] = df['oc.scheduled_date_time'].astype('datetime64')
    df = df[df['oc.scheduled_date_time'] > '2020-01-01']
    return pd.pivot_table(df[['s.student_id', 'ua_scoure']], index='s.student_id', aggfunc=np.mean)


def merge_all_left_on_index(df_list, how='left'):
    primary_df = pd.merge(df_list[0], df_list[1], right_index=True, left_index=True, how=how)
    if len(df_list) > 2:
        for i in range(2, len(df_list)):
            # if not df_list[i].empty:
            primary_df = pd.merge(primary_df, df_list[i],
                                  right_index=True, left_index=True, how=how)
    return primary_df


def get_finish_class_num():
    _df = pd.read_csv("ea_class.csv")
    df = pd.pivot_table(_df, index='s.student_id', aggfunc=np.count_nonzero)
    return df[['c.id', ]].rename(columns={'c.id': '实际完课数'})


if __name__ == "__main__":
    # df = merge_all_left_on_index([get_ea_student(), get_ea_ua(), get_finish_class_num(), get_pay_num_student_df()]).fillna(0)
    # df.info()
    # df.to_csv('student_all.csv')
    df = pd.read_csv('student_all.csv').set_index('student_id')
    df['完课率'] = df['实际完课数']/df['应完课数']
    df.drop(labels=['实际完课数', '应完课数', 'ea_id'], inplace=True, axis=1)
    # 根据完课率透视一下，计算出每一段完课率的出单率为多少
    import matplotlib.pyplot as plt
    from pandas.plotting import scatter_matrix
    scatter_matrix(df, figsize=(12, 8))
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示符号
    plt.show()

