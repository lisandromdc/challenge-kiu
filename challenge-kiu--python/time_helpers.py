import time

def get_current_date():
    return time.strftime("%Y-%m-%d")


def get_yesterday_date():
    now = time.time()
    one_day = 24 * 60 * 60
    yesterday_timestamp = now - one_day
    return time.strftime("%Y-%m-%d", time.localtime(yesterday_timestamp))


def get_tomorrow_date():
    now = time.time()
    one_day = 24 * 60 * 60
    yesterday_timestamp = now + one_day
    return time.strftime("%Y-%m-%d", time.localtime(yesterday_timestamp))
