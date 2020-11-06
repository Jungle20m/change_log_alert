import os
import time
from datetime import datetime, date

from core.config import LOGS_MAIN_DIRECTORY, LOGS_TEMPORARY_DIRECTORY, REGEX


def get_content(file):
    if os.path.exists(file):
        log_file = open(file, "r")
        log_raw = log_file.read()
        return log_raw
    os.mknod(file)
    return ""

def append_change(file, change_log):
    with open(file, 'a') as file_handler:
        file_handler.write(change_log)
        
def split_log(change_log):
    # remove blank and /n at head and tail of change_log
    change_log = change_log.strip()
    # split change log by regex '** '
    frangments = change_log.split("** ")
    for fragment in frangments:
        if fragment != '':
            print(fragment)
            print("="*100)
        
def main():
    while True:
        today = date.today()
        main_file = os.path.join(LOGS_MAIN_DIRECTORY, f"{today}.txt")
        temporary_file = os.path.join(LOGS_TEMPORARY_DIRECTORY, f"{today}.txt")
        main_log = get_content(main_file)
        temporary_log = get_content(temporary_file)
        main_log_size = len(main_log)
        temp_log_size = len(temporary_log)
        # Check log file was change
        if main_log_size != temp_log_size:
            # get the change
            change_log = main_log[temp_log_size:]
            # append the change to file temporary
            append_change(temporary_file, change_log)
            # split change_log
            split_log(change_log)
        time.sleep(2) 

if __name__ == '__main__':
    main()