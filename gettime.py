from time import localtime, time, strftime
from datetime import datetime

#获得当前是星期几，1-7
def get_weekday():
    today = datetime.now().weekday()
    return today+1

#获得当前的时间：小时*60+分钟
def get_time():
    mylocaltime = localtime(time())
    mytime = mylocaltime.tm_hour*60 + mylocaltime.tm_min
    return mytime

#获得当前是该学期的第几周
def get_week(college_boun = '20220214'):
    week_now = strftime('%W')
    week_start = datetime.strptime(college_boun, '%Y%m%d').strftime('%W')
    return (int(week_now) - int(week_start) + 1)


#获得当前是哪一天
def get_day():
    mylocalday = localtime(time())

    mon = str(mylocalday.tm_mon)
    day = str(mylocalday.tm_mday)
    if (mylocalday.tm_mon<10):
        mon = "0" + str(mylocalday.tm_mon)
    if (mylocalday.tm_mday<10):
        day = "0" + str(mylocalday.tm_mday)

    myday = str(mylocalday.tm_year) + mon + day
    return myday
