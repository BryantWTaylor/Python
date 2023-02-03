print() #blank line
print('Please rate the following from 1-10:\n')
size = int(input('How large is the loan? '))
credit = int(input('How good is your credit history? '))
income = int(input('How high is your income? '))
down_payment = int(input('How larege is your down payment? '))
print() #blank line

#calculations
if size >= 5:
    if credit >= 7 and income >= 7:
        can_loan = True
    elif credit >= 7 or income >= 7:
        if down_payment >= 5:
            can_loan = True
        else:
            can_loan = False
    else:
        can_loan = False
elif size < 5:
    if credit < 4:
        can_loan = False
    elif credit >= 4:
        if income >= 7 or down_payment >= 7:
            can_loan = True
        elif income >= 4 and down_payment >= 4:
            can_loan = True
        else:
            can_loan = False


if can_loan:
    print('You are approved!')
else:
    print('You did not qualify. Sorry!')