import os  # os - for providing PAUSE functionality
import platform  # platform - for determining the execution platform
from datetime import datetime  # datetime - for getting current system date and time


# Utility Functions

def get_current_date():
    """
    :return current system date from the datetime module in DD/MM/YYYY format
    :rtype str
    """
    return datetime.today().strftime('%d/%m/%Y')


def get_current_time():
    """
    :return current system time from the datetime module in HH:MM:SS format
    :rtype str
    """
    return datetime.now().strftime("%H:%M:%S")


def get_customer_id(account_number):
    """
    :return customer_id of the account, substring[0:4]
    :rtype str
    """
    return account_number[0:4]


def pause():
    """
    Function to pause program execution. Gives user time to interpret the output
    """
    if platform.system() == 'Linux':
        # For UNIX based systems
        lol = ''
        print('\nEnter any character to continue: ', end='')
        while lol == '':
            lol = input()
    elif platform.system() == 'Windows':
        # For Windows systems
        os.system('PAUSE')
