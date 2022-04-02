from autoclick import signIn
from decidecourse import decide_background
from softconfig import configuration_information

#import txtreader
#txtreader.meeting_reader()

def background_start():

    config = configuration_information()
    college_start = config[0]
    app_address = config[2]
    wait_time = config[3]
    if_read = config[4]

    [result, choice_id, choice_key] = decide_background(college_start, if_read)
    if result != 0:
        signIn(choice_id, choice_key, wait_time, app_address)

    return

