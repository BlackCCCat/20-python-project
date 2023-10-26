# Write your code here
import time
from datetime import datetime

def set_alarm(alarm_time):
    current_timestamp = round(time.time())
    cur_date = datetime.now().date()
    try:
        alarm_timestamp = round(time.mktime(time.strptime(f'{cur_date} {alarm_time}', '%Y-%m-%d %H:%M:%S')))
        if alarm_timestamp > current_timestamp:
            sleeptime = alarm_timestamp - current_timestamp
            time.sleep(sleeptime)
            print('DingDingDing!!!')
        else:
            sleeptime = 24 * 60 * 60 - (current_timestamp - alarm_timestamp)
            time.sleep(sleeptime)
            print('DingDingDing!!!')
    except ValueError as e:
        print('Wrong time format:\n', e)

if __name__ == '__main__':
    alarm_time = input('Enter the time for the alarm (HH:MM:SS): ')
    set_alarm(alarm_time)