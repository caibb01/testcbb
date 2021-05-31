import datetime


def get_time(is_future, format='%Y/%m/%d %H:%M', **kwargs):
    """
    获取格式化后的时间
    :param is_future: boolean. 判断是今天之前的时间，还是今天之后的
    :param format: 格式化时间的格式标准
    :param kwargs: days/seconds/hours/minutes/weeks 参考 datetime.timedelta
    :return:
    """
    today = datetime.datetime.today()
    get_time = (today + datetime.timedelta(**kwargs)) if is_future else (today - datetime.timedelta(**kwargs))
    return get_time.strftime(format)

