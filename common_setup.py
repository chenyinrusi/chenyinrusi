import datetime
import logging
import os


def setup_description():
    print(
        '''
        * parent_folder [os path]: where the scripts reside
            ----default: current folder
        * sub_folders [list]: folders under the parent folder, e.g. LOG folder, SOURCE folder, DATA folder etc.
            ----default: ['LOG','SOURCE', 'DATA']
        * project_name [string]: the name of the project
            ----default: TEST
        
        Return:
            0. log_file_name
            1. source_location
            2. data_location
        '''
    )


def setup(
        parent_folder,
        project_name='TEST',
        sub_folders=['LOG', 'SOURCE', 'DATA']
):
    start_time = datetime.datetime.now()
    start_timestamp = datetime.datetime.now().isoformat()
    start_timestamp = start_timestamp.replace('-', '')
    start_timestamp = start_timestamp.replace(':', '')

    user_name = os.getenv('username')
    computer_name = os.getenv('computername')
    user_string = user_name + '/' + computer_name

    for i in sub_folders:
        folder_check = parent_folder + '\\' + i
        if os.path.exists(folder_check):
            # print(folder_check + ' is existed already, PASS')
            pass
        else:
            os.mkdir(folder_check)

    if os.path.exists(parent_folder + '\\' + sub_folders[0]):
        logger_location = parent_folder + '\\' + sub_folders[0]
    else:
        logger_location = parent_folder + '\\' + input('Please enter the log folder name')
        print('Log folder is set to be: ' + logger_location)
    log_file_name = logger_location + '\\' + project_name + '_' + start_timestamp[:15] + '.log'

    logging.basicConfig(format='[%(asctime)s %(levelname)s] %(message)s', datefmt='%Y-%m-%d %H:%M:%S',
                        filename=log_file_name)
    # print('Passed log configuration set up')
    logger = logging.getLogger(log_file_name)
    logger.setLevel(logging.INFO)
    logger.info('Logger set up - {}'.format(datetime.datetime.now()))
    if os.path.exists(parent_folder + '\\' + sub_folders[1]):
        source_location = parent_folder + '\\' + sub_folders[1]
    else:
        source_location = parent_folder + '\\' + input('Please enter the source folder name')
        print('Source folder is set to be: ' + source_location)

    if os.path.exists(parent_folder + '\\' + sub_folders[2]):
        data_location = parent_folder + '\\' + sub_folders[2]
    else:
        data_location = parent_folder + '\\' + input('Please enter the data folder name')
        print('Data folder is set to be: ' + data_location)

    # os.startfile(log_file_name)

    return log_file_name, source_location, data_location, user_string
