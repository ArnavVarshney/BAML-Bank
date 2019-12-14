class Transaction(object):
    """
    Maintains a structure for all transactions going into log
    :param str date: date of transaction, retrieved from get_current_date()
    :param str time: time of transaction, retrieved from get_current_time()
    :param str customer_id: customer_id of the customer involved
    :param str account_number: account_number of involved account
    :param str branch: branch associated to transaction, retrieved from Account.get_branch_code()
    :param int amount: net amount involved
    :param int opening_balance: initial balance
    :param int closing_balance: final_balance
    :param str remarks: notes for opening/closing of customers/accounts
    """

    def __init__(self, customer_id, account_number, date, time, branch, amount, opening_balance, closing_balance,
                 remarks):
        """
        Initialisation function for Transaction class
        """
        self.date = date
        self.time = time
        self.customer_id = customer_id
        self.account_number = account_number
        self.branch = branch
        self.amount = amount
        self.opening_balance = opening_balance
        self.closing_balance = closing_balance
        self.remarks = remarks

    def __str__(self):
        """
        :return printable string for an object of Customer class
        :rtype str
        """
        return '| {:^13s} | {:^12} | {:^12} | {:^10} | {:^8} | {:^10s} | {:^17s} | {:^18s} | {:^40s} |'.format(
            str(self.customer_id),
            str(self.account_number),
            str(self.date), str(self.time),
            str(self.branch),
            str(self.amount),
            str(self.opening_balance),
            str(self.closing_balance),
            self.remarks)
