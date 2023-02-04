import time
#pip install howdoi 
sec=input("enter the time in sec")
def countdown_timer(sec):
    while sec > 0:
        mins=int(sec/60)
        secs=int(sec%60)
        timer=f'{mins}:{secs}'
        print(timer)
        sec -=1
    print("time Up")

countdown_timer(int(sec))    