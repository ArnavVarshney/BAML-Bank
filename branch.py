class Branch(object):
    """
    Maintains a structure for all branches
    :param str branch_code: branch code of the branch
    :param str branch_name: name of branch
    :param Address address: address of the branch
    """

    def __init__(self, branch_code, branch_name, address):
        self.branch_code = branch_code
        self.branch_name = branch_name
        self.address = address

    def __str__(self):
        """
        :return printable string for an object of Branch class
        :rtype str
        """
        return f'Branch Name: {self.branch_name}\nBranch Code: {self.branch_code}\n{str(self.address)}'
