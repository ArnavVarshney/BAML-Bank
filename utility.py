import os  # os - for providing PAUSE functionality
import platform  # platform - for determining the execution platform
from datetime import datetime  # datetime - for getting current system date and time
from random import randint  # randint - for generating OTP

from twilio.rest import Client

#  Global variables:


global_customer_id = '0001'  # holds currently issued account number
global_customer_map = {}  # maps customer_id to customer
global_branches = {}  # maps branch_code to branch
global_transactions = []  # global transaction log


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


def clear_console():
    """
    Function to clear console window.
    """
    if platform.system() == 'Linux':
        # For UNIX based systems
        os.system('clear')
    elif platform.system() == 'Windows':
        # For Windows systems
        os.system('cls')


def send_message(msg, to_number):
    account_sid = 'ACa506f9dde2c217237c9295cf3b2b37a2'
    auth_token = '99e6e2f5b75ef2a3b9d7c89a53bbcfab'
    client = Client(account_sid, auth_token)
    message = client.messages.create(body=msg, from_='+14154834260', to=to_number)
    print(message.sid)


def generate_otp(to_number):
    otp = randint(10000, 99999)
    send_message(f'Greetings from Bank XXX!\n Your OTP is: {otp}', to_number)
