import datetime
import pandas as pd
import json

MAJOR_WAVE = [
    1,
    (datetime.datetime(2020, 2, 4), datetime.datetime(2020, 2, 20)),
    (datetime.datetime(2020, 2, 20), datetime.datetime(2020, 3, 9)),
    (datetime.datetime(2020, 3, 10), datetime.datetime(2020, 3, 23)),
    (datetime.datetime(2020, 3, 23), datetime.datetime(2020, 4, 1)),

]
MINOR_WAVE = [
    1,
    (datetime.datetime(2020, 2, 11), datetime.datetime(2020, 2, 24)),
    (datetime.datetime(2020, 2, 20), datetime.datetime(2020, 3, 9)),
    (datetime.datetime(2020, 3, 5), datetime.datetime(2020, 3, 16)),
    (datetime.datetime(2020, 3, 16), datetime.datetime(2020, 3, 23)),
    (datetime.datetime(2020, 3, 23), datetime.datetime(2020, 4, 1)),

]

A = {'大包能量石': MAJOR_WAVE, '小包优惠券': MINOR_WAVE}


def cal_one(type_: str, type_index: int):
    temp_dict = dict()
    all_students_df = pd.read_csv('all_students.csv', encoding='gbk').dropna(how='all')
    all_students_df['first_scheduled_date_time'] = all_students_df['first_scheduled_date_time'].astype('datetime64')
    if type_ == '大包能量石':
        temp_pay_df = pd.read_csv('major_pay.csv', encoding='gbk').dropna(how='all')
    else:
        temp_pay_df = pd.read_csv('major_pay.csv', encoding='gbk').dropna(how='all')
    temp_pay_df['paid_date_time'] = temp_pay_df['paid_date_time'].astype('datetime64')
    temp_coupon_df = pd.read_csv(f'{type_}{type_index}.csv', encoding='gbk').dropna(how='all')
    # 计算总学生数：
    temp_dict['总学生数'] = all_students_df[all_students_df['first_scheduled_date_time'] <= A[type_][type_index][1]].shape[0]
    temp_dict['优惠券学生数'] = temp_coupon_df.shape[0]
    temp_dict['优惠券类型'] = f'{type_}第 {type_index} 波'
    temp_dict['优惠券起始日期'] = A[type_][type_index][0].strftime('%Y-%m-%d %H:%M:%S')
    temp_dict['优惠券结束日期'] = A[type_][type_index][1].strftime('%Y-%m-%d %H:%M:%S')
    temp_coupon_pay_df = temp_pay_df[(temp_pay_df['paid_date_time'] >= temp_dict['优惠券起始日期']) & (
            temp_pay_df['paid_date_time'] <= temp_dict['优惠券结束日期']) & (temp_pay_df['student_id']).isin(
        temp_coupon_df['student_id'])]
    temp_dict['出单在优惠券里面的学生数'] = len(set(list(temp_coupon_pay_df['student_id'])))
    temp_dict['出单在优惠券里面的出单数'] = temp_coupon_pay_df.shape[0]
    temp_all_pay_df = temp_pay_df[(temp_pay_df['paid_date_time'] >= temp_dict['优惠券起始日期']) & (
            temp_pay_df['paid_date_time'] <= temp_dict['优惠券结束日期'])]
    temp_dict['出单的总学生数'] = len(set(list(temp_all_pay_df['student_id'])))
    temp_dict['总出单数'] = temp_all_pay_df.shape[0]
    temp_dict['出单不在优惠券里面的学生数'] = len(set(list(temp_all_pay_df['student_id']))) - temp_dict['出单在优惠券里面的学生数']
    temp_dict['优惠券中学生占比'] = temp_dict['出单在优惠券里面的学生数'] / temp_dict['出单的总学生数']
    temp_dict['非优惠券中学生占比'] = temp_dict['出单不在优惠券里面的学生数'] / temp_dict['出单的总学生数']
    temp_dict['出单不在优惠券里面的出单数'] = temp_all_pay_df.shape[0] - temp_dict['出单在优惠券里面的出单数']
    temp_dict['优惠券中出单占比'] = temp_dict['出单在优惠券里面的出单数'] / temp_dict['总出单数']
    temp_dict['非优惠券中出单占比'] = temp_dict['出单不在优惠券里面的出单数'] / temp_dict['总出单数']
    return temp_dict


def cal_major():
    temp_list = []
    for i in range(1, 5):
        print(i)
        temp_list.append(cal_one('大包能量石', i))
    for i in range(1, 6):
        print(i)
        temp_list.append(cal_one('小包优惠券', i))
    pd.read_json(json.dumps(temp_list)).to_csv('111', index=False)


# for i in range(1, 3):
#     print(cal_one('大包能量石', i))
cal_major()
