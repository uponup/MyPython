from random import randint
from time import time, sleep

def download_task(filename):
    print("开始下载%s..." % filename)
    time_to_download = randint(5, 10)
    sleep(time_to_download)
    print('%s下载完成！耗费了%d秒' % (filename, time_to_download))

def main():
    start = time()
    download_task('Python入门到放弃.pdf')
    download_task('Objective-C入门到放弃.pdf')
    end = time()
    print('总共耗费了%.2f秒' % (end - start))

# if __name__ == '__main__':
    # main()





# 以上代码同步执行，下载任务前一个完成之后才开始下一个。这样会耗费太多时间。遇到此类问题，Python为我们提供了多进程、多线程、多线程+多线程

from multiprocessing import Process
from os import getpid
from random import randint
from time import time, sleep

def download_task_2(filename):
    print('启动下载进程，进程号：[%d]' % getpid())
    print('开始下载%s...' % filename)
    time_to_download = randint(5, 10)
    sleep(time_to_download)
    print('%s下载完成！耗费了%d秒' % (filename, time_to_download))

def main_2():
    start = time()
    p1 = Process(target=download_task_2, args=('Python入门到放弃.pdf',))
    p1.start()

    p2 = Process(target=download_task_2, args=('c/c++入门到放弃.pdf',))
    p2.start()

    p1.join()
    p2.join()

    end = time()

    print('总共耗费了%.2f秒' % (end - start))

# if __name__ == '__main__':
#     main_2()
