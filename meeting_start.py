from autoclick import signIn
from decidecourse import decide_meeting
from softconfig import configuration_information

#import txtreader
#txtreader.meeting_reader()

def metting_start():
    [result, meeting] = decide_meeting()

    config = configuration_information()
    app_address = config[2]
    wait_time = config[3]

    meeting_id = meeting[3]
    meeting_key = meeting[4]
    if result == 1:
        signIn(meeting_id, meeting_key, wait_time, app_address)
