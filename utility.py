import os  # os - for providing PAUSE functionality
import platform  # platform - for determining the execution platform
from datetime import datetime  # datetime - for getting current system date and time
from time import sleep

import phonenumbers
from pyisemail import is_email
from termcolor import colored


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
    if platform.system() == 'nt':
        # For UNIX based systems
        lol = ''
        print('\nEnter any character to continue: ', end='')
        while lol == '':
            lol = input()
    elif platform.system() == 'Windows':
        os.system('PAUSE')
    else:
        lol = ' '
        print('\nEnter any character to continue: ', end='')
        while lol == ' ':
            lol = input()


def clear_console():
    """
    Function to clear console window.
    """
    if platform.system() == 'nt':
        # For UNIX based systems
        os.system('clear')
    elif platform.system() == 'Windows':
        # For Windows systems
        os.system('cls')
    else:
        os.system('clear')


def validate_phone(phone_str):
    try:
        phone = phonenumbers.parse(phone_str, None)
        return phonenumbers.is_valid_number(phone)
    except phonenumbers.NumberParseException:
        return False


def validate_email(email_str):
    return is_email(email_str, check_dns=True)


def print_name():
    """
    Beauty Mode: On xD
    """
    color = 'red'
    print(colored('██████╗  █████╗ ███╗   ██╗██╗  ██╗    ███████╗██████╗  █████╗  █████╗ ███╗   ███╗', color))
    print(colored('██╔══██╗██╔══██╗████╗  ██║██║ ██╔╝    ██╔════╝██╔══██╗██╔══██╗██╔══██╗████╗ ████║', color))
    print(colored('██████╔╝███████║██╔██╗ ██║█████╔╝     ███████╗██████╔╝███████║███████║██╔████╔██║', color))
    print(colored('██╔══██╗██╔══██║██║╚██╗██║██╔═██╗     ╚════██║██╔═══╝ ██╔══██║██╔══██║██║╚██╔╝██║', color))
    print(colored('██████╔╝██║  ██║██║ ╚████║██║  ██╗    ███████║██║     ██║  ██║██║  ██║██║ ╚═╝ ██║', color))
    print(colored('╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝    ╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝', color))
    print()


def about():
    """
    Prints the team info with a not-so-typewriter-ish effect
    """
    about_str = colored('Team SPAAM *dab*\n\tMembers:\n\t\t1. Arnav Varshney\n\t\t2. Pradyumn Mishra\n\t\t'
                        '3. Aditi Prasad\n\t\t4. Mihir Ghonge\n\t\t5. Shishir Balasubramanian\n\n', 'green')
    for char in about_str:
        sleep(0.1)
        print(char, end='', flush=True)
