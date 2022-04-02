'''
后台运行的处理主函数
'''

from autoclick import signIn
from decidecourse import decide_background
from softconfig import configuration_information

#import txtreader
#txtreader.meeting_reader()
#----------------------------------------------------------------------------------------
# 后台运行模块
def background_start():

    # 获取当前配置信息
    config = configuration_information()
    college_start = config[0]
    app_address = config[2]
    wait_time = config[3]
    if_read = config[4]

    # 获取选取的ID,KEY
    # 如果result为0，则不操作
    [result, choice_id, choice_key] = decide_background(college_start, if_read)
    if result != 0:
        signIn(choice_id, choice_key, wait_time, app_address)

    return
#----------------------------------------------------------------------------------------
