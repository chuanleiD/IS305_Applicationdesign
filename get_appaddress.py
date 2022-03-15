from os import listdir
from os.path import join
from win32com.client import Dispatch
import getpass

def address():
    user_name = getpass.getuser()  # 获取当前用户名
    directory = "C:\\Users\\" + user_name + "\\Desktop"
    #print(directory)
    shell = Dispatch('wScript.shell')

    for fn in listdir(directory):
        if fn.endswith('.lnk'):
            link = join(directory, fn)
            if link.find("腾讯会议") != -1:
                address = shell.CreateShortCut(link).Targetpath

    return address






