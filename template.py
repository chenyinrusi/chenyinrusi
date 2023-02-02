import datetime
import common_setup
import os
import logging

process_start = datetime.datetime.now()

set_up_process = common_setup.setup('Checks')
log_file_path = set_up_process[0]
source_file_path = set_up_process[1]
data_file_path = set_up_process[2]
user_string = set_up_process[3]

logger = logging.getLogger(log_file_path)

logger.info('Log File Saved: ' + log_file_path)
logger.info('User Detected: ' + user_string)
logger.info('Source File Folder Detected: ' + source_file_path)
logger.info('Data File Folder Detected: ' + data_file_path)

os.startfile(log_file_path)
