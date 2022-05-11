import threading
from threading import current_thread

global lockedIds
lockedIds=[]
threadLocal = threading.local()


def getNewBic():

    if current_thread().name == "MainThread" :
        if len(lockedIds) ==0 :
                lockedIds.append(0)
        lockedIds[0] += 1
        localObjs=lockedIds       
    else:
        initialized = getattr(threadLocal, 'initialized', None)
        localObjs=[]
        if initialized is None:
            print("initilized", current_thread().name)
            threadLocal.initialized = True
            if getattr(threadLocal, 'lockedIds', None) is None:
                threadLocal.lockedIds=[]
        else:
            print("Already initilized",current_thread().name,  )
        if len(threadLocal.lockedIds) ==0 :
                threadLocal.lockedIds.append(0)
        threadLocal.lockedIds[0] += 1
        
        localObjs = threadLocal.lockedIds 
    print("localThread", current_thread().name,  str(localObjs))
        

def runThread():
    getNewBic()
    getNewBic()
    getNewBic()
    getNewBic()
    getNewBic()


t1 = threading.Thread(target=runThread, args=())
t1.start()
t2 = threading.Thread(target=runThread, args=())
t2.start()
getNewBic()
getNewBic()
getNewBic()
getNewBic()
        
