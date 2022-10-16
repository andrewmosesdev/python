input_month = input()
input_day = int(input())
monthsSet = {
    'January',
    'February',
    'March',
    'April',
    'May',
    'June',
    'July',
    'August',
    'September',
    'October',
    'November',
    'December'
}

def checkSet(input):
    return input in monthsSet

approved_month = checkSet(input_month)

if(approved_month == True and input_day >= 1 and input_day <= 31):
    if(input_month == 'January' or input_month == 'February'):
        print('Winter')
    elif(input_month == 'March'):
        if(input_day >= 1 and input_day <= 19):
            print('Winter')
        elif(input_day >= 20 and input_day <= 31):
            print('Spring')
        else: print('Invalid')
    elif(input_month == 'April' or input_month == 'May'):
        print('Spring')
    elif(input_month == 'June'):
        if(input_day >= 1 and input_day <= 20):
            print('Spring')
        elif(input_day >= 21 and input_day <= 30):
            print('Summer')
        else: print('Invalid')
    elif(input_month == 'July' or input_month == 'August'):
        print('Summer')
    elif(input_month == 'September'):
        if(input_day >= 1 and input_day <= 21):
            print('Summer')
        elif(input_day >= 22 and input_day <= 30):
            print('Autumn')
        else: print('Invalid')
    elif(input_month == 'October' or input_month == 'November'):
        print('Autumn')
    elif(input_month == 'December'):
        print('Winter')   
    else: print('Invalid')
else:
    print('Invalid')