import datetime
import pytz
from seatable_api import Base, context

SERVER_URL = context.server_url or "https://cloud.seatable.cn"
API_TOKEN = context.api_token or "7010c3fde8a2639b385f2a3f258a5a27cbdfe1fb"

TABLE_NAME = "Table1"
NAME_COLUMN = "名称"
TIME_COLUMN = "创建时间"

IS_VALID_COLUMN = "标记"

HOUR_LIMIT_MIN = 18  # after 6pm
HOUR_LIMIT_MAX = 21  # before 9pm

TIMEZONE = "Asia/Shanghai"


def _format_time(time_str_utc):
    """
    Transfer the utc time string such as 2020-12-09T02:56:48.780+00:00 into localtime
    """
    try:
        date_time_obj = datetime.datetime.strptime(time_str_utc, '%Y-%m-%dT%H:%M:%S.%f+00:00')
        timezone_utc = pytz.timezone('UTC')
        timezone_local = pytz.timezone('Asia/Shanghai')
        utc_time_obj = timezone_utc.localize(date_time_obj)
        local_time_obj = utc_time_obj.astimezone(timezone_local)
    except:
        return None
    return local_time_obj


def mark_invalid_rows():
    '''
    Mark the invalid member clock-in information in the extra column
    '''
    base = Base(API_TOKEN, SERVER_URL)
    base.auth()
    rows = base.list_rows(TABLE_NAME)
    member_valid_time_dict = {}
    for row in rows:
        if row.get(IS_VALID_COLUMN) == '无效':
            continue
        create_time = _format_time(row.get(TIME_COLUMN))
        name = row.get(NAME_COLUMN)
        valid_time_list = member_valid_time_dict.get(name) or []
        if create_time and create_time.hour in range(HOUR_LIMIT_MIN, HOUR_LIMIT_MAX):
            if create_time.date() in valid_time_list:  # invalid clock-in more than one time within one day
                base.update_row(TABLE_NAME, row['_id'], {IS_VALID_COLUMN: '无效'})
                continue
            valid_time_list.append(create_time.date())
            member_valid_time_dict[name] = valid_time_list
        else:
            base.update_row(TABLE_NAME, row['_id'], {IS_VALID_COLUMN: '无效'})


mark_invalid_rows()
