
def tax(gross_pay: float):
    """ Determines income tax for employees
    parameter: gross_pay is a floating-point number
    return: the amount of tax an employee gets taken out of their gross pay
    """
    net_pay = gross_pay * 0.80
    return net_pay

import doctest
def netpay(hours: float):
    """ Determines net pay of employee's income
    param: hours is a floating-point number
    return: the income of the employee minus the amount taken out from taxes
    >>> netpay(15.5)
    201.5
    >>> netpay(40.50)
    526.5
    """
    gross_pay = 16.25 * hours
    net_pay = tax(gross_pay)
    # note that we are calling our function we defined above, tax(), to use in this function netpay()
    return net_pay
def main():
    """ Net pay of income given 20 percent tax rate """
    print('For 15.5 hours of work, netpay is:', netpay(15.5))
    print('For 40.50 hours of work, netpay is:', netpay(40.50))
    return None
main()
doctest.testmod()




