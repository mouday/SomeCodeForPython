from multiprocessing import Process
import os

#print(help(Process))

def run_process(name):
    '''pip'''
    print("Run Child Process %s (%s)"% (name,os.getpid()))

if __name__ == '__main__':
    print ("Parent process %s"% os.getpid())
    p=Process(target=run_process,args=("test",))
    print("Child process will start.")
    p.start()
    p.join()#等待子进程结束后再继续往下运行
    print("child process end.")
