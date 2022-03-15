from time import localtime, time, strftime
from datetime import datetime

def get_weekday():
    today = datetime.now().weekday()
    return today+1

def get_time():
    mylocaltime = localtime(time())
    mytime = mylocaltime.tm_hour*60 + mylocaltime.tm_min
    return mytime

def get_week(college_boun = '20220214'):
    week_now = strftime('%W')
    week_start = datetime.strptime(college_boun, '%Y%m%d').strftime('%W')
    return (int(week_now) - int(week_start) + 1)
