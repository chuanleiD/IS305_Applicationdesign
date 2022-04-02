


import threading
import time

def read():
    for x in range(5):
        print('在%s,正在听音乐' % time.ctime())
        time.sleep(1.5)

def write():
    for x in range(5):
        print('在%s,正在看电视' % time.ctime())
        time.sleep(1.5)

def main():

    music_threads = []  # 用来存放执行read函数线程的列表
    TV_threads = []  # 用来存放执行write函数线程的列表

    for i in range(1,2):  # 创建1个线程用于read()，并添加到read_threads列表
        t = threading.Thread(target=read) # 执行的函数如果需要传递参数，threading.Thread(target=函数名,args=(参数，逗号隔开))
        music_threads.append(t)

    for i in range(1,2): # 创建1个线程执行write()，并添加到write_threads列表
        t = threading.Thread(target=write) # 执行的函数如果需要传递参数，threading.Thread(target=函数名,args=(参数，逗号隔开))
        TV_threads.append(t)

    for i in range(0,1):  # 启动存放在read_threads和write_threads列表中的线程
        music_threads[i].start()
        TV_threads[i].start()

if __name__ == '__main__':
    main()