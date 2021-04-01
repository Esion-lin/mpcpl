import threading

userName = threading.local()

def SessionThread(userName_in):
    userName.val = userName_in
    print(userName.val)   

Session1 = threading.Thread(target=SessionThread("User1"))
Session2 = threading.Thread(target=SessionThread("User2"))

# start the session threads
Session1.start()
Session2.start()
# wait till the session threads are complete
Session1.join()
Session2.join()

import inspect

def test():
    print()
def test2():
    aaa = 1000
    bbb = 123123
    test()


#load toml

import toml
class ttttt:
    def adfsdf(self):
        return 100;
    def __init__(self):
        self.w = 10000

    def printf(self):
        print(self.__dict__)



config = toml.load('./config.toml')
print(config)
#test global var passed
import inspect
def importbytest2():
    frame = inspect.currentframe()
    frame = frame.f_back
    print

# from mpcpl.libs.Random import random
import threading
# from mpcpl.libs.assign import assign
# from mpcpl.libs.Random import random


if __name__ == "__main__":
    ttttt().printf()
    # def test(name):
    #     with assign(name) as sn:
    #         w = 100
    #         print([name,random()()])
    # # def play(name):
    # #     with assign(name)as sn:
    # #         print(name,sn.thread_local.now_player)
    # #         #random()()
    # test("Alice")
    # # t = []
    # # for ele in range(100):
    # #     t.append(threading.Thread(target=test, args=('{}线程'.format(ele),)))
    # # for ele in t:
    # #     ele.start()