import pandas as pd
import datetime
import numpy as np
import pymysql
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示符号

account_dict_songshuo = {'host': 'birealtime-db.vipkid.com.cn', 'user': 'songshuo', 'password': '82XhwM94hAhJ'}


def get_some_students_birthday(student_ids_list):
    d = pymysql.connect(host=account_dict_songshuo['host'], port=4051, user=account_dict_songshuo['user'],
                        password=account_dict_songshuo['password'])
    sql = f"""
SELECT id AS id,
ROUND((DATEDIFF(CURDATE(), birthday)/365)) AS age
FROM uc_account.student WHERE
id IN ({str(student_ids_list)[1:-1]})
"""
    df = pd.read_sql(sql, d)
    df.to_csv('bbbbbbb')
    return df

def range_datetime_by_month(start, end):
    now_ = start
    while now_ < end:
        yield now_
        temp = now_ + datetime.timedelta(days=45)
        now_ = datetime.datetime(temp.year, temp.month, 1)


def get_one_month_students_csv(month: datetime.datetime):
    """
    读取 一个月
    :param month:
    :return:
    """
    df = pd.read_csv(f"C:\\Users\\zouyun\\Downloads\\tiger_files\\data_ea\\ea_data\\{month.year}_month_course_spend{month.month}_country.csv").rename(columns={'as': '开课时间', 'as.1': '课消'})
    # df.info()
    # [[
    #     'id', '开课时间', '课消']]
    df['开课时间'] = df['开课时间'].astype('datetime64')
    df = df[
        ((month - datetime.timedelta(days=120)) <= df['开课时间']) & (df['开课时间'] < (month - datetime.timedelta(days=90)))]
    df['month'] = month
    print(month)
    b_df = get_some_students_birthday(list(df['id']))
    all_df = pd.merge(df, b_df, on="id")
    return all_df


def draw_an_age_pic(age, df):
    # axis_x = [f"{i[0]}-{i[1]}" for i in date_list]
    if age is None:
        _df = df
    else:
        _df = df[df['age'] == age]
    nums = _df.shape[0]
    _p_df = pd.pivot_table(_df, '课消', index='month', aggfunc=np.mean)
    axis_x = _p_df.index
    values = _p_df['课消']
    plt.figure(figsize=(36, 5))
    plt.ylim((0, 20))
    title = f"全国开课三个月后的新生平均课消 - {age} 岁 （{nums} 学生）"
    plt.title(title)
    plt.plot(values)
    plt.savefig(f'pic\\{title}.png', dpi=72)
    print(_p_df)


if __name__ == "__main__":
    # _a = get_one_month_students_csv(datetime.datetime(2020, 2, 1))
    # df_list = []
    df = pd.read_csv('final')
    for i in range(1, 19):
        draw_an_age_pic(i, df)
    draw_an_age_pic(None, df)

    # for i in range_datetime_by_month(datetime.datetime(2018, 1, 1), datetime.datetime(2020, 6, 1)):
    #     temp_a = get_one_month_students_csv(i)
    #     df_list.append(temp_a)
    # pd.concat(df_list).to_csv('final')
# a.to_csv('11111')
