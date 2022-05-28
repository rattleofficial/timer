import streamlit as sl
import time

def count_down(ts):
    with sl.empty():
        while ts:
            min,secs=divmod(ts,60)
            time_now='{:02d}:{:02d}'.format(min,secs)
            sl.header(time_now)
            time.sleep(1)
            ts -=1
        sl.header('Time up!')




sl.title('Pomodoro timer')
n=sl.number_input('Enter the time in min:',min_value=1,value=25)

if sl.button('START'):
    sec=n*60
    count_down(sec)


