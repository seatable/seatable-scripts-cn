# -*- coding: utf-8 -*-
# 根据中国的假期安排获取计算工作日并写入SeaTable的脚本， 一般在当年年底会更新来年的节假日安排， 目前此脚本作为案例演示只支持2021年和2022年两年。
# 若有更新， 可以补充该脚本中的holidays和workdays的字典。
import datetime
from enum import Enum
from seatable_api import dateutils, Base, context


START_DATE_COL = "开始日期"
END_DATE_COL = "结束日期"
WORK_DAY_COL = "工作日"

TABLE_NAME = "工作任务安排"

# 定义中国的节假日
class Holiday(Enum):
    new_years_day = "元旦"
    spring_festival = "春节"
    tomb_sweeping_day = "清明"
    labour_day ="劳动节"
    dragon_boat_festival = "端午"
    national_day = "国庆节"
    mid_autumn_festival = "中秋"

    # special holidays
    anti_fascist_70th_day = "中国人民抗日战争暨世界反法西斯战争胜利70周年纪念日"


# 节假日列表，2021, 2022两年，
holidays = {
    datetime.date(year=2021, month=1, day=1): Holiday.new_years_day.value,
    datetime.date(year=2021, month=1, day=2): Holiday.new_years_day.value,
    datetime.date(year=2021, month=1, day=3): Holiday.new_years_day.value,
    datetime.date(year=2021, month=2, day=11): Holiday.spring_festival.value,
    datetime.date(year=2021, month=2, day=12): Holiday.spring_festival.value,
    datetime.date(year=2021, month=2, day=13): Holiday.spring_festival.value,
    datetime.date(year=2021, month=2, day=14): Holiday.spring_festival.value,
    datetime.date(year=2021, month=2, day=15): Holiday.spring_festival.value,
    datetime.date(year=2021, month=2, day=16): Holiday.spring_festival.value,
    datetime.date(year=2021, month=2, day=17): Holiday.spring_festival.value,
    datetime.date(year=2021, month=4, day=3): Holiday.tomb_sweeping_day.value,
    datetime.date(year=2021, month=4, day=4): Holiday.tomb_sweeping_day.value,
    datetime.date(year=2021, month=4, day=5): Holiday.tomb_sweeping_day.value,
    datetime.date(year=2021, month=5, day=1): Holiday.labour_day.value,
    datetime.date(year=2021, month=5, day=2): Holiday.labour_day.value,
    datetime.date(year=2021, month=5, day=3): Holiday.labour_day.value,
    datetime.date(year=2021, month=5, day=4): Holiday.labour_day.value,
    datetime.date(year=2021, month=5, day=5): Holiday.labour_day.value,
    datetime.date(year=2021, month=6, day=12): Holiday.dragon_boat_festival.value,
    datetime.date(year=2021, month=6, day=13): Holiday.dragon_boat_festival.value,
    datetime.date(year=2021, month=6, day=14): Holiday.dragon_boat_festival.value,
    datetime.date(year=2021, month=9, day=19): Holiday.mid_autumn_festival.value,
    datetime.date(year=2021, month=9, day=20): Holiday.mid_autumn_festival.value,
    datetime.date(year=2021, month=9, day=21): Holiday.mid_autumn_festival.value,
    datetime.date(year=2021, month=10, day=1): Holiday.national_day.value,
    datetime.date(year=2021, month=10, day=2): Holiday.national_day.value,
    datetime.date(year=2021, month=10, day=3): Holiday.national_day.value,
    datetime.date(year=2021, month=10, day=4): Holiday.national_day.value,
    datetime.date(year=2021, month=10, day=5): Holiday.national_day.value,
    datetime.date(year=2021, month=10, day=6): Holiday.national_day.value,
    datetime.date(year=2021, month=10, day=7): Holiday.national_day.value,
    datetime.date(year=2022, month=1, day=1): Holiday.new_years_day.value,
    datetime.date(year=2022, month=1, day=2): Holiday.new_years_day.value,
    datetime.date(year=2022, month=1, day=3): Holiday.new_years_day.value,
    datetime.date(year=2022, month=1, day=31): Holiday.spring_festival.value,
    datetime.date(year=2022, month=2, day=1): Holiday.spring_festival.value,
    datetime.date(year=2022, month=2, day=2): Holiday.spring_festival.value,
    datetime.date(year=2022, month=2, day=3): Holiday.spring_festival.value,
    datetime.date(year=2022, month=2, day=4): Holiday.spring_festival.value,
    datetime.date(year=2022, month=2, day=5): Holiday.spring_festival.value,
    datetime.date(year=2022, month=2, day=6): Holiday.spring_festival.value,
    datetime.date(year=2022, month=4, day=3): Holiday.tomb_sweeping_day.value,
    datetime.date(year=2022, month=4, day=4): Holiday.tomb_sweeping_day.value,
    datetime.date(year=2022, month=4, day=5): Holiday.tomb_sweeping_day.value,
    datetime.date(year=2022, month=4, day=30): Holiday.labour_day.value,
    datetime.date(year=2022, month=5, day=1): Holiday.labour_day.value,
    datetime.date(year=2022, month=5, day=2): Holiday.labour_day.value,
    datetime.date(year=2022, month=5, day=3): Holiday.labour_day.value,
    datetime.date(year=2022, month=5, day=4): Holiday.labour_day.value,
    datetime.date(year=2022, month=6, day=3): Holiday.dragon_boat_festival.value,
    datetime.date(year=2022, month=6, day=4): Holiday.dragon_boat_festival.value,
    datetime.date(year=2022, month=6, day=5): Holiday.dragon_boat_festival.value,
    datetime.date(year=2022, month=9, day=10): Holiday.mid_autumn_festival.value,
    datetime.date(year=2022, month=9, day=11): Holiday.mid_autumn_festival.value,
    datetime.date(year=2022, month=9, day=12): Holiday.mid_autumn_festival.value,
    datetime.date(year=2022, month=10, day=1): Holiday.national_day.value,
    datetime.date(year=2022, month=10, day=2): Holiday.national_day.value,
    datetime.date(year=2022, month=10, day=3): Holiday.national_day.value,
    datetime.date(year=2022, month=10, day=4): Holiday.national_day.value,
    datetime.date(year=2022, month=10, day=5): Holiday.national_day.value,
    datetime.date(year=2022, month=10, day=6): Holiday.national_day.value,
    datetime.date(year=2022, month=10, day=7): Holiday.national_day.value,
}

# 周六周日安排为工作日列表, 2021，2022年
workdays = {
    datetime.date(year=2021, month=2, day=7): Holiday.spring_festival.value,
    datetime.date(year=2021, month=2, day=20): Holiday.spring_festival.value,
    datetime.date(year=2021, month=4, day=25): Holiday.labour_day.value,
    datetime.date(year=2021, month=5, day=8): Holiday.labour_day.value,
    datetime.date(year=2021, month=9, day=18): Holiday.mid_autumn_festival.value,
    datetime.date(year=2021, month=9, day=26): Holiday.national_day.value,
    datetime.date(year=2021, month=10, day=9): Holiday.national_day.value,
    datetime.date(year=2022, month=1, day=29): Holiday.spring_festival.value,
    datetime.date(year=2022, month=1, day=30): Holiday.spring_festival.value,
    datetime.date(year=2022, month=4, day=2): Holiday.tomb_sweeping_day.value,
    datetime.date(year=2022, month=4, day=24): Holiday.labour_day.value,
    datetime.date(year=2022, month=5, day=7): Holiday.labour_day.value,
    datetime.date(year=2022, month=10, day=8): Holiday.national_day.value,
    datetime.date(year=2022, month=10, day=9): Holiday.national_day.value,
}


def _wrap_date(date):
    if isinstance(date, datetime.datetime):
        date = date.date()
    return date

def _validate_date(*dates):
    if len(dates) != 1:
        return list(map(_validate_date, dates))
    date = _wrap_date(dates[0])
    if not isinstance(date, datetime.date):
        raise NotImplementedError("unsupported type {}, expected type is datetime.date".format(type(date)))
    min_year, max_year = min(holidays.keys()).year, max(holidays.keys()).year
    if not (min_year <= date.year <= max_year):
        raise NotImplementedError(
            "no available data for year {}, only year between [{}, {}] supported".format(date.year, min_year, max_year)
        )
    return date

def get_dates(start, end):
    start, end = map(_wrap_date, (start, end))
    delta_days = (end - start).days
    return [start + datetime.timedelta(days=delta) for delta in range(delta_days + 1)]


def is_workday(date):
    '''
    工作日定义：
    1. 日期在workdays字典的key中
    2. 星期是周一到周五且不在holidays字典的key中
    '''
    date = _validate_date(date)

    weekday = date.weekday()
    return bool(date in workdays.keys() or (weekday <= 4 and date not in holidays.keys()))

def get_workdays(start, end):
    """
    获取两个日期之间的工作日，返回datetime的列表
    """
    start, end = _validate_date(start, end)
    return list(filter(is_workday, get_dates(start, end)))


def calculate_base_workdays(base, table_name):
    '''
    通过seatable表格中的，开始日期, 结束日期， 计算两个日期间工作日的天数，并把其更新到该行的
    工作日字段中
    '''

    for row in base.list_rows(table_name):
        row_id = row.get('_id')
        start_date = row.get(START_DATE_COL)
        end_date = row.get(END_DATE_COL)

        work_day_list = get_workdays(
            datetime.date(
                year=dateutils.year(start_date),
                month=dateutils.month(start_date),
                day=dateutils.day(start_date)
            ),

            datetime.date(
                year=dateutils.year(end_date),
                month=dateutils.month(end_date),
                day=dateutils.day(end_date)
            )
        )
        # 两个日期间的工作日天数
        work_day_counts = len(work_day_list)
        base.update_row(
            table_name,
            row_id,
            {
                WORK_DAY_COL: work_day_counts
            }
        )





if __name__ == '__main__':

    # 测试工作日计算算法
    a = '2022-4-27'
    b = '2022-5-19'
    work_day_list = get_workdays(
        datetime.date(
            year=dateutils.year(a),
            month=dateutils.month(a),
            day=dateutils.day(a)
        ),

        datetime.date(
            year=dateutils.year(b),
            month=dateutils.month(b),
            day=dateutils.day(b)
        )
    )
    # 两个日期间的工作日天数
    work_day_counts = len(work_day_list)

    print(work_day_counts) # 15

    # Seatable数据处理

    SERVER_URL = context.server_url or 'https://cloud.seatable.cn/'
    API_TOKEN = context.api_token or 'cacc42497886e4d0aa8ac0531bdcccb1c93bd0f5'

    base = Base(API_TOKEN, SERVER_URL)
    base.auth()
    calculate_base_workdays(base, TABLE_NAME)






