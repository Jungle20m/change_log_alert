import os

WORK_DIRECTORY=os.getcwd() 

# This is absolute location
# The format of log file in log folder must be 'yyyy-mm-dd'
LOGS_MAIN_DIRECTORY=""

LOGS_TEMPORARY_DIRECTORY = os.path.join(WORK_DIRECTORY, "logs_temporary")

REGEX = "** "
