import time
import datetime

def get_weekday():
    today = datetime.datetime.now().weekday()
    return today+1

def get_time():
    localtime = time.localtime(time.time())
    mytime = localtime.tm_hour*60 + localtime.tm_min
    return mytime

def get_week(college_boun = '20220214'):
    week_now = time.strftime('%W')
    week_start = datetime.datetime.strptime(college_boun, '%Y%m%d').strftime('%W')
    return (int(week_now) - int(week_start) + 1)
