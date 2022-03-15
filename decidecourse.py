import database
import gettime

def course_time(a):
    b = [0, 480, 535, 600, 655, 720, 775, 840, 895, 960, 1015, 1080, 1135, 1175]
    return b[a]


def decide_course(college_start='20220214'):
    mylist = database.read_db()
    week_now = gettime.get_week(college_start)
    localtime = gettime.get_time()
    weekday = gettime.get_weekday()

    list2 = []
    for course in mylist:
        if course[4] == weekday and week_now >= course[5] and week_now <= course[6]:
            if course[9] == 0 or (course[9] == 1 and week_now//2 == 1) or (course[9] == 2 and week_now//2 == 0):
                list2.append(course)

    if len(list2) > 0:
        mycourse = list2[0]
    else:
        mycourse = mylist[0]

    for i in range(0, len(list2), 1):
        course = list2[i]
        if i == 0 and localtime < course_time(course[3]):
            mycourse = course
            break
        elif i == len(list2) - 1:
            mycourse = list2[i]
        elif localtime > course_time(course[3]) and localtime < course_time(list2[i+1][3]):
            mycourse = list2[i+1]

    return mycourse

#a = (course_name, start_time, end_time, weekday, start_week, end_week, meeting_number, meeting_password, single_or_double_week)





